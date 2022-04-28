import sys


# Retrieve the data from the 20 shares list for the brute force.
data = [
    {"name": "action1", "cout": 20, "benefice": 5},
    {"name": "action2", "cout": 30, "benefice": 10},
    {"name": "action3", "cout": 50, "benefice": 15},
    {"name": "action4", "cout": 70, "benefice": 20},
    {"name": "action5", "cout": 60, "benefice": 17},
    {"name": "action6", "cout": 80, "benefice": 25},
    {"name": "action7", "cout": 22, "benefice": 7},
    {"name": "action8", "cout": 26, "benefice": 11},
    {"name": "action9", "cout": 48, "benefice": 13},
    {"name": "action10", "cout": 34, "benefice": 27},
    {"name": "action11", "cout": 42, "benefice": 17},
    {"name": "action12", "cout": 110, "benefice": 9},
    {"name": "action13", "cout": 38, "benefice": 23},
    {"name": "action14", "cout": 14, "benefice": 1},
    {"name": "action15", "cout": 18, "benefice": 3},
    {"name": "action16", "cout": 8, "benefice": 8},
    {"name": "action17", "cout": 4, "benefice": 12},
    {"name": "action18", "cout": 10, "benefice": 14},
    {"name": "action19", "cout": 24, "benefice": 21},
    {"name": "action20", "cout": 114, "benefice": 18}
]

data_size = sys.getsizeof(data)

print("Here is the size of data list object in memory: " + str(data_size) + " bytes")
