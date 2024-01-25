#creating a simple function

def give_taquito():
    print("eat taquito")
    
    
for x in range(0,3):
    give_taquito()
    
def give_taquito_to(name):
    print(f"eat taquito to {name}")
    
#name = input("Who is the taquito for? ")
#for x in range (0,3):
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

def creating_random_password(num_for_password):
    chars = "abcdefghijklmn"
    num_integer = str(num_for_password)
    num = int(num_integer[0])
    c1 = num + 2
    c2 = num + 3
    c3 = num + 2
    create_password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num_integer*2}"
    return create_password
     
result = creating_random_password(9)
print(result) 