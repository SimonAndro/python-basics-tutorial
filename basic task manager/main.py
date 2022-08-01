

## Task one overview
filename = "tasks.txt"
'''
file = open(file=filename,mode='a')
file.write("this is my first file->1\n")
file.write("this is my first file->2\n")
file.write("this is my first file->3\n")
file.close()

file = open(file=filename, mode='r')
for i in range(1,4):
    str = file.readline()
    print(str)
file.close()
'''

## Task two overview
'''
##getting input from the console

print("enter something: ",end="")

str = str(input())

print(str)
'''


##task 1, write 5 names on different lines of a
## file. read back the names and output them to
## to the console

##task 2, get 5 names  from the console and save
## them in a file

##task 3, get names from the console and store
## them to a file as a json object

