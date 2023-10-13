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

A function from a set X to a set Y assigns to each input x to an output y. (f:X->Y)

### Question 502.1.2

### Describe how to calculate the derivative of a function.

Calculate rise over run at a specific point.

For constant terms: The derivative of a constant (C) is 0.
For powers of x: Use the power rule. If you have f(x) = x^n, where n is a constant, then f'(x) = nx^(n-1).
For sums and differences: If you have a function h(x) that is the sum or difference of two functions, h(x) = u(x) ± v(x), then h'(x) = u'(x) ± v'(x).

### Question 502.1.3

### What is a vector?

A list of real numbers. Ex: v=[3,6] v=R^2, w=[-1,2,7] w=R^3

### Question 502.1.4

### Describe how you can use numpy to manipulate vectors.

One must import numpy then cast your lists as numpy arrays before using calculations or other numpy functions to manipulate vectors.

### Week 2

### Question 502.2.1

### Describe some basic operations and features of matrices.

Scalar Multiplication, Transposition, Addition, reshape, slice, 

### Question 502.2.2

### What is the determinant of a matrix? Provide an example of why determinants are useful.

A matrix has to be square to have a determinant. Determinants of function take a matrix as an input and it outputs a single number from the elements of the matrix. Determinants capture what happens to the input space.

### Question 502.2.3

### What are eigenvalues and eigenvectors?

An eigenvalue of a square matrix A is a scalar (a number) λ such that when A is multiplied by a specific vector, the result is a scaled version of that vector. In mathematical terms, if v is an eigenvector of A, then Av = λv, where λ is the eigenvalue associated with the eigenvector v.
Eigenvalues provide insight into how a matrix scales vectors in different directions. A positive eigenvalue λ > 1 indicates that the corresponding eigenvector v is stretched, while 0 < λ < 1 implies compression, and a negative eigenvalue λ < 0 suggests both scaling and reversal of direction.

An eigenvector is a non-zero vector v that, when multiplied by a matrix A, results in a scaled version of itself, with the scaling factor being the corresponding eigenvalue λ. Av = λv.

### Week 3

### Question 502.3.1

### What is a random variable?

"A discrete random variable is one that can take on at most a countable number of possible values." Bernoulli random variable has two possible values, success and failure. Binomial random variable - "the number of ways if you have n objects to choose k of them when the order doesn't matter." Multinomial random variable - like binomial but with k possible outcomes. Continuous random variable - "...is one that takes on an uncountable number of possible values." "A uniform distributed random variable, all values between a and b are equally likely." Normally distributed random variable - two parameters mean Mu and a standard deviation Sigma.
 
### Question 502.3.2

### What is variance and how is it calculated?

Variance is 

### Question 502.3.3

### What is Bayes' rule and why is it important in data science?

### Question 502.3.4

### What are Monte Carlo simulations?

"...simulate some random process a large number of times and then take the average result."

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

Creating dataframes, viewing, selecting, dropping, sorting, grouping, merging/joining.

### Week 3

### Question 505.3.1

### Describe how you used merging or joining in your project. Suggest ways in which the merging could have been made more efficient.

We used SQL statements to join our data. I believe this was the most efficient method for our project.

### Question 505.3.2

### How do/did you decide to use group by when performing exploratory data analysis. What are some characteristics of variables that you can use to group by?

We used group by to group our

### Question 505.3.3

### Pivot tables are often used to summarize data. Describe the process of taking data in “long” form and using a pivot table to convert it to “wide” form.

### Question 505.3.4

### Time series functionality in pandas allows you to “upscale” and “downscale” time-based data. Explain how these functions work and indicate when it’s appropriate to use them.

### Week 4

### Question 505.4.1

### Describe the process of generating hypotheses, including how you come up with a null hypothesis. Why are null hypotheses used?

### Question 505.4.2

### A t-test is often used to look for differences between two groups. What are some of the assumptions about the data that need to be met in order to conduct a statistically valid t-test.

A t-test is a statistical test used to compare the means of two groups and determine if there is a statistically significant difference between them. To conduct a valid t-test the following assumptions must be met. Data points within each group should be independent of each other. Data within each group be roughly normal distribution. The data is continuous. 

The data points within each group should be independent of each other. This means that the value of one observation should not be influenced by or related to the value of another observation within the same group. Equal grouping sample sizes. Variances should be equal.

