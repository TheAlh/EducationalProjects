def avg_student(x): #We derive the average value for each student
    avg_sum = 0
    for i in x:
        avg_sum += int(i)
    return (avg_sum / len(x))

def avg_subject(x): #We derive the average value for each subject
    avg_sum = 0
    for i in avg_score:
        avg_sum += int(i[x])
    return avg_sum / len(avg_score)

avg_score = []
with open('C:/Test Space of Python/test.txt', 'r', encoding='utf-8') as inf: #Reading a document
    for line in inf:
        text = list(line.strip().split(';')) #Enter a string into the text variable
        avg_score_student = [] #We form a list with student grades
        for i in range(len(text)-1):
            if i != range(len(text)-1):
                avg_score_student.append(text[i+1])
        avg_score.append(avg_score_student) #We form a list with the grades of all students

with open('C:/Test Space of Python/out.txt', 'w') as ouf:
    for x in avg_score:
        ouf.write(f'{avg_student(x)}\n')
    for x in range(len(avg_score_student)):
        ouf.write(f'{avg_subject(x)} ')

