
# Program: project_4.py
# Author: Sample Program
# Date: November 2026
# Description: Read survey data from a CSV file,
#              calculate statistics, and create three charts.

import csv
import matplotlib.pyplot as plt

# ==================================================
# 1. READ CSV FILE INTO PARALLEL LISTS
# ==================================================

# Create parallel lists to store data from the CSV columns.
years = []
sports = []
study_hours = []

# Read all rows from the CSV file.
with open("project_4_sample_data.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    data = list(reader)

# Copy the CSV columns into parallel lists.
# Start at row 1 to skip the column headings.
i = 1

while i < len(data):
    years.append(data[i][0])
    sports.append(data[i][1])
    study_hours.append(float(data[i][2]))
    
    i = i + 1

total_responses = len(years)

print("SURVEY RESULTS")
print(f"Total Responses: {total_responses}")

# ==================================================
# 2. SUMMARIZE DATA FOR CHART 1
#    Sports Participation
# ==================================================

yes_count = 0
no_count = 0

# Count Yes and No responses.
i = 0
while i < len(sports):
    if sports[i] == "Yes":
        yes_count = yes_count + 1
    else:
        if sports[i] == "No":
            no_count = no_count + 1
        else:
            print(f"Error: invalid data {sports[i]}")
        
    i = i + 1

print("\nSports Participation")
print(f"Yes: {yes_count}")
print(f"No: {no_count}")

# Store the results in lists for the chart.
sports_labels = ["Yes", "No"]
sports_counts = [yes_count, no_count]


# ==================================================
# 3. SUMMARIZE DATA FOR CHART 2
#    Student Classification
# ==================================================

year_labels = ["Freshman", "Sophomore", "Junior", "Senior"]
year_counts = []

# Count students in each class year.
j = 0

while j < len(year_labels):
    count = 0
    
    # Check each survey response against the current class year.
    i = 0
    while i < len(years):
        # if the data ie. years[i] equals label ie. year_labels[j]
        if years[i] == year_labels[j]:
            count = count + 1
            
        i = i + 1

    year_counts.append(count)
    j = j + 1

# Display the results.
print("\nStudent Classification")

i = 0
while i < len(year_labels):
    print(f"{year_labels[i]}: {year_counts[i]}")
    i = i + 1


# ==================================================
# 4. SUMMARIZE DATA FOR CHART 3
#    Average Weekly Study Hours
# ==================================================

year_averages = []

# Calculate the average study hours for each class.
j = 0

while j < len(year_labels):
    total = 0
    count = 0
    
    i = 0
    while i < len(years):
        
        if years[i] == year_labels[j]:
            total = total + study_hours[i]
            count = count + 1
        
        i = i + 1

    # Avoid dividing by zero if no students
    # belong to this class year.
    if count > 0:
        average = total / count
    else:
        average = 0

    year_averages.append(average)
    j = j + 1

# Display averages for each class year.
print("\nAverage Weekly Study Hours")

i = 0
while i < len(year_labels):
    print(f"{year_labels[i]}: {year_averages[i]:.1f}")
    i = i + 1

# Calculate overall study hour statistics.
total_hours = 0
i = 0

while i < len(study_hours):
    total_hours = total_hours + study_hours[i]
    i = i + 1

overall_average = total_hours / total_responses

print(f"\nOverall Average: {overall_average:.1f}")
print(f"Minimum: {min(study_hours):.1f}")
print(f"Maximum: {max(study_hours):.1f}")


# ==================================================
# 5. DISPLAY CHART 1 - PIE CHART
# ==================================================

plt.figure(num="Chart 1 - Sports Participation")
plt.pie(sports_counts, labels=sports_labels,
        autopct="%1.1f%%", colors=["limegreen", "tomato"],
        textprops={"fontweight": "bold", "fontsize": 12},
        startangle=45,
        wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title("Sports Participation", fontsize=24,
          fontweight="bold",
          color="darkgreen")

# ==================================================
# 6. DISPLAY CHART 2 - COLUMN CHART
# ==================================================

plt.figure(num="Chart 2 - Number of Students")
plt.bar(year_labels, year_counts,
        color=["blue", "green", "orange", "red"],
        edgecolor="black",
        linewidth=1)
plt.title("Student Classification")
plt.xlabel("Class Year")
plt.ylabel("Number of Students")
plt.ylim(0, max(year_counts) + 2)

# ==================================================
# 7. DISPLAY CHART 3 - LINE CHART
# ==================================================

plt.figure(num="Chart 3 - Average Hours Per Week")
plt.plot(year_labels, year_averages, marker="o", color="orange",
         linewidth=3,
         markersize=10,
         linestyle="--")
plt.title("Average Weekly Study Hours by Class Year")
plt.xlabel("Class Year")
plt.ylabel("Average Hours Per Week")
plt.grid(True)
                
                

# ==================================================
# DISPLAY ALL THREE CHARTS
# ==================================================

plt.show()
