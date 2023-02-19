# python3

from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for n, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, n + 1))

        if next in ")]}":
            
            if not opening_brackets_stack:
                return n + 1
            
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return n + 1
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"

def main():
        do=input("F or I")
        if "F" in do:
            name = input("Enter file name: ")
            with open(name, "r", encoding="latinl") as file:
                text=file.read()
            mismatch = find_mismatch(text)
            
            if mismatch == "Success":
                print("Success")
                
            else:
                print(mismatch)
                
        elif "I" in do:
            text = input()
            mismatch = find_mismatch(text)
            
            if mismatch == "Sucess":
                print("Success")
                
            else:
                print(mismatch)

if ___name___ == "__main__":
    main() 
