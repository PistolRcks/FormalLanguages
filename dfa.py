from dataclasses import dataclass, field
from typing import Dict

@dataclass
class DFA:
    """Class defining a deterministic finite automaton (DFA)."""
    
    """ A list defining transitions between states.
        Each index in the list defines a states.
        The keys in each dict define the character used for the transition,
        and the values in each dict define to what node it will transition.
        Each dict should provide a transition for each character in the 
        alphabet, but this is not checked.
    """
    states: list[Dict[str, int]]

    """The state we are currently on. Starts at zero."""
    _currentState: int = field(default=0, init=False)

    """The alphabet of all allowed characters within the DFA."""
    alphabet: list[str]

    """The list of all accepting states."""
    acceptingStates: list[int]

    def transition(self, char : str):
        """Transitions to the next state based on an inputted char."""
        # throw exception if not in alphabet
        if not char in self.alphabet:
            print(f"Character {char} not found in the alphabet!")
            raise KeyError

        self._currentState = self.states[self._currentState][char]
    
    def isAccepting(self) -> bool:
        """Checks to see if the current state we are in is an accepting state."""
        return self._currentState in self.acceptingStates

    def isStringInLanguage(self, string : str) -> bool:
        """Checks if a string is in the language defined by the DFA."""
        for char in string:
            self.transition(char)

        return self.isAccepting()

