# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import random
from scipy.optimize import linprog # Imports the library that will enable us to solve the linear programming problem (ie the library that will enable us to implement the revised simplex solution)
import time                    # Required library to calculate Computational Time

start_time = time.time()                 # Keeps the start time

x_coef_list = [[83.16, 122.22, 82.62, 133.50, 81.81, 65.70, 52.89], # Assigns the x coefficients in the objective function of the mathematical model of the problem to a list
          [97.20, 98.28, 75.48, 147.00, 40.50, 70.20, 110.94],
          [123.84, 99.12, 76.16, 130.00, 79.92, 38.40, 101.48],
          [75.60, 123.48, 42.84, 195.00, 72.90, 88.20, 59.34],
          [139.32, 107.10, 78.54, 121.50, 36.45, 65.70, 99.33],
          [83.88, 92.82, 124.10, 134.50, 75.87, 69.90, 48.59]]

x_coefs = pd.DataFrame(x_coef_list, index=range(1,7), columns=range(1,8)) # Assigns the x coefficients of the objective function to a dataframe

farm_demands= pd.Series([36, 42, 34, 50, 27, 30, 43], index=range(1,8)) # Farm demands are assigned to a series

capacities= pd.Series([80,90, 110, 120, 100, 120], index= range(1,7)) # Facility capacities are assigned to a series

y_coefs= pd.Series([220, 240, 260, 275, 240, 230], index= range(1,7)) # The costs of opening the facilities are assigned to a series



# This is a function that generates the neighbor solutions of any solution and assigns them to the neighbour_solutions variable and returns it
def neighbour_founder(solution):
    
    neighbour_solutions = [] # The variable created to hold the neighbour solutions of a solution
    
    for i in range(6): # In this loop, neighbour solutions are generated and appended to the neighbour_solutions list
        solution_copy = solution.copy() # Create a copy of the solution given as an argument to the function
    
        if solution_copy[i] == 0:            # The index i of this copy is set to 1 if it is 0, 0 if it is 1 (that is, a neighbour solution is created by closing one facility in the solution if it is already open, opening it if it is closed)
            solution_copy[i] = 1
        elif solution_copy[i] == 1:
            solution_copy[i] = 0
            
        neighbour_solutions.append(solution_copy) # Neighbor solutions created are appended to the neighbor_solutions list
            
    return neighbour_solutions
        
    
def simplexsolver(facilities): # To find the cost of the solution options, we need to do the simplex solution, and we send the open (active) facilities in a solution as an argument to this function
    
    coefs = x_coefs.loc[facilities, :].to_numpy().flatten() # Keeps the x coefficients in the objective function of the facilities we have activated, keeps them as a flat numpy array
    
    facility_number = len(facilities) # Keeps the number of active facilities
    
    lessorequal_coef = np.zeros((facility_number,facility_number*7), dtype='float64') # Coefficients of less-equal constraints (ie capacity constraints) are assigned to this variable 
    
    for i in range(facility_number): # We set up a loop whose range is equal to the number of active facilities, in this loop, the x coefficients of the capacity constraints (ie less equal constraints) for active facilities are found
        j = 7 * i
        lessorequal_coef[i][j : j + 7] = farm_demands # The x coefficients of the less-equal constraints are generated here
    
    lessorequal_rhs = capacities[facilities] # Here the right-hand side values ​​of less than equal constraints are created
    
    equal_coef = np.zeros((7, facility_number * 7)) # Create a variable to hold the coefficients of the x's in the equality constraints and fill it with 0
    
    for i in range(7): # The range of this loop is 7 because our problem has 7 equality constraints
        equal_coef[i][i::7] = [1] * facility_number # The x coefficients of the equals constraints are generated here
    
    equal_rhs = [1] * 7 # Since the right-hand side values ​​of the equality constraints are 1 in our problem, the variable holding the right-hand side values ​​is created like this
    
    result = linprog(coefs,
                  A_ub=lessorequal_coef, b_ub=lessorequal_rhs, 
                  A_eq=equal_coef, b_eq=equal_rhs, 
                  method='revised simplex') # Here, we solve linear programming problems with the revised simplex method using the imported library, and the solution found is assigned to the variable "result"
    return result 


def better_solution_founder(feasible_set):
    solution_to_return = []
    objective_value_of_solution_to_return = np.Inf
    
    # In this loop, the numbers of open facilities in a solution are found and appended to the facilities list
    for solution in feasible_set:
        if solution != [0,0,0,0,0,0]:
            facilities = []
            for i, j in enumerate(solution):
                if j == 1:
                    facilities.append(i+1)
                    
            # The numbers of the open facilities of that potential solution are sent to the simplexsolver function and the cost that will occur if those facilities are opened (in short, the cost of the potential solution) is calculated
            simplex_result = simplexsolver(facilities)
            objective_value = simplex_result.fun + np.sum(y_coefs[facilities])
            
            # If the potential solution is better than the best solution so far, the solution_to_return and objective_value_of_solution_to_return are updated
            if objective_value < objective_value_of_solution_to_return:
                solution_to_return = solution
                objective_value_of_solution_to_return = objective_value
    return solution_to_return, objective_value_of_solution_to_return

