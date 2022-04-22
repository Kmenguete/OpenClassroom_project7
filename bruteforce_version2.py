from data import data
import time
import matplotlib.pyplot as plt
import numpy as np

# I retrieve shares data from the shares list.
# I create a function main that should return the best combination.
start = time.time()


def main():
    # I create an empty list where I will store every combination.
    combinations = []
    for i in range(2 ** 20):
        # I am looking for the most profitable combination among all the possible combinations.
        # A binary combination represents a shares list(where each one represents a share).
        binary = '{0:020b}'.format(i)
        actions = []
        benefice = 0
        cout_action = 0
        for j in range(len(binary)):
            # For each combination if a digit is equal to one, I add a share to the combination.
            if binary[j] == "1":
                actions.append(data[j])

        for action in actions:
            # In each combination I compute the real profit of each share(The percentage of the cost of the share).
            benefice += action["cout"] * (action["benefice"] / 100)
            cout_action += action["cout"]

        if cout_action <= 500:
            # For each combination, if the total cost of shares exceed 500 euros, we stop adding shares to the list.
            element = {"actions": actions, "benefice": benefice}
            combinations.append(element)
    combinations.sort(key=lambda x: x["benefice"], reverse=True)
    # Finally, the first combination is the most profitable shares list.
    print("Here is the most profitable shares list: ")
    print(combinations[0])
    print("Here is the total real profit of the following shares list: " + str(combinations[0]["benefice"]) + " euros")
    end = time.time()
    print(f"The runtime of the program is {end - start} seconds")
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
                  524288])
    plt.plot(x, y)
    plt.xlabel('Inputs data')
    plt.ylabel('Time')
    plt.title('Exponential Time O(2^n) complexity of the algorithm')
    plt.show()


if __name__ == '__main__':
    main()
