import pickle

data = [['Name', 'Sex', 'Age', 'Height (in)', 'Weight (lbs)'], ['Alex', 'M', 41.0, 74.0, 170.0],
        ['Bert', 'M', 42.0, 68.0, 166.0], ['Carl', 'M', 32.0, 70.0, 155.0], ['Dave', 'M', 39.0, 72.0, 167.0],
        ['Elly', 'F', 30.0, 66.0, 124.0], ['Fran', 'F', 33.0, 81.0, 115.0], ['Gwen', 'F', 26.0, 64.0, 121.0]]

res = pickle.dumps(data)
print(res)

with open('task_8.pick', 'wb') as file:
    pickle.dump(data, file)

print(type(res))
