from dataclasses import dataclass, field
from typing import Dict, List # List required for versions 3.8 and below

@dataclass
class NFA:
    """Class defining a nondeterministic finite automaton (NFA)."""
    
    """ A list defining transitions between states.
        Each index in the list defines a states.
        The keys in each dict define the character used for the transition,
        and the values in each dict define to which nodes it will transition
        (each position in the binary string defines a state).
    """
    states: List[Dict[str, bytes]]

    """The states we start at, as bytes defined earlier."""
    startingStates: bytes

    """The current states we are on, as bytes defined earlier."""
    _currentStates: bytes = field(init=False)

    """The alphabet of all allowed characters within the NFA."""
    alphabet: List[str]

    """All accepting states, as bytes defined earlier."""
    acceptingStates: bytes 

    def __post_init__(self):
        print(f"Starting bytes: {bin(self.startingStates)}")
        self._currentStates = self.startingStates

    def transition(self, char : str):
        """Transitions to the next state based on an inputted char."""
        # throw exception if not in alphabet
        if not char in self.alphabet:
            print(f"Character {char} not found in the alphabet!")
            raise KeyError

        nextStates: bytes = 0
        stateCounter: int = 0        # Which state number we are on
        # Read from each bit, from right to left
        while self._currentStates != 0:
            # If the last bit is a one (there is a transition to this node)
            if (self._currentStates & 1) == 1:
                trans = self.states[stateCounter][char]
                print(f"Transition: q{stateCounter} -> {self.getStatesFromBytes(trans)}")
                # Bitwise Or on the states to transition to
                nextStates = nextStates | trans

            # Shave off the last bit
            self._currentStates = self._currentStates >> 1
            stateCounter += 1

        # And we're all done
        self._currentStates = nextStates
    
        print(f"Current bytes: {bin(self._currentStates)}")

    def getStatesFromBytes(self, seq : bytes) -> str:
        """Gets a formatted string of all the states representing the byte sequence."""
        stateStr = ""
        stateCounter = 0
        while seq != 0:
            if (seq & 1) == 1:
                # Don't add a comma if this is the first we're appending to the string
                comma = ", " if stateStr != "" else ""
                stateStr += f"{comma}q{stateCounter}"
            seq = seq >> 1
            stateCounter += 1

        return stateStr

    def isAccepting(self) -> bool:
        """Checks to see if the current state we are in is an accepting state."""
        # If, when we intersect (bitwise and), we get a 0, we have the empty set
        # If not (the intersected states are not empty), we have at least one state
        # in which we are accepting
        return self._currentStates & self.acceptingStates 

    def isStringInLanguage(self, string : str) -> bool:
        """Checks if a string is in the language defined by the DFA."""
        for char in string:
            self.transition(char)

        return self.isAccepting()

