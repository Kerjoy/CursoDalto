#open the file with open
with open("files\\text_file.txt","w", encoding="UTF-8") as text: #if the file doesnt exist this create it IMPORTANT with "a"
    #can change
    #overwriting the content
    #content = text.write("Only try writting a new value in the file")
    #text.writelines("Hi rewriting with writelines")
    text.writelines(["This can rewrite with\n","list and work it"]) #Write lines is acumulative not rewriting 
    
    #show the file
    print(text)
    
#is not necesary close the file 

#this is a example the same writing funtion but with a flag for append text lines and bucle for
with open("files\\text_file.txt","a", encoding="UTF-8") as text: #Here change to append 
    for i in range(5): text.writelines(f"This append line {i}\n")
    
#is not necesary close the file 