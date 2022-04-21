from data import data


def main():
    actions = data
    combinations = []
    for i in range(2 ** 20):
        binary = '{0:020b}'.format(i)
        actions = []
        benefice = 0
        cout_action = 0
        for j in range(len(binary)):
            if binary[j] == "1":
                actions.append(data[j])

        for action in actions:
            benefice += action["cout"] * (action["benefice"] / 100)
            cout_action += action["cout"]

        if cout_action <= 500:
            element = {"actions": actions, "benefice": benefice}
            combinations.append(element)
    combinations.sort(key=lambda x: x["benefice"], reverse=True)
    print("Here is the most profitable shares list: ")
    print(combinations[0])
    print("Here is the total real profit of the following shares list: " + str(combinations[0]["benefice"]) + " euros")


if __name__ == '__main__':
    main()