### Question 505.4.3

### Explain what p-hacking is and why it’s a bad thing.

P-hacking could lead to analysts to believing there is a strong statistical relationship, however the strength of the relationship is a result of the sample, the method used, or decisions made by the researcher.

### Question 505.4.4

### The scipy package, while providing some useful statistical functionality, isn’t as widely used one might think. Suggest reasons why that’s the case.

## SIADS 511: SQL and Databases

### Week 1

### Question 511.1.1

### How would you set up a database to store the data that you used in your project?

We used PostgreSQL to set up our database hosted in Heroku. We build tables for various steps of our analysis in which we stored cleansed/manipulated data based on it's usefulness in each step of our analysis.

### Question 511.1.2

### Why do we use indexes with databases?

Indexes are used to enhance the performance and functionality of a database. Improved query performance, faster data retrieval, and efficient joins.

### Question 511.1.3

### Provide an example of an AUTO_INCREMENT field that you might use with the data from your project.

### Question 511.1.4

### What are some common data types in SQL databases?

INTEGER (INT): Used for whole numbers.

NUMERIC/DECIMAL: Used for fixed-point or floating-point numbers with a specified precision and scale.

REAL/FLOAT/DOUBLE: Used for floating-point numbers with varying levels of precision.

CHAR(n): Fixed-length character strings with a specified length, 'n'.

VARCHAR(n): Variable-length character strings with a maximum length of 'n'.

TEXT: Variable-length character strings with no predefined maximum length. Suitable for large text data.

DATE: Used to store dates in 'YYYY-MM-DD' format.

TIME: Used to store time in 'HH:MM:SS' format.

TIMESTAMP: Used to store both date and time information

### Week 2

### Question 511.2.1

### What’s the difference between a primary key and a logical key?

A primary key is a unique key/value to enforces data integrity by ensuring that there are no duplicate or null values in the key column. They are used as a reference point for establishing relationships between tables in a relational database.
Logical Key:

A logical key is a field or set of fields in a database that has business or logical significance. They are used to identify records based on other data content.

### Question 511.2.2

### What does database normalization mean and why is it important?

Database normalization is a process to minimize data redundancy and improve data integrity by organizing data into separate related tables.

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

Modeling a many-to-many relationship in a SQL database requires creating a junction or associative table that connects two entities, each represented by a table. This junction table serves to resolve the many-to-many relationship by associating records from both tables. Here's a step-by-step guide on how to model a many-to-many relationship:

Step 1: Identify the Entities
Identify the two entities involved in the many-to-many relationship. For example, let's consider a scenario involving students and courses. Students can enroll in multiple courses, and each course can have multiple students.

Step 2: Create Tables for Each Entity
Create two separate tables, one for each entity. In this example, you would create a "students" table and a "courses" table. Each table should contain information specific to its entity. For instance:

Students Table:

student_id (Primary Key)
first_name
last_name
other student-related fields
Courses Table:

course_id (Primary Key)
course_name
course_description
other course-related fields
Step 3: Create the Junction Table
Create a third table, known as the junction table or associative table, to represent the many-to-many relationship. In this example, the junction table can be named "enrollments" or "student_courses." The junction table typically contains two columns that act as foreign keys, each referencing the primary key of one of the entity tables. For instance:

Enrollments Table:

enrollment_id (Primary Key)
student_id (Foreign Key referencing students.student_id)
course_id (Foreign Key referencing courses.course_id)
Step 4: Establish Foreign Key Constraints
Set up foreign key constraints to ensure that the values in the "student_id" and "course_id" columns in the junction table reference valid records in the "students" and "courses" tables, respectively. This maintains referential integrity.

Step 5: Populate the Junction Table
To represent the relationships between students and courses, insert records into the junction table. Each row in the junction table corresponds to a student's enrollment in a specific course. For example:

Enrollment 1:

enrollment_id: 1
student_id: 101 (refers to a student in the students table)
course_id: 201 (refers to a course in the courses table)
Enrollment 2:

enrollment_id: 2
student_id: 102
course_id: 201
This approach allows multiple students to be enrolled in multiple courses, creating a many-to-many relationship.

