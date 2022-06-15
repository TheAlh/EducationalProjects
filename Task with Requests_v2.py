import requests

def search_we(file):    #Iterating over nested file addresses with searching for a file where the first word in the text is We
    link = 'https://stepic.org/media/attachments/course67/3.6.3/'
    with open(file, 'r') as inf:
        rec_value = requests.get(inf.readline().strip()).text
        while 'We' not in rec_value:
            rec_value = requests.get(link + rec_value.strip()).text
        print(rec_value)

search_we('C:/Test Space of Python/test.txt')