import pandas as pd
import pickle

# Load model yang sudah dilatih
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Masukkan data yang ingin diprediksi
X_new = pd.DataFrame({
    'Age': [35], 
    'BusinessTravel': ['Travel_Rarely'], 
    'DailyRate': [1100], 
    'Department': ['Sales'], 
    'DistanceFromHome': [5], 
    'Education': [3], 
    'EducationField': ['Life Sciences'], 
    'EnvironmentSatisfaction': [3], 
    'Gender': ['Male'], 
    'HourlyRate': [70], 
    'JobInvolvement': [3], 
    'JobLevel': [2], 
    'JobRole': ['Sales Executive'], 
    'JobSatisfaction': [4], 
    'MaritalStatus': ['Married'], 
    'MonthlyIncome': [5000], 
    'MonthlyRate': [20000], 
    'NumCompaniesWorked': [1], 
    'OverTime': ['No'], 
    'PercentSalaryHike': [12], 
    'PerformanceRating': [3], 
    'RelationshipSatisfaction': [4], 
    'StockOptionLevel': [1], 
    'TotalWorkingYears': [10], 
    'TrainingTimesLastYear': [3], 
    'WorkLifeBalance': [3], 
    'YearsAtCompany': [5], 
    'YearsInCurrentRole': [2], 
    'YearsSinceLastPromotion': [1], 
    'YearsWithCurrManager': [3], 
    'StabilityInRole': [0.6], 
    'LoyaltyToManager': [0.6], 
    'AvgTrainingPerYear': [1.5], 
    'AgeWhenStarted': [25], 
    'AvgYearsPerCompany': [10], 
    'IncomePerKm': [200], 
    'CompanyLoyalty': [0.7], 
    'PromotionFrequency': [2], 
    'AvgMonthlyIncomePerYear': [2000]
})

# Model akan memprediksi
y_pred = model.predict(X_new)

print("Hasil Prediksi:", y_pred)
