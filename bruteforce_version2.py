from data import data
import time
import matplotlib.pyplot as plt
import numpy as np

# I retrieve shares data from the shares list.
# I create a function main that should return the best combination.
# Defining the beginning of the program using time.time()
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
    # Defining the end of the program using time.time()
    end = time.time()
    # Calculating the runtime of the program by subtracting the time(time.time()) at the start of the program with
    # the time(time.time()) at the end of it.
    print(f"The runtime of the program is {end - start} seconds")
    # Creating a matplotlib graph that illustrate exponential time complexity of the algorithm.
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144,
                  524288])
    plt.plot(x, y)
    plt.xlabel('Inputs data')
    plt.ylabel('Time units')
    plt.title('Exponential Time O(2^n) complexity of the brute force algorithm in the big O notation')
    plt.show()

    # Creating a matplotlib graph the number of combinations according the number of shares in a list.

    y_combinations = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072,
                              262144, 524288, 1048576])
    plt.plot(x, y_combinations)
    plt.xlabel('Shares')
    plt.ylabel('Number of combinations')
    plt.title('Number of combinations according the number of shares.')
    plt.show()
    get_space_complexity_of_algorithm()


def get_space_complexity_of_algorithm():
    # The total size of algorithm without any shares share is about 746 bytes
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    y = np.array([898, 906, 946, 1018, 1178, 1482, 2098, 3074, 5138, 9901, 17442,
                  34818, 69898, 141490, 286298, 515490, 1044268, 1881746, 3390506, 6872946])
    plt.plot(x, y)
    plt.xlabel('Inputs data')
    plt.ylabel('Bytes')
    plt.title('Space complexity of brute force algorithm')
    plt.show()


if __name__ == '__main__':
    main()
