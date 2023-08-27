import psycopg2

# Define the database connection parameters
db_params = {
    'host': '127.0.0.1',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'admin'
}

# Function to insert data into the PostgreSQL database
def insert_data(policy_report_record, policy_summary_record):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_params)
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Insert data into the database
        cur.execute("""
            INSERT INTO policy_records (policynumber, policytype, policyholdername, coveragelimits, 
                                       policypremium, claim_status, age, car_value, property_type, property_value, coverage_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            policy_report_record['Policy-Number'],
            policy_report_record['Policy-Type'],
            policy_report_record['Policy-Holder-Name'],
            policy_report_record['Coverage-Limits'],
            policy_report_record['Policy-Premium'],
            policy_report_record['Claim-Status'],
            policy_report_record['Age'],
            policy_report_record['Car-Value'],
            policy_report_record['Property-Type'],
            policy_report_record['Property-Value'],
            policy_report_record['Coverage-Amount']
        ))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        
        print("Data inserted successfully.")
    
    except (Exception, psycopg2.Error) as error:
        print(f"Error inserting data: {error}")

# Example usage
policy_report_record = {
    'Policy-Number': '1234567890',
    'Policy-Type': 'Auto',
    'Policy-Holder-Name': 'John Doe',
    'Coverage-Limits': 1000.00,
    'Policy-Premium': 500.00,
    'Claim-Status': 'PAY',
    'Age': 35,
    'Car-Value': 25000.00,
    'Property-Type': 'Home',
    'Property-Value': 150000.00,
    'Coverage-Amount': 200000.00
}

policy_summary_record = {
    'Total-Policies': 1,
    'Total-Premiums': 500.00,
    'Total-Claims': 1,
    'Total-Rejected-Claims': 0
}

insert_data(policy_report_record, policy_summary_record)
