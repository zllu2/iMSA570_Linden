Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1:
- Question 1.1: What is a module in Python?
  - Type: Multiple choice (single correct response)
  - Answer: A file that contains Python definitions.
  - Choices: A file that contains Python definitions; Python code in a different code cell; Python code in a markdown code cell; Any Function inside of a Class.
- Question 1.2: If you want to use a Python module what keyword must you use?
  - Type: Multiple choice (single correct response)
  - Answer: import
  - Choices: import; def; class; module; function

- Question 2.1: Which built in function lists attributes and functions of a Python module or object?
  - Type: Multiple choice (single correct response)
  - Answer: dir()
  - Choices: dir(); help(); module(); function()

- Question 2.2: Which built in function prints help for a python object?
  - Type: Multiple choice (single correct response)
  - Answer: help()
  - Choices: dir(); help(); module(); function()

- Question 3.1: If my_list = [1, 2, 3], which of the following code lists all attributes and functions of my_list?
  - Type: Multiple choice (multiple correct responses)
  - Answer: dir(my_list), dir(list)
  - Choices: dir(my_list); dir(list); help(my_list); help(list)

- Question 3.2: If my_list = [1, 2, 3], which of the following code print help of list function append()?
  - Type: Multiple choice (multiple correct responses)
  - Answer: help(my_list.append), help(list.append)
  - Choices: dir(my_list.append); dir(list.append); help(my_list.append); help(list.append)

# Lesson 2:
- Question 4.1: True or False? numpy is much faster than using a list.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False
- Question 4.2: True or False? numpy is part of the standard data science Python distribution.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False
- Question 4.3: True or False? NumPy is used by many other libraries like SciPy, MatPlotLib, and Pandas.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False
- Question 4.4: True or False? A numpy array can store data with different types?
  - Type: Multiple choice (single correct response)
  - Answer: False
  - Choices: True, False
- Question 5.1: Which built-in numpy function allows you to create an array whose elements are uninitialized?
  - Type: Multiple choice (single correct response)
  - Answer: empty
  - Choices: empty, zeros, ones, linspace  
- Question 5.2: Which built-in numpy function allows you to create an array whose elements are initialized to zero?
  - Type: Multiple choice (single correct response)
  - Answer: zeros
  - Choices: empty, zeros, ones, linspace
- Question 5.3: Which built-in numpy function allows you to create an array whose elements are initialized to ones?
  - Type: Multiple choice (single correct response)
  - Answer: ones
  - Choices: empty, zeros, ones, linspace
- Question 5.4: Which built-in numpy function allows you to create an array whose elements are evenly spaced from one number to another?
  - Type: Multiple choice (single correct response)
  - Answer: linspace
  - Choices: empty, zeros, ones, linspace

- Question 6.1: What does following code creates?
 import numpy as np  
 np.arange(10)
  - Type: Multiple choice (single correct response)
  - Answer: A numpy array contains integers from 0 to 9.
  - Choices: A numpy array contains integers from 0 to 9; A numpy array contains integers from 1 to 10; A python list contains integers from 0 to 9; A python list contains integers from 1 to 10.

- Question 6.2: What does following code creates?
 import numpy as np  
 np.arange(1, 10)
  - Type: Multiple choice (single correct response)
  - Answer: A numpy array contains integers from 1 to 9.
  - Choices: A numpy array contains integers from 1 to 9; A numpy array contains integers from 1 to 10; A python list contains integers from 1 to 9; A python list contains integers from 1 to 10.

# Lesson 3
- Question 7.1: True or False? Pandas Series is a one-dimensional data structure.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False
- Question 7.2: True or False? Pandas DataFrame is a two-dimensional data structure.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False
- Question 7.3: True or False? You can represent a table of data in Pandas DataFrame.
  - Type: Multiple choice (single correct response)
  - Answer: True
  - Choices: True, False
- Question 8.1: Assume df is a DataFrame, which code prints first 5 rows of the DataFrame?
  - Type: Multiple choice (single correct response)
  - Answer: df.head(5)
  - Choices: df.head(5), df.tail(5), df.sample(5)
- Question 8.2: Assume df is a DataFrame, which code prints last 5 rows of the DataFrame?
  - Type: Multiple choice (single correct response)
  - Answer: df.tail(5)
  - Choices: df.head(5), df.tail(5), df.sample(5)
- Question 8.3: Assume df is a DataFrame, which code prints random 5 samples of the DataFrame?
  - Type: Multiple choice (single correct response)
  - Answer: df.sample(5)
  - Choices: df.head(5), df.tail(5), df.sample(5)
- Question 9.1 What is data type of one row of a DataFrame?
  - Type: Multiple choice (single correct response)
  - Answer: Series
  - Choices: DataFrame; Series; List; Numpy array
- Question 9.2 What is data type of one column of a DataFrame?
  - Type: Multiple choice (single correct response)
  - Answer: Series
  - Choices: DataFrame; Series; List; Numpy array
- Question 10.1 Assume df is a DataFrame, what is df[0:5]?
  - Type: Multiple choice (single correct response)
  - Answer: A DataFrame that has the first 5 rows of df.
  - Choices: A DataFrame that has the first 5 rows of df; A DataFrame that has the first 5 columns of df;
- Question 10.2 Assume df is a DataFrame that has 4 columns, 'C1', 'C2', 'C3', 'C4', what is df['C1']?
  - Type: Multiple choice (single correct response)
  - Answer: A Series which is column 'C1' of df.
  - Choices: A Series which is column 'C1' of df; A DataFrame which is column 'C1' of df.
- Question 10.3 Assume df is a DataFrame that has 4 columns, 'C1', 'C2', 'C3', 'C4', what is df[['C1']]?
  - Type: Multiple choice (single correct response)
  - Answer: A DataFrame which has one column 'C1'.
  - Choices: A Series which is column 'C1' of df; A DataFrame which has one column 'C1'.
