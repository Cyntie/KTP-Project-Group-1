from logic.rules.rule import Rule

from logic.facts import (
    EV_PROD_MAX_TEMP_DIFF,
    EV_MAX_PUMP_CAPACITY,
    EV_MAX_PUMP_POWER,
    EV_PROD_MIN_PERC_DENSITY,
    EV_PROD_MIN_PERC_PUMP_CAPACITY,
    EV_PROD_MAX_RUNTIME,
    EV_CLEAN_MAX_PERC_PUMP_POWER,
    EV_CLEAN_MIN_RUNTIME,
    EV_CLEAN_MAX_TEMP_DIFF
)

def evaporator_production_rules():
    rules = []

    rules.append(
    Rule(
        "EV PREP: compute temp_diff",
        lambda wm: wm.get("temp_diff") is None
                  and wm.get("temp_water_in") is not None
                  and wm.get("temp_product_out") is not None,
        lambda wm: wm.assert_fact("temp_diff", abs(wm.get("temp_water_in") - wm.get("temp_product_out")))
        )
    )

    #  max runtime by product (production state)
    rules.append(
        Rule(
            "EV PROD: set max runtime protein 0.5",
            lambda wm: wm.get("protein_content") == "0.5%",
            lambda wm: wm.assert_fact("max_runtime", EV_PROD_MAX_RUNTIME["Protein 0.5"]),
        )
    )

    rules.append(
        Rule(
            "Ev PROD: set max runtime protein 4 and fat <=4",
            lambda wm: wm.get("protein_content") == "4%"
            and (wm.get("fat_content") == "0.5%" or wm.get("fat_content") == "4%"),
            lambda wm: wm.assert_fact("max_runtime", EV_PROD_MAX_RUNTIME["Protein 4, Fat <= 4"]),
        )
    )

    rules.append(
        Rule(
            "EV PROD: set max runtime protein 4 and fat 8",
            lambda wm: wm.get("protein_content") == "4%"
            and wm.get("fat_content") == "8%",
            lambda wm: wm.assert_fact("max_runtime", EV_PROD_MAX_RUNTIME["Protein 4, Fat 8"]),
        )
    )

    # PRODUCTION STATE: diagnosis rules

    # IF run time > max run time THEN dirty + reason
    rules.append(
        Rule(
            "EV PROD: max runtime exceeded",
            lambda wm: wm.get("max_runtime") is not None
                      and wm.get("run_time") is not None
                      and wm.get("run_time") > wm.get("max_runtime"),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Max run time exceeded: {wm.get("run_time")}/{wm.get("max_runtime")} h.")
            ),
        )
    )    

    # IF pump power = 100% and pump capacity < minimum_percentage of set capacity THEN dirty
    rules.append(
        Rule(
            "EV PROD: pump capacity too low",
            lambda wm: (
                wm.get("curr_pump_capacity") is not None
                and wm.get("curr_pump_power") is not None
                and wm.get("curr_pump_power") >= EV_MAX_PUMP_POWER
                and wm.get("curr_pump_capacity") < EV_PROD_MIN_PERC_PUMP_CAPACITY * EV_MAX_PUMP_CAPACITY
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Pump capacity too low: {wm.get("curr_pump_capacity")} L/h. Should be: >= {EV_PROD_MIN_PERC_PUMP_CAPACITY * EV_MAX_PUMP_CAPACITY} L/h.")
            ),
        )
    )

    # IF temperature difference > 6 °C THEN dirty
    rules.append(
        Rule(
            "EV PROD: temperature difference too high",
            lambda wm: (
                wm.get("temp_diff") is not None
                and wm.get("temp_diff") > EV_PROD_MAX_TEMP_DIFF
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Temperature difference too high: {wm.get("temp_diff")} °C. Should be: <= {EV_PROD_MAX_TEMP_DIFF} °C.")
            ),
        )
    )

    # IF density is <= minimum_percentage of maximum density THEN dirty
    # modified so that when facts are missing, we won't have None/None => error
    rules.append(
        Rule(
            "EV PROD: density too low",
            lambda wm: (
                    wm.get("curr_density") is not None
                    and wm.get("max_density") is not None
                    and (wm.get("curr_density") / wm.get("max_density")) <= EV_PROD_MIN_PERC_DENSITY
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(
                    f"Density too low: {wm.get('curr_density')} kg/m³. "
                    f"Should be: {EV_PROD_MIN_PERC_DENSITY * wm.get('max_density')} - "
                    f"{wm.get('max_density')} kg/m³."
                )
            ),
        )

    )

    # FINAL production rule: if no dirty conclusion, then clean enough
    rules.append(
        Rule(
            "EV PROD: clean enough",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output("Machine is clean enough to continue production"),
        )
    )

    return rules


def evaporator_cleaning_rules():
    rules = []

    rules.append(
    Rule(
        "EV PREP: compute temp_diff",
        lambda wm: wm.get("temp_diff") is None
                  and wm.get("temp_water_in") is not None
                  and wm.get("temp_product_out") is not None,
        lambda wm: wm.assert_fact("temp_diff", abs(wm.get("temp_water_in") - wm.get("temp_product_out")))
        )
    )

    # IF runtime < min_runtime THEN not yet clean
    rules.append(
        Rule(
            "EV CLEAN: run time too short",
            lambda wm: (
                wm.get("run_time") is not None
                and wm.get("run_time") < EV_CLEAN_MIN_RUNTIME
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Minimum cleaning time not yet reached: {wm.get("run_time")}/{EV_CLEAN_MIN_RUNTIME} h.")
            ),
        )
    )

    # IF pump power > max pump power THEN not yet clean
    rules.append(
        Rule(
            "EV CLEAN: pump power too high",
            lambda wm: (
                wm.get("curr_pump_power") is not None
                and (wm.get("curr_pump_power")/EV_MAX_PUMP_POWER) > EV_CLEAN_MAX_PERC_PUMP_POWER
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Pump power too high: {wm.get("curr_pump_power")} kW. Should be: <= {EV_CLEAN_MAX_PERC_PUMP_POWER * EV_MAX_PUMP_POWER} kW.")
            ),
        )
    )

    # IF temperature difference > max temperature difference THEN not yet clean
    rules.append(
        Rule(
            "HE CLEAN: temp diff too high",
            lambda wm: (
                wm.get("temp_diff") is not None
                and wm.get("temp_diff") > EV_CLEAN_MAX_TEMP_DIFF
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Temperature difference too high: {wm.get("temp_diff")} °C. Should be: <= {EV_CLEAN_MAX_TEMP_DIFF}.")
            ),
        )
    )

    # FINAL cleaning rule: if no 'not yet clean', then clean
    rules.append(
        Rule(
            "EV CLEAN: clean, stop cycle",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output("Machine is clean: Stop cleaning cycle"),
        )
    )

    return rules