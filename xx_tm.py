from turing import TuringMachine, Tape

def string_to_tape(inp : str) -> Tape:
    """ Returns the Tape which represents the input `inp` string. """
    arr : list = []
    for c in inp:
        arr.append(c)

    return Tape(arr)

def main():
    inp = input("Please input your starting string (\"a\"s and \"b\"s only accepted):\n")

    tape = string_to_tape(inp) 
    machine = TuringMachine([
        # Routine 1: Determine evenness
        { # State 0: Mark the character as part of the first group; move on if we meet a character of the second group
            "a": ("c", "R", 1),
            "b": ("d", "R", 1),
            "C": ("C", "L", 4),
            "D": ("D", "L", 4),
        },
        { # State 1: Move right; stop and move back upon reaching B or a character of the second group
            "a": ("a", "R", 1),
            "b": ("b", "R", 1),
            "B": ("B", "L", 2),
            "C": ("C", "L", 2),
            "D": ("D", "L", 2),
        },
        { # State 2: Mark the character as part of the second group; move on if we immediately meet a character of the first group
            "a": ("C", "L", 3),
            "b": ("D", "L", 3),
        },
        { # State 3: Move back left until we hit an already marked character
            "c": ("c", "R", 0),
            "d": ("d", "R", 0),
            "a": ("a", "L", 3),
            "b": ("b", "L", 3),
        },
        # Transition...
        { # State 4: Move back to the beginning; move right until we hit a right
            "c": ("c", "L", 4),
            "d": ("d", "L", 4),
            "B": ("B", "R", 5),
        },
        # Routine 2: Determine duplicity
        { # State 5: Mark with an X; split paths based on original "a" or "b"
            "c": ("X", "R", 6),
            "d": ("X", "R", 7),
        },
        { # State 6: ["a" Side] - Continue until reaching an original "a" from group 2; mark with Y, move left
            "c": ("c", "R", 6),
            "d": ("d", "R", 6),
            "Y": ("Y", "R", 6),
            "C": ("Y", "L", 8),
        },
        { # State 7: ["b" Side] - Continue until reaching an original "b" from group 2; mark with Y, move left
            "c": ("c", "R", 7),
            "d": ("d", "R", 7),
            "Y": ("Y", "R", 7),
            "D": ("Y", "L", 9),
        },
        { # State 8: ["a" Side] - Move to accepting if we immediately hit an X; Otherwise move past Y's until we get to group 1 characters (could probably be combined with 9)
            "Y": ("Y", "L", 8),
            "c": ("c", "L", 10),
            "d": ("d", "L", 10),
            "X": ("X", "R", 11),
        },
        { # State 9: ["b" Side] - Move to accepting if we immediately hit an X; Otherwise move past Y's until we get to group 1 characters
            "Y": ("Y", "L", 8),
            "c": ("c", "L", 10),
            "d": ("d", "L", 10),
            "X": ("X", "R", 11),
        },
        { # State 10: Return to the group 1 character after the latest X
            "c": ("c", "L", 10),
            "d": ("d", "L", 10),
            "X": ("X", "R", 5)
        },
        { # State 11: Accepting State; should be the same number of X's and Y's, with X's on the left side and Y's on the right
        },
    ], tape, [11])

    result = machine.evaluate_until_halted()

    if result:
        print("Ended in an accepting state.")
    else:
        print("Did not end in an accepting state.")

if __name__ == "__main__":
    main()
