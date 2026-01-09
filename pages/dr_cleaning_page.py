from pages.content_page import ContentPage

class DryerCleaningPage(ContentPage):
    TITLE = "Dryer — Cleaning"

    STEPS = [
        {
            "field": "cycle",
            "label": "Choose cycle type",
            "type": "choice",
            "choices": ["Wet", "Dry"],
        },
        {
            "field": "curr_pump_power",
            "label": "Enter current pump power (kW)",
            "type": "float",
            "when": lambda c: getattr(c, "cycle", None) == "Wet",
        },
        {
            "field": "run_time",
            "label": "Enter cleaning time (h)",
            "type": "float",
            "min": 0,
        },
    ]
