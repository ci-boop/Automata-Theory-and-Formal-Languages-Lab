
def moore_machine_process(input_string):
    """
    Simulates the converted Moore Machine for a given input string.
    
    The Moore machine is defined by:
    1. Output tied to the State itself.
    2. Initial State: A_A (Initial Output: A)
    """

    # 1. Define the Moore Machine Transition Table: (input) -> next_state
    transitions = {
        'A_A': {'0': 'A_A', '1': 'B_B'},
        'B_B': {'0': 'C_A', '1': 'D_B'},
        'C_A': {'0': 'D_C', '1': 'B_B'},
        'D_B': {'0': 'B_B', '1': 'C_C'},
        'D_C': {'0': 'B_B', '1': 'C_C'},
        'C_C': {'0': 'D_C', '1': 'B_B'},
        'E_C': {'0': 'D_C', '1': 'E_C'}
    }

    # 2. Define the Output for each Moore State
    outputs = {
        'A_A': 'A', 'B_B': 'B', 'C_A': 'A', 'D_B': 'B', 
        'D_C': 'C', 'C_C': 'C', 'E_C': 'C'
    }

    current_state = 'A_A'
    
    # 3. Moore machine outputs the start state's output *before* processing any input.
    output_sequence = outputs[current_state] 
    
    # 4. Process the input string
    for char_input in input_string:
        if char_input not in ['0', '1']:
            # Handle invalid input gracefully
            return f"Invalid Input Character: {char_input}"

        # Transition to the next state
        current_state = transitions[current_state][char_input]

        # Append the new state's output
        output_sequence += outputs[current_state]

    return output_sequence

# --- Process the Required Inputs ---

input_tests = [
    "00110",
    "11001",
    "1010110",
    "101111"
]

print("--- Moore Machine Processing Results ---\n")
for test_input in input_tests:
    result = moore_machine_process(test_input)
    print(f"Input:  {test_input}")
    print(f"Output: {result}")
    # [cite_start]Display the output clearly in the format requested in the problem [cite: 4]
    print(f'"{test_input}","{result}"')
    print("-" * 35)