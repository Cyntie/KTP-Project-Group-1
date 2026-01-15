from pages.content_page import ContentPage
from logic.facts import EV_MAX_PUMP_POWER

class EvaporatorCleaningPage(ContentPage):
    TITLE = "Evaporator — Cleaning"

    STEPS = [
        {
            "field": "run_time",
            "label": "Enter cleaning time (h)",
            "type": "float",
            "min": 0,
        },
        {
            "field": "temp_water_in",
            "label": "Enter water-in temperature (°C)",
            "type": "float",
            "min": 70,
            "max": 80,
        },
        {
            "field": "temp_product_out",
            "label": "Enter product-out temperature (°C)",
            "type": "float",
            "min": 60,
            "max": 80
        },
        {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "min": 0.2 * EV_MAX_PUMP_POWER,
            "max": EV_MAX_PUMP_POWER,
        },
    ]

    def validate_step(self, step, value):
        # Physical invariant: water-in ≥ product-out
        if step["field"] == "temp_product_out":
            water_in = getattr(self.controller, "temp_water_in", None)
            if water_in is not None and value > water_in:
                return "Water-in temperature must be higher than product-out temperature."
        return None
