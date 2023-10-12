# Comprehensive Oral Exam Questions

## SIADS 501: Being a Data Scientist

### Week 1

### Question 501.1.1

### What is the four-stage pipeline and how does it apply to your project?

The four-stage pipeline consists of data collection, data cleaning, data analysis, and data visualization. It's a structured approach to handling data in a project. Our project follows this as we begin by identifying our data sources and pulling the data into our created database using an python library or a developed web scraper. We narrowed our data collection down to the top 100 companies in 3 sectors: healtcare, technology, and industrials. Next, we cleansed our data by dropping null records and dropping data that was not needed for our project by exlcluding them in our SQL statements. Once cleaned, our data was analyze to identify which stock pairs would be best. As we iterated through stocks to pair them with other stocks in the same industry, we tested for stationarity (mean and variance) to ensure stock pair relationships were stable and reliable. Once we identified stocks with the highest stationarity, we tested for co-integration to see if the pairs we identified moved together and could be utilized for pair trading. Lastly, we visualized the path to our findings and the profits we could of made using our method.

### Week 2

### Question 501.2.1

### Explain how the law of small numbers applies to the work you did for your project.

The law of small numbers is when you over generalize from small samples. This could be applied to our work as we only used a year's worth of data as well only using a small sample of shares. This made PODD/REGN seem like the best option to run our algorithm on when another stock pair made more sense.

### Question 501.2.2

### What sources of bias did you identify in your project?

We identified selection bias which came from only focusing on the three sectors of industrials, healthcare, and technology. Another type of bias we identified is look-ahead bias. Look ahead bias occurs when a process relies on data that was not yet known during the time period being analyzed. This happened due to us running our algorithm on historical data.

### Question 501.2.3

### To what degree did you follow the “10 Rules for Creating Reproducible Results in Data Science” in your project work?

Rule 1 - adding comments to our code as it processed and analyzed the data.<br>
Rule 2 - Pandas and SQL was used for all data manipulation steps.<br>
Rile 3 - We archived the versions of all external programs used by documenting them in our requirements.txt file.<br>
Rule 4 - Used GitHub for version control.<br>
Rule 5 - NA<br>
Rule 6 - NA<br>
Rule 7 - Raw data was stored in SQL tables or Pandas dataframes before plotting.<br>
Rule 8 - Data and process steps were documented as comments or markdown in code.<br>
Rule 9 - Data and process steps were documented as comments or markdown in code.<br>
Rule 10 - Public access was granted through our GitHub repo.

### Question 501.2.4

### How did you apply data cleaning principles in your project?

Data cleaning was completed through automation/code for auditablility, reproduciblility, and accountability. Additionally, the root cause of some our inital data problems was addressed during our cleaning process by dropping rows with null values to ensure data consistency.

### Week 3

### Question 501.3.1

### Are there places where overfitting may have played a role in your analyses?

Overfitting did not play a role in our project as we did not create a machine learning model.

### Question 501.3.2

### What is cross-validation?

Cross-validation is used to assess the performance of a model and to mitigate issues related to overfitting and generalization. This involves dividing a dataset into multiple training subsets and testing a model multiple times.

### Question 501.3.3

### What is p-hacking and does it apply to your project work?

P-hacking occurs when a model is ran and analysts are looking for statistically significant relationships. This occured when we conducted our test for stationary (p<.05) and co-integration test (p<.05). For the purpose of our project this made sense, but these relationships may not hold if real-time data and decision making was used.

### Question 501.3.4

### What is the relationship between correlation and causation?

Correlation - When two variables move together. Correlation can be measured using correlation coefficients, which asses the strength and direction of the linear relationship between two variables. Correlation does not imply causation.

Causation - Causation implies a cause-and-effect relationship between two variables. Changes in one variable leads to changes in another variable. Causation implies correlation.

### Week 4

### Question 501.4.1

### How did you engage in the process of storytelling when producing your project report?

We structed our report in a logical manner from start to finish to tell our project's story most effectively. We began by explaining our motivations and the foundational/technical information needed to understand our project. Next, we explained the data collection and cleaning process then the analysis portion of our project. Finally, we finished by walking out to our conclusions and results using visualizations.

### Question 501.4.2

### Discuss the role of uncertainty in your project.

Uncertainty occured as we begun our project. We were unsure of stock pairs that would be best as we didn't know what to expect prior to conducting our stationarity analysis and co-integration analysis. Additionally, we did not know how well our algorithm would perform. This was verified with the comparison to the S&P 500 during the same time period our analysis was ran. Other uncertainty with our data was documented in our code.

