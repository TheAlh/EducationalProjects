# MyFirstProjects

Here will be my work done during the training and maybe something else

[File InOut.py]
Write a program that reads from a file a line corresponding to the text compressed using repetition coding and performs the reverse operation, obtaining the original text.
Write the received text to a file and attach it as an answer to this task.

[File InOut_v2.py]
Write a program that reads text from a file (there may be more than one line in the file) and outputs the most frequent word in this text and, separated by a space, how many times it occurred. If there are several such words, output the first one lexicographically (you can use the < operator for strings).

[File InOut_v3.py]
There is a file with data on the progress of applicants. It is a set of lines, where each line contains the following information:
Last name; Grade_in_math; Grade_in_physics; Grade_in_language

Fields within a row are separated by semicolons, scores are integers.
Write a program which reads a source file with a similar structure and for each applicant writes his average mark in three subjects on a separate line corresponding to this applicant to the file with the answer.
Also calculate the average scores in math, physics and language for all applicants and add the resulting values, separated by a space,
the last line in the file with the answer.

[Task with Requests.py]
You need to download the file. It specifies the address of another file that needs to be downloaded using the requests module and count the number of lines in it.
Use the get function to get the file (it makes sense to call the strip method on the passed parameter to strip whitespace around the edges).
After receiving the file, you can check the result by accessing the text field. If the result of the script is not accepted, check the url field for correctness. To count the number of lines, split the text using the splitlines method.
Enter a single number in the response field, or send a file containing a single number.

[Task with Requests_v2.py]
There is a set of files, each of which, except for the last one, contains the name of the next file.
The first word in the text of the last file: "We".
The first file contains a link - https://stepic.org/media/attachments/course67/3.6.3/699991.txt.
This is a link to the second file from this set.
All files are located in the directory at:
https://stepic.org/media/attachments/course67/3.6.3/
The content of the last file from the set is the answer to this task.
