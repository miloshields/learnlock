import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Number of records for the sample
num_records = 1800

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
    'Email': generate_emails(num_records),
    'Phone': generate_phones(num_records)
})

# Generate ratios for demographics
def generate_demographic_weights(n):
    boundaries = sorted(random.random() for _ in range(n-1))
    boundaries = [0] + boundaries + [1]
    weights = [boundaries[i + 1] - boundaries[i] for i in range(n)]
    return weights

# Generate sample income data for a given distribution and range
def generate_income_data(n, possible_distributions, mean_range, std_range):
    distribution = random.choice(possible_distributions)
    mean = random.uniform(*mean_range)
    std = random.uniform(*std_range)

    if distribution == 'normal':
        data = np.random.normal(mean, std, n)
    elif distribution == 'bimodal':
        mean2 = random.uniform(*mean_range)
        std2 = random.uniform(*std_range)
        data = np.concatenate([np.random.normal(mean, std, n // 2), np.random.normal(mean2, std2, n - n // 2)])
    elif distribution == 'lognormal':
        # Convert mean and std of the normal distribution to the scale of the lognormal distribution
        mu = np.log(mean**2 / np.sqrt(std**2 + mean**2))
        sigma = np.sqrt(np.log(1 + (std**2 / mean**2)))
        data = np.random.lognormal(mu, sigma, n)

    return data.round().astype(int)

# Race generation settings
race_options = ['White', 'Black or African American', 'American Indian or Alaska Native', 'Asian', 'Native Hawaiian or Other Pacific Islander', 'Two Or More Races']
race_weights = generate_demographic_weights(len(race_options))

# Income generation settings
possible_income_distributions = ['normal', 'bimodal', 'lognormal']
mean_income_range = (20000, 150000)
std_income_range = (5000, 30000)

# Gender generation settings
gender_distribution = {
    'Male': 0.495,
    'Female': 0.495, 
    'Non-Binary': 0.01
}

# Generate Demographics
demographics = pd.DataFrame({
    'Race': random.choices(race_options, race_weights, k=num_records),
    'Income': generate_income_data(num_records, possible_income_distributions, mean_income_range, std_income_range),
    'Distance from School': np.random.uniform(0.5, 20.0, num_records).round(2),
    'Gender': random.choices(population=list(gender_distribution.keys()),weights=list(gender_distribution.values()),k=num_records)
})
print(demographics.head())

# Class settings
freshman_classes = [
    "Algebra I",
    "Geometry",
    "Biology",
    "English I",
    "World History",
    "Spanish I",
    "French I",
    "German I",
    "Latin I",
    "Mandarin Chinese I",
    "Art I",
    "Music Theory",
    "Band",
    "Choir",
    "Orchestra",
    "Drama",
    "Physical Education",
    "Health"
]
sophomore_classes = [
    "Algebra II",
    "Geometry",
    "Pre-Calculus",
    "Biology",
    "Chemistry",
    "English II",
    "World History",
    "U.S. History",
    "Spanish II",
    "French II",
    "German II",
    "Latin II",
    "Mandarin Chinese II",
    "Art II",
    "Music Theory",
    "Band",
    "Choir",
    "Orchestra",
    "Drama",
    "Computer Science",
    "Health",
    "Physical Education"
]
junior_classes = [
    "Algebra II",
    "Pre-Calculus",
    "Calculus",
    "Chemistry",
    "Physics",
    "English III",
    "U.S. History",
    "AP U.S. History",
    "Spanish III",
    "French III",
    "AP Spanish Language",
    "AP French Language",
    "AP Art History",
    "AP Music Theory",
    "Band",
    "Choir",
    "Orchestra",
    "Drama",
    "Journalism",
    "Speech and Debate",
    "Computer Science",
    "AP Computer Science A",
    "Business Management",
    "Marketing",
    "Accounting",
    "Entrepreneurship",
    "Physical Education"
]
senior_classes = [
    "Calculus",
    "AP Calculus AB",
    "AP Calculus BC",
    "Statistics",
    "AP Statistics",
    "Physics",
    "AP Physics 1",
    "AP Physics 2",
    "Environmental Science",
    "AP Environmental Science",
    "English IV",
    "AP English Language and Composition",
    "AP English Literature and Composition",
    "Government",
    "AP Government and Politics",
    "Economics",
    "AP Microeconomics",
    "AP Macroeconomics",
    "Psychology",
    "AP Psychology",
    "AP Art History",
    "AP Studio Art",
    "AP Music Theory",
    "Band",
    "Choir",
    "Orchestra",
    "Drama",
    "Film Studies",
    "Creative Writing",
    "Speech and Debate",
    "AP Computer Science Principles",
    "Web Design",
    "Graphic Design",
    "Digital Photography",
    "Culinary Arts",
    "Automotive Technology",
    "Carpentry",
    "Welding",
    "Electrical Technology",
    "Anatomy and Physiology",
    "Sports Medicine",
    "Personal Finance",
    "Law and Justice",
    "Forensic Science",
    "Marine Biology",
    "Astronomy",
    "Geology",
    "AP Human Geography",
    "Philosophy",
    "Ethics",
    "World Religions",
    "Gender Studies",
    "African American Studies",
    "Latin American Studies",
    "Native American Studies",
    "AP Capstone Seminar"
]

# Function to choose class year randomly
def choose_class_year():
    return random.choice(['Freshman', 'Sophomore', 'Junior', 'Senior'])

# Function to generate a list of lists of classes for a student in a given year
# for example, a sophomore should have a list for freshman and sophomore years
def generate_class_lists(class_year):
    if class_year == 'Freshman':
        # Randomly select 6-8 classes from the freshman class list
        return [random.sample(freshman_classes, k=random.randint(6, 8))]
    elif class_year == 'Sophomore':
        # Randomly select 6-8 classes for freshman and sophomore years
        return [random.sample(freshman_classes, k=random.randint(6, 8)),
                random.sample(sophomore_classes, k=random.randint(6, 8))]
    elif class_year == 'Junior':
        # Randomly select 6-8 classes from junior, sophomore, and freshman years
        return [random.sample(freshman_classes, k=random.randint(6, 8)),
                random.sample(sophomore_classes, k=random.randint(6, 8)),
                random.sample(junior_classes, k=random.randint(6, 8))]
    else:  # Randomly select 6-8 classes from senior, junior, sophomore, and freshman years
        return [random.sample(freshman_classes, k=random.randint(6, 8)),
                random.sample(sophomore_classes, k=random.randint(6, 8)),
                random.sample(junior_classes, k=random.randint(6, 8)),
                random.sample(senior_classes, k=random.randint(6, 8))]
       
def generate_yearly_grades(class_lists):
    """
    Generates grades for a list of classes for each year based on a specified trend and average grade.

    Parameters:
    - class_lists: List of lists of classes taken by the student for each year.

    Returns:
    - yearly_grades: List of lists of grades for each class in each year, following the specified trend and average grade.
    """
    num_years = len(class_lists)
    yearly_grades = []
    trend = random.choice(['improving', 'declining', 'constant'])
    avg_grade = random.randint(60, 100)

    if trend == 'improving':
        # Start with lower grades and gradually increase
        avg_grade_range = np.linspace(avg_grade - 10, avg_grade + 10, num_years)
    elif trend == 'declining':
        # Start with higher grades and gradually decrease
        avg_grade_range = np.linspace(avg_grade + 10, avg_grade - 10, num_years)
    else:  # 'constant'
        # All grades are around the average grade
        avg_grade_range = np.full(num_years, avg_grade)

    # Generate grades for each year
    for i, class_list in enumerate(class_lists):
        year_avg_grade = avg_grade_range[i]
        grades = [min(max(int(year_avg_grade + np.random.uniform(-5, 5)), 0), 100) for _ in class_list]
        yearly_grades.append(grades)

    return yearly_grades

# Function to generate a list of standardized tests taken based on class year,
# allowing for multiple tests to be taken, and the scores for each test
def generate_test_scores(class_year):
    if class_year == 'Freshman':
        # Randomly select 0-2 tests from the freshman test list
        tests = random.sample(['PSAT 8/9', 'ACT Aspire', 'Pre-ACT', 'SAT', 'ACT'], k=random.randint(0, 1))
    elif class_year == 'Sophomore':
        # Randomly select 0-2 tests from the freshman and sophomore test lists
        tests = random.sample(['PSAT 8/9', 'ACT Aspire', 'Pre-ACT', 'SAT', 'ACT', 'PSAT 10'], k=random.randint(0, 2))
    elif class_year == 'Junior':
        # Randomly select 0-2 tests from the junior and sophomore test lists
        tests = random.sample(['PSAT 8/9', 'ACT Aspire', 'Pre-ACT', 'SAT', 'ACT', 'PSAT 10', 'PSAT/NMSQT', 'SAT Subject Tests', 'AP Exams'], k=random.randint(0, 6))
    else:  # Randomly select 0-2 tests from the senior, junior, and sophomore test lists
        tests = random.sample(['PSAT 8/9', 'ACT Aspire', 'Pre-ACT', 'SAT', 'ACT', 'PSAT 10', 'PSAT/NMSQT', 'SAT Subject Tests', 'AP Exams'], k=random.randint(0, 8))

    # Generate scores for each test (normalized to 0-100)
    scores = {test: np.random.randint(60, 100) for test in tests}
    return tests, scores

def generate_infractions(category, class_year):
    if category == 'Well-Behaved':
        return {'Detentions': 0, 'Suspensions': 0, 'Expulsions': 0}
    elif category == 'Occasionally Troubled':
        detention_range = (0, 4) if class_year in ['Freshman', 'Sophomore'] else (1, 5)
        suspension_chance = 0.05 if class_year in ['Freshman', 'Sophomore'] else 0.1
        return {'Detentions': np.random.randint(*detention_range), 'Suspensions': np.random.choice([0, 1], p=[1-suspension_chance, suspension_chance]), 'Expulsions': 0}
    elif category == 'Frequently Troubled':
        detention_range = (3, 11) if class_year in ['Freshman', 'Sophomore'] else (4, 12)
        suspension_chance = [0.7, 0.25, 0.05] if class_year in ['Freshman', 'Sophomore'] else [0.65, 0.25, 0.1]
        expulsion_chance = 0.05 if class_year in ['Junior', 'Senior'] else 0
        return {'Detentions': np.random.randint(*detention_range), 'Suspensions': np.random.choice([0, 1, 2], p=suspension_chance), 'Expulsions': np.random.choice([0, 1], p=[1-expulsion_chance, expulsion_chance])}

def generate_academic_history():
    class_year = choose_class_year()
    class_lists = generate_class_lists(class_year)
    yearly_grades = generate_yearly_grades(class_lists)
    test_scores = generate_test_scores(class_year)
    infraction_history = generate_infractions(random.choice(['Well-Behaved', 'Occasionally Troubled', 'Frequently Troubled']), class_year)
    return class_year, class_lists, yearly_grades, test_scores, infraction_history

# Generate academic data for each student
academic_records   = []
infraction_records = []
for _ in range(num_records):
    class_year, class_lists, yearly_grades, test_scores, infraction_history = generate_academic_history()
    record = {
        'Class Year': class_year,
        'Class Lists': class_lists,
        'Yearly Grades': yearly_grades,
        'Test Scores': test_scores
    }
    academic_records.append(record)
    infraction_records.append(infraction_history)


# Create a DataFrame from the records
academics = pd.DataFrame(academic_records)
behavior  = pd.DataFrame(infraction_records)

# Combine all data into one DataFrame
synthetic_data = pd.concat([personal_identifiers, demographics, academics, behavior], axis=1)

# Display the first few rows of the synthetic data
print(synthetic_data.head())

# Save the synthetic data to a CSV file
synthetic_data.to_csv('../synthetic_data.csv', index=False)