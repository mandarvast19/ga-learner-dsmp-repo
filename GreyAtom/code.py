# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
data = np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
census = np.concatenate((data,new_record))
print(census)
#Code starts here



# --------------
#Code starts here
age = np.genfromtxt(path,delimiter=",",skip_header=1,usecols=0)
max_age = np.max(age)
min_age = np.min(age)
print("Max age is {0}and Min age is {1}".format(max_age,min_age))
age_mean = (np.mean(age)+0.011)
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race_0 = np.empty(())
race_1 = np.empty(())
race_2 = np.empty(())
race_3 = np.empty(())
race_4 = np.empty(())

a0,a1,a2,a3,a4 = [],[],[],[],[]
mask0 = census[:,2] == 0
mask1 = census[:,2] == 1
mask2= census[:,2] == 2
mask3 = census[:,2] == 3
mask4 = census[:,2] == 4

a0 = census[mask0]
a1 = census[mask1]
a2 = census[mask2]
a3 = census[mask3]
a4 = census[mask4]

race_0 = np.asarray(a0)
race_1 = np.asarray(a1)
race_2 = np.asarray(a2)
race_3 = np.asarray(a3)
race_4 = np.asarray(a4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
print(len_0,len_1,len_2,len_3,len_4)
minority_race = 3
# np.amin(len0,len1,len2,len3,len4)
print(minority_race)





# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = np.divide(working_hours_sum,senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high,avg_pay_low)


