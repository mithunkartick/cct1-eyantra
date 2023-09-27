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
# Filename:         question_1.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]

    ####################### Write your code here #######################

def print_pattern(rows):
    n=1 # start from #
    no=0
    for i in range(1, rows+1):
        for j in range(n, i+no):
            print("{:02d}".format(j), end=" ")
            n+=1
            no+=i
            
        print('')

rows = 5 # You can change this value to match the number of rows in your pattern
print_pattern(rows)


