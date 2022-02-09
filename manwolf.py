from dfa import DFA
import sys

def main():
    alpha = ["m", "w", "g", "c"]
    states = [
        { # 0 - mwgc |
            "m": 10,
            "w": 10,
            "g": 1,
            "c": 10
        },
        { # 1 - wc | mg
            "m": 2,
            "w": 10,
            "g": 0,
            "c": 10
        },
        { # 2 - mwc | g
            "m": 1,
            "w": 3,
            "g": 10,
            "c": 4
        },
        { # 3 - c | mwg
            "m": 10,
            "w": 2,
            "g": 5,
            "c": 10
        },
        { # 4 - w | mgc
            "m": 10,
            "w": 10,
            "g": 6,
            "c": 2
        },
        { # 5 - mgc | w
            "m": 10,
            "w": 10,
            "g": 3,
            "c": 7
        },
        { # 6 - mgw | c
            "m": 10,
            "w": 7,
            "g": 4,
            "c": 10
        },
        { # 7 - g | mwc
            "m": 8,
            "w": 6,
            "g": 10,
            "c": 5
        },
        { # 8 - mg | wc
            "m": 7,
            "w": 10,
            "g": 9,
            "c": 10
        },
        { # 9 - | mwgc (accepting state)
            "m": 10,
            "w": 10,
            "g": 8,
            "c": 10
        },
        { # 10 - failstate
            "m": 10,
            "w": 10,
            "g": 10,
            "c": 10
        },
    ]
    acceptingStates = [9]

    mwgcDFA = DFA(states=states, alphabet=alpha, acceptingStates=acceptingStates)
    stringIsInLanguage = False

    try:
        stringIsInLanguage = mwgcDFA.isStringInLanguage(sys.argv[1])
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
        

if __name__ == '__main__':
    main()
