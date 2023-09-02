import numpy as np

# Simulate throwing two dice a large number of times
num_simulations = 1000000

# Simulate throwing two dice and calculate the probabilities
def simulate_dice_rolls(target_sum):
    dice1 = np.random.randint(1, 7, num_simulations)
    dice2 = np.random.randint(1, 7, num_simulations)
    sum_of_rolls = dice1 + dice2
    successful_outcomes = np.count_nonzero(sum_of_rolls == target_sum)
    probability = successful_outcomes / num_simulations
    return probability

# Calculate probabilities for different target sums 
prob_sum_7 = simulate_dice_rolls(7)

target_sums = np.arange(2, 13)  # Possible sums range from 2 to 12
probabilities = np.array([simulate_dice_rolls(target) for target in target_sums])

# Calculate the probability of prime sums
prime_sums = [2, 3, 5, 7, 11]
prime_sum_probabilities = np.sum(probabilities[np.isin(target_sums, prime_sums)])

prob_sum_1 = simulate_dice_rolls(1)

# Print the probabilities
print("Probability of sum 7:", prob_sum_7)
print("Probability of prime sum:", prime_sum_probabilities)
print("Probability of sum 1:", prob_sum_1)
