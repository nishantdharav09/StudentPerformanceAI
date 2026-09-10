import pandas as pd
import numpy as np

# Same results every time
np.random.seed(42)

# Number of students
n = 500

# Generate student data
study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
previous_marks = np.random.uniform(40, 95, n)
assignment_score = np.random.uniform(40, 100, n)
internal_marks = np.random.uniform(40, 95, n)
participation = np.random.uniform(1, 10, n)

# Calculate final marks
final_marks = (
    study_hours * 2.5
    + attendance * 0.15
    + previous_marks * 0.25
    + assignment_score * 0.20
    + internal_marks * 0.25
    + participation * 0.5
)

# Add small random variation
final_marks += np.random.normal(0, 3, n)

# Keep final marks between 0 and 100
final_marks = np.clip(final_marks, 0, 100)

# Create DataFrame
data = pd.DataFrame({
    "study_hours": study_hours.round(1),
    "attendance": attendance.round(1),
    "previous_marks": previous_marks.round(1),
    "assignment_score": assignment_score.round(1),
    "internal_marks": internal_marks.round(1),
    "participation": participation.round(1),
    "final_marks": final_marks.round(1)
})

# Save new dataset
data.to_csv(
    "data/student_performance_500.csv",
    index=False
)

print("✅ 500 student dataset created successfully!")

print("\nDataset Shape:")
print(data.shape)

print("\nFirst 5 Records:")
print(data.head())

print("\nDataset saved as:")
print("data/student_performance_500.csv")