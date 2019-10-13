# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
categorical_var
numerical_var = bank.select_dtypes(include='number')
numerical_var

# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
print( banks.isnull().sum())
bank_mode = banks.mode
banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')



# code ends here



# --------------
# code starts here
mask1 = banks['Self_Employed']=='Yes'
mask2 = banks['Loan_Status']=='Y'
loan_approved_se = banks[mask1&mask2].count()
mask1 = banks['Self_Employed']=='No'
mask2 = banks['Loan_Status']=='Y'
loan_approved_nse = banks[mask1&mask2].count()
Loan_Status = 614
percentage_se = loan_approved_se*100/Loan_Status
percentage_se=9.120521
percentage_nse = loan_approved_nse*100/Loan_Status
percentage_nse=59.609121
# code ends here


# --------------
# code starts here
loan_term = banks.Loan_Amount_Term.apply(lambda x:(x/12))
big_loan_term = loan_term >= 25
big_loan_term = len(big_loan_term[big_loan_term==True])
big_loan_term


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()


# code ends here


