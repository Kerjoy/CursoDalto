def sum():
    while True:
        #ask numbers
        a = input("give me first number: ")
        b = input("give me second number: ")
        try:
            result = int(a) + int (b)
            #if raise a exception, ask for data entry again
        except Exception as e:
            print("what are you doing e.e?")
            print(f"showing this exception: {e}")
            print(f"showing type error: {type(e).__name__}")
            #if all works fine use break with else
        else:
            break
        finally:
            print("this it execute anytime")
    return result

print(sum())