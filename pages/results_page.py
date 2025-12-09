# pages/results_page.py
import tkinter as tk
from logic.inference_engine import evaluate_machine


class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.result_label = tk.Label(
            self,
            text="No result yet.",
            font=("Arial", 14)
        )
        self.result_label.pack(pady=10)

        tk.Button(
            self,
            text="Restart",
            font=("Arial", 14),
            bg="#E0C2FF",
            fg="#0D001A",
            command=self.go_to_start
        ).pack(pady=20)

    def go_to_start(self):
        from pages.start_page import StartPage
        self.controller.show_page(StartPage)

    def on_show(self):
        """
        Called when this page is shown.
        Uses controller.state_mode and controller's stored values.
        """

        inputs = {}
        for attr in [
            "product",
            "run_time",
            "curr_pump_capacity",
            "curr_pump_power",
            "temp_water_in",
            "temp_product_out",
            "start_pressure",
            "end_pressure",
            "time_at_75"
        ]:
            value = getattr(self.controller, attr, None)
            if value is not None:
                inputs[attr] = value

        text = evaluate_machine(
            machine_type=self.controller.machine_type,
            state=self.controller.state_mode,
            **inputs
        )

        self.result_label.config(text=text)

