# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference code provided by the lab: view the employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("-------------------Employee Data-------------------")
print(employee_data)
print("-----------------End Employee Data-----------------")

# STEP 2
# Employee number and last name only
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Same as step 2, but last name comes first
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Same as step 3, but rename employeeNumber to ID with an alias
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# Use CASE to bin job titles into a new 'role' column
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
                THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
# Length of each last name as 'name_length'
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# First two letters of each job title as 'short_title'
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# Reference code provided by the lab: view the orderDetails table
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("-------------------Order Details Data-------------------")
print(order_details)
print("-----------------End Order Details Data-----------------")

# STEP 8
# Sum of each order line's total price, rounding the product (priceEach * quantityOrdered)
# before summing. Values are stored as text, so SQLite converts them for the math.
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""", conn).sum().reset_index(drop=True)  # index 0 so sum_total_price[0] works on any pandas version

# STEP 9
# Order dates live in the orders table (orderDetails has no date column).
# Dates are stored as YYYY-MM-DD, so split them with SUBSTR.
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           SUBSTR(orderDate, 9, 2) AS day,
           SUBSTR(orderDate, 6, 2) AS month,
           SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)

# Close the connection
conn.close()