import sys

# List of state transitions
states = [
    { # State 0
        "a": [0, 1],
        "b": [0]
    },
    { # State 1
        "a": [2],
        "b": []
    },
    { # State 2
        "a": [2],
        "b": [2]
    },
]

# List of accepting states
accepting = [2]

def accepts(curState : int, inStr : str, pos : int) -> bool:
    """ Tests whether there is some path for the NFA to reach 
        an accepting state from the given state, reading the 
        given string at the given character position.

        Parameters:
            `int` curState - The current state.
            `str` inStr - The input string.
            `int` pos - The index of the next character to be read

        Returns:
            True if the NFA accepts on some path with the inputted string.
    """

    # No more to read, stop and check if the current state is an accepting one
    if pos == len(inStr):
        return curState in accepting

    c = inStr[pos] # Get next character
    nextStates = states[curState][c]

    # Spawn multiple recursions for each next possible state
    for state in nextStates:
        if accepts(state, inStr, pos + 1):
            return True # One recursion worked
        
    return False # Oops, it didn't work

# Apparently Python doesn't support overloading? Weird.
def acceptsStr(inStr : str) -> bool:
    """ Tests whether the NFA accepts the string.
        
        Parameters:
            `str` inStr - The string to check.

        Returns:
            True if the NFA accepts on some path with the inputted string.
    """

    return accepts(0, inStr, 0)

def main():
    stringIsInLanguage = acceptsStr(sys.argv[1])

    if stringIsInLanguage:
        print("Inputted string is in the language.")
    else:
        print("Inputted string is not in the language.")

if __name__ == "__main__":
    main()
