from pages.content_page import ContentPage
from logic.facts import ME_PROD_MIN_POSSIBLE_TMP, ME_PROD_MAX_POSSIBLE_TMP

class MembranesProductionPage(ContentPage):
    TITLE = "Membranes — Production"

    STEPS = [
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
            "min": ME_PROD_MIN_POSSIBLE_TMP,
            "max": ME_PROD_MAX_POSSIBLE_TMP,
        },
    ]
