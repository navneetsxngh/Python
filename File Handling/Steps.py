#----> To read a file using loops
# file  = open('navneet.txt', 'r')
# for i in file:
#     print(i)



#----> To read a File using inbuilt function.
# file = open("hell.txt", "r")
# print(file.readlines())


##----> Using the "With" Statement
# with open("hell.txt") as file:
#     data = file.read()
# print(data)


##----> Splitting the file
# with open("hell.txt", 'r') as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)




##-------------------------------------------------------------
# (read)----> Python Script -----> OS ----> Buffer Memory(RAM)  <---> Disk
##-------------------------------------------------------------



## To write a file
# file = open("super.txt", "w")
# file.write("This is a Write Command. \n")
# file.write("It allows us to write in a particular file. \n")
# file.write("We have to read loop in Python. \n")
# file.write("We love JS. \n")
# file.close()

## Using With Statement

# with open("file.txt", "w") as f:
#     f.write("Hello World!!!")