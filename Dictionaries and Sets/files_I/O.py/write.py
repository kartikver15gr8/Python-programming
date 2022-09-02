f = open("anotherfile.txt","w")
f.write("here i created another file by using write function ")      # here we created a new file by using write function
f.close()


f = open("anotherfile.txt","a")
f.write("i am appending")   # Here i appended the "anotherfile.txt" by using "a" i.e append mode
f.close()

