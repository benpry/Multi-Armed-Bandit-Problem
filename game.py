import numpy as np
from strategy import Player


class Machine:
    """A slot machine class"""
    mean: float
    stdev: float

    def __init__(self, mean, stdev):
        self.mean = mean
        self.stdev = stdev

    def play(self):
        return round(np.random.normal(self.mean, self.stdev, 1)[0], 1)


if __name__ == '__main__':
    scores = []
    for iteration in range(10000):
        score = 0
        machines = []
        for _ in range(10):
            machines.append(Machine(np.random.uniform(-5, 5, 1), np.random.uniform(0, 3, 1)))

        player = Player()

        for n in range(1, 101):
            choice = player.choose_machine()

            if type(choice) != int or choice < 0 or choice > 9:
                continue

            result = machines[choice].play()
            score += result
            player.update_results(choice, result)
        scores.append(score)

    print('Your final score is', round(np.mean(scores), 1))
