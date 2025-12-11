from logic.rules.rule import Rule

from logic.facts import (
    DR_MAX_PUMP_POWER,
    DR_MAX_PUMP_CAPACITY,
    DR_PROD_MAX_DIFF_TEMP_DIFF,
    DR_PROD_MIN_PERC_PUMP_CAPACITY,
    DR_CLEAN_MIN_RUNTIME,
    DR_CLEAN_MAX_PERC_PUMP_POWER
)

def dryer_production_rules():
    rules = []
    
    rules.append(
    Rule(
        "DR PREP: compute temp_diff at t1",
        lambda wm: wm.get("temp_diff_t1") is None
                  and wm.get("temp_air_in_t1") is not None
                  and wm.get("temp_product_out_t1") is not None,
        lambda wm: wm.assert_fact("temp_diff_t1", abs(wm.get("temp_air_in_t1") - wm.get("temp_product_out_t1")))
        )
    )

    rules.append(
    Rule(
        "DR PREP: compute temp_diff at t2",
        lambda wm: wm.get("temp_diff_t2") is None
                  and wm.get("temp_air_in_t2") is not None
                  and wm.get("temp_product_out_t2") is not None,
        lambda wm: wm.assert_fact("temp_diff_t2", abs(wm.get("temp_air_in_t2") - wm.get("temp_product_out_t2")))
        )
    )

    # IF pump power = 100% and pump capacity < minimum_percentage of set capacity THEN dirty
    rules.append(
        Rule(
            "DR PROD: pump capacity too low",
            lambda wm: (
                wm.get("pump_capacity_t2") is not None
                and wm.get("curr_pump_power") is not None
                and wm.get("curr_pump_power") >= DR_MAX_PUMP_POWER
                and wm.get("pump_capacity_t2") < DR_PROD_MIN_PERC_PUMP_CAPACITY * DR_MAX_PUMP_CAPACITY
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Pump capacity too low: {wm.get("pump_capacity_t2")} L/h")
            )
        )
    )

    # IF pump capacity at t1 = pump capacity at t2 
    # and temperature difference at t2 < max difference in temperature difference of temperature difference at t1 
    # THEN dirty
    rules.append(
        Rule(
            "DR PROD: temperature difference too low",
            lambda wm: (
                wm.get("pump_capacity_t1") is not None
                and wm.get("pump_capacity_t2") is not None
                and wm.get("temp_diff_t1") is not None
                and wm.get("temp_diff_t2") is not None
                and wm.get("pump_capacity_t1") == wm.get("pump_capacity_t2")
                and (wm.get("temp_diff_t2")/wm.get("temp_diff_t1")) < DR_PROD_MAX_DIFF_TEMP_DIFF
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Difference in temperature difference too low: {wm.get("temp_diff_t1")} °C at t1 and {wm.get("temp_diff_t2")} °C at t2")
            )
        )
    )

    # FINAL production rule: if no dirty conclusion, then clean enough
    rules.append(
        Rule(
            "DR PROD: clean enough",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output(f"Machine is clean enough to continue production"),
        )
    )

    return rules


def dryer_cleaning_rules():
    rules = []

    #  max runtime by cycle type
    rules.append(
        Rule(
            "DR CLEAN: set min runtime wet cycle",
            lambda wm: wm.get("cycle") == "Wet",
            lambda wm: wm.assert_fact("min_runtime", DR_CLEAN_MIN_RUNTIME["Wet"]),
        )
    )

    rules.append(
        Rule(
            "DR CLEAN: set min runtime dry cycle",
            lambda wm: wm.get("cycle") == "Dry",
            lambda wm: wm.assert_fact("min_runtime", DR_CLEAN_MIN_RUNTIME["Dry"]),
        )
    )

    # IF run time < min run time THEN not clean + reason
    rules.append(
        Rule(
            "DR CLEAN: min runtime not reached",
            lambda wm: wm.get("min_runtime") is not None
                      and wm.get("run_time") is not None
                      and wm.get("run_time") < wm.get("min_runtime"),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Minimum cleaning time not yet reached: {wm.get("run_time")}/{wm.get("min_runtime")} h for {wm.get("cycle").lower()} cycle")
            ),
        )
    )

    # IF wet cycle AND pump power > max pump power THEN not yet clean
    rules.append(
        Rule(
            "DR CLEAN: pump power too high",
            lambda wm: (
                wm.get("cycle") == "Wet"
                and wm.get("curr_pump_power") is not None
                and (wm.get("curr_pump_power")/DR_MAX_PUMP_POWER) > DR_CLEAN_MAX_PERC_PUMP_POWER
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Pump power too high for wet cycle: {wm.get("curr_pump_power")} kW")
            ),
        )
    )

    # FINAL cleaning rule: if no 'not yet clean', then clean
    rules.append(
        Rule(
            "HE CLEAN: clean, stop cycle",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output("Machine is clean: Stop cleaning cycle"),
        )
    )

    return rules
