
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("dataset/employee_attendance.csv")

# Create output directory
os.makedirs("output", exist_ok=True)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

print("\n========== EMPLOYEE ATTENDANCE ANALYTICS ==========")

# 1. Dataset overview
print("\nDataset Overview:")
print(df.head())
print("\nTotal Records:", len(df))
print("Total Employees:", df["Employee_ID"].nunique())

# 2. Attendance status analysis
print("\nAttendance Status:")
print(df["Attendance_Status"].value_counts())

# 3. Department-wise attendance
department_summary = df.groupby(
    "Department"
)["Attendance_Status"].value_counts().unstack(fill_value=0)

print("\nDepartment-wise Attendance:")
print(department_summary)

department_summary.to_csv(
    "output/department_summary.csv"
)

# 4. Late arrivals
late_count = (df["Attendance_Status"] == "Late").sum()
print("\nTotal Late Arrivals:", late_count)

# 5. Average working hours
print("\nAverage Working Hours:")
print(df["Work_Hours"].mean())

# 6. Monthly attendance
df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_summary = df.groupby(
    "Month"
)["Attendance_Status"].value_counts().unstack(fill_value=0)

print("\nMonthly Attendance:")
print(monthly_summary)

monthly_summary.to_csv(
    "output/monthly_summary.csv"
)

# 7. Attendance status chart
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="Attendance_Status",
    hue="Attendance_Status",
    legend=False
)
plt.title("Employee Attendance Status")
plt.xlabel("Attendance Status")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("output/attendance_status.png")
plt.close()

# 8. Department-wise chart
department_summary.plot(
    kind="bar",
    figsize=(10, 6)
)
plt.title("Department-wise Attendance Analysis")
plt.xlabel("Department")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/department_analysis.png")
plt.close()

print("\nAnalysis completed successfully!")
print("Check the output folder for reports and charts.")
