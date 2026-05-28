
import pandas as pd
import random
from datetime import datetime, timedelta

companies = [
    "Barclays", "HSBC", "Deloitte", "Monzo", "Revolut", "KPMG",
    "Lloyds", "Natwest", "PwC", "Accenture", "McKinsey", "Capgemini",
    "JP Morgan", "Goldman Sachs", "Santander", "Nationwide", "BDO",
    "EY", "IBM", "Thoughtworks", "Experian", "Aviva", "Aon", "Sage"
]

roles = [
    "Business Analyst", "Junior BA", "BA Consultant",
    "Operations Analyst", "Data Analyst", "Systems Analyst"
]

sources = ["LinkedIn", "Indeed", "Company Site", "Glassdoor", "Referral"]
statuses = ["No Response", "Rejected", "Interview", "Offer"]
weights = [0.45, 0.25, 0.25, 0.05]

applications = []
start_date = datetime(2026, 1, 1)

for i in range(50):
    date = start_date + timedelta(days=random.randint(0, 140))
    applications.append({
        "company": random.choice(companies),
        "role": random.choice(roles),
        "date": date.strftime("%Y-%m-%d"),
        "source": random.choice(sources),
        "status": random.choices(statuses, weights=weights)[0]
    })

df = pd.DataFrame(applications)
df = df.sort_values("date").reset_index(drop=True)

print(df)
print("\n--- Summary ---")
print("Total applications: " + str(len(df)))
print("\nStatus breakdown:")
print(df["status"].value_counts())
print("\nApplications by source:")
print(df["source"].value_counts())


print("\n--- Conversion Rates by Source ---")
for source in df["source"].unique():
    source_df = df[df["source"] == source]
    total = len(source_df)
    offers = len(source_df[source_df["status"] == "Offer"])
    rate = round((offers / total) * 100, 1)
    print(source + ": " + str(offers) + " offers from " + str(total) + " applications (" + str(rate) + "%)")


print("\n--- Interview to Offer Rate ---")
interviews = len(df[df["status"] == "Interview"])
offers = len(df[df["status"] == "Offer"])
total = len(df)

print("Total applications: " + str(total))
print("Interviews: " + str(interviews))
print("Offers: " + str(offers))
print("Application to interview rate: " + str(round((interviews/total)*100, 1)) + "%")
print("Interview to offer rate: " + str(round((offers/interviews)*100, 1)) + "%")


import matplotlib.pyplot as plt

status_counts = df["status"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(status_counts.index, status_counts.values, color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
plt.title("Job Application Status Breakdown")
plt.xlabel("Status")
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.savefig("application_chart.png")
plt.show()
print("Chart saved as application_chart.png")

df.to_csv("job_applications.csv", index=False)
print("Data exported to job_applications.csv")
