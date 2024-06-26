from dataclasses import dataclass, field

@dataclass
class Tape:
    data : list
    position : int = field(default=1, init=False)
    
    # Init with a blank at the beginning and end
    def __post_init__(self):
        self.data.append("B")
        self.data.insert(0, "B")

    def to_string(self) -> str:
        """ Returns the contents of the tape as a string. """
        string : str = ""
        for i, c in enumerate(self.data):
            string += c
            # Draw arrows around the head
            if i + 1 == self.position:
                string += ">"
            if i == self.position:
                string += "<"

        return string

    def read(self) -> str:
        """ Returns the character at the current tape position. """
        return self.data[self.position]

    def write(self, char : str):
        """ Writes a character `char` at the current tape position.
            Overwrites that character.
        """
        self.data[self.position] = char

    def move_right(self):
        """ Moves the tape head one to the right. 
            Appends a blank char if there are no more characters to read.
        """
        self.position += 1
        # Try to get the next character; if we fail, we know we must add a blank
        try:
            self.data[self.position]
        except:
            self.data.append("B")

    def move_left(self):
        """ Moves the tape head one to the left. 
            Prepends a blank char if there are no more characters to read.
        """
        self.position -= 1
        # Overshooting at the left will always lead to idx 0
        if self.position == -1:
            self.data.insert(0, "B")
            # If we overshoot at the left, it's always at zero
            self.position = 0

    def perform_action(self, write : str, move_dir : str):
        """ Attempts to perform the action of a Turing Machine state transition.
            
            Parameters:
                `str` write - The character to write onto the tape
                `str` move_dir` - The direction ("l", "r", "L", "R") to move the head
                    after the write operation. If not in the list, automatically choose
                    to move to the right.
        """
        self.write(write)
        if move_dir.upper() == "L":
            self.move_left()
        else:
            self.move_right()

@dataclass
class TuringMachine():

    """ The list of the states of the Turing Machine. 
        States are formatted as:
            {
                "<char_to_read0>" : <StateTransition0>,
                "<char_to_read1>" : <StateTransition1>,
                ...
            }
        StateTransitions are a three-tuple:
            (
                "<char_to_write>",
                "<char_direction_to_move>",   # Only "L", "R", "l", or "r"
                <int_state_to_transition>
            )
        State 0 is always the starting state.
    """
    states : list
    """ Tape with which to use the Turing Machine. """
    tape : Tape
    """ List of ints which describes which states are accepting. """
    accepting_states : list
    """ The current state we are in. """
    current_state : int = field(default=0, init=False)
    """ Whether or not the Turing Machine has halted. """
    is_halted : bool = field(default=False, init=False)

    def is_accepting(self) -> bool:
        """ Returns whether or not the Turing Machine is in an accepting state. """
        return self.current_state in self.accepting_states

    def evaluate_step(self):
        """ Evaluates one step of the Turing Machine. """
        print(f"Current tape: {self.tape.to_string()}, state {self.current_state}")
        # Check if we can transition with this character
        tape_char = self.tape.read()
        if tape_char in self.states[self.current_state].keys() and not self.is_halted:
            # Apply the transition
            transition = self.states[self.current_state][tape_char]
            self.tape.perform_action(transition[0], transition[1])
            self.current_state = transition[2]
            # Halt on accepting states
            if self.is_accepting():
                self.is_halted = True
        # Otherwise halt
        else:
            self.is_halted = True

    def evaluate_until_halted(self) -> bool:
        """ Evaluates the Turing Machine until it halts.
            Returns whether or not the Turing Machine halted on an accepting state.
        """
    
        while not self.is_halted:
            self.evaluate_step()

        return self.is_accepting()
        
    
