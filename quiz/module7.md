Format:
Question: ...  
Type: Multiple Choice (Single Correct Answer),  Multiple Choice (Multiple Correct Answers), Free Response (Text Answers, Code Expression)
Answer: ...  
Choices: ...  

# Lesson 1

- Question 1.1: True of False? CRISP-DM is an iterative process.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False
- Question 1.2: True of False? Among tasks in CRISP-DM, data preparation is most time consuming.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False

# Lesson 2
- Question 2.1: True of False? Pandas has function to load data from a csv file to a dataframe?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False
- Question 2.2: True of False? Pandas has function to load data from an excel file to a dataframe?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False

- Question 3.1: True of False? Assume df is a dataframe with missing values. After executing df.dropna(), there's no missing values in df.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: False
    - Choices: True; False
- Question 3.2: True of False? Assume df is a dataframe with missing values. After executing df.dropna(inplace=True), there's no missing values in df.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False

- Question 4.1: True of False? Assume df is a dataframe with missing values. After executing df.fillna(10), there's no missing values in df.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: False
    - Choices: True; False
- Question 4.2: True of False? Assume df is a dataframe with missing values. After executing df.fillna(10, inplace=True), there's no missing values in df.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False

- Question 5.1: Assume df is a dataframe that has a column "FirstName", which code correctly convert values in "FirstName" column to all upper case?     - Type: Multiple Choice (Multiple Correct Answers)
    - Answer: df["FirstName"] = df["FirstName"].str.upper();df.FirstName = df.FirstName.str.upper()
    - Choices: df["FirstName"] = df["First Name"].str.upper(); df.FirstName = df.FirstName.str.upper(); df["FirstName"].str.upper(); df.FirstName.str.upper();
- Question 5.2: Assume df is a dataframe that has columns "FirstName" and "LastName", which code correctly create a new column "FullName" in df?
    - Type: Multiple Choice (Multiple Correct Answers)
    - Answer: df["FullName"] = df["FirstName"] + " " + df["LastName"]; df["FullName"] = df.FirstName + " " + df.LastName
    - Choices: df["FullName"] = df["FirstName"] + " " + df["LastName"]; df["FullName"] = df.FirstName + " " + df.LastName; df.FullName = df["FirstName"] + " " + df["LastName"]; df.FullName = df.FirstName + " " + df.LastName;

- Question 6.1: Which of the following datetime string matches this python datetime format: ""%m-%d-%Y"?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: 12-31-2018
    - Choices: 12-31-18; 12-31-2018; 12/31/2018; 12/31/18.
- Question 6.2: Which of the following datetime string matches this python datetime format: ""%m/%d/%Y"?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: 12/31/2018
    - Choices: 12-31-18; 12-31-2018; 12/31/2018; 12/31/18.  

- Question 7.1: Assume df is a dataframe that has a column "desc", what is x in df.desc.apply(lambda x:x.upper())?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: One value in desc column
    - Choices: One value in desc column; One row in df; One column in df
- Question 7.2: Assume df is a dataframe and f() is a function that takes one argument, what is x in df.apply(lambda x:f(x))?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: One column in df
    - Choices: One value in desc column; One row in df; One column in df
- Question 7.3: Assume df is a dataframe and f() is a function that takes one argument, what is x in df.apply(lambda x:f(x), axis=1)?
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: One row in df
    - Choices: One value in desc column; One row in df; One column in df

# Lesson 3
- Question 8.1: True of False? When constructing a regression formula for statsmodels ols using dataframe column names, there can't be whitespaces in the column names.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: True
    - Choices: True; False
- Question 8.2: True of False? When constructing a regression formula for statsmodels ols using dataframe column names, there can be whitespaces in the column names.
    - Type: Multiple Choice (Single Correct Answer)
    - Answer: False
    - Choices: True; False

- Question 9.1: A categorical variable has 5 unique values, when create dummy variables for this feature, at lease how many dummy variables are needed for this variable?
  - Type: Multiple Choice (Single correct answer)
  - Answer: 4
  - Choices: 3; 4; 5; 6
- Question 9.2: A categorical variable has 3 unique values, when create dummy variables for this feature, at lease how many dummy variables are needed for this variable?
  - Type: Multiple Choice (Single correct answer)
  - Answer: 2
  - Choices: 1; 2; 3; 4

- Question 10.1: In regression result, if p value of a coefficient is 0.2, it means the coefficient is?
  - Type: Multiple Choice (Single correct answer)
  - Answer: Not significant at 95% confidence level
  - Choices: Not significant at 95% confidence level; Significant at 95% confidence level
- Question 10.2: In regression result, if p value of a coefficient is less than 0.05, it means the coefficient is?
  - Type: Multiple Choice (Single correct answer)
  - Answer: Significant at 95% confidence level
  - Choices: Not significant at 95% confidence level; Significant at 95% confidence level
