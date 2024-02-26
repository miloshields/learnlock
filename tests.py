# Import functions from generation.py
from generation import generate_demographic_weights


# Testing custom demographic weight generation function
for i in range(5):
    print("Generating demographic weights. Test #", i)
    print(generate_demographic_weights())