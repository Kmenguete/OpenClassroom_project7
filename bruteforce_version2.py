from data import data
import time

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


if __name__ == '__main__':
    main()
