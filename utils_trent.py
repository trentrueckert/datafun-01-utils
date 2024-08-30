''' ITERATION 1

Module: Rueckert Analytics - Data Interpretations

This module provides a simple, reusable foundation for my analytics projects. 
This docstring helps describe what is going on for better clarification for any viewer.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Rueckert Analytics: Data Interpretations'

#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()

''' ITERATION 2

Module: Rueckert Analytics - Data Interpretations

This module provides a simple, reusable foundation for my analytics projects.

Process: 
In this second iteration, add a function that returns the byline as a string.
I'll create a function named get_byline().
It'll return my byline to whatever calls the get_byline() function.
I'll update the main() function to use the new get_byline() function.

Same conditional boilerplate at the end. 

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Rueckert Analytics: Data Interpretations'

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
   '''Print the byline to the console when this function is called.'''
   print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

''' ITERATION 3

Module: Rueckert Analytics - Data Interpretations

This module provides a simple, reusable foundation for my analytics projects.

Process:
In this third iteration, I declare additional variables to show skills with different data types.
'''

#####################################
# Declare global variables - keep byline at the end
# We will use the information in a smaller byline
#####################################

# Boolean variable to indicate if the company has international clients 
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 6

# List of strings representing the skills offered by the company
skills_offered: list = ["GitHub", "RStudio", "Python"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.7, 4.8, 4.8, 5.0, 4.9]

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
----------------------------------------------------------
Rueckert Analytics: Data Interpretations
----------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
   '''Print the byline to the console when this function is called.'''
   print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

''' ITERATION 4

Module: Rueckert Analytics - Data Interpretations

This module provides a simple, reusable foundation for my analytics projects.
'''

import statistics

has_international_clients: bool = True

years_in_operation: int = 6

average_client_satisfaction: float = 4.8

skills_offered: list = ["GitHub", "RStudio", "Python"]

client_satisfaction_scores: list = [4.7, 4.8, 4.8, 5.0, 4.9]

client_ages: list = [34, 42, 53, 67, 98]

min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_age: float = min(client_ages)
max_age: float = max(client_ages)
mean_age: float = statistics.mean(client_ages)
stdev_age: float = statistics.stdev(client_ages)

byline: str = f"""
----------------------------------------------------------
Rueckert Analytics: Data Interpretations
----------------------------------------------------------
Has International Clients:                        {has_international_clients}
Years in Operation:                               {years_in_operation}
Skills Offered:                                   {skills_offered}
Client Satisfaction Scores:                       {client_satisfaction_scores}
Minimum Client Satisfaction Score:                {min_score}
Maximum Client Satisfaction Score:                {max_score}
Average Client Satisfaction Score:                {mean_score}
Standard Deviation of Client Satisfaction Scores: {stdev_score}
Minimum Client Age:                               {min_age}
Maximum Client Age:                               {max_age}
Average Client Age:                               {mean_age}
Standard Deviation of Client Ages:                {stdev_age}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
   '''Print the byline to the console when this function is called.'''
   print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
