# pages/results_page.py
import tkinter as tk
from logic.inference_engine import evaluate_heat_exchanger


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

    def on_show(self):
        """
        Called when this page is shown.
        Uses controller.state_mode and controller's stored values.
        """
        mode = self.controller.state_mode  # "production" or "cleaning"

        if mode == "production":
            text = evaluate_heat_exchanger(
                state="production",
                product=self.controller.selected_product,
                run_time=self.controller.run_time,
                temp_water_in=self.controller.temp_water_in,
                temp_product_out=self.controller.temp_product_out,
                pump_capacity=self.controller.curr_pump_capacity,
            )
        else:
            # for now we only have fouling rate + pump capacity in the UI.
            # The formal cleaning rules need more inputs, so we pass only what we can.
            text = evaluate_heat_exchanger(
                state="cleaning",
                # temp_diff, pump_power, pressure_diff, time_at_75 could be added
                # later via extra fields in CleaningQuestionPage.
                pump_capacity=self.controller.curr_pump_capacity,
            )

        self.result_label.config(text=text)

