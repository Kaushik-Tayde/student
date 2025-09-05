

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# 1. Load Dataset
# --------------------------
# Example dataset: student_marks.csv
# Columns -> Name, Math, Science, English, Attendance, Study_Hours
df = pd.read_csv("student_marks.csv")

print("First 5 records:")
print(df.head())

# --------------------------
# 2. Data Cleaning
# --------------------------
# Check for null values
print("\nMissing Values:\n", df.isnull().sum())

# Fill missing marks with subject mean
df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['English'] = df['English'].fillna(df['English'].mean())

# Fill Attendance / Study Hours with median
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Study_Hours'] = df['Study_Hours'].fillna(df['Study_Hours'].median())

# --------------------------
# 3. Feature Engineering
# --------------------------
# Calculate total and average marks
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total'] / 3

# Assign grade based on average marks
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Average'].apply(assign_grade)

# --------------------------
# 4. Analysis & Insights
# --------------------------
print("\nOverall Statistics:\n", df.describe())

# Average marks in each subject
print("\nAverage Marks by Subject:")
print(df[['Math', 'Science', 'English']].mean())

# Top 5 students
print("\nTop 5 Students:")
print(df[['Name', 'Total', 'Grade']].sort_values(by='Total', ascending=False).head(5))

# --------------------------
# 5. Data Visualization
# --------------------------
plt.figure(figsize=(8,5))
sns.histplot(df['Total'], bins=10, kde=True, color="skyblue")
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df[['Math','Science','English']])
plt.title("Subject-wise Marks Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(df[['Math','Science','English','Attendance','Study_Hours','Total']].corr(), 
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# --------------------------
# 6. Save Results
# --------------------------
df.to_csv("student_marks_analysis_output.csv", index=False)
print("\nAnalysis complete! Results saved to 'student_marks_analysis_output.csv'")