def main(tabu_tanure, tabu_list_length):
    
    # Random initial solution is created
    while True:
        current_sol = [] # An empty list is created to hold the initial solution
        for i in range(6): # Since there are 6 facilities, the range of the loop is 6
            current_sol.append(random.choice([0,1])) # The facilities in the initial solution are randomly selected to be open or closed and appended to the current_sol list
        if np.sum(current_sol*capacities) > np.sum(farm_demands): # The initial solution created is accepted if it meets the total farm demand (and exits the initial solution generation loop)    
            break
    
    
    # Tabu list is created to hold taboos that will be created later
    tabu_list = []
    
    best_sol = current_sol # This variable will always keep the best solution found during the execution of the code
    best_sol, best_sol_cost = better_solution_founder([best_sol]) # The cost of the best solution is also found here
    print("Initial solution: ", best_sol)
    print("Initial solution cost: ", best_sol_cost)
    
    
    # Taboo search loop
    h=0 # Keeps the number of iterations
    while True:
        h+=1
        print("---------------------------------------------")
        print("Iteration:",h)
        neighbour_solutions = neighbour_founder(current_sol) # Neighbor solutions are created using the current solution
        [[]]
        
        # Feasible set; that is, what will hold the taboo-free neighbor solutions is created with the bottom 2 loops
        tabu_indexes_list = [] # This empty list is created to hold indexes that are taboo to modify (i.e. facilities that we have recently opened or closed)
        for tabu in tabu_list: # Iterate through the tabu list
            tabu_indexes_list.append(tabu[0]) # Since the first numbers in the taboos hold the indexes of the facilities whose status we are not allowed to change, those numbers are added to the tabu indexes list
        tabu_indexes_list.sort(reverse = True)
        
        for i in tabu_indexes_list: # Iterate through taboo indexes (i.e. facilities where status change is prohibited)
            del neighbour_solutions[i] # From the list of neighbor solutions, those that contain forbidden changes (that is, those that will cause taboo changes) are deleted
        feasible_set = neighbour_solutions # Remaining neighbor solutions are assigned to the feasible set variable
        
        
        # Solutions that cannot meet the total farm demand will be deleted from the Feasible set list.
        feasible_set_copy = feasible_set.copy()
        for solution in feasible_set_copy:
            if np.sum(solution*np.array(capacities)) < np.sum(farm_demands):
                feasible_set.remove(solution)
            
        # Potential solution (that is, the best of the remaining solutions in the feasible set) and cost
        potential_sol, potential_sol_cost  = better_solution_founder(feasible_set) # Use the better solution founder function
        
        # We find in which index the solution update will make changes to the current solution (ie, by looking at the new solution and the last solution before it, we find which facility's status will be changed so that we make these changes a "taboo")
        for index, (first, second) in enumerate(zip(potential_sol, current_sol)):
            if first != second:
                index_hold=index
                
        # Taboos resulting from the solution update will be added to the tabu list (for example, if the index that will change in the solution is 3; a tabu like [3,tabu tenure] is added to the tabu list)
        tabu_list.append([index_hold, tabu_tanure]) 
        
        # The lifetimes of the taboos (ie tabu tanures) in the tabu list are updated (decreased by 1)
        for tabu in tabu_list:
            tabu[1] -= 1
        
        # Taboos in the tabu list that do not have a lifetime, that is, taboos with a tabu tanure of 0 are deleted
        for tabu in tabu_list:
            if tabu[1] == 0:
                tabu_list.remove(tabu)
        
        # If the size of the tabu list exceeds the tabu_list_length, the oldest tabu is deleted
        if len(tabu_list) > tabu_list_length:
            tabu_list.pop(0)
        
        # Potential sol is assigned to current sol
        current_sol = potential_sol
        current_sol_cost = potential_sol_cost
        print("Current solution: ", current_sol)
        print("Current solution cost: ", current_sol_cost)
        
        # If a better solution than the best solution so far is found, the best solution is also updated
        if current_sol_cost < best_sol_cost:
            best_sol = current_sol
            best_sol_cost = current_sol_cost
        
        # If the new solution found gives the same cost as the best solution so far, the algorithm is exited
        elif current_sol_cost == best_sol_cost:
            break
        
        print("Best solution: ", best_sol)
        print("Best solution cost: ", best_sol_cost)
        
    print("-----------------------RESULTS----------------------")
    print("Iterations:", h)
    print("Best solution founded: ", best_sol)
    print("Cost of best solution: ", best_sol_cost)
    comp_time = time.time() - start_time     # Subtracts the start time from the end time and keeps the result
    print(f"-> Computational Time: {comp_time} seconds")     # Prints Computational Time
    
main(2, 2)
    



















