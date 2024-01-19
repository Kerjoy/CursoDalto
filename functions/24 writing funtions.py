#creating a simple function

def give_taquito():
    print("eat taquito")
    
    
for x in range(0,3):
    give_taquito()
    
def give_taquito_to(name):
    print(f"eat taquito to {name}")
    
name = input("Who is the taquito for? ")
for x in range (0,3):
    give_taquito_to(name)
    
genre = "man"
name = "superman"
def function_with_condition(genre,name):
    genre.lower()
    if genre == "man":
        print("Hi superman")
    else:
        print("Hi superwoman")
        
function_with_condition(genre,name)