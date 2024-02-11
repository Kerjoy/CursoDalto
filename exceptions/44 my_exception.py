#class and heritage
class MyException (Exception):
    def __init__(self,err):
        print(f"My first modification to a exception: {err}")
        
#raising my exception
#raise MyException("Never i try this it before")

#handle
try:
    raise MyException("Something works bad, i dont think what is a good message for this")
except:
    print("Do you want a taquito?")