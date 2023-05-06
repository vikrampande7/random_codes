import numpy as np

"""
Environment is presented by a grid where the agent moves from one state to another.
The agent receives rewards for reaching out the goal state and penalties for entering penalty states.
Q-learning algorithm is used to learn the optimal policy by updating the Q-value based on the rewards and penalties encountered during the exlporation porcess.
The learned -table represents the expected future rewards for each state-action pair.
"""
# Set up the environment
environment = [
    [-1, -1, -1, -1, 0],
    [-1, -1, -1, 0, -1],
    [-1, -1, 0, -1, -1],
    [-1, 0, -1, -1, -1],
    [0, -1, -1, -1, -1]
]

# Initialize the Q-table
q_table = np.zeros((5, 5))

# HyperParameters
learning_rate = 0.1
discount_factor = 0.9
epochs = 1000

# Define the rewards and penalties
rewards = {
    0: 100,    # Goal state
    1: -10,    # Penalty state
    2: -10,    # Penalty state
    3: -10,    # Penalty state
    4: -10     # Penalty state
}

# Q-learning algorithm
for epoch in range(epochs):
    # Reset the current state to a random initial state
    current_state = np.random.randint(0, 5)

    while True:
        # Choose an action with epsilon-greedy strategy
        if np.random.uniform(0, 1) < 0.1:
            action = np.random.randint(0, 5)
        else:
            action = np.argmax(q_table[current_state])

        # Move to the next state based on the chosen action
        next_state = action

        # Calculate the Q-value for the current state-action pair
        q_value = q_table[current_state, action]

        # Calculate the maximum Q-value for the next state
        max_q_value = np.max(q_table[next_state])

        # Calculate the reward/penalty for the current state-action pair
        reward = rewards.get(next_state, -1)

        # Update the Q-value using the Q-learning formula
        new_q_value = (1 - learning_rate) * q_value + learning_rate * (reward + discount_factor * max_q_value)
        q_table[current_state, action] = new_q_value

        # Move to the next state
        current_state = next_state

        # Check if the goal state is reached
        if current_state == 0:
            break


# Print the learned Q-table
print("Learned Q-table:")
print(q_table)

# Output:
"""
Learned Q-table:
[[853.33645837 217.75505008 112.03630566  45.38017507 209.04891047]
 [858.56007727 184.378501   240.72880613 293.32558337 267.57644373]
 [854.57264418 313.69646624  66.11618665 175.03366709 213.65758548]
 [847.99168495 204.64138233 217.56033908 104.52651454 306.92820102]
 [858.93620778  49.57654085 385.2654106  161.40940713 101.82300813]]
"""