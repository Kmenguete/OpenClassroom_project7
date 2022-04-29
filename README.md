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
***
### 3. The optimized solution algorithm
***
The optimized solution algorithm is very interesting. Because, during the implementation of this solution, we discovered
that we don't need to explore all possible combinations, in order to get the most profitable shares list. We succeeded
to get the best combination with less time and fewer spaces in memory. This is what makes our solution optimal(less 
time and fewer spaces in memory for the same result). Anyway, our bruteforce algorithm was not suitable at all for 
very large dataset.

However, our optimized solution is perfectly suitable for very large dataset. Before to implement our optimized solution,
we had to clean and analyze our dataset. This is why, we created a python file for this. Unfortunately, the possible
cleaning operations that may be required for our datasets are not comprehensive and may need to be completed by future
developers or data scientists that will resume this project.

As stated on the first paragraph of the third part of this README file, the bruteforce algorithm is not suitable for 
very large datasets. This is why, we had to think about a way to get the best combination without exploring all of them.
Instead of trying to test x billions of combinations, I decided to adopt another approach. Then, I asked my self the 
following question:

-among thousands of shares, which of them return the highest profit? For a 500 euros maximum investment?

Instead of exploring billions of combinations, I decided to adopt a funnel logic instead. First, I select the 10% of 
shares that return the highest profit from a given dataset. In a second time, I sort this list in descending order. And
finally, I create an algorithm that purchase shares from this sorted list until we reached the maximum amount of 
authorized investment(500 euros). This is how I got the most profitable shares list without exploring billions of 
combinations.
***
### 4. The analysis of both algorithm and their comparison
***
One of the major requirements of this project was to perform a comparison of the brute force algorithm with the optimized
solution. We had to analyze the runtime and the memory used by both of them. For this, we were asked to refer to the big
O notation. The big O notation is a system that let to evaluate the complexity of an algorithm. There is two kind of 
complexity. The time complexity and the space complexity. The time complexity refer to the time a program takes to run
according the number of inputs data. And the space complexity refer to the space a program takes in memory according 
the number of inputs data. In order to simplify the big O notation explanation, I will make a focus on time complexity
before to summarize a little explanation of its space counterparts.

Globally, in the big O notation, there is 6 level of complexity. I will first go to the best case level of complexity
to the worst one:
***
#### 1. The constant time complexity O(1)
***
An algorithm is said to have a constant time complexity when the running time is not dependent of the size of the input data.
No matter, the size of the input data, the running time will be always the same. This is the best level of time complexity.
***
#### 2. The logarithmic time complexity O(log n)
***
An algorithm is said to have a logarithmic time complexity when it reduces the size of the input data in each step 
(it doesn't need to look at all values of the input data). This is also an excellent level of time complexity(similar
level to the constant time complexity).
***
#### 3. The linear time complexity O(n)
***
An algorithm is said to have a linear time complexity when the running time increases at most linearly with the size of 
the input data. This is the best possible time complexity when the algorithm must examine all values in the input data.
However, it is considered as a bad level in the big O notation because the running time of the program increases 
gradually as the size of the input data increases.
***
#### 4. The quadratic time complexity O(n^2)
***
An algorithm is said to have a quadratic time complexity when it needs to perform a linear time operation for each 
value in the input data. In the big O notation, it is one of the worst level of complexity.
***
#### 5. The exponential time complexity O(2^n)
***
An algorithm is said to have an exponential time complexity when the growth doubles with each addition to the input 
data set. This kind of time complexity is usually seen in brute-force algorithms. The level of time complexity is 
worse than the quadratic complexity(who is already one of the worst).
***
#### 6. The factorial time complexity O(n!)
***
An algorithm is said to have a factorial time complexity when it grows in a factorial way based on the size of the 
input data. The complexity of this kind of algorithm grow very fast, even for a small size input of data. In the big 
O notation, it is the worst level of complexity.
***
The space complexity has the same big O notation as the time complexity. In the space complexity, we evaluate, the 
complexity by the space an algorithm and its input data takes in memory(in bytes). Generally, an algorithm that is
time-consuming takes very few places in memory. On the reverse, an algorithm that does not take a lot of place in 
memory is time-consuming. Consequently, when we write an algorithm, we have to find a delicate compromise between
the time it takes to run and the space it takes in memory.
