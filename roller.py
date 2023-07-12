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

probabilities = generateProbabilites(2,6)

possibilities = []
correspondningProbabilities = []
for key, value in probabilities.items():
    if value != 0:
        possibilities.append(key)
        correspondningProbabilities.append(value)

roll = random.choices(possibilities, correspondningProbabilities)
print(roll[0])
