from logic.knowledge import WorkingMemory
from logic.rules import heat_exchanger_rules


def evaluate_heat_exchanger(state, **inputs):
    """
    state: "production" or "cleaning"
    inputs: domain-specific values, e.g.
        product, run_time, temp_water_in, temp_product_out,
        pump_capacity, pump_power, set_capacity,
        temp_diff, pressure_diff, time_at_75,
    """

    wm = WorkingMemory()
    wm.assert_fact("machine", "heat_exchanger")
    wm.assert_fact("state", state)

    # load input facts
    for k, v in inputs.items():
        wm.assert_fact(k, v)

    # derive temp_diff from water-in & product-out if not given
    if wm.get("temp_diff") is None:
        tw_in = wm.get("temp_water_in")
        tp_out = wm.get("temp_product_out")
        if tw_in is not None and tp_out is not None:
            wm.assert_fact("temp_diff", abs(tw_in - tp_out))

    # provide some sensible defaults if missing (so GUI can stay simple for now)
    if wm.get("pump_power") is None:
        # in production rules you need pump_power; default to 100% for now.
        wm.assert_fact("pump_power", 100.0)
    if wm.get("set_capacity") is None and wm.get("pump_capacity") is not None:
        # assume current capacity should be 100% of nominal if not explicitly set
        wm.assert_fact("set_capacity", wm.get("pump_capacity"))

    # run rule base (single forward pass, rules are ordered)
    rules = heat_exchanger_rules()
    for rule in rules:
        rule.try_fire(wm)

    # build explanation string
    if wm.output_text is None:
        return "No conclusion could be drawn."

    if wm.reasons:
        return wm.output_text + "\nReasons:\n- " + "\n- ".join(wm.reasons)

    return wm.output_text

