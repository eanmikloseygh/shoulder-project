import pandas as pd

df = pd.read_csv(r"C:\Users\leosp\PyCharmMiscProject\cleaned_performance_data.csv")
print(df)
y = df['Shoulder_score']
x = df[['Sleep_hours','Sleep_Quality','Resting_HR','Stress_level','Vol_RPE']]

import statsmodels.api as sm
x = sm.add_constant(x)
reg = sm.OLS(y,x)
reg_fit=reg.fit()
reg_fit.summary()
print(reg_fit.summary())

# resting heartrate seems bad, lets remove it

import pandas as pd

df = pd.read_csv(r"C:\Users\leosp\PyCharmMiscProject\cleaned_performance_data.csv")
print(df)
y = df['Shoulder_score']
x = df[['Sleep_hours','Sleep_Quality','Stress_level','Vol_RPE']]

import statsmodels.api as sm
x = sm.add_constant(x)
reg = sm.OLS(y,x)
reg_fit=reg.fit()
reg_fit.summary()
print(reg_fit.summary())

#repeat until models seems to fit well

import pandas as pd

df = pd.read_csv(r"C:\Users\leosp\PyCharmMiscProject\cleaned_performance_data.csv")
print(df)
y = df['Shoulder_score']
x = df[['Sleep_hours','Stress_level','Vol_RPE']]

import statsmodels.api as sm
x = sm.add_constant(x)
reg = sm.OLS(y,x)
reg_fit=reg.fit()
reg_fit.summary()
print(reg_fit.summary())

# because the R squared value went down, we can conclude that the best fit for this model was the version with the 4 predictor values
