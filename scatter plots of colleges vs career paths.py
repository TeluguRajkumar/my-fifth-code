#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:48:42 2020

@author: rajkumar
"""

import pandas as pd
import matplotlib.pyplot as plt

EmployeeData = pd.read_excel("/Users/rajkumar/Desktop/Task nimbke/EmployeeData.xlsx")

# Create and display the first scatter plot
EmployeeData.plot(kind='scatter', x='College Name', y='Which language you use mostly in your work', rot=70)
plt.show()

# Create and display the second scatter plot
EmployeeData.plot(kind='scatter', x='College Name', y='Which language you use mostly in your work', rot=70)
plt.show()