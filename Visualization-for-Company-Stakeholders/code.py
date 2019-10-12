# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
#Code starts here
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar')


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar')
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']
data.plot(kind='density',label='Graduate')
data.plot(kind='density',label='Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3)
al = data.groupby(['ApplicantIncome','LoanAmount']).size().unstack()
data.plot.scatter(x='ApplicantIncome',y='LoanAmount',ax=ax_1)
plt.title('Applicant Income')
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount',ax=ax_2)
plt.title('Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y='LoanAmount',ax=ax_3)
plt.title('Total Income')


