from logic.rules.rule import Rule

from logic.facts import (
    ME_PROD_MAX_TMP,
    ME_CLEAN_MAX_TMP,
    ME_CLEAN_MIN_CWF
)

def membranes_production_rules():
    rules = []

    #  max tmp by membrane type
    rules.append(
        Rule(
            "ME PROD: set max tmp MF",
            lambda wm: wm.get("membrane") == "Micro Filtration",
            lambda wm: wm.assert_fact("max_tmp", ME_PROD_MAX_TMP["MF"]),
        )
    )

    rules.append(
        Rule(
            "ME PROD: set max tmp UF",
            lambda wm: wm.get("membrane") == "Ultra Filtration",
            lambda wm: wm.assert_fact("max_tmp", ME_PROD_MAX_TMP["UF"]),
        )
    )

    rules.append(
        Rule(
            "ME PROD: set max tmp NF",
            lambda wm: wm.get("membrane") == "Nano Filtration",
            lambda wm: wm.assert_fact("max_tmp", ME_PROD_MAX_TMP["NF"]),
        )
    )

    rules.append(
        Rule(
            "ME PROD: set max tmp RO",
            lambda wm: wm.get("membrane") == "Reversed Osmosis",
            lambda wm: wm.assert_fact("max_tmp", ME_PROD_MAX_TMP["RO"]),
        )
    )

    # PRODUCTION STATE: diagnosis rules

    # IF tmp > max tmp THEN dirty + reason
    rules.append(
        Rule(
            "ME PROD: max TMP exceeded",
            lambda wm: wm.get("max_tmp") is not None
                      and wm.get("curr_tmp") is not None
                      and wm.get("curr_tmp") > wm.get("max_tmp"),
            lambda wm: (
                wm.set_output("Machine is dirty: Stop production"),
                wm.add_reason(f"Max TMP exceeded: {wm.get("curr_tmp")} mbar. Should be: <= {wm.get("max_tmp")} mbar for {wm.get("membrane")}.")
            ),
        )
    )

    # FINAL production rule: if no dirty conclusion, then clean enough
    rules.append(
        Rule(
            "ME PROD: clean enough",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output("Machine is clean enough to continue production"),
        )
    )

    return rules


def membranes_cleaning_rules():
    rules = []

#  max tmp by membrane type
    rules.append(
        Rule(
            "ME CLEAN: set max tmp MF",
            lambda wm: wm.get("membrane") == "Micro Filtration",
            lambda wm: wm.assert_fact("max_tmp", ME_CLEAN_MAX_TMP["MF"]),
        )
    )

    rules.append(
        Rule(
            "ME CLEAN: set max tmp UF",
            lambda wm: wm.get("membrane") == "Ultra Filtration",
            lambda wm: wm.assert_fact("max_tmp", ME_CLEAN_MAX_TMP["UF"]),
        )
    )

    rules.append(
        Rule(
            "ME CLEAN: set max tmp NF",
            lambda wm: wm.get("membrane") == "Nano Filtration",
            lambda wm: wm.assert_fact("max_tmp", ME_CLEAN_MAX_TMP["NF"]),
        )
    )

    rules.append(
        Rule(
            "ME CLEAN: set max tmp RO",
            lambda wm: wm.get("membrane") == "Reversed Osmosis",
            lambda wm: wm.assert_fact("max_tmp", ME_CLEAN_MAX_TMP["RO"]),
        )
    )

    # PRODUCTION STATE: diagnosis rules

    # IF tmp > max tmp THEN not yet clean + reason
    rules.append(
        Rule(
            "ME CLEAN: max TMP exceeded",
            lambda wm: wm.get("max_tmp") is not None
                      and wm.get("curr_tmp") is not None
                      and wm.get("curr_tmp") > wm.get("max_tmp"),
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"Max TMP exceeded: {wm.get("curr_tmp")} mbar. Should be: <= {wm.get("max_tmp")} mbar for {wm.get("membrane")}.")
            ),
        )
    )

    # IF cwf < min cwf THEN not yet clean + reason
    rules.append(
        Rule(
            "ME CLEAN: min CWF not yet reached",
            lambda wm: wm.get("curr_cwf") is not None
                      and wm.get("curr_cwf") < ME_CLEAN_MIN_CWF,
            lambda wm: (
                wm.set_output("Machine is not yet clean"),
                wm.add_reason(f"CWF too low: {wm.get("curr_cwf")} L/m²h. Should be: >= {ME_CLEAN_MIN_CWF} L/m²h.")
            ),
        )
    )


    # FINAL cleaning rule: if no 'not yet clean', then clean
    rules.append(
        Rule(
            "ME CLEAN: clean, stop cycle",
            lambda wm: wm.output_text is None,
            lambda wm: wm.set_output("Machine is clean: Stop cleaning cycle"),
        )
    )

    return rules