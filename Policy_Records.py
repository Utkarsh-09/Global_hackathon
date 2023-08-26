import psycopg2

# Define your PostgreSQL connection parameters
db_params = {
    'host': '127.0.0.1',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'admin'
}

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define your PolicyRecord data as a list of dictionaries
policy_records = [
    {
        'Policy_Number': 'Policy123',
        'Policy_Holder_Name': 'John Doe',
        'Premium_Amount': 1000.99,
        'Policy_Type': 'CAR_INSURANCE',
        'Age': 30,
        'Car_Value': 25000.50,
        'Property_Type': 'House',
        'Property_Value': 300000.75,
        'Coverage_Amount': 500000.00,
        'Claim_Status':'APPROVED'
    },
    # Add more records as needed
]

# Iterate through policy records and perform the calculations
for policy_record in policy_records:
    if policy_record['Policy_Type'] == 'CAR_INSURANCE':
        policy_record['Coverage_Limits'] = 100000
        policy_record['Policy_Premium'] = 1000
    elif policy_record['Policy_Type'] == 'HOME_INSURANCE':
        policy_record['Coverage_Limits'] = 500000
        policy_record['Policy_Premium'] = 2000
    elif policy_record['Policy_Type'] == 'LIFE_INSURANCE':
        policy_record['Coverage_Limits'] = 1000000
        policy_record['Policy_Premium'] = 3000
    else:
        policy_record['Coverage_Limits'] = 0
        policy_record['Policy_Premium'] = 0

    # Perform additional premium calculations
    age = policy_record['Age']
    car_value = policy_record['Car_Value']

    if age < 25:
        policy_record['Policy_Premium'] += 300
    elif age < 41:
        policy_record['Policy_Premium'] += 200
    elif age <= 60:
        policy_record['Policy_Premium'] += 400

    if car_value < 20000:
        policy_record['Policy_Premium'] += 0.05
    elif car_value < 50000:
        policy_record['Policy_Premium'] += 0.08

# Insert policy records into the PostgreSQL database
for policy_record in policy_records:
    cursor.execute("""
        INSERT INTO policy_records (
            PolicyNumber,
            PolicyHolderName,
            PremiumAmount,
            PolicyType,
            CoverageLimits,
            PolicyPremium,
            Age,
            Car_Value,
            Property_Type,
            Property_Value,
            Coverage_Amount,
            Claim_Status       
        )
        VALUES (%(Policy_Number)s, %(Policy_Holder_Name)s, %(Premium_Amount)s, 
                %(Policy_Type)s, %(Coverage_Limits)s, %(Policy_Premium)s, %(Age)s, 
                %(Car_Value)s, %(Property_Type)s, %(Property_Value)s, %(Coverage_Amount)s,%(Claim_Status)s)
    """, policy_record)

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()
