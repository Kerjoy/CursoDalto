file_open = open("files\\text_file.txt", encoding="UTF-8") #according to dalto, i can reall all characters with this encoding

#read all file only can read a file one each time
#file_read = file_open.read()

#read each line
file_read_line = file_open.readlines()
#read only a line
#file_read_line = file_open.readline() #if i give a integer, only read this number of character in the line

file_open.close()

print(file_read_line)