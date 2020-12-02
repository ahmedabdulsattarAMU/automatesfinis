#!/usr/bin/env python3
"""
Read an automaton and a word, returns:
 * ERROR if non deterministic
 * YES if word is recognized
 * NO if word is rejected
"""

import automaton
import sys
import pdb  # for debugging

# if len(sys.argv) != 3:
#     usagestring = "Usage: {} <automaton-file.af> <word-to-recognize>"
#     automaton.error(usagestring.format(sys.argv[0]))
#
# automatonfile = sys.argv[1]
# word = sys.argv[2]

# Question 1

from automaton import Automaton


def isDeterministic(automaton: automaton.Automaton):
    return hasAcceptState(automaton) and not hasEpsilon(automaton) and hasUniqueTransition(automaton)


def hasAcceptState(automaton: automaton.Automaton):
    return len(automaton.acceptstates) > 0


def hasEpsilon(automaton: automaton.Automaton):
    return "%" in automaton.alphabet


def hasUniqueTransition(automaton: automaton.Automaton):
    for state in automaton.statesdict.values():
        for symbol in state.transitions:
            if len(list(automaton.statesdict[str(state)].transitions[str(symbol)])) > 1:
                return False
    return True


# tests

# source = """0 a 1
# 0 b 2
# 1 a 1
# 2 b 2
# A 0 1 2
# """
# automate = automaton.Automaton("automate")
# automate.from_txt(source)


# print("hasAcceptState:")
# print(hasAcceptState(automate))
#
# print("hasEpsilon:")
# print(hasEpsilon(automate))
#
# print("has a unique transition:")
# print(hasUniqueTransition(automate))
#
# print("is deterministic:")
# print(isDeterministic(automate))


# tests


# Question 2
from automaton import State
from customAutomaton import CustomAutomaton

inputIndex = 0


def isRecognizable(word: str, automaton: automaton.Automaton) -> bool:
    if len(word) < 1:
        return False

    global inputIndex
    inputIndex = 0

    return consume(automaton, word[inputIndex], automaton.initial, word)


def consume(automaton: automaton.Automaton, symbol: str, state: State, word) -> bool:
    try:
        nextState = getNextState(automaton, state, symbol)
    except:
        return False

    if endOfInput(word):  # if we reach the last symbol of the word
        return state.is_accept  # we check if the current state is a final state
    return consume(automaton, nextSymbol(word), nextState, word)


def endOfInput(word: str) -> bool:
    global inputIndex
    return inputIndex == len(word) - 1


def getNextState(automaton: automaton.Automaton, state: State, symbol):
    transitionsDict = automaton.statesdict[state.name].transitions
    if symbol in transitionsDict:
        return list(transitionsDict[symbol].keys())[0]

    raise Exception("No next state")


def nextSymbol(word: str) -> str:
    global inputIndex
    inputIndex += 1
    return word[inputIndex]


source = """0 a 1
0 b 2
1 a 1
2 b 2
A 0 1 2
"""


# automate = CustomAutomaton("automate")
# automate.from_txt(source)

# tests

# automate = automaton.Automaton("automate")
# automate.from_txt(source)
# word = "bb"
# print(isRecognizable(word, automate))

# %%

# Quesiton 3

def checkFromFile(fileName: str, word: str):
    automata = automaton.Automaton(fileName)
    automata.from_txtfile(fileName)

    if not isDeterministic(automata):
        print("ERROR")
        return

    if isRecognizable(word, automata):
        print("YES")
    else:
        print("NO")


#checkFromFile(automatonfile, word)
