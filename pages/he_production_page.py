from pages.content_page import ContentPage
from logic.facts import (HE_MAX_PUMP_POWER, HE_MAX_PUMP_CAPACITY, 
                         HE_PROD_MIN_POSSIBLE_RUNTIME, HE_PROD_MAX_POSSIBLE_RUNTIME, 
                         HE_PROD_MIN_POSSIBLE_WATER_IN_TEMP, HE_PROD_MAX_POSSIBLE_WATER_IN_TEMP,
                         HE_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP, HE_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP)

class HeatExchangerProductionPage(ContentPage):
    TITLE = "Heat Exchanger — Production"

    STEPS = [
        {
            "field": "product",
            "label": "Choose product type",
            "type": "choice",
            "choices": ["Skim milk", "Whole milk", "Cream"],
        },
        {
            "field": "run_time",
            "label": "Enter run time (h)",
            "type": "float",
            "min": HE_PROD_MIN_POSSIBLE_RUNTIME,
            "max": HE_PROD_MAX_POSSIBLE_RUNTIME,
        },
        {
            "field": "temp_water_in",
            "label": "Enter water-in temperature (°C)",
            "type": "float",
            "min": HE_PROD_MIN_POSSIBLE_WATER_IN_TEMP,
            "max": HE_PROD_MAX_POSSIBLE_WATER_IN_TEMP,
        },
        {
            "field": "temp_product_out",
            "label": "Enter product-out temperature (°C)",
            "type": "float",
            "min": HE_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP,
            "max": HE_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP,
        },
        {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "min": 0.2 * HE_MAX_PUMP_POWER,
            "max": HE_MAX_PUMP_POWER,
        },
        {
            "field": "curr_pump_capacity",
            "label": "Enter current pump capacity (L/h)",
            "type": "float",
            "min": 0.8 * HE_MAX_PUMP_CAPACITY,
            "max": HE_MAX_PUMP_CAPACITY,
            "when": lambda c: getattr(c, "curr_pump_power", None) == HE_MAX_PUMP_POWER,
        },
    ]

    def validate_step(self, step, value):
        # Physical invariant: water-in ≥ product-out
        if step["field"] == "temp_product_out":
            water_in = getattr(self.controller, "temp_water_in", None)
            if water_in is not None and value > water_in:
                return "Water-in temperature must be higher than product-out temperature."
        return None
