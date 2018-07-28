import numpy as np


class Player:

    results: dict

    def __init__(self):
        self.results = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    def update_results(self, choice, result):
        self.results[choice].append(result)

    def choose_machine(self):
        """This is where you will program your strategy. Currently, it just chooses a random machine.
        You must resturn an integer, 0 to 9, which indicates the machine you are choosing."""
        return np.random.randint(0, 10)
