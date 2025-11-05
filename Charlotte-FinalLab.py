# Mealy Machine Transition Table
# Format: state : { input : (next_state, output) }

mealy = {
    'A': {'0': ('A', 'A'), '1': ('B', 'B')},
    'B': {'0': ('C', 'A'), '1': ('D', 'B')},
    'C': {'0': ('D', 'C'), '1': ('B', 'B')},
    'D': {'0': ('B', 'B'), '1': ('C', 'C')},
    'E': {'0': ('D', 'C'), '1': ('E', 'C')}
}

def run_mealy(input_str, start='A'):
    state = start
    output = ""
    for ch in input_str:
        state, out = mealy[state][ch]
        output += out
    return output


# Moore Machine Conversion
# State format: "BaseState/Output"

moore_transitions = {
    "A/A": {'0': "A/A", '1': "B/B"},
    "B/B": {'0': "C/A", '1': "D/B"},
    "C/A": {'0': "D/C", '1': "B/B"},
    "C/C": {'0': "D/C", '1': "B/B"},
    "D/B": {'0': "B/B", '1': "C/C"},
    "D/C": {'0': "B/B", '1': "C/C"},
    "E/C": {'0': "D/C", '1': "E/C"}
}

moore_output = {
    "A/A": "A",
    "B/B": "B",
    "C/A": "A",
    "C/C": "C",
    "D/B": "B",
    "D/C": "C",
    "E/C": "C"
}

def run_moore(input_str, start="A/A"):
    state = start
    output = moore_output[state]  # Moore outputs on state entry
    for ch in input_str:
        state = moore_transitions[state][ch]
        output += moore_output[state]
    return output


# --------------------------
# Test the required inputs
# --------------------------

inputs = ["00110", "11001", "1010110", "101111"]

print("Input\tMealy Output\tMoore Output")
for inp in inputs:
    print(inp, run_mealy(inp), run_moore(inp), sep="\t")
