import math
import random
import numpy as np
import itertools

def getProbability(numberToCalculateFor, numberOfDice, numberOfFaces):
    # Calculate the total number of possible outcomes
    totalOutcomes = numberOfFaces ** numberOfDice

    # Calculate the number of favorable outcomes
    favorableOutcomes = 0

    # Generate all possible combinations of dice rolls
    rolls = [[i+1 for i in range(numberOfFaces)]] * numberOfDice
    for combination in itertools.product(*rolls):
        if sum(combination) == numberToCalculateFor:
            favorableOutcomes += 1

    # Calculate the probability
    probability = favorableOutcomes / totalOutcomes

    return favorableOutcomes

def generateProbabilites(numberOfDice=1, numberOfFaces=6):
    probabilites = {}
    for i in range(1, numberOfDice*numberOfFaces+1):
        probabilites.update({i:getProbability(i, numberOfDice, numberOfFaces)})
    return probabilites

def generateGameRolls():
    probabilities = generateProbabilites(2,6)

    possibilities = []
    correspondningProbabilities = []
    for key, value in probabilities.items():
        if value != 0:
            possibilities.append(key)
            correspondningProbabilities.append(value)


    rolls = []
    for i in range(len(possibilities)):
        for j in range(correspondningProbabilities[i]):
            rolls.append(possibilities[i])

    gameLength = 80
    multiplyingFactor = math.ceil(gameLength/len(rolls))

    gameRolls = []
    for i in range(multiplyingFactor):
        for j in rolls:
            gameRolls.append(j)

    with open("rolls.txt", "w") as f:
        for i in gameRolls:
            f.write(f"{i} \n")

def Roll():
    # Read the contents of the file into a list
    with open("rolls.txt", "r") as f:
        remainingRolls = []
        for line in f.readlines():
            remainingRolls.append(int(line.strip()))

    # Choose a random item from the list
    roll = random.choice(remainingRolls)

    # Remove the chosen item from the list
    remainingRolls.remove(roll)

    # Write the updated list back to the file
    with open("rolls.txt", "w") as f:
        for item in remainingRolls:
            f.write(str(item) + "\n")

    return roll

while __name__ == "__main__":
    choice = input("Would you like to [r]oll or [c]reate a new game? ")
    if choice == "c":
        generateGameRolls()
        print("A new game has been created!")
    else:
        print(Roll())
