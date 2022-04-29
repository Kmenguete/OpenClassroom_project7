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
First, the customer requested us to explore every possible combinations and returning the best. But this solution 
has two major drawbacks:
-The program is time-consuming
-The program consume a lot of space in memory
This is why, in a second time, we developed an optimized solution. The optimized solution does not necessary return
the best combination, but it is less time-consuming and the space used in memory is lower.
***
### 2. The bruteforce algorith
***
