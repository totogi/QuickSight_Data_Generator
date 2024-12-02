import random
import pandas as pd
from datetime import datetime, timedelta

# Configuration
num_records = 25000  # Set the number of records you want to generate
country_code = "960"
num_digits = 8
start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 10, 16)
credit_limit_min = 50.00
credit_limit_max = 500.00
plan_names = ["Basic Plan", "Standard Plan", "Premium Plan", "Unlimited Plan"]
tenant_id = "Ooredoo Maldives"

# Function to generate random mobile number
def generate_mobile_number():
    return f"{country_code}{random.randint(10**(num_digits-1), 10**num_digits - 1)}"

# Function to generate random activation date
def generate_activation_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate random credit limit/balance
def generate_credit_limit(min_limit, max_limit):
    return round(random.uniform(min_limit, max_limit), 2)

# Generate data
data = []
for _ in range(num_records):
    tenant_name = tenant_id
    account_id = generate_mobile_number()
    device_id = account_id  # same as account_id
    activation_date = generate_activation_date(start_date, end_date)
    account_type = random.choice(["prepaid", "postpaid"])
    credit_limit = generate_credit_limit(credit_limit_min, credit_limit_max)
    plan_name = random.choice(plan_names)
    
    data.append({
        "tenant_name": tenant_id,
        "account_id": account_id,
        "device_id": device_id,
        "activation_date": activation_date.strftime("%Y-%m-%d"),
        "account_type": account_type,
        "credit_limit": credit_limit,
        "plan_name": plan_name
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the generated DataFrame (Remove or modify this line depending on your environment)
# import ace_tools as tools; tools.display_dataframe_to_user(name="Generated Mobile Data", dataframe=df)

# If you want to save it to a CSV file, uncomment the following line
df.to_csv("MNO_Accounts_data_v1.2.csv", index=False)

# For now, just print the DataFrame to the console
print(df)

