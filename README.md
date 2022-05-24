# tabu-search-algorithm-in-Python-for-Capacitated-Plant-Location-Problem
As alternative heuristic technique; tabu search algorithm is implemented in Python for a capacitated plant location (CPL) problem. Details on implementation and test results can be found in this Github repository. 

Tabu Search Algorithm has been tested as a solution to a capacitated plant location problem. In our problem, there is a company producing cattle forage. And there are seven farms which have an average daily forage demand (in quintals) equal to 36, 42, 34, 50, 27, 30 and 43, respectively. The company intends to purchase some silos, to supply the seven farms. Six different potential sites in the area have been identified, with a maximum daily forage throughput (expressed in quintals) equal to, respectively, 80, 90, 110, 120, 100 and 120. For the next four years, Milatog has estimated the following fixed costs (in e): 321420, 350640, 379860, 401775, 350640 and 336030, respectively. The daily average marginal facility cost per quintal of forage, for each potential site, is equal to 0.15, 0.18, 0.20, 0.18, 0.15 and 0.17, respectively. The transport cost per quintal of forage and per kilometre travelled is equal to 0.06. The kilometric distances for each origin-destination pair are shown in that Table:

![image](https://user-images.githubusercontent.com/82934361/170112148-ec83d55d-c1ad-4d76-8dc5-54a1bd0b0514.png)

Note: The daily transport costs should be computed by considering that every journey is made up of both an outward and a return journey.

Note: The company is planning to keep the warehouses in operation for four years (corresponding to 365×3+366 = 1461 days).

We aim to find the least costly solution that will meet the demands of all customers (farms) without exceeding the capacity of the facilities. So our aim is to decide which facilities we will open.

Before we start solving the problem with the algorithm, we need to create the mathematical model. On a "daily" basis, the CPL model can be formulated as follows:

We start by writing the objective function first.   
