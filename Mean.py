import csv

with open("height-weight.csv",newline="") as f:
    read = csv.reader(f)
    file_data= list(read)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
total = 0
for x in new_data:
    total += x

mean = total/n
print("The mean of the given data is: " + str(mean))