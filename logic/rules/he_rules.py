from logic.rules.rule import Rule

from logic.facts import (
    HE_PROD_MAX_RUNTIME,
    HE_PROD_MAX_TEMP_DIFF,
    HE_CLEAN_MAX_TEMP_DIFF,
    HE_CLEAN_MIN_TIME_AT_75,
    HE_CLEAN_MAX_PRESSURE_DIFF,
    HE_CLEAN_MAX_PERC_PUMP_POWER,
    HE_MAX_PUMP_CAPACITY,
    HE_PROD_MIN_PERC_PUMP_CAPACITY,
    HE_MAX_PUMP_POWER
)


def heat_exchanger_production_rules():
    rules = []

    rules.append(
    Rule(
        "HE PREP: compute temp_diff",
        lambda wm: wm.get("temp_diff") is None
                  and wm.get("temp_water_in") is not None
                  and wm.get("temp_product_out") is not None,
        lambda wm: wm.assert_fact("temp_diff", abs(wm.get("temp_water_in") - wm.get("temp_product_out")))
        )
    )


    #  max runtime by product (production state)
    rules.append(
        Rule(
            "HE PROD: set max runtime skim",
            lambda wm: wm.get("product") == "Skim milk",
            lambda wm: wm.assert_fact("max_runtime", HE_PROD_MAX_RUNTIME["Skim milk"]),
        )
    )

    rules.append(
        Rule(
            "HE PROD: set max runtime whole milk",
            lambda wm: wm.get("product") == "Whole milk",
            lambda wm: wm.assert_fact("max_runtime", HE_PROD_MAX_RUNTIME["Whole milk"]),
        )
    )

    rules.append(
        Rule(
            "HE PROD: set max runtime cream",
            lambda wm: wm.get("product") == "Cream",
            lambda wm: wm.assert_fact("max_runtime", HE_PROD_MAX_RUNTIME["Cream"]),
        )
    )

    # PRODUCTION STATE: diagnosis rules

    # IF run time > max run time THEN dirty + reason
    rules.append(
        Rule(
            "HE PROD: max runtime exceeded",
            lambda wm: wm.get("max_runtime") is not None
                      and wm.get("run_time") is not None
                      and wm.get("run_time") > wm.get("max_runtime"),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Max run time exceeded: {wm.get("max_runtime")} h")
            ),
        )
    )

    # IF pump power = 100% and pump capacity < minimum_percentage of set capacity THEN dirty
    rules.append(
        Rule(
            "HE PROD: pump capacity too low",
            lambda wm: (
                wm.get("curr_pump_capacity") is not None
                and wm.get("curr_pump_power") is not None
                and wm.get("curr_pump_power") >= HE_MAX_PUMP_POWER
                and wm.get("curr_pump_capacity") < HE_PROD_MIN_PERC_PUMP_CAPACITY * HE_MAX_PUMP_CAPACITY
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Pump capacity too low: {wm.get("curr_pump_capacity")} L/h")
            ),
        )
    )


    # IF temperature difference > 2.5 °C THEN dirty
    rules.append(
        Rule(
            "HE PROD: temperature difference too high",
            lambda wm: (
                wm.get("temp_diff") is not None
                and wm.get("temp_diff") > HE_PROD_MAX_TEMP_DIFF
            ),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Temperature difference too high: {wm.get("temp_diff")} °C")
            ),
        )
    )

    # FINAL production rule: if no dirty conclusion, then clean enough
    rules.append(
        Rule(
            "HE PROD: clean enough",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output("Machine is clean enough to continue production"),
        )
    )
    return rules



def heat_exchanger_cleaning_rules():
    rules = []

    rules.append(
    Rule(
        "HE PREP: compute temp_diff",
        lambda wm: wm.get("temp_diff") is None
                  and wm.get("temp_water_in") is not None
                  and wm.get("temp_product_out") is not None,
        lambda wm: wm.assert_fact("temp_diff", abs(wm.get("temp_water_in") - wm.get("temp_product_out")))
        )
    )

    
    rules.append(
    Rule(
        "HE PREP: compute pressure_diff",
        lambda wm: wm.get("pressure") is None
                  and wm.get("start_pressure") is not None
                  and wm.get("end_pressure") is not None,
        lambda wm: wm.assert_fact("pressure_diff", abs(wm.get("end_pressure") - wm.get("start_pressure")))
        )
    )


    # IF temperature difference > max temperature difference THEN not yet clean
    rules.append(
        Rule(
            "HE CLEAN: temp diff too high",
            lambda wm: (
                wm.get("temp_diff") is not None
                and wm.get("temp_diff") > HE_CLEAN_MAX_TEMP_DIFF
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Temperature difference too high: {wm.get("temp_diff")} °C")
            ),
        )
    )

    # IF pump power > max pump power THEN not yet clean
    rules.append(
        Rule(
            "HE CLEAN: pump power too high",
            lambda wm: (
                wm.get("curr_pump_power") is not None
                and (wm.get("curr_pump_power")/HE_MAX_PUMP_POWER) > HE_CLEAN_MAX_PERC_PUMP_POWER
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Pump power too high: {wm.get("curr_pump_power")} kW")
            ),
        )
    )

    # IF pressure difference > max pressurde difference THEN not yet clean
    rules.append(
        Rule(
            "HE CLEAN: pressure diff too high",
            lambda wm: (
                wm.get("pressure_diff") is not None
                and wm.get("pressure_diff") > HE_CLEAN_MAX_PRESSURE_DIFF
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Pressure difference too high: {wm.get("pressure_diff")} bar")
            ),
        )
    )

    # IF 75 °C time < 20 THEN not yet clean
    rules.append(
        Rule(
            "HE CLEAN: time at 75 too short",
            lambda wm: (
                wm.get("time_at_75") is not None
                and wm.get("time_at_75") < HE_CLEAN_MIN_TIME_AT_75
            ),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Machine has not cleaned for at least {HE_CLEAN_MIN_TIME_AT_75} minutes at 75 °C")
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

