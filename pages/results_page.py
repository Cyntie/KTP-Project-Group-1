import tkinter as tk
from logic.inference_engine import evaluate_machine

def format_result(result: dict) -> str:
    """
    result = {"decided": bool, "text": str|None, "reasons": list[str]}
    """
    if not isinstance(result, dict):
        return str(result)

    decided = result.get("decided", False)
    text = result.get("text", None)
    reasons = result.get("reasons", []) or []

    if not decided or not text:
        return "No conclusion could be drawn."

    if reasons:
        return text + "\nReasons:\n- " + "\n- ".join(reasons)

    return text

def classify_status(text: str) -> str:
    t = (text or "").lower()
    if "dirty" in t:
        return "DIRTY"
    if "not yet clean" in t:
        return "NOT_YET_CLEAN"
    if "clean" in t:
        return "CLEAN"
    return "UNKNOWN"


class ResultsPage(tk.Frame):
    TITLE = ("Result")

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

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

        self.status_label = tk.Label(
            self.card,
            text="",
            font=("Arial", 12, "bold"),
            padx=12,
            pady=6
        )
        self.status_label.pack(pady=(0, 14))

        self.result_label = tk.Label(
            self.card,
            text="No result yet.",
            font=("Arial", 14),
            justify="left",
            anchor="w",
            wraplength=520
        )
        self.result_label.pack(pady=(0, 16), fill="x")


        self.btns = tk.Frame(self.card)
        self.btns.pack(pady=(8, 0))

        self.restart_btn = tk.Button(
            self.btns,
            text="← Back to Start",
            font=("Arial", 12, "bold"),
            bg="#E0E0E0",
            padx=16,
            pady=6,
            command=self.go_to_start
        )
        self.restart_btn.grid(row=0, column=0, padx=8)


    def set_status_style(self, status: str):
        if status == "CLEAN":
            self.status_label.config(text="CLEAN", bg="#DFF2DF", fg="#1B5E20")
        elif status == "NOT_YET_CLEAN":
            self.status_label.config(text="NOT YET CLEAN", bg="#FFF1D6", fg="#8A5A00")
        elif status == "DIRTY":
            self.status_label.config(text="DIRTY", bg="#FFE0E0", fg="#8B0000")
        else:
            self.status_label.config(text="NO CONCLUSION", bg="#EEEEEE", fg="#333333")

    def go_to_start(self):
        from pages.start_page import StartPage
        self.controller.reset_inputs()
        self.controller.show_page(StartPage)


    def on_show(self):
        """
        Called when this page is shown.
        Uses controller.state_mode and controller's stored values.
        """

        inputs = {}
        for attr in [
            "product",
            "fat_content",
            "protein_content",
            "run_time",
            "curr_pump_capacity",
            "pump_capacity_t1",
            "pump_capacity_t2",
            "curr_pump_power",
            "curr_density",
            "max_density",
            "temp_water_in",
            "temp_product_out",
            "temp_air_in_t1",
            "temp_product_out_t1",
            "temp_air_in_t2",
            "temp_product_out_t2",
            "start_pressure",
            "end_pressure",
            "time_at_75",
            "cycle",
            "membrane",
            "curr_tmp",
            "curr_cwf"
        ]:
            value = getattr(self.controller, attr, None)
            if value is not None:
                inputs[attr] = value

        if self.controller.override_result is not None:
            result = self.controller.override_result
            self.controller.override_result = None
        else:
            result = evaluate_machine(
                machine_type=self.controller.machine_type,
                state=self.controller.state_mode,
                **inputs
            )

        self.result_label.config(text=format_result(result))
        self.set_status_style(classify_status(format_result(result)))


