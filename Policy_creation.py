import psycopg2

# Database connection details
db_config = {
    "database": "postgres",
    "user": "postgres",
    "password": "admin",
    "host": "127.0.0.1",
    "port": "5432"
}

def additional_premium(age, car_value, base_premium):
    additional_premium_temp = 0

    if age < 25:
        additional_premium_temp += 300
    elif age < 41:
        additional_premium_temp += 200
    elif age <= 60:
        additional_premium_temp += 400
    
    if car_value < 20000:
        additional_premium_temp += 0.05
    elif car_value < 50000:
        additional_premium_temp += 0.08

    return base_premium + additional_premium_temp

def create_policy_table(cursor):
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS policy_records ("
            "PolicyNumber VARCHAR(10),"
            "PolicyHolderName VARCHAR(50),"
            "PremiumAmount NUMERIC(9, 2),"
            "PolicyType VARCHAR(15),"
            "CoverageLimits NUMERIC(9, 2),"
            "PolicyPremium NUMERIC(9, 2),"
            "Age NUMERIC(9,2),"
            "Car_Value NUMERIC(9,2),"
            "Property_Type VARCHAR(100),"
            "Property_Value NUMERIC(9,2),"
            "Claim_Status VARCHAR(50),"
            "Coverage_Amount NUMERIC(9, 2))"
        )
    except psycopg2.Error as e:
        print("Error creating the PolicyTable.")
        print(e)

def create_db(cursor):
    try:
        sql = '''CREATE database mydb''';
        #Creating a database
        cursor.execute(sql)
        print("Database created successfully........")
    except psycopg2.Error as e:
        print("Error making database connection")
        print(e)

def main():
    try:
        print("Initializing PostgreSQL connection...")
        connection = psycopg2.connect(**db_config)
        connection.autocommit = True
        cursor = connection.cursor()

        # Create PolicyTable if it doesn't exist
        create_db(cursor)
        create_policy_table(cursor)

        policy_records = [
            # ("Policy123", "John Doe", 1500.00, "CAR_INSURANCE", 1000,1000, 30,10000,"Residential", 2000, 5000)
            # # ... Add more policy records here ...


           
        ]

        for record in policy_records:
            policy_type = record[3]
            age = record[6]
            car_value = record[7]
            base_premium = record[2]

            coverage_limits = 0
            policy_premium = 0

            if policy_type == "CAR_INSURANCE":
                coverage_limits = 100000
                policy_premium = 1000
            elif policy_type == "HOME_INSURANCE":
                coverage_limits = 500000
                policy_premium = 2000
            elif policy_type == "LIFE_INSURANCE":
                coverage_limits = 1000000
                policy_premium = 3000

            # policy_premium = additional_premium(age, car_value, policy_premium)


    #     cursor.execute("""
    #     INSERT INTO policy_records (
    #         Policy_Number,
    #         Policy_Holder_Name,
    #         Premium_Amount,
    #         Policy_Type,
    #         Coverage_Limits,
    #         Policy_Premium,
    #         Age,
    #         Car_Value,
    #         Property_Type,
    #         Property_Value,
    #         Coverage_Amount
    #     )
    #     VALUES (%(Policy_Number)s, %(Policy_Holder_Name)s, %(Premium_Amount)s, 
    #             %(Policy_Type)s, %(Coverage_Limits)s, %(Policy_Premium)s, %(Age)s, 
    #             %(Car_Value)s, %(Property_Type)s, %(Property_Value)s, %(Coverage_Amount)s)
    # """, record)

            cursor.execute(
                "INSERT INTO policy_records (PolicyNumber, PolicyHolderName, PremiumAmount, PolicyType, CoverageLimits, PolicyPremium,Age,Car_Value,Property_Type,Property_Value,Coverage_Amount) "
                "VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)",
                (record[0], record[1], record[2], record[3], coverage_limits, policy_premium,age,car_value,'','','')
            )

        connection.commit()

        print("Policy records inserted successfully.")

    except psycopg2.Error as e:
        print("Error: Unable to connect to or interact with the database.")
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
