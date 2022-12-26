import pandas as pd
from collections import Counter

#code starts here

#importing the data file 
df = pd.read_csv("data.csv")
#removing the rows which have atleast one of the values as empty|null
df = df.dropna()
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
date_list={}
for i in customer_IDs:
  for j in df.values:
    if(i==j[0]):
      if i in dict1.keys():
        date_val=j[1]
        str1=list(date_val.split("/"))
        month=int(str1[0])
        year=int(str1[-1])
        monthAndYear=str(month)+"/"+str(year)
        if monthAndYear+"/"+i not in date_list.keys():
          date_list[monthAndYear+"/"+i]={}
          date_list[monthAndYear+"/"+i][date_val]=[int(j[2])]
        else:
          l=[o for o in date_list[monthAndYear+"/"+i].keys()]
          if date_val not in l:
            date_list[monthAndYear+"/"+i][date_val]=[int(j[2])]
          else:
            date_list[monthAndYear+"/"+i][date_val].append(int(j[2]))
        date_list[monthAndYear+"/"+i][date_val].sort()
        date_list[monthAndYear+"/"+i][date_val]=date_list[monthAndYear+"/"+i][date_val][::-1]
        if monthAndYear not in dict1[i]:
          dict1[i].append(monthAndYear)

dict2 = dict()

for key,value in dict1.items():
  c_id=key
  for k in date_list.keys():
    date_cust_id=k
    #l=dict_of_date
    str1=date_cust_id.split("/")
    month=str1[0]
    year=str1[1]
    monthWithYear=month+"/"+year
    id=str1[2]
    if(c_id==id):
      #correct
      for m in range(len(value)):
        #value[m]=11/2022
        #initiliaze value for minimum, maximum, and ending balance
        sum1=0
        mini=float("inf")
        maxi=float("-inf")
        if(value[m]==monthWithYear):
          key_val=dict1[key]
          value[m]={monthWithYear:date_list[k]}
          for h,p in date_list[k].items():
            #logic for finding minimum, maximum, and ending balance
            for y in p:
              sum1+=y
              mini=min(mini,sum1)
              maxi=max(maxi,sum1)
          #inserting minimum, maximum, and ending value as a list in dictionary to use later
          dict2[c_id+"/"+monthWithYear]=[mini,maxi,sum1]

dict3 = dict()
for i in customer_IDs:
  dict3[i]={}
  for key,value in dict2.items():
    str1=key.split("/")
    date1=str1[1]+"/"+str1[2]
    if(i==str1[0]):
      dict_val=dict3[i]
      dict_val[date1]=value


#creating list for all the required columns customer id, minBalance, maxBalance, endingBalance
cust_id=[]
date=[]
minBalance=[]
maxBalance=[]
endingBalance=[]
for key,value in dict3.items():
  for l,m in value.items():
    cust_id.append(key)
    date.append(l)
    minBalance.append(m[0])
    maxBalance.append(m[1])
    endingBalance.append(m[2])


#generating output.csv with required template

df1=pd.DataFrame.from_dict({"CustomerID":cust_id,
                            "MM/YYYY":date,
                            "MinBalance":minBalance,
                            "MaxBalance":maxBalance,
                            "EndingBalance":endingBalance})
df1.to_csv("output1.csv")
