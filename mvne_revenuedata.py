import random
import pandas as pd
from datetime import datetime, timedelta

# Configuration for multiple tenants
tenants = [
    {
        "tenant_name": "ConnectaLatina",
        "event_types": ["Voice", "SMS", "Data", "Top-up"],
        "num_accounts": 55600,
        "avg_calls_per_account": 10,
        "avg_minutes_per_call": 2,
        "avg_sms_per_account": 15,
        "avg_data_sessions_per_account": 5,
        "avg_gb_per_session": 0.5,
        "avg_topups_per_account": 3,
        "revenue_start": 1000,
        "revenue_end": 5000,
        "start_date": datetime(2024, 9, 1),
        "end_date": datetime(2024, 10, 2)
    },
    {
        "tenant_name": "MovilAndes",
        "event_types": ["Voice", "SMS", "Data", "Top-up"],
        "num_accounts": 78500,
        "avg_calls_per_account": 12,
        "avg_minutes_per_call": 1.5,
        "avg_sms_per_account": 20,
        "avg_data_sessions_per_account": 6,
        "avg_gb_per_session": 0.7,
        "avg_topups_per_account": 4,
        "revenue_start": 2000,
        "revenue_end": 6000,
        "start_date": datetime(2024, 8, 1),
        "end_date": datetime(2024, 10, 2)
    },
    {
        "tenant_name": "TeleSur Mobile",
        "event_types": ["Voice", "SMS", "Data", "Top-up"],
        "num_accounts": 40200,
        "avg_calls_per_account": 8,
        "avg_minutes_per_call": 2.5,
        "avg_sms_per_account": 10,
        "avg_data_sessions_per_account": 7,
        "avg_gb_per_session": 0.8,
        "avg_topups_per_account": 2,
        "revenue_start": 1500,
        "revenue_end": 5500,
        "start_date": datetime(2024, 9, 1),
        "end_date": datetime(2024, 10, 2)
    }
]

# Function to generate random values for the day
def generate_daily_data(tenant, event_type, date):
    tenant_name = tenant["tenant_name"]
    
    if event_type == "Voice":
        count_of_calls = random.randint(tenant["avg_calls_per_account"] - 2, tenant["avg_calls_per_account"] + 2)
        voice_minutes = count_of_calls * random.uniform(tenant["avg_minutes_per_call"] - 0.5, tenant["avg_minutes_per_call"] + 0.5)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": count_of_calls,
            "Voice Minutes": round(voice_minutes, 2),
            "Count of SMS": None,
            "Data Count": None,
            "Data in GB": None,
            "Revenue": round(random.uniform(tenant["revenue_start"], tenant["revenue_end"]), 2)
        }
    elif event_type == "SMS":
        count_of_sms = random.randint(tenant["avg_sms_per_account"] - 5, tenant["avg_sms_per_account"] + 5)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": None,
            "Voice Minutes": None,
            "Count of SMS": count_of_sms,
            "Data Count": None,
            "Data in GB": None,
            "Revenue": round(random.uniform(tenant["revenue_start"], tenant["revenue_end"]), 2)
        }
    elif event_type == "Data":
        data_sessions = random.randint(tenant["avg_data_sessions_per_account"] - 1, tenant["avg_data_sessions_per_account"] + 1)
        data_in_gb = data_sessions * random.uniform(tenant["avg_gb_per_session"] - 0.1, tenant["avg_gb_per_session"] + 0.1)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": None,
            "Voice Minutes": None,
            "Count of SMS": None,
            "Data Count": data_sessions,
            "Data in GB": round(data_in_gb, 2),
            "Revenue": round(random.uniform(tenant["revenue_start"], tenant["revenue_end"]), 2)
        }
    elif event_type == "Top-up":
        topup_count = random.randint(tenant["avg_topups_per_account"] - 1, tenant["avg_topups_per_account"] + 1)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": None,
            "Voice Minutes": None,
            "Count of SMS": None,
            "Data Count": None,
            "Data in GB": None,
            "Revenue": round(random.uniform(tenant["revenue_start"], tenant["revenue_end"]), 2),
            "Top-up Count": topup_count
        }

# Generate data for every day between start and end date for each event type and each tenant
data = []
for tenant in tenants:
    current_date = tenant["start_date"]
    while current_date <= tenant["end_date"]:
        for event_type in tenant["event_types"]:
            data.append(generate_daily_data(tenant, event_type, current_date))
        current_date += timedelta(days=1)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = "mvne_revenue_data.csv"
df.to_csv(output_file, index=False)

print(f"Data has been generated and saved to {output_file}")

