import sys
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

phone_book = {}

for i in range(1, n + 1):
    entry = data[i]
    name, number = entry.split()  
    phone_book[name] = number     

for i in range(n + 1, len(data)):
    query = data[i]
    if query in phone_book:
        print(f"{query}={phone_book[query]}")  
    else:
        print("Not found")  
