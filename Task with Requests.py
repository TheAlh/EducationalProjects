import requests

num = 0
with open('C:/Test Space of Python/test.txt', 'r') as inf:  #Read file
    for line in inf:
        link = requests.get(line.strip())   #Output a link in variable

with open('C:/Test Space of Python/download.txt', 'wb') as download:    #Download file
    download.write(link.content)

with open('C:/Test Space of Python/download.txt', 'r') as inf:  #Reading a file and counting the number of lines in it
    for _ in inf:
        num += 1
print(num)