# f= open("kartik.txt","r")       # This kartik.txt file is made by me using notepad  
# f= open("kartik.txt",)       # here we can see that if we will not specify the mode, the it will automatically yake read as a mode
# data = f.read()             # And here i'm using f.read command to read that kartik.txt file
# # data = f.readline()             # we can also read the first line of our text file by using built in function "readline()"
# # data = f.readline()             # read another line of our text file
# # data = f.read(5)             # we can also specify that how much charracter we want to read, as here i want to read only 5 char.
# print(data)                 # Here i printed the data which is written inside the kartik.txt file
# f.close()                   # Here we closed the kartik.txt file by using f.close command

p = open("badhiya.txt","r")
read = p.read()
print(read)
p.close()








