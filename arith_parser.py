import re
from time import sleep
from copy import copy

LOOKUP_TABLE = {
    #      +       -       *       /       (       )       double  $
    "t" : {"+" : ""     ,"-" : ""     ,"*" : ""     ,"/" : ""     ,"(" : "rT"   ,")" : ""     ,"d" : "rT"   ,"$" : ""},  # t->
    "T" : {"+" : "+rT"  ,"-" : "-rT"  ,"*" : ""     ,"/" : ""     ,"(" : ""     ,")" : "e"    ,"d" : ""     ,"$" : "e"}, # T->
    "r" : {"+" : ""     ,"-" : ""     ,"*" : ""     ,"/" : ""     ,"(" : "vR"   ,")" : ""     ,"d" : "vR"   ,"$" : ""},  # r->
    "R" : {"+" : "e"    ,"-" : "e"    ,"*" : "*vR"  ,"/" : "/vR"  ,"(" : ""     ,")" : "e"    ,"d" : ""     ,"$" : "e"}, # R->
    "v" : {"+" : ""     ,"-" : ""     ,"*" : ""     ,"/" : ""     ,"(" : "(t)"  ,")" : ""     ,"d" : "d"    ,"$" : ""}   # v->
}

ACCEPTED_CHARS = ["+", "-", "*", "/", "d", "(", ")", "$"]


# Slightly dangerous? Just found out python does PBR
# Pushes a string onto a stack, in reverse order
def pushString(stack : list, strToPush : str):
    for i,v in enumerate(strToPush):
        stack.append(strToPush[-i-1])


def main():
    stack : list = []   # Python doesn't *really* have a stack library, so we'll just
                        # use append (push) and pop on a list
    inStr : str = input("Input your mathematical expression:\n")
    
    # Replace doubles with the d character
    expr : str = re.sub(r"(\d+\.?\d*|\.d+)", "d", inStr)

    # $ is the one character we can't handle in the loop (since we need to look out for it)
    # However, we don't want users to input it
    if re.search(r"\$", expr):
        print(f"ERROR: Unintended character \"$\" in string. Please remove it, and try again.")
        return

    # add EOL char to the end of the expr
    expr += "$"

    pushString(stack, "t$")

    for i, char in enumerate(expr):
        stack_top = copy(stack[-1])
        if not char in ACCEPTED_CHARS:
            print(f"ERROR: Unintended character \"{char}\" in string. Please remove it, and try again.")
            return
        # Continue to process the current character until we end up pushing a matching terminal
        while char != stack_top:
            print(f"Char: {char}")
            print(f"Pre-push Stack: {stack}")
            # ignore epsilons
            if stack_top == "e":
                stack.pop()
            else:
                try:
                    # don't push empties!!! Immediately throw
                    if LOOKUP_TABLE[stack_top][char] == "":
                        raise Exception()

                    top_idx = len(stack) - 1
                    pushString(stack, LOOKUP_TABLE[stack_top][char])
                    stack.pop(top_idx)
                except:
                    print(f"Expression is incorrectly formatted.\nError: {expr[:i]} ^ {expr[i:-2]}")
                    return

            print(f"Post-push stack: {stack}\n")
            stack_top = copy(stack[-1]) # Copy instead of reference

        # Pop the terminal (but only get the top if the stack exists!)
        stack.pop()
        if stack:
            stack_top = copy(stack[-1])

    print("Mathematical expression is correctly formatted!")


if __name__ == "__main__":
    main()
