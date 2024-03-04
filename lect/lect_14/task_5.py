with open('top_secret.txt', 'w', encoding='utf-8') as f:
    for i in range(10):
        f.write(f'{i:05}\n')

with open('top_secret.txt') as f:
    count = 0
    for i in f:
        count += 1
        print(count)
