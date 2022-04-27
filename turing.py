from dataclasses import dataclass, field

@dataclass
class Tape:
    data : list
    position : int = field(default=1, init=False)
    
    # Init with a blank at the beginning and end
    def __post_init__(self):
        self.data.append("B")
        self.data.insert(0, "B")

    def read(self) -> str:
        """ Returns the character at the current tape position."""
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

    def perform_action(self, read : str, write : str, move_dir : str):
        """ Attempts to perform the action of a Turing Machine state transition.
            
            Parameters:
                `str` read - The required character to be read
                `str` write - The character to write onto the tape
                `str` move_dir` - The direction ("l", "r", "L", "R") to move the head
                    after the write operation. If not in the list, automatically choose
                    to move to the right.
        """
        if self.read() == read:
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
    """
    states : list
    """ Initial tape state """
    tape : Tape

    
