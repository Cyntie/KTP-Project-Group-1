from pages.content_page import ContentPage

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
            "label": "Enter current TMP (mbar)",
            "type": "float",
            "min": 0,
        },
    ]
