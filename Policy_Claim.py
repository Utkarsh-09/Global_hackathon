import psycopg2

# Database connection parameters
db_params = {
    'host': '127.0.0.1',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'admin'
}

def main():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    claim_record = {
        "Policy-Number": "Policy123",
        "Date-of-Loss": "2023-08-15",
        "Cause-of-Loss": "CAR_INSURANCE",   # cause -of- loss change - FIRE To CAR_INSurance
        "Amount-of-Loss": 0.0  # Initial value, will be calculated
    }

    cursor.execute("SELECT * FROM policy_records WHERE PolicyNumber = %s", (claim_record["Policy-Number"],))
    policy_record = cursor.fetchone()

    if claim_record["Date-of-Loss"] > "2023-12-31":
        claim_status = "REJECT"
    else:
        claim_record["Cause-of-Loss"] = policy_record[3]  # Policy-Type

        if policy_record[3] == "CAR_INSURANCE": # FIRE TO CAR_INSURANCE
            claim_record["Amount-of-Loss"] = 5000.0
        elif policy_record[3] == "THEFT":
            claim_record["Amount-of-Loss"] = 10000.0
        elif policy_record[3] == "FLOOD":
            claim_record["Amount-of-Loss"] = 20000.0
        else:
            claim_status = "REJECT"

        if claim_record["Amount-of-Loss"] <= policy_record[4]:  # Coverage-Limits
            claim_status = "PAID"
        else:
            claim_status = "REJECT"

    # Update the claim status in the database
    cursor.execute("UPDATE policy_records SET Claim_Status = %s WHERE PolicyNumber = %s",
                   (claim_status, claim_record["Policy-Number"]))
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
