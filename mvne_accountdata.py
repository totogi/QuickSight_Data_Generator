import random
import pandas as pd
from datetime import datetime, timedelta

# Configuration for multiple tenants
tenants = [
    {
        "tenant_name": "ConnectaLatina",
        "country_code": "596",
        "num_digits": 8,
        "num_records": 55600,
        "start_date": datetime(2024,9 , 1),
        "end_date": datetime(2024, 10, 2),
        "credit_limit_min": 10.00,
        "credit_limit_max": 500.00,
        "plan_names": ["Basic Plan", "Standard Plan", "Premium Plan", "Unlimited Plan"]
    },
    {
        "tenant_name": "MovilAndes",
        "country_code": "598",
        "num_digits": 10,
        "num_records": 78500,
        "start_date": datetime(2024, 8, 1),
        "end_date": datetime(2024, 10, 2),
        "credit_limit_min": 20.00,
        "credit_limit_max": 600.00,
        "plan_names": ["Economy Plan", "Business Plan", "First Class Plan"]
    },
    {
        "tenant_name": "TeleSur Mobile",
        "country_code": "597",
        "num_digits": 10,
        "num_records": 40200,
        "start_date": datetime(2024, 9, 1),
        "end_date": datetime(2024, 10, 2),
        "credit_limit_min": 15.00,
        "credit_limit_max": 700.00,
        "plan_names": ["Starter Plan", "Pro Plan", "Ultra Plan"]
    }
]

# Function to generate random mobile number
def generate_mobile_number(country_code, num_digits):
    return f"{country_code}{random.randint(10**(num_digits-1), 10**num_digits - 1)}"

# Function to generate random activation date
def generate_activation_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate random credit limit/balance
def generate_credit_limit(min_limit, max_limit):
    return round(random.uniform(min_limit, max_limit), 2)

# Generate data for each tenant
data = []
for tenant in tenants:
    for _ in range(tenant["num_records"]):
        tenant_name = tenant["tenant_name"]
        account_id = generate_mobile_number(tenant["country_code"], tenant["num_digits"])
        device_id = account_id  # same as account_id
        activation_date = generate_activation_date(tenant["start_date"], tenant["end_date"])
        account_type = random.choice(["prepaid", "postpaid"])
        credit_limit = generate_credit_limit(tenant["credit_limit_min"], tenant["credit_limit_max"])
        plan_name = random.choice(tenant["plan_names"])

        data.append({
            "tenant_name": tenant_name,
            "account_id": account_id,
            "device_id": device_id,
            "activation_date": activation_date.strftime("%Y-%m-%d"),
            "account_type": account_type,
            "credit_limit": credit_limit,
            "plan_name": plan_name
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the generated data to a CSV file
df.to_csv("mvne_account_data.csv", index=False)

# Print the DataFrame to the console
print(df)

