#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:42:51 2020

@author: rajkumar
"""


####################bar graphs####

import pandas as pd
import numpy as np

####importing data set######
EmployeeData = pd.read_excel("/Users/rajkumar/Desktop/Task nimbke/EmployeeData.xlsx")

#####import matplotlib#######
import matplotlib.pyplot as plt   
programinglanguage = ['python', 'c', 'java/python', 'java', 'python', 'c++', 'R', 'python', 'c', 'c', 'c', 'java']
currenttitle = ['Data scientist', 'customer support', 'software engineer', 'technical support', 'data science intern', 'senior developer', 'software', 'IT', 'software tester', 'Quality control', 'customer care', 'Employee(govt)']

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(programinglanguage, currenttitle, color=New_Colors)
plt.title('programinglanguage Vs currenttitle', fontsize=14)
plt.xlabel('programinglanguage', fontsize=14)
plt.ylabel('currenttitle', fontsize=14)
plt.grid(True)
plt.show()


#################bar graph using matplotlib##############
import pandas as pd
import numpy as np

####importing data set######
EmployeeData = pd.read_excel("/Users/rajkumar/Desktop/Task nimbke/EmployeeData.xlsx")
import matplotlib.pyplot as plt
Programinglanguage = ['python', 'c', 'java/python', 'java', 'python', 'c++', 'R', 'python', 'c', 'c', 'c', 'java']
currenttitle = ['Data scientist', 'customer support', 'software engineer', 'technical support', 'data science intern', 'senior developer', 'software', 'IT', 'software tester', 'Quality control', 'customer care', 'Employee(govt)']
New_Colors = ['green','blue','purple','brown','teal']
plt.bar(Programinglanguage, currenttitle, color=New_Colors)
plt.title('programinglanguage Vs currenttitle', fontsize=12)
plt.xlabel('programinglanguage', fontsize=12)
plt.ylabel('currenttitle', fontsize=12)
plt.grid(True)
plt.show()



#######line chart using matplotlib####### 
import pandas as pd
import numpy as np

###########importing data##########
EmployeeData = {'programinglanguage': ['python', 'c', 'java/python', 'java', 'python', 'c++', 'R', 'python', 'c', 'c', 'c', 'java'],
        'currenttitle': ['Data scientist', 'customer support', 'software engineer', 'technical support', 'data science intern', 'senior developer', 'software', 'IT', 'software tester', 'Quality control', 'customer care', 'Employee(govt)']
       }
  
df = pd.DataFrame(EmployeeData,columns=['programinglanguage','currenttitle'])
  
plt.plot(df['programinglanguage'], df['currenttitle'], color='red', marker='o')
plt.title('currenttitle Vs programinglanguage', fontsize=14)
plt.xlabel('programinglanguage', fontsize=14)
plt.ylabel('currenttitle', fontsize=14)
plt.grid(True)
plt.show()



############scatter diagram using matplotlib#######

import pandas as pd
import numpy as np

####importing data set######
EmployeeData = pd.read_excel("/Users/rajkumar/Desktop/Task nimbke/EmployeeData.xlsx")

import matplotlib.pyplot as plt
   
programinglanguage = ['python', 'c', 'java/python', 'java', 'python', 'c++', 'R', 'python', 'c', 'c', 'c', 'java']
currenttitle = ['Data scientist', 'customer support', 'software engineer', 'technical support', 'data science intern', 'senior developer', 'software', 'IT', 'software tester', 'Quality control', 'customer care', 'Employee(govt)']
  
plt.scatter(programinglanguage, currenttitle, color='green')
plt.title('programinglanguage Vs currenttitle', fontsize=14)
plt.xlabel('programinglanguage', fontsize=14)
plt.ylabel('currenttitle', fontsize=14)
plt.grid(True)
plt.show()















