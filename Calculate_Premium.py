import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432"
)
cursor = conn.cursor()

def calculate_additional_premium(age, car_value):
    additional_premium = 0
    
    if age < 25:
        additional_premium += 300
    elif age < 41:
        additional_premium += 200
    elif age <= 60:
        additional_premium += 400
    
    if car_value < 20000:
        additional_premium += 0.05
    elif car_value < 50000:
        additional_premium += 0.08
    
    return additional_premium

def calculate_premium(policy):
    policy_type = policy[4]
    base_premiums = {
        "CAR_INSURANCE": 1000,
        "HOME_INSURANCE": 2000,
        "LIFE_INSURANCE": 3000
    }
    
    base_premium = base_premiums.get(policy_type, 0)
    additional_premium = calculate_additional_premium(policy[7], policy[11])
    
    return base_premium + additional_premium

def update_policy_records(policy_records):
    for record in policy_records:
    
        policy_premium = calculate_premium(record)
        coverage_limits = 0
          
        if record[4] == "CAR_INSURANCE":
            coverage_limits = 100000
        elif record[4] == "HOME_INSURANCE":
            coverage_limits = 500000
        elif record[4] == "LIFE_INSURANCE":
            coverage_limits = 1000000
        
        # Update the records in the database
        update_query = """
        UPDATE policy_records
        SET "coveragelimits" = %s, "policypremium" = %s
        WHERE "policynumber" = %s;
        """
        cursor.execute(update_query, (coverage_limits, policy_premium, record[0]))
    
    conn.commit()

def main():
    # Fetch policy records from the database
    select_query = """
    SELECT *
    FROM policy_records
    LIMIT 10;
    """
    cursor.execute(select_query)
    policy_records = cursor.fetchall()
    
    # Perform premium calculations and update records
    update_policy_records(policy_records)
    
    print("Premiums calculated.")
    
    # Close the database connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
