import sys


def interpret(program, input='', memsize=1024):
    pointers = [0] * memsize
    currentPointer = 0
    currentCommand = 0
    currentInput = 0
    while currentCommand < len(program):
        if program[currentCommand] == '>':
            currentPointer += 1
        elif program[currentCommand] == '<':
            currentPointer -= 1
        elif program[currentCommand] == '+':
            pointers[currentPointer] += 1
        elif program[currentCommand] == '-':
            pointers[currentPointer] -= 1
        elif program[currentCommand] == '.':
            sys.stdout.write(chr(pointers[currentPointer]))
        elif program[currentCommand] == ',':
            if currentInput >= len(input):
                return
            else:
                pointers[currentPointer] = ord(input[currentInput])
            currentInput += 1
        elif program[currentCommand] == '[':
            i = 0
            if pointers[currentPointer] == 0:
                currentCommand += 1
                while program[currentCommand] != ']' or i != 0:
                    if program[currentCommand] == '[':
                        i += 1
                    elif program[currentCommand] == ']':
                        i -= 1
                    currentCommand += 1
        elif program[currentCommand] == ']':
            i = 0
            if pointers[currentPointer] != 0:
                currentCommand -= 1
                while program[currentCommand] != '[' or i != 0:
                    if program[currentCommand] == ']':
                        i += 1
                    elif program[currentCommand] == '[':
                        i -= 1
                    currentCommand -= 1
        currentCommand += 1

#interpret("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
#interpret(" ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")
