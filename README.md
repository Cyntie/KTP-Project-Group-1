# Assessing Machine Cleanliness App

## Purpose

This application is a rule-based decision support system implemented as a Tkinter GUI.
It guides the user through a wizard-style interface to collect inputs about an industrial machine 
and evaluates those inputs in order to determine whether the machine can continue its
production, or stop for cleaning.

## Features

- Wizard-style input flow with conditional steps
- Supports multiple machine types: 
    - Heat Exchanger
    - Evaporator
    - Dryer
    - Membrane
- Separates production and cleaning modes
- Rule-based inference engine
- Early stopping when a conclusion can be reached
- Final results page with reasoning

## Files

```text
main.py
pages/
    app.py
    content_page.py
    dr_cleaning_page.py
    dr_production_page.py
    ev_cleaning_page.py
    ev_production_page.py
    he_cleaning_page.py
    he_production_page.py
    me_cleaning_page.py
    me_production_page.py
    results_page.py
    start_page.py
logic/
    _init_.py
    facts.py
    inference_engine.py
    knowledge.py
    rules/
        dr_rules.py
        ev_rules.py
        he_rules.py
        me_rules.py
        rule.py

```

## How to Run

```bash
python main.py
```
1. The user selects the machine type and state (production or cleaning).
2. The wizard dynamically asks relevant questions based on user's choices.
3. After each input, a partial rule evaluation is performed.
4. If a decisive rule fires, the wizard stops early and displays the result.
5. Otherwise, it continues until all relevant inputs are collected.
6. The final rule evaluation produces the final decision and explanation. 
