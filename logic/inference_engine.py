from logic.knowledge import WorkingMemory
from logic.rules.he_rules import heat_exchanger_production_rules, heat_exchanger_cleaning_rules
from logic.rules.ev_rules import evaporator_production_rules, evaporator_cleaning_rules
from logic.rules.dr_rules import dryer_production_rules, dryer_cleaning_rules
from logic.rules.me_rules import membranes_production_rules, membranes_cleaning_rules 

RULE_SETS = {
    "Heat Exchanger, production": heat_exchanger_production_rules,
    "Heat Exchanger, cleaning": heat_exchanger_cleaning_rules,
    "Evaporator, production": evaporator_production_rules,
    "Evaporator, cleaning": evaporator_cleaning_rules,
    "Dryer, production": dryer_production_rules,
    "Dryer, cleaning": dryer_cleaning_rules,
    "Membranes, production": membranes_production_rules,
    "Membranes, cleaning": membranes_cleaning_rules
}

def evaluate_machine(machine_type, state, **inputs):
    """
    machine_type: "heat_exchanger", "evaporator", "dryer", "membranes"
    state: "production" or "cleaning"
    inputs: all domain-specific facts
    """

    wm = WorkingMemory()
    wm.assert_fact("machine", machine_type)
    wm.assert_fact("state", state.lower())

    # load input facts
    for k, v in inputs.items():
        wm.assert_fact(k, v)

    key = f"{machine_type}, {state.lower()}"
    rule_func = RULE_SETS.get(key)
    if rule_func is None:
        return f"No rule set found for machine type '{machine_type} - {state}'"
    
    # run rule base (single forward pass, rules are ordered)
    rules = rule_func()
    for rule in rules:
        rule.try_fire(wm)

    # build explanation string
    if wm.output_text is None:
        return "No conclusion could be drawn."

    if wm.reasons:
        return wm.output_text + "\nReasons:\n- " + "\n- ".join(wm.reasons)

    return wm.output_text

