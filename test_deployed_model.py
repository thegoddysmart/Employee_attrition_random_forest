import requests
import json

# Sample data for prediction
input_data = {
    "Age": 19,
    "BusinessTravel": "Non-Travel",
    "DailyRate": 992,
    "Department": "Research & Development",
    "DistanceFromHome": 1,
    "Education": 1,
    "EducationField": "Medical",
    "EmployeeCount": 1,
    "EnvironmentSatisfaction": 4,
    "Gender": "Male",
    "HourlyRate": 43,
    "JobInvolvement": 3,
    "JobLevel": 1,
    "JobRole": "Laboratory Technician",
    "JobSatisfaction": 3,
    "MaritalStatus": "Single",
    "MonthlyIncome": 2318,
    "MonthlyRate": 17778,
    "NumCompaniesWorked": 1,
    "Over18": "Y",
    "OverTime": "No",
    "PercentSalaryHike": 12,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 4,
    "StandardHours": 80,
    "StockOptionLevel": 0,
    "TotalWorkingYears": 2,
    "TrainingTimesLastYear": 2,
    "WorkLifeBalance": 1,
    "YearsAtCompany": 0,
    "YearsInCurrentRole": 0,
    "YearsSinceLastPromotion": 0,
    "YearsWithCurrManager": 0,
}

# Make a POST request to the Flask app with the sample data
# response = requests.post("https://6233-102-176-75-190.ngrok.io/predict", json=input_data) 
response = requests.post("https://6233-102-176-75-190.ngrok.io/predict", json={'input_data': input_data})

# Print the response
print("Prediction:", response.json())
