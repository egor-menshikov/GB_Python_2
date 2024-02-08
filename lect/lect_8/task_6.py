import csv
from typing import Iterator

with open('task_4.csv', 'r', newline='') as file, open('task_4_out.csv', 'w', newline='') as file_out:
    data: Iterator = csv.DictReader(file, fieldnames=['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)'],
                                    restkey='new',
                                    restval='other', quoting=csv.QUOTE_NONNUMERIC)
    file_w = csv.DictWriter(file_out, fieldnames=['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)'],
                            quoting=csv.QUOTE_NONNUMERIC)
    for i, entry in enumerate(data):
        if i == 0:
            file_w.writerow(entry)
        else:
            entry['Age'] = int(entry['Age'])
            file_w.writerow(entry)
