from turing import TuringMachine, Tape

def main():
    tape = Tape(["a", "a", "a"])
    # Simple turing machine that turns a's into blanks and ends when we hit a blank
    machine = TuringMachine([
        {
            "a" : ("B", "R", 0),
            "B" : ("B", "R", 1)
        },
        {}
    ], tape, [1])

    result = machine.evaluate_until_halted()

    if result:
        print("Ended in an accepting state.")
    else:
        print("Did not end in an accepting state.")

if __name__ == "__main__":
    main()
