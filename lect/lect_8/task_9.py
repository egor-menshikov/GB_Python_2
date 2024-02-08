import pickle
from task_8 import res

with open('task_8.pick', 'rb') as file:
    data = pickle.load(file)

results = pickle.loads(res)
print(data)
print(results)