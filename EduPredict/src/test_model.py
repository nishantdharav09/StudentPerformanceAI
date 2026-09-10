import joblib
import pandas as pd

# Load trained model
model = joblib.load("student_performance_model.pkl")

# Test student
student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [90],
    "previous_marks": [75],
    "assignment_score": [85],
    "internal_marks": [80],
    "participation": [8]
})

# Predict final marks
prediction = model.predict(student)

print("======================================")
print("       EduPredict Model Testing")
print("======================================")

print("\nStudent Details:")
print(student)

print("\n🎯 Predicted Final Marks:")
print(round(prediction[0], 2))