# Function to calculate GPA
def calculate_gpa(subjects):
    total_grade_points = 0
    total_cus = 0

    for subject in subjects:
        grade_point = subject['grade_point']
        credits = subject['credits']
        
        total_grade_points += grade_point * credits
        print(f"Subject: {subject['name']}, Grade: {subject['grade']}, Credits: {credits}, Grade Point: {grade_point}")
        total_cus += credits
    
    if total_cus == 0:
        return 0  # Avoid division by zero
    
    gpa = total_grade_points / total_cus
    print(f"Total credits Points: {total_cus}")
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

# Input list of subjects with grades and credits
subjects =[{'name': 'ITC 1013', 'grade': 'A-', 'credits': 3}, {'name': 'ITC 1023', 'grade': 'A', 'credits': 3}, {'name': 'ITC 1032', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 1042', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 1052', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 1062', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 1071', 'grade': 'A-', 'credits': 1}, {'name': 'ITC 1082', 'grade': 'B', 'credits': 2}, {'name': 'ITC 1102', 'grade': 'B', 'credits': 2}, {'name': 'ITC 1112', 'grade': 'A+', 'credits': 2}, {'name': 'ITC 1132', 'grade': 'B', 'credits': 2}, {'name': 'ITC 1141', 'grade': 'A-', 'credits': 1}, {'name': 'ITC 1153', 'grade': 'A-', 'credits': 3}, {'name': 'ITC 1163', 'grade': 'A-', 'credits': 3}, {'name': 'ITC 1172', 'grade': 'B', 'credits': 2}, {'name': 'ITC 2192', 'grade': 'D+', 'credits': 2}, {'name': 'ITC 2202', 'grade': 'A-', 'credits': 2}, {'name': 'ITC 2212', 'grade': 'A-', 'credits': 2}, {'name': 'ITC 2223', 'grade': 'B-', 'credits': 3}, {'name': 'ITC 2242', 'grade': 'C', 'credits': 2}, {'name': 'ITC 2243', 'grade': 'C+', 'credits': 3}, {'name': 'ITC 2252', 'grade': 'A-', 'credits': 2}, {'name': 'ITC 2272', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 2282', 'grade': 'B', 'credits': 2}, {'name': 'ITC 2292', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 2302', 'grade': 'A-', 'credits': 2}, {'name': 'ITC 2303', 'grade': 'B', 'credits': 3}, {'name': 'ITC 2342', 'grade': 'C+', 'credits': 2}, {'name': 'ITC 2353', 'grade': 'B+', 'credits': 3}, {'name': 'ITC 3013', 'grade': 'A+', 'credits': 3}, {'name': 'ITC 3023', 'grade': 'B-', 'credits': 3}, {'name': 'ITC 3032', 'grade': 'A-', 'credits': 2}, {'name': 'ITC 3052', 'grade': 'B', 'credits': 2}, {'name': 'ITC 3071', 'grade': 'A+', 'credits': 1}, {'name': 'ITC 3081', 'grade': 'B', 'credits': 1}, {'name': 'ITC 3082', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 3093', 'grade': 'B-', 'credits': 3}, {'name': 'ITC 3113', 'grade': 'A+', 'credits': 3}, {'name': 'ITC 3122', 'grade': 'B+', 'credits': 2}, {'name': 'ITC 4156', 'grade': 'A', 'credits': 6}, {'name': 'ITC 4166', 'grade': 'B+', 'credits': 6}, {'name': 'ITC 4172', 'grade': 'A+', 'credits': 2}, {'name': 'ITC 4182', 'grade': 'A-', 'credits': 2}, {'name': 'ITC 4212', 'grade': 'B+', 'credits': 2}, {'name': 'ITS 3043', 'grade': 'A-', 'credits': 3}, {'name': 'ITS 3052', 'grade': 'A-', 'credits': 2}, {'name': 'ITS 3102', 'grade': 'B', 'credits': 2}, {'name': 'ITS 3142', 'grade': 'B', 'credits': 2}, {'name': 'ITS 3173', 'grade': 'B', 'credits': 3}, {'name': 'ITS 4202', 'grade': 'A-', 'credits': 2}, {'name': 'ITS 4243', 'grade': 'B-', 'credits': 3}]

# Convert grades to grade points
for subject in subjects:
    subject['grade_point'] = get_grade_point(subject['grade'])

# Calculate GPA
gpa = calculate_gpa(subjects)
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
