import sys
from nfa import NFA

# FIXME: Doesn't work right now

def main():
    alpha = ["0", "1"]

    states = [
        { # State: 876543210
            "0": 0b000010010, # >q1>q1, >q4>q4
            "1": 0b000100100  # >q1>q2, >q4>q5
        },
        { #        876543210 
            "0": 0b000000010, # >q1
            "1": 0b000000100  # >q2
        },
        { #        876543210
            "0": 0b000011010, # >q3, >q0>q1>q1, >q0>q4>q4
            "1": 0b000100110  # >q1, >q0>q1>q2, >q0>q4>q5
        },
        { #        876543210
            "0": 0b000010111, # >q2, >q2>q0, >q2>q0>q1, >q2>q0>q4
            "1": 0b000001000  # >q3
        },
        { #        876543210
            "0": 0b000010000, # >q4
            "1": 0b000100000  # >q5
        },
        { #        876543210
            "0": 0b001010010, # >q6, >q6>q0>q1, >q6>q0>q4
            "1": 0b010000000  # >q7
        },
        { #        876543210
            "0": 0b100010010, # >q8, >q0>q1>q1, >q0>q4>q4
            "1": 0b000110100  # >q4, >q0>q1>q2, >q0>q4>q5
        },
        { #        876543210
            "0": 0b000000000, # >q5
            "1": 0b001010010  # >q6, >q6>q0>q1, >q6>q0>q4 
        },
        { #        876543210
            "0": 0b010000000, # >q7
            "1": 0b100000000  # >q8
        },
    ]
    #          876543210
    start  = 0b000010011
    accept = 0b001000100


    omttmfNFA = NFA(states=states, alphabet=alpha, acceptingStates=accept, startingStates=start)
    stringIsInLanguage = False

    try:
        stringIsInLanguage = omttmfNFA.isStringInLanguage(sys.argv[1])
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