## SIADS 502: Math Methods I

### Week 1

### Question 502.1.1

### What is a mathematical function?

### Question 502.1.2

### Describe how to calculate the derivative of a function.

### Question 502.1.3

### What is a vector?

### Question 502.1.4

### Describe how you can use numpy to manipulate vectors.

### Week 2

### Question 502.2.1

### Describe some basic operations and features of matrices.

### Question 502.2.2

### What is the determinant of a matrix? Provide an example of why determinants are useful.

### Question 502.2.3

### What are eigenvalues and eigenvectors?

### Week 3

### Question 502.3.1

### What is a random variable?

### Question 502.3.2

### What is variance and how is it calculated?

### Question 502.3.3

### What is Bayes' rule and why is it important in data science?

### Question 502.3.4

### What are Monte Carlo simulations?

### Week 4

### Question 502.4.1

### What is the Central Limit Theorem and why is important in statistics?

### Question 502.4.2

### Describe hypothesis testing and provide an example of how one might conduct a hypothesis test.

### Question 502.4.3

### Describe how to conduct a linear regression.

### Question 502.4.4

### What is a logistic regression?

## SIADS 503: Data Science Ethics

### Week 1

### Question 503.1.1

### List 5 misconceptions about data science ethics and explain how each of them might apply to your project.

### Question 503.1.2

### Comment on the importance of data privacy in your project work.

### Week 2

### Question 503.2.1

### Describe how your project could be used as a case study about bias.

### Question 503.2.2

### With respect to Data Provenance, Aggregation, and Trust, what does your project “leave out”?

### Week 3

### Question 503.3.1

### Discuss issues around data provenance with respect to the data you used for your project.

### Question 503.3.2

### What role does trust play in the analyses that you did for your project?

### Week 4

### Question 503.4.1

### Comment on issues arising from the publication of results stemming from your project.

## SIADS 505: Data Manipulation

### Week 1

### Question 505.1.1

### Describe how regular expressions can be used to analyze text-based data.

### Question 505.1.2

### Describe some of the functionality that NumPy provides and explain how it is related to the pandas library.

### Question 505.1.3

### Provide an example of how you can use the NumPy library in the analysis of your project data.

### Question 505.1.4

### What are some of the challenges associated with using NumPy?

### Week 2

### Question 505.2.1

### Describe the pandas Series and DataFrame objects and explain how they are related to each other.

### Question 505.2.2

### How does indexing work with pandas DataFrames and Series? Provide examples of indexing that you used in your project.

### Question 505.2.3

### List different ways to deal with missing values and explain when each of those is appropriate. Provide examples from your project of how you either had to, or, if you didn’t have missing values, how you would have, dealt with missing values.

### Question 505.2.4

### What are some common techniques that you use to manipulate pandas data structures.

### Week 3

### Question 505.3.1

### Describe how you used merging or joining in your project. Suggest ways in which the merging could have been made more efficient.

### Question 505.3.2

### How do/did you decide to use group by when performing exploratory data analysis. ### What are some characteristics of variables that you can use to group by?

### Question 505.3.3

### Pivot tables are often used to summarize data. Describe the process of taking data in “long” form and using a pivot table to convert it to “wide” form.

### Question 505.3.4

### Time series functionality in pandas allows you to “upscale” and “downscale” time-based data. Explain how these functions work and indicate when it’s appropriate to use them.

### Week 4

### Question 505.4.1

### Describe the process of generating hypotheses, including how you come up with a null hypothesis. Why are null hypotheses used?

### Question 505.4.2

### A t-test is often used to look for differences between two groups. What are some of the assumptions about the data that need to be met in order to conduct a statistically valid t-test.

### Question 505.4.3

### Explain what p-hacking is and why it’s a bad thing.

P-hacking could lead to analysts to believing there is a strong statistical relationship, however the strength of the relationship is a result of the sample, the method used, or decisions made by the researcher.

### Question 505.4.4

### The scipy package, while providing some useful statistical functionality, isn’t as widely used one might think. Suggest reasons why that’s the case.

## SIADS 511: SQL and Databases

### Week 1

### Question 511.1.1

### How would you set up a database to store the data that you used in your proejct?

### Question 511.1.2

### Why do we use indexes with databases?

### Question 511.1.3

### Provide an example of an AUTO_INCREMENT field that you might use with the data from your project.

### Question 511.1.4

