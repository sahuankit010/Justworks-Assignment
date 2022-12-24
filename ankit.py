# importing the module
import csv
import datetime

# open the file in read mode
filename = open('data_jw.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
customerIds = []
dates = []
amounts = []
print(file)
# iterating over each row and append
# values to empty list
for col in file:
    key_arr = list(col.keys())
    key_arr = [item for item in key_arr if len(item)>0]
    # print(key_arr)
    if col[key_arr[0]]:
        customerIds.append(col[key_arr[0]])
        dates.append(col[key_arr[1]])
        amounts.append(col[key_arr[2]])

# printing lists
print(type(customerIds[0]))
print(type(dates[0]))
print(type(amounts[0]))
format = '%m/%d/%y'

for i in range(len(dates)):
    dates[i] = datetime.datetime.strptime(dates[i], format)
    dates[i] = dates[i].date()

# toRemove = datetime.datetime(9999, 9, 9, 0, 0)
# for date in dates:
#     if (date == toRemove):
#         date.remove(date)

# goodDates = [d for d in dates if d != datetime.datetime(9999, 9, 9, 0, 0)]
print(dates)
for i in range(len(customerIds)):
    amounts[i] = int(amounts[i])
    print(customerIds[i],end = " ")
    print(dates[i], end=" ")
    print(amounts[i])

print(type(customerIds[0]))
print(type(dates[0]))
print(type(amounts[0]))

print(len(customerIds))
print(len(dates))
print(len(amounts))

my_dict = dict()
final = {}

# l=[1,2,3,4,5]
# for i in range(len(customerIds)):
#     if customerIds[i] in my_dict:
#         my_dict[dates[i]].append(amounts[i])
#     else:
#         my_dict[dates[i]]= [amounts[i]]

for i in range(len(customerIds)):
    if customerIds[i] in my_dict:
        if dates[i] in my_dict.has_keys(customerIds[i]):
            if amounts[i] in my_dict[customerIds][dates[i]]:
                my_dict[customerIds][dates[i]].append(amounts[i])
            else:
                my_dict[customerIds][dates[i]] = [amounts[i]]
        else:
            my_dict[customerIds[i]] = [dates[i]]
    else:
        my_dict = [customerIds[i]]                
print(my_dict)    

