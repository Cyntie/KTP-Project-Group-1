from pages.content_page import ContentPage

class MembranesCleaningPage(ContentPage):
    TITLE = "Membranes — Cleaning"

    STEPS = [
        {
            "field": "curr_cwf",
            "label": "Enter current CWF (L/m²h)",
            "type": "float",
            "min": 0,
            "max": 400,
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
            "min": 0,
            "max": 25,
        },
    ]
