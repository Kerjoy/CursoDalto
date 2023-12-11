montly_income = 15000
montly_outcome = 7000

#nested if and else if (elif)

if montly_income >= 15000:
    if montly_income - montly_outcome < 0:
        print("deficit")
    elif montly_income - montly_outcome > 0:
        print("ok you can still existing")
    else:
        print("excesive expenses")
elif montly_income >= 10000:
    print("You are wealthy, do you want a friend?")
elif montly_income >= 1000:
    print("You are ok, for Latam standars")
else:
    print("are you okay?")