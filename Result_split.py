import pandas as pd

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
# csv_file_path = 'IBST.csv'
csv_file_path = 'ST ICT.csv'
index_number = 'ICT/19/867'

subjects_for_index = get_subjects_for_index(index_number, csv_file_path)
print(subjects_for_index)

