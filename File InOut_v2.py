max_str = {}
with open('C:/Test Space of Python/test.txt', 'r') as inf: #Reading the file
    for line in inf:
        text = list(line.strip().split(' ')) #Enter a string into the text variable
        for i in range(len(text)):
            if str.lower(text[i]) in max_str:
                max_str[str.lower(text[i])] += 1 #If the given string value is already in the dictionary key, then increase the value in the dictionary by one
            else:
                max_str[str.lower(text[i])] = 1 #Else create a key with value equal to one

with open('C:/Test Space of Python/out.txt', 'w') as ouf:
    values, key = 0, ' '
    for k, v in max_str.items(): #Passing the value and key from the dictionary
        if values < v: #In this block, we define the largest value and its key
            values = v
            key = k
    ouf.write(f'{key} {values}\n') #Output string to file
    values, key = 0, ' ' #Reset variables for comparison
