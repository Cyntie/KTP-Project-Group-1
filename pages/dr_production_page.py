from pages.content_page import ContentPage

class DryerProductionPage(ContentPage):
    TITLE = "Dryer — Production"

    STEPS = [
        {
            "field": "pump_capacity_t1",
            "label": "Enter pump capacity at t₁ (L/h)",
            "type": "float",
            "min": 0,
        },
        {
            "field": "pump_capacity_t2",
            "label": "Enter pump capacity at t₂ (L/h)",
            "type": "float",
            "min": 0,
        },

        {
            "field": "temp_air_in_t1",
            "label": "Enter air-in temperature at t₁ (°C)",
            "type": "float",
        },
        {
            "field": "temp_product_out_t1",
            "label": "Enter product-out temperature at t₁ (°C)",
            "type": "float",
        },
        {
            "field": "temp_air_in_t2",
            "label": "Enter air-in temperature at t₂ (°C)",
            "type": "float",
        },
        {
            "field": "temp_product_out_t2",
            "label": "Enter product-out temperature at t₂ (°C)",
            "type": "float",
        },
        {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "min": 0,
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
