import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


df = pd.read_csv("C:\\Users\\ameer\\OneDrive\\Documents\\GitHub\\Mini-Project CIS3311\\patient_health.csv")
#this was done in google colab so it may not work without it pls access
#using the following link:https://colab.research.google.com/drive/1WA_b3WsvtNBQqAq1vx-uuS37l7LvoEX_?usp=sharing


print("Missing values before handling:\n", df.isnull().sum())
duplicate_count = df.duplicated().sum()
print(f"Number of duplicates: {duplicate_count}")
#the missing data here is 6 from Age,Biomarker and Blood pressure.
#there is no whole row duplicated but there is 3 IN iD which we can easily fix later on

#1
#a)i am going to impute age with median because age is more rather a scale than quantity so someone very old would make the info not very correct and inacurate
#b)i am going to impute biomaker with mean because it is not a "scale" it is more quantity type of information which i would rather use mean with
#2
#a) i would keep
#b) 5 outliers won't make that difference in this type of dataset in my opinion because they are less than 4% only making 3.2% of the whole dataset



#cleaning my data like i did in my assignment using the if numerical then replace empty values with mean or median if caterogical use mode


# Impute missing values
for col in ['Age']:
    if col in df.columns:
        # Fix: Assign the result back to the column instead of using inplace=True
        df[col] = df[col].fillna(df[col].median())

for col in ['Biomarker', 'Blood_Pressure']:
    if col in df.columns:
        # Fix: Assign the result back to the column instead of using inplace=True
        df[col] = df[col].fillna(df[col].mean())

#now we remove our duplicate also same proccess as last assignment (although there is no duplicates)
df.drop_duplicates(inplace=True)

#now we change manually the 3 wrong ids
df.loc[150, 'Patient_ID'] = 151
df.loc[151, 'Patient_ID'] = 152
df.loc[152, 'Patient_ID'] = 153





#this is our cleaned Dataframe now in the print down.
print(df.to_string())
#1
#a)i am going to impute age with median because age is more rather a scale than quantity so someone very old would make the info not very correct and inacurate
#b)i am going to impute biomaker with mean because it is not a "scale" it is more quantity type of information which i would rather use mean with
#2
#a) i would keep
#b) 5 outliers won't make that difference in this type of dataset in my opinion because they are less than 4% only making 3.2% of the whole dataset



#cleaning my data like i did in my assignment using the if numerical then replace empty values with mean or median if caterogical use mode


# Impute missing values
for col in ['Age']:
    if col in df.columns:
        # Fix: Assign the result back to the column instead of using inplace=True
        df[col] = df[col].fillna(df[col].median())

for col in ['Biomarker', 'Blood_Pressure']:
    if col in df.columns:
        # Fix: Assign the result back to the column instead of using inplace=True
        df[col] = df[col].fillna(df[col].mean())

#now we remove our duplicate also same proccess as last assignment (although there is no duplicates)
df.drop_duplicates(inplace=True)

#now we change manually the 3 wrong ids
df.loc[150, 'Patient_ID'] = 151
df.loc[151, 'Patient_ID'] = 152
df.loc[152, 'Patient_ID'] = 153





#this is our cleaned Dataframe now in the print down.
print(df.to_string())

plt.boxplot(df.Biomarker)
plt.title("Biomarker")
plt.show()

#and it clearly shows 5 outliers which is not that bad for a sample of 150 which we have,(outliers are the circles away from main box)

#i put task 2 under 3 so plotbox works



X = df[['Biomarker']]
y = df['Blood_Pressure']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print("Intercept (b0):", model.intercept_)
print("Slope (b1):", model.coef_[0])

print("Mean Absolute Error (MAE):", mean_absolute_error(y, y_pred))
print("Mean Squared Error (MSE):", mean_squared_error(y, y_pred))
