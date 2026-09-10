import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

departments = [
    "HR",
    "IT",
    "Finance",
    "Sales",
    "Marketing",
    "Operations",
    "Customer Support"
]

themes = {
    "Communication": [
        "Need better internal communication",
        "Important information is not shared on time",
        "Teams should communicate more clearly",
        "There should be better communication between departments",
        "We need regular team updates"
    ],

    "Workload": [
        "The workload is too high",
        "Too many tasks are assigned at once",
        "Work pressure is increasing",
        "We need better workload distribution",
        "Some employees have too much work"
    ],

    "Management": [
        "Managers should give more feedback",
        "Management should listen to employees",
        "We need better support from managers",
        "Managers should communicate expectations clearly",
        "Leadership can improve employee support"
    ],

    "Work Environment": [
        "The workplace environment is comfortable",
        "The office environment could be improved",
        "We need a better working environment",
        "The workplace facilities are good",
        "The work environment needs improvement"
    ],

    "Recognition": [
        "Employees should be appreciated more",
        "Good work should receive more recognition",
        "We need better employee appreciation",
        "Hard work should be recognized",
        "Employees deserve more recognition"
    ],

    "Career Growth": [
        "More training opportunities are needed",
        "Employees need better career growth opportunities",
        "We need more learning programs",
        "There should be clearer promotion opportunities",
        "More professional development would help"
    ],

    "Compensation": [
        "Salary structure could be improved",
        "Employees need better compensation",
        "Pay should be reviewed regularly",
        "Compensation should reflect responsibilities",
        "Benefits could be improved"
    ]
}

uncertain_comments = [
    "Things could be better",
    "Not sure about this",
    "Maybe some changes are needed",
    "It is okay",
    "Could improve",
    "I don't know",
    "No clear opinion",
    "There are some issues",
    "Nothing specific"
]

incomplete_comments = [
    "",
    "Need improvement",
    "Communication...",
    "Workload",
    "Manager",
    "Better",
    "Not good"
]

records = []

start_date = datetime.now() - timedelta(days=30)

for i in range(1, 1201):

    record_id = f"HR-{300 + i}"

    employee_alias = f"EMP-{random.randint(100, 999)}"

    department = random.choice(departments)

    record_type = random.random()

    if record_type < 0.10:

        input_text = random.choice(uncertain_comments)
        category = "Unclear"

    elif record_type < 0.15:

        input_text = random.choice(incomplete_comments)
        category = "Unclear"

    else:

        category = random.choice(list(themes.keys()))
        input_text = random.choice(themes[category])

    source_id = f"SRC-{random.randint(1000, 9999)}"

    if category == "Unclear":
        score = round(random.uniform(0.20, 0.55), 2)
    else:
        score = round(random.uniform(0.60, 0.98), 2)

    status = "Pending"

    reviewer_action = "None"

    audit_timestamp = (
        start_date +
        timedelta(minutes=random.randint(0, 43200))
    ).strftime("%Y-%m-%d %H:%M:%S")

    records.append({
        "record_id": record_id,
        "employee_alias": employee_alias,
        "department": department,
        "input_text": input_text,
        "category": category,
        "source_id": source_id,
        "score": score,
        "status": status,
        "reviewer_action": reviewer_action,
        "audit_timestamp": audit_timestamp
    })


df = pd.DataFrame(records)

df.to_csv("survey_data.csv", index=False)

print("Successfully generated 1,200 synthetic survey comments.")
print("\nFirst 5 records:")
print(df.head())

print("\nCategory distribution:")
print(df["category"].value_counts())