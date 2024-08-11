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
       
    print("total_cus: ", total_cus)
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

# Function to extract subjects and grades for all index numbers from the CSV
def calculate_gpa_for_all_indices(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    results = []
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        index_number = row['Unnamed: 0']
        subjects = []
        
        for col in df.columns[1:]:
            grade = row[col]
            if pd.notna(grade):  # Only process columns with non-null grades
                subject_code = col
                credits = int(subject_code[-1])
                subjects.append({
                    'name': subject_code,
                    'grade': grade,
                    'credits': credits
                })
        
        # Convert grades to grade points
        for subject in subjects:
            subject['grade_point'] = get_grade_point(subject['grade'])

        # Calculate GPA
        gpa = calculate_gpa(subjects)
        
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
        
        # Store the result
        results.append({
            'Index Number': index_number,
            'GPA': round(gpa, 2),
            'Classification': classification
        })
    
    return results

# Example usage
csv_file_path = 'GEO.csv'

# Calculate GPA for all index numbers
overall_results = calculate_gpa_for_all_indices(csv_file_path)

# Print the results
for result in overall_results:
    print(f"Index Number: {result['Index Number']}, GPA: {result['GPA']}, Classification: {result['Classification']}")
