# This is the simple and the main code of the repeate text generator.

# Here the txt.txt is the name of the file in which you want to save the repeated text

file1 = open('txt.txt',"w")
l = "\n I will not do this again" * 100
file1.writelines(l)
file1.close()