Step 6: Query the Data
When querying data, you can use SQL JOIN operations to retrieve information about students, courses, and their enrollments. For example, to find which courses a particular student is enrolled in, you would use a SQL query like this:

### Week 3

### Question 511.3.1

### Give an example of how transactions are useful for mitigating problem associated with concurrency.

ransactions are a fundamental concept in database management systems (DBMS) that help mitigate problems associated with concurrency in multi-user environments. They ensure that database operations are executed in an isolated, consistent, and reliable manner. Here's an example of how transactions can be useful for addressing concurrency issues:

Scenario: Consider an online banking system where multiple users are transferring money between accounts concurrently. Each transfer involves two steps: subtracting the amount from one account and adding it to another. Without transactions, the following problems can occur due to concurrency:

Lost Updates: If two users simultaneously transfer money from the same source account, there is a risk of a lost update. One user's transfer may overwrite the changes made by the other, resulting in an incorrect account balance.

Inconsistent States: In a concurrent environment, intermediate states can be visible to other transactions, leading to inconsistent account balances. For example, a user might see an account with a balance that is temporarily lower than expected.

Solution Using Transactions:

With transactions, the above issues can be mitigated effectively. Here's how:

Atomicity: Transactions are atomic, meaning they are treated as a single, indivisible unit of work. In the online banking system, each transfer operation is wrapped in a transaction. If any part of the transaction (e.g., deducting money or adding money) fails, the entire transaction is rolled back, and no changes are made to the database. This ensures that no money is lost due to concurrent updates.

Isolation: Transactions are executed in isolation from each other, meaning that one transaction does not see the intermediate states of another. When two transfers occur concurrently, they are executed one after the other in isolation. Each transaction only observes the final, consistent state of the database.

Consistency: Transactions ensure that the database transitions from one consistent state to another. In the banking example, the account balance is consistent before and after the transaction. No interim states are visible to other users.

By using transactions, the online banking system can maintain data consistency, prevent lost updates, and provide a reliable and correct representation of account balances, even in a highly concurrent environment. This ensures that customers' money is managed safely and accurately.

### Question 511.3.2

### What are stored procedures? Give an example of a stored procedure that you might have found useful in your project if you had used a SQL database to store your data.

### Question 511.3.3

### What are subqueries and when should they be used?

A subquery is a query that is embedded within another query. Subqueries should be used to retrieve data that will be used in the main query as a condition for filtering, joining, or performing calculations.

### Question 511.3.4

### Provide an example of a GROUP BY statement that could be used in your project if your data was stored in a SQL database.

An example that was used is 

### Week 4

### Question 511.4.1

### Describe some ways to store text data in SQL databases.

Some ways to store text data in a SQL database is by using the data types VARCHAR, CHAR, or TEXT

### Question 511.4.2

### What are some common functions that can be applied to text data in SQL databases?

Some common functions are concat, len, upper, lower, trim, replace, regex_replace, left, right

### Question 511.4.3

### What is a b-tree index?

A B-tree index, also known as a balanced tree index, is a data structure used in database management systems to improve the efficiency of data retrieval operations. It is a self-balancing tree structure that stores keys (and sometimes associated values) in a way that allows for quick access and efficient range queries. B-tree indexes are commonly used in relational database systems, file systems, and other applications that require fast data retrieval.

Here are some key characteristics and features of B-tree indexes:

Balanced Structure: The "B" in B-tree stands for "balanced." B-tree indexes maintain their balance by ensuring that the height of the tree remains relatively constant. This balance ensures that search operations have a predictable and efficient time complexity.

Hierarchical: B-tree indexes are hierarchical in nature, with a root node at the top and leaf nodes at the bottom. Intermediate nodes, often referred to as internal nodes, form the levels between the root and the leaves.

Sorted Data: Data within a B-tree index is sorted, which allows for efficient range queries. The keys in each node are ordered, making it possible to perform binary searches to find the desired data quickly.

Efficient Search: B-tree indexes support efficient search operations with a time complexity of O(log n), where "n" is the number of keys in the index. This makes them suitable for indexing large datasets.

Balancing Mechanism: As data is inserted or removed from a B-tree index, the structure automatically rebalances itself to maintain its balanced nature. This self-balancing mechanism ensures that the height of the tree remains logarithmic.