### What are some common data types in SQL databases?

### Week 2

### Question 511.2.1

### What’s the difference between a primary key and a logical key?

### Question 511.2.2

### What does database normalization mean and why is it important?

### Question 511.2.3

### Describe how you would use a JOIN statement to combine data from two tables.

JOIN statements are used to combine data from two or more tables into a single result set. This allows us to extract data that is related to each other and combine it in a meaningful way.

The first step in using a JOIN statement is to identify the tables we want to retrieve data from and determine the relationship between them. In this example, we will use two tables, "customers" and "orders". The "customers" table contains information about customers such as their name, address, and contact information, while the "orders" table contains information about orders placed by these customers.

To combine data from these two tables, we need to specify a column that is common between them. In this case, the "customer_id" column is present in both tables, and it serves as the primary key in the "customers" table and a foreign key in the "orders" table. This means that each order placed by a customer can be identified by their unique customer ID.

To retrieve data from both tables, we use the SELECT statement and specify the columns we want to retrieve, followed by the JOIN keyword, and then the name of the second table. We also need to specify the type of JOIN we want to use, such as INNER, LEFT, RIGHT, or FULL, depending on the type of relationship we want to establish between the two tables.

For example, to retrieve the customer's name and the order date for all orders placed, we can use the following SQL query:

SELECT customers.name, orders.order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;

The ON clause is used to specify the condition for joining the two tables. In this case, the values in the "customer_id" column from both tables must match in order for the data to be combined and retrieved.

Other types of JOIN statements can also be used depending on the desired result. For instance, if we want to retrieve all customers, regardless of whether they have placed an order or not, we can use the LEFT JOIN statement. This will return all customers from the "customers" table, and any matching orders from the "orders" table. If a customer has not placed an order, the corresponding values from the "orders" table will be null.

### Question 511.2.4

### How do you model a many-to-many relationship in a SQL database?

### Week 3

### Question 511.3.1

### Give an example of how transactions are useful for mitigating problem associated with concurrency.

### Question 511.3.2

### What are stored procedures? Give an example of a stored procedure that you might have found useful in your project if you had used a SQL database to store your data.

### Question 511.3.3

### What are subqueries and when should they be used?

### Question 511.3.4

### Provide an example of a GROUP BY statement that could be used in your project if your data was stored in a SQL database.

### Week 4

### Question 511.4.1

### Describe some ways to store text data in SQL databases.

### Question 511.4.2

### What are some common functions that can be applied to text data in SQL databases?

### Question 511.4.3

### What is a b-tree index?

### Question 511.4.4

### Show how regular expressions can be used with SQL databases.

## SIADS 515: Efficient Data Processing

### Week 1: Linux command line

### Question 515.1.1

### How would you explain what the linux CLI is to someone new to data science?

### Question 515.1.2

### What are some of the more common CLI commands?

### Question 515.1.3

### What are some of the difficulties associated with using the CLI?

### Question 515.1.4

### Describe ways in which you could have (or did) use the linux command line in your project.

### Week 2

### Question 515.2.1

### Describe some of the common Jupyter magic commands and identify those which have proved to be useful to you in your work to date.

### Question 515.2.2

### Look at the code that you used for your project and see if you can identify at least one place where you either used or could have used a generator.

### Question 515.2.3

### Recall the use of decorators and suggest at least one place in your code where you could use this approach.

### Question 515.2.4

### Caching involves storing the results of a deterministic function (i.e. given an input, the output is exactly the same each time the function is called). Identify one place in your code where you used a function and indicate why you did or did not use caching.

### Week 3

### Question 515.3.1

### While developing your code for the project there were likely times that your code didn’t work, or didn’t work as expected. ### Describe the process you followed to fix the problem(s) with your code.

### Question 515.3.2

### Suggest some reasons why print debugging, while common, may not be the best approach.

### Question 515.3.3

### JupyterLab provides access to a debugger but it isn’t commonly used. Propose reasons why that’s the case and suggest ways in which the debugger could be changed to make it more accessible.

### Question 515.3.4

### One of the more common errors is the syntax error. Sometimes, syntax errors are accompanied by a statement like “missing : “. Explain why, if python knows what’s missing, it can’t simply fix the problem for you.

### Week 4

### Question 515.4.1

Why do we care about code complexity?

### Question 515.4.2

### Identify places in your code where the complexity of your approach resulted in suboptimal efficiency. Propose ways in which you could have improved your code.

### Question 515.4.3

