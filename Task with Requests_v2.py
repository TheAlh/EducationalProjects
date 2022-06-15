import requests

def search_we(file):
    link = 'https://stepic.org/media/attachments/course67/3.6.3/'   #Website directory where the files are located
    with open(file, 'r') as inf:  #Reading a file with a link to the next file
        rec_value = ((requests.get(inf.readline().strip()).text.splitlines()))
        while 'We' not in rec_value[0]:   #Until the first line contains "We", the loop will work to get data from each file
            url = link + rec_value[0]   #We get a url from the path to the directory and the name of the next file
            rec_value = (requests.get(url.strip()).text.splitlines())   #Getting the contents of a file
        print(' '.join(rec_value), end='')  #Output the found string

search_we('C:/Test Space of Python/test.txt')