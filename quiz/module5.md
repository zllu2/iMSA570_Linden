Format:
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Question: ...  
Answer: ...  
Choices: ...  

# Lesson 1

- Question 1.1: What mode argument is used to open a file in  binary mode?
  - Type: Multiple Choice (Single Answer)
  - Answer: b
  - Choices: b; r; rb; w
- Question 1.2: What mode argument is used to open a text file to write?
  - Type: Multiple Choice (Single Answer)
  - Answer: w
  - Choices: b; r; rb; w
- Question 1.3: What mode argument is used to open a text file to read?
  - Type: Multiple Choice (Single Answer)
  - Answer: r
  - Choices: b; r; rb; w

- Question 2.1: Which pandas function is used to read a csv file and load the data in the file to a DataFrame?
  - Type: Multiple Choice (Single Answer)
  - Answer: read_csv()
  - Choices: to_pickle(); to_csv(); load_csv(); read_csv()
- Question 2.2: Assume df is a DataFrame, which command writes df to a csv file named 'data.csv'?
  - Type: Multiple Choice (Single Answer)
  - Answer: df.to_csv('data.csv')
  - Choices: df.to_csv('data.csv'); df.to_pickle('data.csv'); df.write_csv('data.csv').
- Question 2.3: What is the typical delimiter for a csv formatted file?
	- Type: Multiple Choice (Single Correct Answer)
	- Answer: Comma
	- Choices: Comma; Tab; Space; Column

- Question 3.1: Which pandas function is used to read a pickled file and load the data in the file to a DataFrame?
  - Type: Multiple Choice (Single Answer)
  - Answer: read_pickle()
  - Choices: to_pickle(); to_csv(); read_pickle(); read_csv()
- Question 3.2: Assume df is a DataFrame, which command pickles df to a file named 'data.p'?
  - Type: Multiple Choice (Single Answer)
  - Answer: df.to_pickle('data.p')
  - Choices: df.to_csv('data.p'); df.to_pickle('data.p'); df.write_pickle('data.p').

# Lesson 2
- Question 4.1: Which pandas DataFrame function is used to print a concise summary of the DataFrame?
  - Type: Multiple Choice (Single Answer)
  - Answer: info()
  - Choices: info(); describe(); summary(); type()
- Question 4.2: Which pandas DataFrame function is used to generates descriptive statistics of the DataFrame?
  - Type: Multiple Choice (Single Answer)
  - Answer: describe()
  - Choices: info(); describe(); summary(); type()
- Question 5.1: Which DataFrame property is used to slice a dataframe with explicit indexes?
  - Type: Multiple Choice (Single Answer)
  - Answer: loc
  - Choices: loc; iloc
- Question 5.2: Which DataFrame property is used to slice a dataframe with implicit indexes?
  - Type: Multiple Choice (Single Answer)
  - Answer: iloc
  - Choices: loc; iloc
- Question 6.1: Assume df is a DataFrame that has columns 'Name' and 'Age', which code selects all rows in df that have Age greater than 20?
  - Type: Multiple Choice (Single Answer)
  - Answer: Both of above
  - Choices: df[df.Age>20]; df[df['Age']>20]; Both of above; None of above.
- Question 6.2: Assume df is a DataFrame that has columns 'Name' and 'Age', which code selects all rows in df that have Age less than 30?
  - Type: Multiple Choice (Single Answer)
  - Answer: Both of above
  - Choices: df[df.Age<30]; df[df['Age']<20]; Both of above; None of above.

- Question 6.3: Assume df is a DataFrame that has columns 'Name' and 'Age', which code selects all rows in df that have Age greater than 20 and less than 30?
  - Type: Multiple Choice (Single Answer)
  - Answer: df[(df.Age>20) & (df.Age<30)]
  - Choices: df[(df.Age>20) & (df.Age<30)]; df[df.Age>20 & df.Age<30]; Both of above; None of above.
- Question 6.4: Assume df is a DataFrame that has columns 'Name' and 'Age', which code selects all rows in df that have Age less than 20 or greater than 30?
  - Type: Multiple Choice (Single Answer)
  - Answer: df[(df.Age>20) | (df.Age<30)]
  - Choices: df[(df.Age>20) | (df.Age<30)]; df[df.Age>20 | df.Age<30]; Both of above; None of above.
- Question 7.1: Assume df is a DataFrame that has columns 'Name' and 'Age', what data type is df['Age']?
  - Type: Multiple Choice (Single Answer)
  - Answer: Series
  - Choices: Series; DataFrame; list; numpy array
- Question 7.2: Assume df is a DataFrame that has columns 'Name' and 'Age', what data type is df[['Age']]?
    - Type: Multiple Choice (Single Answer)
    - Answer: DataFrame
    - Choices: Series; DataFrame; list; numpy array
- Question 8.1: Assume df is a DataFrame, in df.groupby(by='column1', as_index=False).agg({'column2':'mean'}), what type of data is in column1?
  - Type: Multiple Choice (Single Answer)
  - Answer: Categorical data
  - Choices: Categorical data; Continuous data; Both of above.
- Question 8.2: Assume df is a DataFrame, in df.groupby(by='column1', as_index=False).agg({'column2':'mean'}), what type of data is in column2?
  - Type: Multiple Choice (Single Answer)
  - Answer: Continuous data
  - Choices: Categorical data; Continuous data; Both of above.
- Question 8.2: Assume df is a DataFrame, in df.groupby(by='column1', as_index=False).agg({'column2':'mean'}), what does as_index=False mean?
  - Type: Multiple Choice (Single Answer)
  - Answer: column1 will be a column of resulting dataframe.
  - Choices: column1 will be a column of resulting dataframe; column2 will be a column of resulting dataframe; column1 will be the index of resulting dataframe; column2 will be the index of resulting dataframe.

# Lesson 3
- Question 9.1: What is median of the numbers in the list [1,2,3,4,5,6]?
  - Type: Multiple Choice (Single Answer)
  - Answer: 3.5
  - Choices: 3; 4; 3.5
- Question 9.2: What is median of the numbers in the list [1,2,3,4,5]?
  - Type: Multiple Choice (Single Answer)
  - Answer: 3
  - Choices: 3; 4; 3.5
- Question 10.1: What is mean of the numbers in the list [1,2,3,4,5,6]?
  - Type: Multiple Choice (Single Answer)
  - Answer: 3.5
  - Choices: 3; 4; 3.5
- Question 10.2: What is mean of the numbers in the list [1,2,3,4,5,]?
  - Type: Multiple Choice (Single Answer)
  - Answer: 3
  - Choices: 3; 4; 3.5
