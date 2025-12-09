# heat exchanger: production state

HE_SET_PUMP_CAPACITY = 900 # L/h
HE_SET_PUMP_POWER = 20 # kW

HE_PROD_MAX_RUNTIME = {
    "Skim milk": 9.0,
    "Whole milk": 8.0,
    "Cream": 7.0,   
}

HE_PROD_TEMP_DIFF_LIMIT = 2.5  # °C

# heat exchanger: cleaning state
HE_CLEAN_TEMP_DIFF_LIMIT = 0.5   # °C
HE_CLEAN_MIN_TIME_AT_75 = 20.0   # min
HE_CLEAN_MAX_PUMP_POWER = 50.0   # %
HE_CLEAN_MAX_PRESSURE_DIFF = 0.5 # (some units)

