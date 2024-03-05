import json

class TuringMachine:

    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        self.states = config['states']
        self.alphabet = config['alphabet']
        self.tape_symbols = config['tape_symbols']
        self.transitions = config['transitions']
        self.current_state = config['initial_state']
        self.blank_symbol = config['blank_symbol']
        self.final_states = config['final_states']
    
    def step(self):
        
        current_symbol = self.tape[self.head_position]
        
        if (self.current_state, current_symbol) in self.transitions:
            
            next_state, write_symbol, move_direction = self.transitions[(self.current_state, current_symbol)]
            
            self.current_state = next_state
            
            self.tape[self.head_position] = write_symbol
            
            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1
            
            if self.head_position == len(self.tape):
                self.tape.append(self.blank_symbol)
            elif self.head_position == -1:
                self.tape.insert(0, self.blank_symbol)
            
            if self.current_state in self.final_states:
                return False  
            else:
                return True  
        else:
            return False  

    def read_input(self, input_file):
        with open(input_file, 'r') as f:
            word = f.read().strip()
        self.tape = [self.blank_symbol] + list(word) + [self.blank_symbol]
        self.head_position = 1

    def write_output(self, output_file):
        with open(output_file, 'w') as f:
            if self.current_state in self.final_states:
                f.write(''.join(self.tape).strip(self.blank_symbol) + 'a')
            else:
                f.write(''.join(self.tape).strip(self.blank_symbol) + 'r')

# tm = TuringMachine('tests.json')
tm = TuringMachine('tm_binarysum.json')
tm.read_input('input_word.txt')

while tm.step():
    pass

tm.write_output('output_word.txt')
