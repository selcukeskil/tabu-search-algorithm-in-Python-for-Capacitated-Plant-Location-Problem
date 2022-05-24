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




