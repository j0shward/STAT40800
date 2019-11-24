# Week 1 - Assessed Exercises
# Fill in the following Python script and submit it on Brightspace.
# An empty line between the question and 'Ans:' implies that you will need to 
# write a piece of code to get the answer.
import pandas as pd

# Import Heart Disease UCI data set and call is heart

hearts = pd.read_csv('/Users/joshward/Downloads/heart.csv')

# Q1 (a) How many rows and columns there are in the Heart Disease UCI data set?

hearts.shape

#or alternatively

len(hearts)
len(hearts.columns)

# Ans: This data set has 303 rows and 14 columns 

# Q1 (b) What sex is the 3rd person in the data set, i.e. on the third row?

hearts['sex'][2]

# Ans: 0 = Female

# Compute the table of different chest pain types.

hearts.cp.value_counts()

# Q2 How many people have type 3 chest pain? 

hearts.cp.value_counts()[3]

#or alternatively

x = 0
for i in range (len(hearts)-1):
    if hearts['cp'][i] == 3:
        x += 1
x

# Ans: x = 23

# Q3 (a) What age is the youngest person in this dataset? 

hearts.age.min()

# Ans:29

# Q3 (b) What age is the oldest person in this dataset? 

hearts.age.max()

# Ans:77

# Look up what the cut function (pd.cut) does and use it to create a new 
# variable which is age grouped into 20-30, 30-40, 40-50, 50-60, 60-70, 70-80. 

hearts['age_group'] = pd.cut(hearts.age,[20,30,40,50,60,70,80])

# Q4 How many people are in the group (50,60)? 

hearts.age_group.value_counts()

# Ans:129



