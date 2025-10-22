# ===============================================
# Mealy and Moore Machine Simulator (OOP Version)
# Detects the sequence '01'
# ===============================================

class FiniteStateMachine:
    """Base class for both Mealy and Moore machines."""

    def __init__(self, states, start_state):
        self.states = states
        self.start_state = start_state

    def _print_header(self, machine_type, input_string):
        print(f"\n--- {machine_type} SIMULATION ---")
        print(f"Input: {input_string}")
        # The header must match the original output format
        print(f"{'Step':<5}{'State':<10}{'Input':<10}{'Next':<10}{'Output':<10}")
        print("-" * 45)


class MealyMachine(FiniteStateMachine):
    """Mealy Machine: Output depends on state + input."""

    # Slight change: Store transitions as a nested dictionary: states[current_state][input] = {'next': next_state, 'out': output}
    def process(self, input_string):
        self._print_header("MEALY MACHINE", input_string)
        current_state = self.start_state
        output_sequence = ""
        
        for step, symbol in enumerate(input_string, 1):
            # Accessing the transition data using the slightly modified structure
            transition_data = self.states[current_state][symbol]
            next_state = transition_data['next']
            out = transition_data['out']
            
            print(f"{step:<5}{current_state:<10}{symbol:<10}{next_state:<10}{out:<10}")
            output_sequence += out
            current_state = next_state
            
        # Slight change: Printing the final output slightly differently (using formatted string)
        print(f"Final Output: {output_sequence}\n") 
        return output_sequence


class MooreMachine(FiniteStateMachine):
    """Moore Machine: Output depends only on the current state."""

    # Helper method for clarity (slight change)
    def _get_next_state(self, current_state, symbol):
        return self.states[current_state][symbol]

    def process(self, input_string):
        self._print_header("MOORE MACHINE", input_string)
        current_state = self.start_state
        
        # Initial output based on the start state
        output_sequence = self.states[current_state]['out']
        
        for step, symbol in enumerate(input_string, 1):
            next_state = self._get_next_state(current_state, symbol) # Using the helper method
            out = self.states[next_state]['out']
            
            print(f"{step:<5}{current_state:<10}{symbol:<10}{next_state:<10}{out:<10}")
            output_sequence += out
            current_state = next_state
            
        print(f"Final Output: {output_sequence}\n")
        return output_sequence


class MachineVisualizer:
    """Optional: Displays machine diagrams (for clarity only)."""

    @staticmethod
    def show_diagrams():
        print("\n======================")
        print("      MEALY MACHINE")
        print("======================")
        print("(Outputs 'a' when '01' occurs, else 'b')\n")
        print(" A --0/b--> B --1/a--> C --0/b--> A")
        print(" ^     |               |")
        print(" |1/b   |0/b           |1/b")
        print(" +-----+----------------+\n")

        print("======================")
        print("      MOORE MACHINE")
        print("======================")
        print("(Outputs 'a' in state C)\n")
        print(" A(b) --0--> B(b) --1--> C(a) --0--> A(b)")
        print(" ^      |                |")
        print(" |1     |0               |1")
        print(" +------+----------------+\n")


# ===============================================
# MAIN EXECUTION
# ===============================================
if __name__ == "__main__":
    # MODIFIED MEALY STRUCTURE: Use a dictionary for state/output instead of a tuple
    mealy_transitions = {
        'A': {'0': {'next': 'B', 'out': 'b'}, '1': {'next': 'A', 'out': 'b'}},
        'B': {'0': {'next': 'B', 'out': 'b'}, '1': {'next': 'C', 'out': 'a'}},
        'C': {'0': {'next': 'A', 'out': 'b'}, '1': {'next': 'C', 'out': 'b'}}
    }

    # MOORE STRUCTURE is kept the same
    moore_transitions = {
        'A': {'0': 'B', '1': 'A', 'out': 'b'},
        'B': {'0': 'B', '1': 'C', 'out': 'b'},
        'C': {'0': 'A', '1': 'C', 'out': 'a'}
    }

    visualizer = MachineVisualizer()
    visualizer.show_diagrams()

    mealy = MealyMachine(mealy_transitions, start_state='A')
    moore = MooreMachine(moore_transitions, start_state='A')

    for seq in ["011001", "110011"]:
        mealy.process(seq)
        moore.process(seq)