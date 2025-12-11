# heat exchanger
HE_MAX_PUMP_CAPACITY = 900 # L/h
HE_MAX_PUMP_POWER = 20 # kW

# heat exchanger: production state
HE_PROD_MAX_RUNTIME = {
    "Skim milk": 9.0,
    "Whole milk": 8.0,
    "Cream": 7.0,   
}

HE_PROD_MAX_TEMP_DIFF = 2.5  # °C
HE_PROD_MIN_PERC_PUMP_CAPACITY = 0.90

# heat exchanger: cleaning state
HE_CLEAN_MAX_TEMP_DIFF = 0.5   # °C
HE_CLEAN_MIN_TIME_AT_75 = 20.0   # min
HE_CLEAN_MAX_PERC_PUMP_POWER = 0.50  
HE_CLEAN_MAX_PRESSURE_DIFF = 0.5 # bar


# evaporator
EV_MAX_PUMP_CAPACITY = 1900 # L/h
EV_MAX_PUMP_POWER = 25 # kW

# evaporator: production state
EV_PROD_MAX_RUNTIME = {
    "Protein 0.5": 20.0,
    "Protein 4, Fat <= 4": 16.0,
    "Protein 4, Fat 8": 14.0
}

EV_PROD_MAX_TEMP_DIFF = 6.0 # °C
EV_PROD_MIN_PERC_PUMP_CAPACITY = 0.90
EV_PROD_MIN_PERC_DENSITY = 0.95 

# evoporator: cleaning state
EV_CLEAN_MIN_RUNTIME = 1.5 # h
EV_CLEAN_MAX_PERC_PUMP_POWER = 0.50
EV_CLEAN_MAX_TEMP_DIFF = 2.0 # °C


# dryer
DR_MAX_PUMP_POWER = 30 # kW
DR_MAX_PUMP_CAPACITY = 1000 # L/h

# dryer: production state
DR_PROD_MAX_DIFF_TEMP_DIFF = 0.85
DR_PROD_MIN_PERC_PUMP_CAPACITY = 0.90

# dryer: cleaning state
DR_CLEAN_MIN_RUNTIME = {
    "Wet": 1.0,
    "Dry": 3.0  
}

DR_CLEAN_MAX_PERC_PUMP_POWER = 0.5

# membranes


# membranes: production state


# membranes: cleaning state
