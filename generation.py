import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Number of records for the sample
num_records = 1000

# Function to generate a list of fake names
def generate_names(n):
    return [fake.name() for _ in range(n)]

# Function to generate a list of fake addresses
def generate_addresses(n):
    return [fake.address().replace("\n", ", ") for _ in range(n)]

# Function to generate a list of fake emails
def generate_emails(n):
    return [fake.email() for _ in range(n)]

# Function to generate a list of fake phone numbers
def generate_phones(n):
    return [fake.phone_number() for _ in range(n)]

# Generate Personal Identifiers
personal_identifiers = pd.DataFrame({
    'Name': generate_names(num_records),
    'Address': generate_addresses(num_records),
    'Email': generate_emails(num_records),
    'Phone': generate_phones(num_records)
})

# Generate Demographics
demographics = pd.DataFrame({
    'Race': [fake.random_element(elements=('White', 'Black', 'Asian', 'Hispanic', 'Other')) for _ in range(num_records)],
    'Income': np.random.randint(20000, 100000, num_records),
    'Distance from School': np.random.uniform(0.5, 20.0, num_records).round(2),
    'Gender': [fake.random_element(elements=('Male', 'Female', 'Non-Binary')) for _ in range(num_records)]
})

# Generate Academics - Simplified for this example
academics = pd.DataFrame({
    'Class Enrollment History': ['Math, Science, English' for _ in range(num_records)],  # Simplified example
    'Grade History': ['A, B, A' for _ in range(num_records)],  # Simplified example
    'Current Grades': ['A' for _ in range(num_records)],  # Simplified example
    'Test Scores': np.random.randint(60, 100, num_records),
    'Special Needs': [fake.boolean(chance_of_getting_true=20) for _ in range(num_records)]  # 20% chance
})

# Combine all data into one DataFrame
synthetic_data = pd.concat([personal_identifiers, demographics, academics], axis=1)

# Display the first few rows of the synthetic data
print(synthetic_data.head())
