import sqlite3
import pandas as pd

# Load the Chinook database
conn = sqlite3.connect('chinook.db')

# Perform an inner join between customers and invoices tables on CustomerId
query = '''
SELECT c.CustomerId, c.FirstName, c.LastName, COUNT(i.InvoiceId) AS TotalInvoices
FROM customers c
INNER JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId;
'''
customers_invoices = pd.read_sql_query(query, conn)
print(customers_invoices.head())

# Load the movie dataset
movies = pd.read_csv('movie.csv')

# Create two smaller DataFrames
df1 = movies[['director_name', 'color']]
df2 = movies[['director_name', 'num_critic_for_reviews']]

# Perform a left join
left_join = df1.merge(df2, on='director_name', how='left')

# Perform a full outer join
full_outer_join = df1.merge(df2, on='director_name', how='outer')

# Print row counts
print("Left Join Row Count:", len(left_join))
print("Full Outer Join Row Count:", len(full_outer_join))
