from pages.content_page import ContentPage
from logic.facts import DR_MAX_PUMP_POWER, DR_CLEAN_MIN_POSSIBLE_RUNTIME, DR_CLEAN_MAX_POSSIBLE_RUNTIME

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
            "min": 0.2 * DR_MAX_PUMP_POWER,
            "max": DR_MAX_PUMP_POWER,
            "when": lambda c: getattr(c, "cycle", None) == "Wet",
        },
        {
            "field": "run_time",
            "label": "Enter cleaning time (h)",
            "type": "float",
            "min": DR_CLEAN_MIN_POSSIBLE_RUNTIME,
            "max": DR_CLEAN_MAX_POSSIBLE_RUNTIME,
        },
    ]