### Jupyter notebooks promote a fragmented approach to coding, with each cell being executed independently of others. Explain why this promotes inefficient code design and suggest ways to promote the creation of efficient code.

### Question 515.4.4

### Explain how source code for underlying libraries such as pandas, numpy, and scipy can be examined to understand how the underlying operations are coded.

## SIADS 516: Big Data: Scalable Data Processing

### Week 1

### Question 516.1.1

### What are the characteristics of Big Data?

### Question 516.1.2

### What is map reduce and how can it be used to help analyze Big Data?

### Question 516.1.3

### What are some advantages and limitations of using distributed computing?

### Question 516.1.4

### Provide a description of Hadoop and explain why it’s a reasonable choice for analyzing Big Data.

### Week 2

### Question 516.2.1

### What is Apache Spark?

### Question 516.2.2

### How do Resilient Distributed Datasets facilitate the use of distributed computing?

### Question 516.2.3

### How do Pair RDDs differ from plain RDDs, and why is that important?

### Question 516.2.4

### What are some limitations of using RDDs?

### Week 3

### Question 516.3.1

### What are Spark DataFrames?

### Question 516.3.2

### Describe how Spark DataFrames can be used for the manipulation and analysis of structured data.

### Question 516.3.3

### What are user-defined functions and when is it appropriate to use them?

### Question 516.3.4

### What are some limitations of using Spark DataFrames?

### Week 4

### Question 516.4.1

### Describe how Spark SQL works and explain why it is sometimes advantageous to use it.

### Question 516.4.2

### Describe, using an example, of how Spark DataFrames can be merged or joined using Spark SQL.

### Question 516.4.3

### How do user-defined functions (UDFs) work in Spark SQL and explain how they differ from UDFs from the previous week.

### Question 516.4.4

### Describe a scenario where you would interchange data between Spark and Pandas.

## SIADS 521: Visual Exploration of Data

### Week 1

### Question 521.1.1

### What is matplotlib?

### Question 521.1.2

### Describe how you could use matplotlib to create a histogram of some data that you used in your project.

### Question 521.1.3

### Create a boxplot of one of the variables from your data.

### Question 521.1.4

### Create a univariate plot of your choice and annotate something noteworthy in your plot.

### Week 2

### Question 521.2.1

### What is meant by “the computational narrative”? ### How did you create a computational narrative in your project work?

### Question 521.2.2

Demonstrate the effect of changing the number of bins in a histogram of one of your variables.

### Question 521.2.3

### What are the advantages and drawbacks of using violin plots?

### Question 521.2.4

### Show how a probability plot can be used to gain insights about any of the variables you used in your project.

### Week 3

### Question 521.3.1

### What sorts of data are suitable for use in heat maps?

### Question 521.3.2

### What are tree maps used for?

### Question 521.3.3

### Demonstrate the use of a SPLOM with data from your project.

### Week 4

### Question 521.4.1

### What are some advantages and drawbacks of using 3D plots?

### Question 521.4.2

### What is autocorrelation and how can visualization be used to detect it?

### Question 521.4.3

### Describe some of the challenges associated with using geographic maps as visualizations.

## SIADS 522: Information Visualization I

### Week 1

### Question 522.1.1

### What is Anscombe’s Quartet and why is it important in visualization?

### Question 522.1.2

Who is Edward Tufte and why is he important in visualization?

### Question 522.1.3

### What is the block model and how might it apply to the work you did in your project?

### Week 2

### Question 522.2.1

### What are nominal, ordinal and quantitative data types? Provide examples from your project.

### Question 522.2.2

### In visualization, what does “encoding” mean?

### Question 522.2.3

### In visualization, what do “expressiveness” and “effectiveness” mean?

### Question 522.2.4

### What is the grammar of graphics?

### Week 3

### Question 522.3.1

### Describe how the limits of perceptual systems affect your choices of visualizations.

### Question 522.3.2

### What is preattentive processing and describe how it applies to visualizations you generated for your project.

### Question 522.3.3

### What does Gestalt psychology have to offer the field of visualization?

### Question 522.3.4

### What is change blindness?

### Week 4

### Question 522.4.1

### Comment on several design principles that you used when generating visualizations for your project.

### Question 522.4.2

### Provide a hypothetical example of how you could lie about your project data using visualizations.

### Question 522.4.3

### What is chart junk? Comment on the degree to which you have chart junk in your visualizations.

### Question 522.4.4

### Discuss the role of ethics when creating visualizations.

