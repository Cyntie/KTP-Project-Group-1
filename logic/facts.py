# heat exchanger
HE_MAX_PUMP_CAPACITY = 900 # L/h
HE_MAX_PUMP_POWER = 20 # kW

# heat exchanger: production state
HE_PROD_MAX_RUNTIME = {
    "Skim milk": 9.0, # h
    "Whole milk": 8.0, # h
    "Cream": 7.0, # h   
}

HE_PROD_MAX_TEMP_DIFF = 2.5  # °C
HE_PROD_MIN_PERC_PUMP_CAPACITY = 0.90

# min and max values for user input
HE_PROD_MIN_POSSIBLE_RUNTIME = 0 # h
HE_PROD_MAX_POSSIBLE_RUNTIME = 10 # h
HE_PROD_MIN_POSSIBLE_WATER_IN_TEMP = 65  # °C
HE_PROD_MAX_POSSIBLE_WATER_IN_TEMP = 95  # °C
HE_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP = 60  # °C
HE_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP = 95  # °C

# heat exchanger: cleaning state
HE_CLEAN_MAX_TEMP_DIFF = 0.5   # °C
HE_CLEAN_MIN_TIME_AT_75 = 20.0   # min
HE_CLEAN_MAX_PERC_PUMP_POWER = 0.50  
HE_CLEAN_MAX_PRESSURE_DIFF = 0.5 # bar

# min and max values for user input
HE_CLEAN_MIN_POSSIBLE_75_RUNTIME = 0 # min
HE_CLEAN_MAX_POSSIBLE__75_RUNTIME = 45 # min
HE_CLEAN_MIN_POSSIBLE_PRESSURE = 0 # bar
HE_CLEAN_MAX_POSSIBLE_PRESSURE = 10 # bar
HE_CLEAN_MIN_POSSIBLE_WATER_IN_TEMP = 70  # °C
HE_CLEAN_MAX_POSSIBLE_WATER_IN_TEMP = 80  # °C
HE_CLEAN_MIN_POSSIBLE_PRODUCT_OUT_TEMP = 60  # °C
HE_CLEAN_MAX_POSSIBLE_PRODUCT_OUT_TEMP = 80  # °C


# evaporator
EV_MAX_PUMP_CAPACITY = 1900 # L/h
EV_MAX_PUMP_POWER = 25 # kW

# evaporator: production state
EV_PROD_MAX_RUNTIME = {
    "Protein 0.5": 20.0, # h
    "Protein 4, Fat <= 4": 16.0, # h
    "Protein 4, Fat 8": 14.0 # h
}

EV_PROD_MAX_TEMP_DIFF = 6.0 # °C
EV_PROD_MIN_PERC_PUMP_CAPACITY = 0.90
EV_PROD_MIN_PERC_DENSITY = 0.95 

# min and max values for user input
EV_PROD_MIN_POSSIBLE_RUNTIME = 0 # h
EV_PROD_MAX_POSSIBLE_RUNTIME = 24 # h
EV_PROD_MIN_POSSIBLE_DENSITY = 950 # kg/m3
EV_PROD_MAX_POSSIBLE_DENSITY = 1100 # kg/m3
EV_PROD_MIN_POSSIBLE_WATER_IN_TEMP = 50  # °C
EV_PROD_MAX_POSSIBLE_WATER_IN_TEMP = 90  # °C
EV_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP = 44  # °C
EV_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP = 90  # °C

# evoporator: cleaning state
EV_CLEAN_MIN_RUNTIME = 1.5 # h
EV_CLEAN_MAX_PERC_PUMP_POWER = 0.50
EV_CLEAN_MAX_TEMP_DIFF = 2.0 # °C

# min and max values for user input
EV_CLEAN_MIN_POSSIBLE_RUNTIME = 0 # h
EV_CLEAN_MAX_POSSIBLE_RUNTIME = 6 # h
EV_CLEAN_MIN_POSSIBLE_WATER_IN_TEMP = 70  # °C
EV_CLEAN_MAX_POSSIBLE_WATER_IN_TEMP = 80  # °C
EV_CLEAN_MIN_POSSIBLE_PRODUCT_OUT_TEMP = 60  # °C
EV_CLEAN_MAX_POSSIBLE_PRODUCT_OUT_TEMP = 80  # °C


# dryer
DR_MAX_PUMP_POWER = 30 # kW
DR_MAX_PUMP_CAPACITY = 1000 # L/h

# dryer: production state
DR_PROD_MAX_DIFF_TEMP_DIFF = 0.85
DR_PROD_MIN_PERC_PUMP_CAPACITY = 0.90

# min and max values for user input
DR_PROD_MIN_POSSIBLE_AIR_IN_TEMP = 170  # °C
DR_PROD_MAX_POSSIBLE_AIR_IN_TEMP = 230  # °C
DR_PROD_MIN_POSSIBLE_PRODUCT_OUT_TEMP = 25  # °C
DR_PROD_MAX_POSSIBLE_PRODUCT_OUT_TEMP = 50  # °C


# dryer: cleaning state
DR_CLEAN_MIN_RUNTIME = {
    "Wet": 1.0, # h
    "Dry": 3.0  # h
}

DR_CLEAN_MAX_PERC_PUMP_POWER = 0.5

# min and max values for user input
DR_CLEAN_MIN_POSSIBLE_RUNTIME = 0 # h
DR_CLEAN_MAX_POSSIBLE_RUNTIME = 4 # h

# membranes

# membranes: production state
ME_PROD_MAX_TMP = {
    "MF": 0.3, # bar
    "UF": 0.9, # bar
    "NF": 1.2, # bar
    "RO": 1.5 # bar
}

# min and max values for user input
ME_PROD_MIN_POSSIBLE_TMP = 0 # bar
ME_PROD_MAX_POSSIBLE_TMP = 25 # bar

# membranes: cleaning state
ME_CLEAN_MAX_TMP = {
    "MF": 0.15, # bar
    "UF": 0.5, # bar
    "NF": 0.8, # bar
    "RO": 1.0 # bar
}

ME_CLEAN_MIN_CWF = 100 # L/m²h

# min and max values for user input
ME_CLEAN_MIN_POSSIBLE_CWF = 0 # L/m2h
ME_CLEAN_MAX_POSSIBLE_CWF = 400 # L/m2h
ME_CLEAN_MIN_POSSIBLE_TMP = 0 # bar
ME_CLEAN_MAX_POSSIBLE_TMP = 25 # bar
