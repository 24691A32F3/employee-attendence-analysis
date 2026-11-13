Employee Attendance Analysis

Project Overview

Employee Attendance Analysis is a Big Data Analytics (BDA) project developed using Python.

The project analyzes employee attendance records to identify attendance patterns, late arrivals, absences, leaves, and department-wise attendance statistics.

Objectives

- Analyze employee attendance records.
- Calculate Present, Absent, Late and Leave counts.
- Perform department-wise attendance analysis.
- Generate monthly attendance summaries.
- Visualize attendance statistics using graphs.

Technologies Used

- Python
- Pandas
- Data Analytics
- Matplotlib
- Visual Studio Code
- Ubuntu / WSL

Project Structure

employee-attendance-analytics/
│
├── dataset/
│   └── employee_attendance.csv
│
├── notebooks/
│
├── output/
│   ├── attendance_status.png
│   ├── department_analysis.png
│   ├── department_summary.csv
│   └── monthly_summary.csv
│
├── src/
│   └── analysis.py
│
├── README.md
├── requirements.txt
└── .gitignore

Dataset Information

- Total Records: 880
- Total Employees: 40
- Month: October 2026

Attendance Analysis Results

Attendance Status| Count
Present| 635
Late| 135
Absent| 77
Leave| 33
Total| 880

Project Outputs

1. Attendance Status Graph
2. Department-wise Attendance Graph
3. Department Summary CSV
4. Monthly Summary CSV

How to Run the Project

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Run the Python program

python src/analysis.py

Step 3: View Results

Check the generated graphs and CSV reports inside the output folder.

Conclusion

This project helps analyze employee attendance patterns and provides useful insights into employee attendance, punctuality, and department-wise attendance performance.