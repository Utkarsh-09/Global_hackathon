import psycopg2
import random

def random_policy_type():
    random_value = random.randint(1, 3)
    if random_value == 1:
        return "CAR_INSURANCE"
    elif random_value == 2:
        return "HOME_INSURANCE"
    else:
        return "LIFE_INSURANCE"

def random_property_type():
    random_value = random.randint(1, 3)
    if random_value == 1:
        return "Condo"
    elif random_value == 2:
        return "Townhouse"
    else:
        return "Single-family home"

def fetch_policy_data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="127.0.0.1",
        port="5432"
    )

    cursor = conn.cursor()

    print("Fetching policy data from PostgreSQL...")

    for record_count in range(1, 11):
        policy_number = f"POLICY00{record_count}"
        policy_holder_name = f"Policy Holder {record_count}"
        premium_amount = record_count * 100.50
        policy_type = random_policy_type()
        coverage_limits = record_count * 1000
        policy_premium = record_count * 200.75
        age = record_count
        car_value = record_count * 5000.50
        property_type = random_property_type()
        property_value = record_count * 10000.25
        coverage_amount = record_count * 5000

        cursor.execute(
            "INSERT INTO policy_records (PolicyNumber, PolicyHolderName, PremiumAmount, PolicyType, "
            "CoverageLimits, PolicyPremium, Age, Car_Value, Property_Type, Property_Value, Coverage_Amount) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (policy_number, policy_holder_name, premium_amount, policy_type, coverage_limits, policy_premium,
             age, car_value, property_type, property_value, coverage_amount)
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Policy data fetched.")

if __name__ == "__main__":
    fetch_policy_data()
