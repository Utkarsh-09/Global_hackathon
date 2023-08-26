import psycopg2

# Define your PostgreSQL database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432'
}

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL query to retrieve data from the PolicyDB2File
select_query = "SELECT * FROM Policy_records;"

# Execute the SQL query
cursor.execute(select_query)

# Fetch all rows from the result set
policy_records = cursor.fetchall()

# Close the database connection
conn.close()

# Define a function to update the PolicyRecord based on Policy-Type
def update_policy_record(policy_type):
    if policy_type == "CAR_INSURANCE":
        return 200000, 1200
    elif policy_type == "HOME_INSURANCE":
        return 600000, 2400
    elif policy_type == "LIFE_INSURANCE":
        return 1200000, 3600
    else:
        return 0, 0

# Define lists to store updated values
coverage_limits = []
policy_premiums = []

# Loop through each record from the PolicyDB2File
for record in policy_records:
    policy_type = record[4]  # Assuming Policy-Type is at index 3
    coverage_limit, policy_premium = update_policy_record(policy_type)
    coverage_limits.append(coverage_limit)
    policy_premiums.append(policy_premium)

# Now, you have the updated coverage limits and policy premiums in the lists
# You can use these lists to update the PolicyRecord in Python as needed
