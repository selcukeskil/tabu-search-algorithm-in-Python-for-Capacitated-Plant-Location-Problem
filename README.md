# tabu-search-algorithm-in-Python-for-Capacitated-Plant-Location-Problem
As alternative heuristic technique; tabu search algorithm is implemented in Python for a capacitated plant location (CPL) problem. Details on implementation and test results can be found in this Github repository. 

Tabu Search Algorithm has been tested as a solution to a capacitated plant location problem. In our problem, there is a company producing cattle forage. And there are seven farms which have an average daily forage demand (in quintals) equal to 36, 42, 34, 50, 27, 30 and 43, respectively. The company intends to purchase some silos, to supply the seven farms. Six different potential sites in the area have been identified, with a maximum daily forage throughput (expressed in quintals) equal to, respectively, 80, 90, 110, 120, 100 and 120. For the next four years, Milatog has estimated the following fixed costs (in e): 321420, 350640, 379860, 401775, 350640 and 336030, respectively. The daily average marginal facility cost per quintal of forage, for each potential site, is equal to 0.15, 0.18, 0.20, 0.18, 0.15 and 0.17, respectively. The transport cost per quintal of forage and per kilometre travelled is equal to 0.06. The kilometric distances for each origin-destination pair are shown in that Table:

![image](https://user-images.githubusercontent.com/82934361/170112148-ec83d55d-c1ad-4d76-8dc5-54a1bd0b0514.png)

Note: The daily transport costs should be computed by considering that every journey is made up of both an outward and a return journey.

Note: The company is planning to keep the warehouses in operation for four years (corresponding to 365×3+366 = 1461 days).

We aim to find the least costly solution that will meet the demands of all customers (farms) without exceeding the capacity of the facilities. So our aim is to decide which facilities we will open.

Before we start solving the problem with the algorithm, we need to create the mathematical model. On a "daily" basis, the CPL model can be formulated as follows:

We start by deciding on the decision variables. Let y_i (i = 1,...,6) be the binary decision variable associated to potential site i (with value 1 if silo i is purchased by the Company, 0 otherwise). And, let x_ij (i = 1,...,6 and j = 1,...,7) be the "fraction" of the farm j demand satisfied by the site i.

Now we write the objective function that we aim to minimize. 

Activating facilities will have a cost, and of course we must include them in the objective function. For example, the "daily" cost of activating potential site 1 is calculated as follows: 321420 / 1461 = 220. We calculate the cost of activating the remaining facilities in the same way.

We should also include the costs of transportation from the facilities to the farms in the objective function. For example, if facility 1 meets the entire demand of farm 1, the cost to be incurred (c_11) is calculated as follows: 0.06 × 2 × 18 × 36 + 0.15 × 36 = 83.16. Similar procedure is used to calculate the other costs c_ij (i = 1,...,6, j = 1,...,7). 


As a result, we can write the objective function we want to minimize as follows:

![image](https://user-images.githubusercontent.com/82934361/170119711-49f8fb40-2195-4882-99d7-15f4c5f2e576.png)

Next, we must write the constraints of the mathematical model. 

Our first set of constraints is as you can see below. These are demand constraints. That is, they are constraints that ensure that all farm demands are fully met:

![image](https://user-images.githubusercontent.com/82934361/170120206-1413758d-2335-41f4-b520-b1e26493d85f.png)

Our second set of constraints is as you can see below. These are logical constraints; that is, as soon as the left side of any constraint is positive, the binary y decision variable on the right is forced to be 1. Logically, for example, if the left side of the 1st less than equal constraint is positive, it means that some farm demands will be met by facility 1, and for this to happen, facility 1 must be open, that is, the decision variable y_1 must be forced to be 1. At the same time, these constraints ensure that the capacity limits are not exceeded:

![image](https://user-images.githubusercontent.com/82934361/170121588-e814fc9b-15d3-4a3b-9e37-c4a986f681ae.png)

And below you can see the constraints of the decision variables. These constraints force the decision variable x_ij to be non-negative and the decision variable y_i to be binary:

![image](https://user-images.githubusercontent.com/82934361/170121718-cd82c95f-2015-4983-8f03-2a29ca3e35c3.png)

It should be noted that; the optimal solution to the problem ensures that facilities 1, 5 and 6 are capitalized and the total daily cost is equal to 1218.08.

# Interpreting the output of the algorithm's code
Output is as you can see below:

![image](https://user-images.githubusercontent.com/82934361/170123703-15788e8e-6a46-4c7f-a7f4-c56d4f0ba39f.png)

The code reached the optimum result in approximately 0.153 seconds and 8 iterations. We know that if we increase the size of the problem, it will not be as successful, but it is clear that this result is quite fast. 

# Taboo Search Algorithm in Brief
Tabu search is a "metaheuristic" search method used for mathematical optimization. To explain the difference between heuristics and metaheuristics; heuristics are often problem dependent, meaning you define a heuristic for a particular problem. Metaheuristics are problem-free techniques that can be applied to a wide range of problems. Tabu search (TS) is a metaheuristic algorithm that can be used for solving combinatorial optimization problems. 

Taboo search implements the methods of local search, and at some moments (i.e. where all the neighbouring solutions are non-improving) it can use more than one way to escape the local optimum: accepting bad moves (that is, accepting a solution as an current solution even though it costs more), changing the objective function or changing the neighborhood structure. In our code, tabu search occasionally accepts bad moves to avoid local optima's.

Briefly; In tabu search, a move is always made towards the best solution in the neighborhood, even if it is worse than the current solution. This helps to avoid local optima.

In tabu search, "short-term memory" is used to avoid cyclic moves (that is, the same region is visited over and over) in problem solving. The algorithm's "Short-term memory" is created by preventing the search from revisiting previously visited solutions (i.e. creating a "tabu list"). We do not store ALL visited solutions in the Tabu list. Usually, only some forbidden solutions, moves or their attributes are stored in the Tabu list. 

In our code; to the tabu list, moves that are taboo are appended with their tabu tanure; tabu tanure is the lifetime of a taboo (ie how many iterations a tabu will remain taboo for).

# Procedure of our code
![image](https://user-images.githubusercontent.com/82934361/170269853-922040b5-9696-4b01-a61e-77a034bff419.png)

Note: You can find detailed explanations of how the code works in the comments of code.  













