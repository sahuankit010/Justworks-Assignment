import pandas as pd
from collections import Counter

#Author: Ankit Sahu
#code starts here

#importing the data file 
df = pd.read_csv("data_jw.csv")

#removing the rows which have atleast one of the values as empty|null
df = df.dropna()

#renaming Customer Id as Customer_ID to use it later
df.rename(columns = {'Customer Id':'Customer_ID',}, inplace = True)

#dictionary for customer ids with count
counterCustIDs = Counter(df.Customer_ID)

#list of customer ids
customer_IDs = [i for i in counterCustIDs.keys()]

#creating dictionary
dict1 = dict()

#dictionary with customer IDs as key and creating empty list as its value for now
for i in customer_IDs:
  dict1[i]=[]

#customers IDs with their month of transactions generated here

#monthAndYear is month and year to be added as the list of values in customer ids
monthAndYear=""

#date list is used in the next segment of code, storing currently
date_list={}

#at the end of the loop, dict1 will have a dictionary having customer id as key and list of months for the transaction
for i in customer_IDs:
  for j in df.values:
    #j is list of each row (having customer id(j[0]), date(j[1]), amount (j[2]))
    if(i == j[0]):
      if i in dict1.keys():
        #grabbing the date in date_val variable
        date_val = j[1]
        str1 = list(date_val.split("/"))
        month = int(str1[0])
        year = int(str1[-1])
        #monthAndYear is like "11/22"
        monthAndYear = str(month) + "/" + str(year)
        #logic for date with customer id
        #date_list is storing the month+customer id as key and the date with
        #list of transaction as the values. date will be the key for the list
        # of the transaction on that particular date
        if monthAndYear + "/" + i not in date_list.keys():
          date_list[monthAndYear + "/" + i] = dict()
          date_list[monthAndYear + "/" + i][date_val] = [int(j[2])]
        else:
          l = [o for o in date_list[monthAndYear + "/" + i].keys()]
          if date_val not in l:
            date_list[monthAndYear + "/" + i][date_val] = [int(j[2])]
          else:
            date_list[monthAndYear + "/" + i][date_val].append(int(j[2]))
        #logic for getting all the transaction amount in credit first
        #and then debit(next 2 lines)
        date_list[monthAndYear + "/" + i][date_val].sort()
        date_list[monthAndYear + "/" + i][date_val] = date_list[monthAndYear + "/" + i][date_val][::-1]
        if monthAndYear not in dict1[i]:
          dict1[i].append(monthAndYear)

dict2 = dict()

for key, value in dict1.items():
  c_id = key
  for k in date_list.keys():
    date_cust_id = k
    #l=dictionary of date (month and year)
    str1 = date_cust_id.split("/")
    #extracting the month
    month = str1[0]
    #extracting the year
    year = str1[1]
    monthWithYear = month + "/" + year
    id = str1[2]
    if(c_id == id):
      #correct
      for m in range(len(value)):
        #value[m]=11/2022
        #initiliaze value for minimum, maximum, and ending balance
        sum1 = 0
        mini = float("inf")
        maxi = float("-inf")
        if(value[m] == monthWithYear):
          key_val = dict1[key]
          value[m] = {monthWithYear: date_list[k]}
          for h,p in date_list[k].items():
            #logic for finding minimum, maximum, and ending balance
            for y in p:
              sum1 += y
              mini = min(mini, sum1)
              maxi = max(maxi, sum1)
          #inserting minimum, maximum, and ending balance value as a list in dictionary to use later
          dict2[c_id+ "/" + monthWithYear] = [mini, maxi, sum1]

finalAnswer = dict()
#creating final dictionary finalAnswer with customer ID as the key and value as month
#that will be key for list of value of [minumum, maximum, ending balance]
for i in customer_IDs:
  finalAnswer[i] = dict()
  for key, value in dict2.items():
    str1 = key.split("/")
    date1 = str1[1] + "/" + str1[2]
    if(i == str1[0]):
      dict_val = finalAnswer[i]
      dict_val[date1] = value

#creating list for all the required columns customer id, months, minBalance, maxBalance, endingBalance
#each index in the list corresponds to the one row of customer id, minimum balance, maximum balance, and ending balance
cust_id = []
date = []
minBalance = []
maxBalance = []
endingBalance = []
for key,value in finalAnswer.items():
  #here key is customer id, and value is a list in which minimum balance, maximum balance, and ending balance are stored
  for key1,value1 in value.items():
    #iterating the list, at each index there are 3 values corresponds to minimum balance, maximum balance, and ending balance
    cust_id.append(key)
    date.append(key1)
    minBalance.append(value1[0])
    maxBalance.append(value1[1])
    endingBalance.append(value1[2])

#generating output.csv with required template
df1=pd.DataFrame.from_dict({"CustomerID":cust_id,
                            "MM/YYYY":date,
                            "MinBalance":minBalance,
                            "MaxBalance":maxBalance,
                            "EndingBalance":endingBalance})
df1.to_csv("output.csv")
