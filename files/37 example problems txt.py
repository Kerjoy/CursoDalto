#list with names and other with lastnames 

name = ["Paco","Juan","Barbara","Dimitri","Pablo"]
last_name = ["Paquin","Juanin","Barbarin","Dimitrin","Pablin"]

#register this info with a optimal way

with open("files\\names_and_lastnames.txt","w") as file: #works fine for me with relative path but can use absolute path
    file.writelines("The data is: \n")
    #brackets is important with for in one line [expresion]
    [file.writelines(f"Name: {n}\nApellido: {l}\n------------\n") for n,l in zip(name,last_name)]      
    
    #with standar for            
    for n,l in zip(name,last_name):
        file.writelines(f"Name: {n}\nApellido: {l}\n------------\n")
    
