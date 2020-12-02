from typing import List, Tuple

import automaton
import tp1automates

# !/usr/bin/env python3
"""
Read an automaton and a word, returns:
 * ERROR if non deterministic
 * YES if word is recognized
 * NO if word is rejected
"""

# !/usr/bin/env python3
"""
Read an automaton and a word, returns:
 * YES if word is recognized
 * NO if word is rejected
Determinises the automaton if it's non deterministic
"""

import automaton
import sys
import pdb  # for debugging
from tp1automates import *


# if len(sys.argv) != 3:
#   usagestring = "Usage: {} <automaton-file.af> <word-to-recognize>"
#   automaton.error(usagestring.format(sys.argv[0]))
#
# # automatonfile = sys.argv[1]
# # word = sys.argv[2]


def checkFromFile(fileName: str, word: str):
    automata = automaton.Automaton(fileName)
    automata.from_txtfile(fileName)

    if not isDeterministic(automata):
        makeDeterministic(automata)

    if isRecognizable(word, automata):
        print("YES")
    else:
        print("NO")


# checkFromFile(sys.argv[1], sys.argv[2])


def makeDeterministic(automaton: automaton.Automaton) -> automaton.Automaton:
    return automaton


def deleteEpsilons(automaton: automaton.Automaton):
    # loop through each epsilon transition, this transition has an origin state, a symbol and a destination state
    for transition in getTransitionsWithSymbol("%", automaton):
        # we just get the transitions outbound the destination state
        stateTransitions = getStateTransitions(transition[2], automaton)
        if transition[2] in automaton.acceptstates:
            automaton.make_accept(transition[0])
        # if the list stateTransitions is empty
        if not stateTransitions:
            automaton.remove_transition(transition[0], transition[1], transition[2])

        else:
            # we select the symbol of the first state (actually it doesn't matter which state as long it's coming away from the destination state
            stateSymbol = list(stateTransitions[0])[1]
            automaton.add_transition(transition[0], stateSymbol, list(stateTransitions[0])[2])
            automaton.remove_transition(transition[0], transition[1], transition[2])
    return automaton


def getTransitionsWithSymbol(symbol: str, automaton: automaton.Automaton) -> List[Tuple[str, str, str]]:
    listOfTransitions = []
    for transition in automaton.transitions:
        if transition[1] == symbol:
            listOfTransitions.append(transition)

    return listOfTransitions


def getStateTransitions(state: str, automaton: automaton.Automaton):
    listOfStateTransitions = []
    for transition in automaton.transitions:
        if transition[0] == state:
            listOfStateTransitions.append(transition)

    if listOfStateTransitions == None:
        raise Exception("there are no transitions from this state")

    return listOfStateTransitions


a = automaton.Automaton("a-epsilon")
source = """0 % 1
1 a 1
0 % 2
2 b 2
A 1 2
"""
a.from_txt(source)

print(deleteEpsilons(a))
