# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
#p_a = df[df['fico']>700]
n = len(df)
p_a = len( df[df['fico']>700])/n
#p_b = df[df['purpose']== 'debt_consolidation']
p_b = len(df[df['purpose']== 'debt_consolidation'])/n
df1 = df[df['purpose']== 'debt_consolidation']
p_a_b = p_a+p_b
result = p_a_b==p_a
result


# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/n
prob_cs = len(df[df['credit.policy']=='Yes'])/n
new_df = df[df['paid.back.loan']=='Yes']
prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)
# prob_pd_cs = df[df['paid.back.loan'] == 'Yes'] & df[df['credit.policy']=='Yes']
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here
purpose = df['purpose'].value_counts()
purpose.plot(kind="bar")
df1 = df[df['paid.back.loan']=='No']
purpose1 = df1['purpose'].value_counts()
purpose1.plot(kind='bar')


# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df['installment'].hist()
df['log.annual.inc'].hist()

# code ends here


