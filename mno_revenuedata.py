import random
import pandas as pd
from datetime import datetime, timedelta

# Configuration variables
tenant_name = "Ooredoo Maldives"  # You can change this to fetch from a variable
event_types = ["Voice", "SMS", "Data", "Top-up"]
num_accounts = 25000  # Number of accounts
avg_calls_per_account = 10  # Y value for calls
avg_minutes_per_call = 2  # X value for minutes per call
avg_sms_per_account = 15  # Z value for SMS
avg_data_sessions_per_account = 5  # T value for data sessions
avg_gb_per_session = 0.5  # R value for GB per session
avg_topups_per_account = 3  # I value for top-ups
revenue_start = 1000
revenue_end = 50000
start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 10,16)

# Function to generate random values for the day
def generate_daily_data(event_type, date):
    if event_type == "Voice":
        count_of_calls = random.randint(avg_calls_per_account - 2, avg_calls_per_account + 2)
        voice_minutes = count_of_calls * random.uniform(avg_minutes_per_call - 0.5, avg_minutes_per_call + 0.5)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": count_of_calls,
            "Voice Minutes": round(voice_minutes, 2),
            "Count of SMS": None,
            "Data Count": None,
            "Data in GB": None,
            "Revenue": round(random.uniform(revenue_start, revenue_end), 2)
        }
    elif event_type == "SMS":
        count_of_sms = random.randint(avg_sms_per_account - 5, avg_sms_per_account + 5)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": None,
            "Voice Minutes": None,
            "Count of SMS": count_of_sms,
            "Data Count": None,
            "Data in GB": None,
            "Revenue": round(random.uniform(revenue_start, revenue_end), 2)
        }
    elif event_type == "Data":
        data_sessions = random.randint(avg_data_sessions_per_account - 1, avg_data_sessions_per_account + 1)
        data_in_gb = data_sessions * random.uniform(avg_gb_per_session - 0.1, avg_gb_per_session + 0.1)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": None,
            "Voice Minutes": None,
            "Count of SMS": None,
            "Data Count": data_sessions,
            "Data in GB": round(data_in_gb, 2),
            "Revenue": round(random.uniform(revenue_start, revenue_end), 2)
        }
    elif event_type == "Top-up":
        topup_count = random.randint(avg_topups_per_account - 1, avg_topups_per_account + 1)
        return {
            "Tenant Name": tenant_name,
            "Event Type": event_type,
            "Date": date.strftime("%Y-%m-%d"),
            "Count of Voice Calls": None,
            "Voice Minutes": None,
            "Count of SMS": None,
            "Data Count": None,
            "Data in GB": None,
            "Revenue": round(random.uniform(revenue_start, revenue_end), 2),
            "Top-up Count": topup_count
        }

# Generate data for every day between start and end date for each event type
data = []
current_date = start_date
while current_date <= end_date:
    for event_type in event_types:
        data.append(generate_daily_data(event_type, current_date))
    current_date += timedelta(days=1)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = "MNO_Revenue_Data_v1.2.csv"
df.to_csv(output_file, index=False)

print(f"Data has been generated and saved to {output_file}")

