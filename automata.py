#Number 1
def dfa_accepts_1(string):
    state = 'a'  # start state
    
    for symbol in string:
        if state == 'a':
            if symbol == 0:
                state = 'a'
            elif symbol == 1:
                state = 'b'
            else:
                return False  # invalid symbol
        elif state == 'b':
            if symbol == 0:
                state = 'end'
            elif symbol == 1:
                state = 'a'
            else:
                return False
        elif state == 'end':
            if symbol == 0:
                state = 'b'
            elif symbol == 1:
                state = 'end'
            else:
                return False
        else:
            return False  # invalid state
    
    # Define accepting states
    accepting_states = {'end'}
    
    return state in accepting_states

# Original test cases
accepted_1 = [[0,1,0], [1,0,1], [0,1,0,1]]
rejected_1 = [[0,1,0,1,0], [1,0,0,1], [1,0,0,1,0]]

print("Testing accepted Number 1:")
for s in accepted_1:
    result = "Accepted" if dfa_accepts_1(s) else "Rejected"
    print(f"{s}: {result}")

print("\nTesting rejected Number 1:")
for s in rejected_1:
    result = "Accepted" if dfa_accepts_1(s) else "Rejected"
    print(f"{s}: {result}")

#Number 2

def dfa_accepts_2(string):
    state = 'q0'  # start and accepting state
    
    for symbol in string:
        if state == 'q0':
            if symbol == 'a':
                state = 'q1'
            elif symbol == 'b':
                state = 'q2'
            else:
                return False
        elif state == 'q1':
            if symbol == 'a':
                state = 'q0'
            elif symbol == 'b':
                state = 'q3'
            else:
                return False
        elif state == 'q2':
            if symbol == 'a':
                state = 'q3'
            elif symbol == 'b':
                state = 'q0'
            else:
                return False
        elif state == 'q3':
            if symbol == 'a':
                state = 'q2'
            elif symbol == 'b':
                state = 'q1'
            else:
                return False
        else:
            return False

    accepting_states = {'q0', 'q3'}
    return state in accepting_states

# Test cases
accepted_2 = [['a','b'], ['a','b','a','a'], ['a','b','a','b']]
rejected_2 = [['a','b','b'], ['a','b','a'], ['a','b','a','b','b']]

print("Testing accepted Number 2:")
for s in accepted_2:
    result = "Accepted" if dfa_accepts_2(s) else "Rejected"
    print(f"{s}: {result}")

print("\nTesting rejected Number 2:")
for s in rejected_2:
    result = "Accepted" if dfa_accepts_2(s) else "Rejected"
    print(f"{s}: {result}")

