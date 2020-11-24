from automaton import Automaton
from automaton import State


class CustomAutomaton(Automaton):
    _word: str
    _inputIndex: int = 0

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def isRecognizable(self, word: str) -> bool:
        if len(word) < 1:
            return False

        _inputIndex = 0

        self._word = word
        return self._consume(word[0], self.initial)

    def _consume(self, symbol: str, state: State) -> bool:
        try:
            nextState = self._getNextState(state, symbol)
        except:
            return False

        if self._endOfInput():
            return state.is_accept
        return self._consume(self._nextSymbol(), nextState)

    def _endOfInput(self) -> bool:
        return self._inputIndex == len(self._word) - 1

    def _getNextState(self, state: State, symbol) -> State:
        transitionsDict = self.statesdict[state.name].transitions
        if symbol in transitionsDict:
            return list(transitionsDict[symbol].keys())[0]

        raise Exception("No next state")

    def _nextSymbol(self) -> str:
        self._inputIndex += 1
        return self._word[self._inputIndex]
