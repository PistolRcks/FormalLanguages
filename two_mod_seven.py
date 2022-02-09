import sys
from dfa import DFA

def main():
    alpha = ["0", "1"]
    states = [
        { # State 0
            "0": 0,
            "1": 1
        },
        { # State 1
            "0": 2,
            "1": 3
        },
        { # State 2
            "0": 4,
            "1": 5
        },
        { # State 3
            "0": 6,
            "1": 0
        },
        { # State 4
            "0": 1,
            "1": 2
        },
        { # State 5
            "0": 3,
            "1": 4
        },
        { # State 6 
            "0": 5,
            "1": 6
        },
    ]
    acceptingStates = [2]


    tmsDFA = DFA(states=states, alphabet=alpha, acceptingStates=acceptingStates)
    stringIsInLanguage = False

    try:
        stringIsInLanguage = tmsDFA.isStringInLanguage(sys.argv[1])
    except KeyError:
        print("A character used in the string is not in the alphabet! Stopping prematurely.")
        return
    except IndexError:
        print("No string was inputted. Remember to input a string.")
        return
    except BaseException as err:
        print(f"An exception occurred. Stopping prematurely.\nException: {err}")
        return

    if stringIsInLanguage:
        print("Inputted string is in the language.")
    else:
        print("Inputted string is not in the language.")

if __name__ == "__main__":
    main()
