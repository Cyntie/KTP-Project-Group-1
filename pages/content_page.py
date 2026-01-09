import tkinter as tk
from tkinter import messagebox

from logic.inference_engine import evaluate_machine_partial
from pages.results_page import ResultsPage


class ContentPage(tk.Frame):
    TITLE = "Content"
    STEPS = []

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.step_index = 0

        self.title_label = tk.Label(
            self,
            text=self.TITLE,
            font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=(12, 18))

        self.outer = tk.Frame(self)
        self.outer.pack(expand=True)

        self.card = tk.Frame(self.outer, padx=28, pady=22, bd=1, relief="solid")
        self.card.pack()

        self.question_label = tk.Label(self.card, text="", font=("Arial", 15))
        self.question_label.pack(pady=(0,12))

        self.input_var = tk.StringVar()
        self.entry = tk.Entry(self.card, textvariable=self.input_var, font=("Arial", 14), justify="center")

        self.choice_var = tk.StringVar()
        self.choice_menu = None

        self.btns = tk.Frame(self.card)
        self.btns.pack(pady=(14,0))

        self.back_btn = tk.Button(
            self.btns, text="Back", font=("Arial", 12, "bold"),
            bg="#E0E0E0", padx=16, pady=6,
            command=self.go_back
        )
        self.back_btn.grid(row=0, column=0, padx=8)

        self.next_btn = tk.Button(
            self.btns, text="Next →", font=("Arial", 12, "bold"),
            bg="#4CAF50", fg="white", activebackground="#43A047",
            padx=16, pady=6,
            command=self.on_next
        )
        self.next_btn.grid(row=0, column=1, padx=8)

        self.bind_all("<Return>", lambda e: self.on_next())

    def on_show(self):
        self.step_index = 0
        self._render_step()

    def _step_applies(self, step) -> bool:
        cond = step.get("when")
        return True if cond is None else bool(cond(self.controller))

    def _render_step(self):
        # skip steps that don't apply
        while self.step_index < len(self.STEPS) and not self._step_applies(self.STEPS[self.step_index]):
            self.step_index += 1

        # if we've skipped past the end, go to results
        if self.step_index >= len(self.STEPS):
            self.controller.override_result = None
            self.controller.show_page(ResultsPage)
            return

        step = self.STEPS[self.step_index]
        self.question_label.config(text=step["label"])

        if self.choice_menu is not None:
            self.choice_menu.destroy()
            self.choice_menu = None

        self.input_var.set("")
        self.entry.pack_forget()

        if step["type"] == "choice":
            choices = step.get("choices", [])
            self.choice_var.set("")
            self.choice_menu = tk.OptionMenu(self.card, self.choice_var, *choices)
            self.choice_menu.config(font=("Arial", 12))
            self.choice_menu.pack(pady=6, before=self.btns)
        else:
            self.entry.pack(pady=6, before=self.btns)
            self.entry.focus_set()

        if self.step_index == 0:
            self.back_btn.config(text="← Start")
        else:
            self.back_btn.config(text="Back")

    def go_back(self):
        if self.step_index > 0:
            self.step_index -= 1
            self._render_step()
        else:
            # go back to start page
            from pages.start_page import StartPage
            self.controller.show_page(StartPage)

    def validate_step(self, step, value):
        # subclasses can override for validation
        return None

    def _parse_value(self, step):
        t = step["type"]

        if t == "choice":
            v = self.choice_var.get()
            if v == "":
                raise ValueError("Please select an option.")
            return v

        raw = self.input_var.get().strip()
        if raw == "":
            raise ValueError("Please enter a value.")

        if t == "int":
            v = int(raw)
        elif t == "float":
            v = float(raw)
        else:
            raise ValueError(f"Unknown type: {t}")

        if "min" in step and v < step["min"]:
            raise ValueError(f"Value must be >= {step['min']}.")
        if "max" in step and v > step["max"]:
            raise ValueError(f"Value must be <= {step['max']}.")

        return v

    def on_next(self):
        step = self.STEPS[self.step_index]

        try:
            value = self._parse_value(step)
        except Exception as e:
            messagebox.showerror("Invalid input", str(e))
            return

        err = self.validate_step(step, value)
        if err:
            messagebox.showerror("Invalid input", err)
            return

        setattr(self.controller, step["field"], value)

        inputs = {}
        for s in self.STEPS:
            if not self._step_applies(s):
                continue
            f = s["field"]
            v = getattr(self.controller, f, None)
            if v is not None:
                inputs[f] = v

        result = evaluate_machine_partial(
            machine_type=self.controller.machine_type,
            state=self.controller.state_mode,
            **inputs
        )

        if result.get("decided"):
            self.controller.override_result = result
            self.controller.show_page(ResultsPage)
            return

        self.step_index += 1
        self._render_step()
