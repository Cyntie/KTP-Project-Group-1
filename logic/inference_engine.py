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

# This function is for checking after each field if the machine is dirty or not.
def _is_unconditional_final_rule(rule) -> bool:
    name = getattr(rule, "name", "") or ""
    n = name.lower()
    return (
            "clean enough" in n
            or "clean, stop cycle" in n
            or "clean stop cycle" in n
    )

def evaluate_machine_partial(machine_type, state, **inputs):
    """
    Partial evaluation: runs rules but SKIPS the final 'clean' rule.
    Returns:
      - decided: bool
      - text: conclusion text (or None)
      - reasons: list[str]
    """
    wm = WorkingMemory()
    wm.assert_fact("machine", machine_type)
    wm.assert_fact("state", state.lower())

    for k, v in inputs.items():
        if v is not None:
            wm.assert_fact(k, v)

    key = f"{machine_type}, {state.lower()}"
    rule_func = RULE_SETS.get(key)
    if rule_func is None:
        return {
            "decided": True,
            "text": f"No rule set found for machine type '{machine_type} - {state}'",
            "reasons": [],
        }

    rules = rule_func()
    for rule in rules:
        if _is_unconditional_final_rule(rule):
            continue

        rule.try_fire(wm)

        # stop early once a real diagnosis rule fired
        if wm.output_text is not None:
            break

    return {
        "decided": wm.output_text is not None,
        "text": wm.output_text,
        "reasons": wm.reasons.copy(),
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
        if v is not None:
            wm.assert_fact(k, v)

    key = f"{machine_type}, {state.lower()}"
    rule_func = RULE_SETS.get(key)
    if rule_func is None:
        return {
            "decided": True,
            "text": f"No rule set found for machine type '{machine_type} - {state}'",
            "reasons": [],
        }

    # run rule base (single forward pass, rules are ordered)
    rules = rule_func()
    for rule in rules:
        rule.try_fire(wm)

    # build explanation string
    if wm.output_text is None:
        return {
            "decided": False,
            "text": None,
            "reasons": [],
        }

    return {
        "decided": True,
        "text": wm.output_text,
        "reasons": wm.reasons.copy(),
    }

