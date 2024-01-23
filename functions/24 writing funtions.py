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
    genre = genre.lower()
    if genre == "man":
        adj = "queen"
    elif genre == "hombre":
        adj = "king"
    else:
        anj = "crack"
        
    print(f"Hi {name}, my {adj} whats up?")
 
function_with_condition(genre,name)