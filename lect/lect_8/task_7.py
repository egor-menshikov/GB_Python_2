import csv

data_l = [{'Name': 'Alex', 'Sex': 'M', 'Age': 41.0, 'Height (in)': 74.0, 'Weight (lbs)': 170.0},
          {'Name': 'Bert', 'Sex': 'M', 'Age': 42.0, 'Height (in)': 68.0, 'Weight (lbs)': 166.0},
          {'Name': 'Carl', 'Sex': 'M', 'Age': 32.0, 'Height (in)': 70.0, 'Weight (lbs)': 155.0},
          {'Name': 'Dave', 'Sex': 'M', 'Age': 39.0, 'Height (in)': 72.0, 'Weight (lbs)': 167.0},
          {'Name': 'Elly', 'Sex': 'F', 'Age': 30.0, 'Height (in)': 66.0, 'Weight (lbs)': 124.0}]

with open('task_7.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=list(data_l[0].keys()))
    writer.writeheader()
    writer.writerows(data_l)
