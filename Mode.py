import csv
from collections import Counter

with open("height-weight.csv", newline="") as f:
    read = csv.reader(f)
    file_data = list(read)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

data=Counter(new_data)
modeDataForRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height, occurrence in data.items():
    if 50<float(height)<60:
        modeDataForRange["50-60"]+=occurrence
    elif 60<float(height)<70:
        modeDataForRange["60-70"]+=occurrence
    elif 70<float(height)<80:
        modeDataForRange["70-80"]+=occurrence

modeRange,modeOccurrence = 0,0

for range,occurrence in  modeDataForRange.items():
    if occurrence>modeOccurrence:
        modeRange,modeOccurrence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence

mode = float((modeRange[0]+modeRange[1])/2)
print(f"mode -> {mode:2f}")


