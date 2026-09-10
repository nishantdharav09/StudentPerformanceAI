import pandas as pd

# Load dataset
data = pd.read_csv("../data/student_performance.csv")

# Remove duplicate rows
data = data.drop_duplicates()

# Remove rows with missing values
data = data.dropna()

# Display cleaned dataset
print("Cleaned Dataset:")
print(data)

# Check missing values again
print("\nMissing Values:")
print(data.isnull().sum())

# Check duplicates again
print("\nDuplicate Rows:")
print(data.duplicated().sum())

# Save cleaned dataset
data.to_csv("../data/student_performance_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")