import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("../data/student_performance_cleaned.csv")

# Display basic information
print("Dataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Graph 1: Study Hours vs Final Marks
plt.figure()
plt.scatter(data["study_hours"], data["final_marks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.show()

# Graph 2: Attendance vs Final Marks
plt.figure()
plt.scatter(data["attendance"], data["final_marks"])
plt.xlabel("Attendance")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.show()

# Graph 3: Previous Marks vs Final Marks
plt.figure()
plt.scatter(data["previous_marks"], data["final_marks"])
plt.xlabel("Previous Marks")
plt.ylabel("Final Marks")
plt.title("Previous Marks vs Final Marks")
plt.show()