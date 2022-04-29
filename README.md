## Table of contents
1. About the project
2. The bruteforce algorithm
3. the optimized solution algorithm
4. The analysis of both algorithm and their comparison
5. Discussion for further development
### 1. About the project
***
The project aims to develop an algorithm in order to know the most profitable shares of a given list of shares.
The customer is an investment consulting firm that helps its customers to invest in most profitable companies.
Each share(of a given company) is represented by its name, its price and its profit(after 2 years). The profit of each 
share is a percentage of its cost. In order to find the most profitable shares, we were required to respect some 
requirements from customers of the firm:
-Each share can be purchased once.
-The maximum amount of authorized investment is 500 euros.
-It is not possible to purchase a part of the share.
First, the customer requested us to explore all possible combinations and returning the best one. But this solution 
has two major drawbacks:
-The program is time-consuming
-The program consume a lot of space in memory
This is why, in a second time, we developed an optimized solution. The optimized solution does not necessary return
the best combination, but it is less time-consuming and the space used in memory is lower.
***
### 2. The bruteforce algorithm
***
As mentioned in the first part, the bruteforce algorithm has the disadvantage to be time-consuming and greedy in memory.
That said, this algorithm has the advantage to return the best combination. For this algorithm, we worked with a first 
list of 20 shares. From this list, we computed that there is 1 048 576 possible combinations for a list of 20 shares.
First, we try every possible combinations. Once we tried it, we sort them according their total price(each combination
is a shares list). We selected, only combinations from which, the total price does not exceed 500 euros. Once, we 
selected it, we have found that the best combination was the first one of the list(of combinations) and the profit 
generated two years later will be 99.08 euros worth.