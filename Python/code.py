# --------------
# Importing header files
import numpy as np
import warnings
import statistics 
warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

census=np.concatenate((data,new_record), axis=0)
#print("CENSUS:",census)

print("DATA:",data.shape)
print("CENSUS:",census.shape)
print("#########################################################")

#STEP 2
age=census[:,0]
print("AGE:",age)
print("AGE_Length:",len(age))

max_age=np.max(age)
print("MAX_AGE:",max_age)

min_age=np.min(age)
print("MIN_AGE:",min_age)

age_mean=np.mean(age)
print("AGE_mean:",age_mean)

age_std=np.std(age)
print("STD_AGE:",age_std)

print("#########################################################")

#STEP 3

race=census[:,2]
#print("RACE:",race)
print("Race_Length:",len(race))

race_0=list(filter(lambda x:(x == 0),race))  
#print("RACE_0:",race_0) 
len_0=len(race_0)
print("Race_0_Length:",len_0)

race_1=list(filter(lambda x:(x == 1),race))  
#print("RACE_1:",race_1) 
len_1=len(race_1)
print("Race_1_Length:",len_1)

race_2=list(filter(lambda x:(x == 2),race))  
#print("RACE_2:",race_2) 
len_2=len(race_2)
print("Race_2_Length:",len_2)

race_3=list(filter(lambda x:(x == 3),race))  
#print("RACE_3:",race_3) 
len_3=len(race_3)
print("Race_3_Length:",len_3)

race_4=list(filter(lambda x:(x == 4),race))  
#print("RACE_4:",race_4) 
len_4=len(race_4)
print("Race_4_Length:",len_4)

race_length=[len_0,len_1,len_2,len_3,len_4]

minority_race=race_length.index(min(race_length))

print("\nMinority_race:",minority_race)

print("#########################################################")

#STEP 4
senior_citizens=list(filter(lambda x:(x>60),census[:,0]))
#print("Senior_citizen:",senior_citizens)
print("senior_citizens_len:",len(senior_citizens))


age_working_hours=census[np.ix_(census[:,0] > 60, (0,6))]
print("working_hours:",len(age_working_hours))

working_hours=age_working_hours[:,1]
print("working_hours_sum:",sum(working_hours))

avg_working_hours=sum(working_hours)/len(senior_citizens)
print("avg_working_hours:",avg_working_hours)

print("#########################################################")
#STEP 5
high=list(filter(lambda x:(x > 10),census[:,1]))
low=list(filter(lambda x:(x <= 10),census[:,1]))

print("High:",len(high))
print("LOW:",len(low))

income_high=census[np.ix_(census[:,1] > 10, (0,7))]
#print("income_high:",income_high)
pay_high=income_high[:,1]
avg_pay_high=sum(pay_high)/len(pay_high)
print("avg_pay_high:",avg_pay_high)

income_low=census[np.ix_(census[:,1] <= 10, (0,7))]
#print("income_high:",income_low)
pay_low=income_low[:,1]
avg_pay_low=sum(pay_low)/len(pay_low)
print("avg_pay_low:",avg_pay_low)


