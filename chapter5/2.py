def temperature_check():
    i = int(input("Enter the temperaure:"))

    if i > 100:
        print("It is Hot")
    elif i < 60:
        print("It is Cold")
    elif i > 61 and i <= 99:
        print("It is just Right")

temperature_check()
