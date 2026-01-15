from pages.content_page import ContentPage
from logic.facts import DR_MAX_PUMP_POWER, DR_MAX_PUMP_CAPACITY

class DryerProductionPage(ContentPage):
    TITLE = "Dryer — Production"

    STEPS = [
        {
            "field": "pump_capacity_t1",
            "label": "Enter pump capacity at t₁ (L/h)",
            "type": "float",
            "min": 0.8 * DR_MAX_PUMP_CAPACITY,
            "max": DR_MAX_PUMP_CAPACITY,
        },
        {
            "field": "pump_capacity_t2",
            "label": "Enter pump capacity at t₂ (L/h)",
            "type": "float",
            "min": 0.8 * DR_MAX_PUMP_CAPACITY,
            "max": DR_MAX_PUMP_CAPACITY,
        },
        {
            "field": "temp_air_in_t1",
            "label": "Enter air-in temperature at t₁ (°C)",
            "type": "float",
            "min": 170,
            "max": 230,
            "when": lambda c: getattr(c, "pump_capacity_t1", None) == getattr(c, "pump_capacity_t2", None),
        },
        {
            "field": "temp_product_out_t1",
            "label": "Enter product-out temperature at t₁ (°C)",
            "type": "float",
            "min": 25,
            "max": 50,
            "when": lambda c: getattr(c, "pump_capacity_t1", None) == getattr(c, "pump_capacity_t2", None),
        },
        {
            "field": "temp_air_in_t2",
            "label": "Enter air-in temperature at t₂ (°C)",
            "type": "float",
            "min": 170,
            "max": 230,
            "when": lambda c: getattr(c, "pump_capacity_t1", None) == getattr(c, "pump_capacity_t2", None),
        },
        {
            "field": "temp_product_out_t2",
            "label": "Enter product-out temperature at t₂ (°C)",
            "type": "float",
            "min": 25,
            "max": 50,
            "when": lambda c: getattr(c, "pump_capacity_t1", None) == getattr(c, "pump_capacity_t2", None),
        },
        {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "min": 0.2 * DR_MAX_PUMP_POWER,
            "max": DR_MAX_PUMP_POWER,
            "when": lambda c: (
                getattr(c, "pump_capacity_t2", None) is not None
                and c.pump_capacity_t2 < 0.9 * DR_MAX_PUMP_CAPACITY
            ),
        },
    ]

    def validate_step(self, step, value):
        # Cross-field temperature checks
        if step["field"] == "temp_product_out_t1":
            air = getattr(self.controller, "temp_air_in_t1", None)
            if air is not None and value > air:
                return "Air-in temperature must be higher than product-out temperature at t₁."

        if step["field"] == "temp_product_out_t2":
            air = getattr(self.controller, "temp_air_in_t2", None)
            if air is not None and value > air:
                return "Air-in temperature must be higher than product-out temperature at t₂."

        return None
