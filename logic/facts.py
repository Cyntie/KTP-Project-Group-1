# heat exchanger: production state

HE_MAX_PUMP_CAPACITY = 900 # L/h
HE_MAX_PUMP_POWER = 20 # kW

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


# evaporator: production state
EV_MAX_PUMP_CAPACITY = 1900 # L/h
EV_MAX_PUMP_POWER = 25 # kW

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