Disk-Friendly: B-tree indexes are designed to be disk-friendly, making them well-suited for database systems where data is stored on disk. They minimize the number of I/O operations required to access data.

Supports Duplicate Values: Some variations of B-trees, such as B+ trees, are designed to support duplicate values efficiently. This is important in database systems that allow duplicate keys.

Multi-Level Structure: B-tree indexes can have multiple levels, with the root at the top and leaf nodes at the bottom. The number of levels depends on the number of keys and the branching factor (maximum number of child nodes) of the B-tree.

Widely Used: B-tree indexes are widely used in database systems, including popular relational databases like PostgreSQL, MySQL, and Oracle, to accelerate data retrieval and indexing operations.

### Question 511.4.4

### Show how regular expressions can be used with SQL databases.

Regular expressions can be used to query text data. For example, a SQL statement can contain the regex as part of the where portion.

## SIADS 515: Efficient Data Processing

### Week 1: Linux command line

### Question 515.1.1

### How would you explain what the linux CLI is to someone new to data science?

IT is a text-based interface that allows you to interact with a computer or server by typing commands rather than using a graphical user interface (GUI). 

### Question 515.1.2

### What are some of the more common CLI commands?

ls: List files and directories in the current directory.
cd: Change the current directory.
pwd: Print the current working directory.
touch: Create an empty file.
mkdir: Create a new directory.
rm: Remove files and directories.
cp: Copy files and directories.
mv: Move or rename files and directories.
cat: Concatenate and display the content of files.
more or less: Paginate and display the content of files.
head and tail: Display the beginning or end of a file.
grep: Search for patterns in files.
find: Search for files and directories in a directory hierarchy.
ps: Display a list of running processes.
kill: Terminate processes.
top or htop: Monitor system resource usage and processes.
chmod: Change file and directory permissions.
chown: Change file and directory ownership.
tar: Create or extract compressed archive files.
ssh: Connect to a remote server via Secure Shell.
scp: Securely copy files between local and remote systems.
rsync: Synchronize files and directories between systems.
df and du: Display disk space usage information.
ifconfig or ip: Configure network interfaces.
ping and traceroute: Network diagnostic tools.
wget or curl: Download files from the internet.
man: Display manual pages for commands.
history: View command history.
alias: Create command aliases.
date: Display or set the system date and time.
Windows:

