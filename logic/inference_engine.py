from logic.knowledge import WorkingMemory
from logic.rules import heat_exchanger_rules, evaporator_rules, dryer_rules, membranes_rules

RULE_SETS = {
    "Heat Exchanger": heat_exchanger_rules,
    "Evaporator": evaporator_rules,
    "Dryer": dryer_rules,
    "Membranes": membranes_rules
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

    rule_func = RULE_SETS.get(machine_type)
    if rule_func is None:
        return f"No rule set found for machine type '{machine_type}'"
    
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

