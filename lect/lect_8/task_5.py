import csv

data = [['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)'], ['Alex', 'M', 41.0, 74.0, 170.0],
        ['Bert', 'M', 42.0, 68.0, 166.0], ['Carl', 'M', 32.0, 70.0, 155.0], ['Dave', 'M', 39.0, 72.0, 167.0],
        ['Elly', 'F', 30.0, 66.0, 124.0], ['Fran', 'F', 33.0, 81.0, 115.0], ['Gwen', 'F', 26.0, 64.0, 121.0]]

with open('task_5.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_STRINGS)
    for item in data:
        csv_writer.writerow(item)
