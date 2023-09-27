'''
*****************************************************************************************
*
*        		===============================================
*           		e-Yantra School Robotics Competition (eYSRC 2023)
*        		===============================================
*
*  This script is to be used to implement Mini Assignment titled- 'Drawing Maurer Rose using Turtle'.
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*  
*  e-Yantra - A MOE project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          
# 					[ Team-ID ]
# Author List:      
# 					[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         question_4.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################
import math
import random
##############################################################



####################### Write your code here #######################

# Input the number of coin tosses from the user
n = int(input("Enter the number of coin tosses you want: "))



# Simulate coin tosses 'n' times
     # Generate a random number (0 or 1) where 0 represents 'heads' and 1 represents 'tails'
heads=0
tails=0
for i in range(n):
     k=random.randint(0,1)
     if k == 0:
          heads+=1
     else:
          tails+=1


# Print the count of heads and tails
print('The number of tosses that resulted in \'heads\' =', heads)
print('The number of tosses that resulted in \'tails\' =', tails)
