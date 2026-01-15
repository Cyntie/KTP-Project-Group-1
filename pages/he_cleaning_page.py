from pages.content_page import ContentPage
from logic.facts import (HE_MAX_PUMP_POWER,
                         HE_CLEAN_MIN_POSSIBLE_75_RUNTIME, HE_CLEAN_MAX_POSSIBLE__75_RUNTIME,
                         HE_CLEAN_MIN_POSSIBLE_PRESSURE, HE_CLEAN_MAX_POSSIBLE_PRESSURE,
                         HE_CLEAN_MIN_POSSIBLE_WATER_IN_TEMP, HE_CLEAN_MAX_POSSIBLE_WATER_IN_TEMP,
                         HE_CLEAN_MIN_POSSIBLE_PRODUCT_OUT_TEMP, HE_CLEAN_MAX_POSSIBLE_PRODUCT_OUT_TEMP)

class HeatExchangerCleaningPage(ContentPage):
    TITLE = "Heat Exchanger — Cleaning"

    STEPS = [
        {
            "field": "time_at_75",
            "label": "Enter time at 75 °C (min)",
            "type": "float",
            "min": HE_CLEAN_MIN_POSSIBLE_75_RUNTIME,
            "max": HE_CLEAN_MAX_POSSIBLE__75_RUNTIME,
        },
        {
            "field": "start_pressure",
            "label": "Enter start pressure (bar)",
            "type": "float",
            "min": HE_CLEAN_MIN_POSSIBLE_PRESSURE,
            "max": HE_CLEAN_MAX_POSSIBLE_PRESSURE,
        },
        {
            "field": "end_pressure",
            "label": "Enter end pressure (bar)",
            "type": "float",
            "min": HE_CLEAN_MIN_POSSIBLE_PRESSURE,
            "max": HE_CLEAN_MAX_POSSIBLE_PRESSURE,
        },
        {
            "field": "temp_water_in",
            "label": "Enter water-in temperature (°C)",
            "type": "float",
            "min": HE_CLEAN_MIN_POSSIBLE_WATER_IN_TEMP,
            "max": HE_CLEAN_MAX_POSSIBLE_WATER_IN_TEMP,
        },
        {
            "field": "temp_product_out",
            "label": "Enter product-out temperature (°C)",
            "type": "float",
            "min": HE_CLEAN_MIN_POSSIBLE_PRODUCT_OUT_TEMP,
            "max": HE_CLEAN_MAX_POSSIBLE_PRODUCT_OUT_TEMP,
        },
                {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "min": 0.2 * HE_MAX_PUMP_POWER,
            "max": HE_MAX_PUMP_POWER

        },
    ]

    def validate_step(self, step, value):
        # Physical invariant: water-in ≥ product-out
        if step["field"] == "temp_product_out":
            water_in = getattr(self.controller, "temp_water_in", None)
            if water_in is not None and value > water_in:
                return "Water-in temperature must be higher than product-out temperature."

        # Physical invariant: end pressure ≥ start pressure
        if step["field"] == "end_pressure":
            start = getattr(self.controller, "start_pressure", None)
            if start is not None and value < start:
                return "End pressure must be greater than or equal to start pressure."

        return None
