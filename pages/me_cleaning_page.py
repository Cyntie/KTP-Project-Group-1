from pages.content_page import ContentPage

class MembranesCleaningPage(ContentPage):
    TITLE = "Membranes — Cleaning"

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
            "label": "Enter current TMP (mbar)",
            "type": "float",
            "min": 0,
        },
        {
            "field": "curr_cwf",
            "label": "Enter current CWF (L/m²h)",
            "type": "float",
            "min": 0,
        },
    ]
