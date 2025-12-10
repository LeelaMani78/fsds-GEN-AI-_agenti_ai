import random

# Define the U.S. states and their neighbors
states = {
    'WA': ['OR', 'ID'],
    'OR': ['WA', 'ID', 'CA', 'NV'],
    'CA': ['OR', 'NV', 'AZ'],
    'ID': ['WA', 'OR', 'MT', 'WY', 'UT', 'NV'],
    'NV': ['OR', 'ID', 'UT', 'AZ'],
    'AZ': ['CA', 'NV', 'UT'],
    'UT': ['ID', 'NV', 'AZ', 'CO', 'WY'],
    'MT': ['ID', 'ND', 'SD', 'WY'],
    'WY': ['MT', 'SD', 'NE', 'CO', 'UT', 'ID'],
    'CO': ['WY', 'NE', 'KS', 'OK', 'NM', 'UT'],
    'NM': ['CO', 'OK', 'TX', 'AZ']
    # we can add more states if we needed 
}

# The colours 
colors = ['R', 'G', 'B', 'Y']

def is_valid_color(state, color):
    for neighbor in states[state]:
        if state_colors.get(neighbor) == color:
            return False
    return True

def color_states(state_index):
    if state_index == len(states):
        return True  # the states we have taken are coloured 
    
    state = list(states.keys())[state_index]
    for color in colors:
        if is_valid_color(state, color):
            state_colors[state] = color
            if color_states(state_index + 1):
                return True
            state_colors[state] = None  # Backtrack
    return False

state_colors = {state: None for state in states}
random.shuffle(list(states.keys()))  # Shuffle the order of states for variety
if color_states(0):
    print("Map coloring is successful. Final mapping:")
    for state, color in state_colors.items():
        print(f"{state}: {color}")
else:
    print("No valid coloring found with the given constraints.")