dir: List files and directories in the current directory.
cd: Change the current directory.
echo: Display messages or set variables.
type: Display the content of files.
copy: Copy files and directories.
move or ren: Move or rename files and directories.
del: Delete files.
mkdir: Create a new directory.
rmdir: Remove directories.
cls: Clear the screen.
ipconfig: Display network configuration information.
ping: Test network connectivity.
tasklist: List running processes.
taskkill: Terminate processes.
regedit: Access the Windows Registry.
systeminfo: Display system information.
sfc: System File Checker for system file integrity.
chkdsk: Check and repair disk errors.
net: Network-related commands (e.g., net user, `

### Question 515.1.3

### What are some of the difficulties associated with using the CLI?

Using the Command Line Interface (CLI) can be a powerful and efficient way to interact with a computer, but it also comes with its share of difficulties and challenges. Here are some of the common difficulties associated with using the CLI:

Lack of Graphical Interface: The CLI is text-based, which means it lacks the graphical elements and user-friendly interfaces found in Graphical User Interfaces (GUIs). This can make it less intuitive, especially for users who are more accustomed to GUIs.

Steep Learning Curve: CLI commands often require specific syntax and options. Learning the commands and their associated flags can be challenging for beginners, and it may take time to become proficient.

Case Sensitivity: Most CLIs are case-sensitive, meaning that "command," "Command," and "COMMAND" could be treated as different commands. This can lead to errors, especially for users not accustomed to case sensitivity.

Command Memorization: CLI users often need to memorize or refer to documentation to recall the correct command syntax and options. This can be time-consuming and may result in frequent lookup tasks.

Lack of Discoverability: Unlike GUIs, CLIs may not provide on-screen guidance or menus to help users discover available commands and features. Users must often rely on documentation or external sources.

Errors and Typos: Typing errors can result in unintended consequences or errors. A simple typo in a command can lead to a different action than what was intended.

Complex Pipelines: Building complex data processing pipelines or sequences of commands can be challenging, especially when combining multiple tools and utilities.

Limited Visual Feedback: The CLI typically provides textual feedback, which may not be as informative or visually appealing as GUI feedback, making it harder to interpret results.

Security Risks: Running commands with administrative privileges can lead to security risks if not done carefully. In the CLI, it's essential to be cautious with commands that can affect system configuration or access sensitive data.

Scripting Complexity: Writing and debugging scripts in the CLI can be complex, as scripts often need to handle variables, conditionals, loops, and error handling.

Platform Differences: Different operating systems and distributions may have variations in commands, flags, and file paths, which can lead to confusion for users moving between platforms.

Accessibility: The CLI can be challenging for users with certain disabilities, such as visual impairments, as it relies heavily on text-based interaction.

Version Compatibility: Command-line tools and utilities may have different versions, and scripts written for one version may not be compatible with another. Managing version compatibility can be a challenge.

Multilingual Challenges: For users who do not speak English as their first language, the CLI may pose language and syntax challenges, as many commands and documentation are in English.

### Question 515.1.4

### Describe ways in which you could have (or did) use the linux command line in your project.

We used the CLI for git commands for version control.

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

### While developing your code for the project there were likely times that your code didn’t work, or didn’t work as expected. Describe the process you followed to fix the problem(s) with your code.

We began troubleshooting the most fundamental/basic issues then progressively moved to more complex issues. For example, we checked initial set up configuration like if Python was install, then the version installed, next we checked if the repo was cloned correctly. We also checked the library/packages versions that were installed. These problems were mitigated with a requirements.txt file and using a virtual environment.

### Question 515.3.2

### Suggest some reasons why print debugging, while common, may not be the best approach.

It is less effective in complex or long-term projects. This approach has limited visibility, adds code congestion, amd added security risks.

### Question 515.3.3

### JupyterLab provides access to a debugger but it isn’t commonly used. Propose reasons why that’s the case and suggest ways in which the debugger could be changed to make it more accessible.

upyterLab does provide access to a debugger, but it is true that it may not be as commonly used as other features in JupyterLab. There are several reasons for this, and there are ways to make the debugger more accessible and user-friendly:

Reasons for Limited Use of the Debugger in JupyterLab:

Awareness: Many users, especially beginners in data science and programming, may not be aware of the debugger's existence or how to use it effectively. They often rely on print statements or other debugging techniques.

Ease of Use: Some users find the debugger's interface and functionality in JupyterLab less intuitive compared to integrated development environments (IDEs) like PyCharm or Visual Studio Code, which have more robust debugging features.

Complexity: Debugging can be seen as a complex process, and users might find it daunting to learn how to set breakpoints, inspect variables, and step through code.

Prior Experience: Users who have prior experience with other IDEs might prefer those environments for debugging because they are more familiar with the tools available.

Ways to Make the Debugger More Accessible in JupyterLab:

Improved Documentation and Tutorials: Provide clear and beginner-friendly documentation and tutorials on how to use the debugger in JupyterLab. Include step-by-step guides and examples to help users get started.

Interactive Walkthroughs: Implement interactive walkthroughs or guided tours within JupyterLab that introduce users to the debugger's features and how to use them effectively.

Integration with Notebooks: Make the debugger seamlessly integrated with Jupyter notebooks. Allow users to set breakpoints directly within code cells, and provide a visual indication when a breakpoint is active.

Simplified User Interface: Simplify the user interface for the debugger. Make it more user-friendly and intuitive, especially for users who are not familiar with debugging concepts.

Interactive Variable Inspection: Offer interactive variable inspection within the notebook environment, allowing users to view the values of variables at different points in their code with ease.

Code Annotations: Allow users to add comments or annotations to their code during debugging sessions. This can help with documenting the debugging process.

Integration with Popular Libraries: Ensure that the debugger integrates seamlessly with popular data science libraries like NumPy, pandas, and Matplotlib, making it a valuable tool for data scientists.

Community Engagement: Encourage the JupyterLab community to share best practices for debugging in JupyterLab and create a space for users to seek help and share their experiences.

Visual Debugging: Consider implementing visual debugging features, such as the ability to visualize data structures or flowcharts, which can make the debugging process more intuitive.

Error Handling and Messaging: Provide clearer error messages and handling within JupyterLab to guide users when they encounter issues during debugging.

### Question 515.3.4

### One of the more common errors is the syntax error. Sometimes, syntax errors are accompanied by a statement like “missing : “. Explain why, if python knows what’s missing, it can’t simply fix the problem for you.

### Week 4

### Question 515.4.1

### Why do we care about code complexity?



### Question 515.4.2

### Identify places in your code where the complexity of your approach resulted in suboptimal efficiency. Propose ways in which you could have improved your code.

### Question 515.4.3

### Jupyter notebooks promote a fragmented approach to coding, with each cell being executed independently of others. Explain why this promotes inefficient code design and suggest ways to promote the creation of efficient code.

Code is often written in small, isolated cells can make it difficult to reuse code or maintain a clear codebase. Variables created in one cell are accessible in other cells. If code cells are executed out of order, this can cause issues related to execution order.

Some ways to Promote Efficient Code in Jupyter Notebooks is to use Markdown for documentation, efficiency/logically structure your notebook, create functions to encapsulate code with specific functionality, use clear and meaningful variable names.

### Question 515.4.4

### Explain how source code for underlying libraries such as pandas, numpy, and scipy can be examined to understand how the underlying operations are coded.

By viewing documentation found in the websites or repositories of their respective sources.

## SIADS 516: Big Data: Scalable Data Processing

### Week 1

### Question 516.1.1

### What are the characteristics of Big Data?

### Question 516.1.2

### What is map reduce and how can it be used to help analyze Big Data?

Map Reduce is a processing framework to process and analyze large volumes of data in a parallel and distributed computing environment. 

### Question 516.1.3

### What are some advantages and limitations of using distributed computing?

Advantages - Scalablilty, fault tolerance, performance, load balancing, cost efficiency
Disadvantages - Complexity, Security concerns, consistency and syncronization

### Question 516.1.4

### Provide a description of Hadoop and explain why it’s a reasonable choice for analyzing Big Data.

Hadoop is a collection of resources/computers to act as a large scale database. Hadoop is able to allocate copmuting power and resources accordingly to store and query data. 

### Week 2

### Question 516.2.1

### What is Apache Spark?

An open-source, distributed data processing framework designed for big data and advanced analytics. It provides a powerful, fast, and general-purpose data processing engine that supports a wide range of use cases.

### Question 516.2.2

### How do Resilient Distributed Datasets facilitate the use of distributed computing?

Resilient Distributed Datasets (RDDs) are a fundamental data structure in Apache Spark that facilitate the use of distributed computing by providing a way to represent and manipulate data in a distributed and fault-tolerant manner. RDDs offer several key features that make them essential for distributed computing:

Distribution: RDDs are distributed collections of data. They partition the data into smaller chunks, which can be distributed across multiple nodes in a cluster. This enables parallel processing of data, as different nodes can work on different parts of the dataset simultaneously.

Fault Tolerance: RDDs are fault-tolerant. They automatically track the lineage of data transformations, which means that if a node fails, the lost data partitions can be recomputed based on the transformations applied to the original data. This lineage information ensures that data is not lost in the event of a node failure, making RDDs robust for distributed computing.

Immutability: RDDs are immutable, which means that once data is created in an RDD, it cannot be changed. Instead, transformations applied to RDDs create new RDDs. This immutability simplifies the process of reasoning about the data flow and maintaining fault tolerance.

Parallel Operations: RDDs support various high-level, parallel operations, such as map, reduce, filter, and join. These operations can be applied to the data partitions on different nodes concurrently, allowing for efficient data processing.

In-Memory Computing: RDDs can be cached in memory, which significantly speeds up data processing. By persisting data in memory, Spark avoids the need to read from disk for each operation, resulting in much faster computations.

Ecosystem Integration: RDDs can be seamlessly integrated with Spark's higher-level libraries and components, such as Spark SQL, Spark Streaming, and MLlib. This integration enables a wide range of data processing tasks, including batch processing, real-time streaming, machine learning, and graph processing, all using a common data structure.

User-Defined Functions: RDDs allow users to define custom functions and operations that can be applied to the data. This flexibility makes them suitable for a wide range of data manipulation and transformation tasks.

### Question 516.2.3

### How do Pair RDDs differ from plain RDDs, and why is that important?

### Question 516.2.4

### What are some limitations of using RDDs?

### Week 3

### Question 516.3.1

### What are Spark DataFrames?

A distributed collection of data organized into named columns, similar to data frames in Python and data sets in SQL. They are a fundamental data structure in Apache Spark, an open-source, distributed data processing framework designed for big data processing and analytics. 

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

Working at an enterprise-sized company you leverage Apache Spark for initial data processing and filtering, and then use Pandas for in-depth local analysis when the dataset is smaller and feasible to use Pandas with.

## SIADS 521: Visual Exploration of Data

### Week 1

### Question 521.1.1

### What is matplotlib?

Matplotlib is a Python library for creating static, animated, and interactive data visualizations in various formats. 

### Question 521.1.2

### Describe how you could use matplotlib to create a histogram of some data that you used in your project.

### Question 521.1.3

### Create a boxplot of one of the variables from your data.

plt.figure(figsize=(8, 6))
plt.boxplot(df, vert=False)
plt.title('Boxplot of Your Variable')
plt.xlabel('Values')
plt.show()

### Question 521.1.4

### Create a univariate plot of your choice and annotate something noteworthy in your plot.

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=20, edgecolor='k', alpha=0.7)
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

mean_value = np.mean(data)

plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
plt.legend()

plt.show()

### Week 2

### Question 521.2.1

### What is meant by “the computational narrative”? How did you create a computational narrative in your project work?

The practice of combining code and data with explanations, visualizations, and storytelling to convey information, insights, or explanations of a computational process or analysis. We added comments in our code and using markdown to explain our process through each step of our analysis.

### Question 521.2.2

### Demonstrate the effect of changing the number of bins in a histogram of one of your variables.

### Question 521.2.3

### What are the advantages and drawbacks of using violin plots?

Advantages - displays distribution shape, comparison across categories/variables

Disadvantages - complexity, not suitable for large datasets, possible misinterpretation, dependence on binwidth, can only be used with continuous data.

### Question 521.2.4

### Show how a probability plot can be used to gain insights about any of the variables you used in your project.

### Week 3

### Question 521.3.1

### What sorts of data are suitable for use in heat maps?

2-D data, matrix data, numerical data, categorical data

### Question 521.3.2

### What are tree maps used for?

Tree maps are visualizations used to display hierarchical data to represent the structure and proportions of data elements. 

### Question 521.3.3

### Demonstrate the use of a SPLOM with data from your project.

### Week 4

### Question 521.4.1

### What are some advantages and drawbacks of using 3D plots?

Advantages - Can plot more variables, enhanced presentation/representation
Disadvantages - Can be too complex or messy, difficulty of comparison

### Question 521.4.2

### What is autocorrelation and how can visualization be used to detect it?

### Question 521.4.3

### Describe some of the challenges associated with using geographic maps as visualizations.

## SIADS 522: Information Visualization I

### Week 1

### Question 522.1.1

### What is Anscombe’s Quartet and why is it important in visualization?

### Question 522.1.2

### Who is Edward Tufte and why is he important in visualization?

### Question 522.1.3

### What is the block model and how might it apply to the work you did in your project?

### Week 2

### Question 522.2.1

### What are nominal, ordinal and quantitative data types? Provide examples from your project.

### Question 522.2.2

### In visualization, what does “encoding” mean?

Mapping data attributes to visual properties of a graph or chart. 

### Question 522.2.3

### In visualization, what do “expressiveness” and “effectiveness” mean?

Expressiveness is how many variables are visualized and effectiveness is 

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

We could make our algorithm seem like it performed much better than it actually did.

### Question 522.4.3

### What is chart junk? Comment on the degree to which you have chart junk in your visualizations.

Unnecessary, distracting, or non-informative elements or decorations added to a data visualization or chart that do not contribute to the audience's understanding of the data. I believe we minimized chart junk to ensure our visualizations were effective yet still being clean. For example we added grid lines when it made sense and didn't when it made the chart too congested/messy.

### Question 522.4.4

### Discuss the role of ethics when creating visualizations.

It is important to try to portray the data as accurately as possible when creating a visualization. Visualizations can be powerful tools for conveying information, shaping opinions, and influencing decisions. Ethical considerations should guide the creation and presentation of visualizations to ensure that they are honest, fair, and respectful of individuals and groups. 
