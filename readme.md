# Slot Machine Strategy Game

You find yourselves in a room with 10 slot machines. You can pull whichever lever you want, and you must make 100 pulls. Each machine has an average return between -5 and 5, with a standard deviation between 0 and 3.

Your job is to program a strategy to maximize your total return from these machines. The simulation will run 10,000 times and your team's score average score will be compared with others. Good luck!

# How to Use

Write your strategy in the "Choose Machine" function in strategy.py. This function should return a number between 0 and 9, indicating the number of the slot machine you choose. The default setup simply chooses a random machine.
After each pull, the result is logged in self.results. This is a record of all previous slot machine results, stored as a dictionary of lists. The keys of the dictionary correspond with slot machine numbers and the values are lists of all past scores from the slot machine.

To test your strategy, simply run game.py.