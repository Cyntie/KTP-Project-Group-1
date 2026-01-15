from pages.content_page import ContentPage
from logic.facts import (EV_MAX_PUMP_POWER, EV_MAX_PUMP_CAPACITY,
                         EV_PROD_MIN_POSSIBLE_RUNTIME, EV_PROD_MAX_POSSIBLE_RUNTIME,
                         EV_PROD_MIN_POSSIBLE_DENSITY, EV_PROD_MAX_POSSIBLE_DENSITY,
                         EV_PROD_MIN_POSSIBLE_WATER_IN_TEMP, EV_PROD_MAX_POSSIBLE_WATER_IN_TEMP,
                         EV_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP, EV_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP)

class EvaporatorProductionPage(ContentPage):
    TITLE = "Evaporator — Production"

    STEPS = [
        {
            "field": "protein_content",
            "label": "Protein content of product",
            "type": "choice",
            "choices": ["0.5%", "4%"],
        },
        {
            "field": "fat_content",
            "label": "Fat content of product",
            "type": "choice",
            "choices": ["0.5%", "4%", "8%"],
        },
        {
            "field": "run_time",
            "label": "Enter run time (h)",
            "type": "float",
            "min": EV_PROD_MIN_POSSIBLE_RUNTIME,
            "max": EV_PROD_MAX_POSSIBLE_RUNTIME,
        },
        {
            "field": "curr_density",
            "label": "Enter current product density (kg/m³)",
            "type": "float",
            "min": EV_PROD_MIN_POSSIBLE_DENSITY,
            "max": EV_PROD_MAX_POSSIBLE_DENSITY,
        },
        {
            "field": "max_density",
            "label": "Enter maximum product density (kg/m³)",
            "type": "float",
            "min": EV_PROD_MIN_POSSIBLE_DENSITY,
            "max": EV_PROD_MAX_POSSIBLE_DENSITY,
        },
        {
            "field": "temp_water_in",
            "label": "Enter water-in temperature (°C)",
            "type": "float",
            "min": EV_PROD_MIN_POSSIBLE_WATER_IN_TEMP,
            "max": EV_PROD_MAX_POSSIBLE_WATER_IN_TEMP,
        },
        {
            "field": "temp_product_out",
            "label": "Enter product-out temperature (°C)",
            "type": "float",
            "min": EV_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP,
            "max": EV_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP,
        },
        {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "min": 0.2 * EV_MAX_PUMP_POWER,
            "max": EV_MAX_PUMP_POWER,
        },
        {
            "field": "curr_pump_capacity",
            "label": "Enter current pump capacity (L/h)",
            "type": "float",
            "min": 0.8 * EV_MAX_PUMP_CAPACITY,
            "max": EV_MAX_PUMP_CAPACITY,
            "when": lambda c: getattr(c, "curr_pump_power", None) == EV_MAX_PUMP_POWER,
        },
    ]

    def validate_step(self, step, value):
        # Physical invariant: water-in ≥ product-out
        if step["field"] == "temp_product_out":
            water_in = getattr(self.controller, "temp_water_in", None)
            if water_in is not None and value > water_in:
                return "Water-in temperature must be higher than product-out temperature."

        # Density sanity check
        if step["field"] == "max_density":
            curr = getattr(self.controller, "curr_density", None)
            if curr is not None and value < curr:
                return "Maximum density must be greater than or equal to current density."

        return None
