import sm
class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = (val0, val1) # исправьте это

    def getNextValues(self, state, inp):
        nstate = (state[1], inp)
        return (nstate, state[0])


if __name__ == "__main__":
    sm = Delay2Machine(100, 10)
    print(sm.transduce([1, 2, 10, 20, 30, 35]))
