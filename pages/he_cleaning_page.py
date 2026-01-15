from pages.content_page import ContentPage

class HeatExchangerCleaningPage(ContentPage):
    TITLE = "Heat Exchanger — Cleaning"

    STEPS = [
        {
            "field": "time_at_75",
            "label": "Enter time at 75 °C (min)",
            "type": "float",
            "min": 0,
        },
        {
            "field": "start_pressure",
            "label": "Enter start pressure (bar)",
            "type": "float",
            "min": 0,
        },
        {
            "field": "end_pressure",
            "label": "Enter end pressure (bar)",
            "type": "float",
            "min": 0,
        },
        {
            "field": "temp_water_in",
            "label": "Enter water-in temperature (°C)",
            "type": "float",
        },
        {
            "field": "temp_product_out",
            "label": "Enter product-out temperature (°C)",
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
