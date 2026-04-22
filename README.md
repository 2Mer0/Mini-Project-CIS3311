<<<<<<< HEAD
This project is a data cleaning, visualization, and regression analysis mini‑project created for CIS 3311.
It analyzes a patient health dataset by handling missing values, fixing data inconsistencies, visualizing outliers, and applying Linear Regression to study the relationship between biomarkers and blood pressure.


📂 Dataset

File Name: patient_health.csv
Source: Provided for coursework
Size: ~150 patient records
Key Features:

Patient_ID
Age
Biomarker
Blood_Pressure

🧹 Data Cleaning & Preprocessing
The following steps were applied:

Checked for missing values and duplicate records
Missing value imputation

Age → replaced using median
Biomarker, Blood_Pressure → replaced using mean


Removed duplicate rows
Manually corrected 3 incorrect Patient_ID values
Outliers were identified but retained, as they represented less than 4% of the dataset


📊 Data Visualization

Generated a box plot for the Biomarker column
Identified 5 outliers, which were kept to preserve data integrity


📈 Linear Regression Model
A Simple Linear Regression model was built using:

Feature (X): Biomarker
Target (y): Blood Pressure

Model Outputs:

Intercept (b₀)
Slope (b₁)
Evaluation Metrics:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)




🛠️ Libraries Used

pandas
numpy
matplotlib
seaborn
scikit-learn


▶️ How to Run

Clone this repository
Ensure required libraries are installed
Update the CSV file path if running locally
Run the Python script or open the Colab notebook


🎓 Course Information

Course: CIS 3311
Project Type: Mini Project
Purpose: Data cleaning, visualization, and regression practice


✅ Notes

Code includes detailed comments explaining each step
Designed for educational use and coursework submission
=======
#CIS 3311 Intro into Datascience mini project
i cleaned health data and represented them in a helpful matter.
>>>>>>> e6bcfb8c71d483544b2f40f335f1f0d01f8b0d1f
