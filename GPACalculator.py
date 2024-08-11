import pandas as pd

# Function to calculate GPA
def calculate_gpa(subjects):
    total_grade_points = 0
    total_cus = 0

    for subject in subjects:
        grade_point = subject['grade_point']
        credits = subject['credits']
        
        total_grade_points += grade_point * credits
        total_cus += credits
    
    if total_cus == 0:
        return 0  # Avoid division by zero
    
    gpa = total_grade_points / total_cus
    return gpa

# Function to get grade point based on grade
def get_grade_point(grade):
    grade_points = {
        'A+': 4.00,
        'A': 4.00,
        'A-': 3.70,
        'B+': 3.30,
        'B': 3.00,
        'B-': 2.70,
        'C+': 2.30,
        'C': 2.00,
        'C-': 1.70,
        'D+': 1.30,
        'D': 1.00,
        'E': 0.00
    }
    return grade_points.get(grade, 0.00)  # Default to 0.00 if grade is not found

# Function to extract subjects and grades for a given index number from the CSV
def get_subjects_for_index(index_number, file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Find the row corresponding to the given index number
    row = df[df['Unnamed: 0'] == index_number]
    
    # Check if the index number exists in the DataFrame
    if row.empty:
        return f"Index number {index_number} not found."
    
    subjects = []
    
    # Iterate through the columns, skipping the first one (which contains the index numbers)
    for col in df.columns[1:]:
        grade = row[col].values[0]
        if pd.notna(grade):  # Only process columns with non-null grades
            subject_code = col
            credits = int(subject_code[-1])
            subjects.append({
                'name': subject_code,
                'grade': grade,
                'credits': credits
            })
    
    return subjects

# Example usage
csv_file_path = 'ST ICT.csv'
index_number = 'ICT/19/823'

# Get the subjects and grades for the given index number
subjects_for_index = get_subjects_for_index(index_number, csv_file_path)

if isinstance(subjects_for_index, str):
    # If the function returned an error message, print it
    print(subjects_for_index)
else:
    # Convert grades to grade points
    for subject in subjects_for_index:
        subject['grade_point'] = get_grade_point(subject['grade'])

    # Calculate GPA
    gpa = calculate_gpa(subjects_for_index)
    print(f"Your GPA is: {gpa:.2f}")

    # Determine classification based on GPA
    if gpa >= 3.70:
        classification = "1st Class"
    elif 3.30 <= gpa < 3.70:
        classification = "2nd Upper"
    elif 3.00 <= gpa < 3.30:
        classification = "2nd Lower"
    elif 2.00 <= gpa < 3.00:
        classification = "Ordinary Pass"
    else:
        classification = "Fail"

    print(f"Your classification is: {classification}")
