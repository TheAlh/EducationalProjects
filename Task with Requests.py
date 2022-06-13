import requests

with open('C:/Test Space of Python/test.txt', 'r') as inf:
    print(len(requests.get(inf.readline().strip()).text.splitlines()))