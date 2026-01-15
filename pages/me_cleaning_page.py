from pages.content_page import ContentPage
from logic.facts import (ME_CLEAN_MIN_POSSIBLE_CWF, ME_CLEAN_MAX_POSSIBLE_CWF, 
                         ME_CLEAN_MIN_POSSIBLE_TMP, ME_CLEAN_MAX_POSSIBLE_TMP) 

class MembranesCleaningPage(ContentPage):
    TITLE = "Membranes — Cleaning"

    STEPS = [
        {
            "field": "curr_cwf",
            "label": "Enter current CWF (L/m²h)",
            "type": "float",
            "min": ME_CLEAN_MIN_POSSIBLE_CWF,
            "max": ME_CLEAN_MAX_POSSIBLE_CWF,
        },
        {
            "field": "membrane",
            "label": "Select membrane type",
            "type": "choice",
            "choices": [
                "Micro Filtration",
                "Ultra Filtration",
                "Nano Filtration",
                "Reversed Osmosis",
            ],
        },
        {
            "field": "curr_tmp",
            "label": "Enter current TMP (bar)",
            "type": "float",
            "min": ME_CLEAN_MIN_POSSIBLE_TMP,
            "max": ME_CLEAN_MAX_POSSIBLE_TMP,
        },
    ]
