while True:

    print("For Fahrenheit conversion, enter fah or For Celsius conversion, enter cels")
    line = input(">")
    if line[0] == "f":
        print("Enter Celsius value to converted to Fahrenheit.")
        val = input(">")
        res = (int(val) * 9/5) + 32
        print(res)
    elif line[0] == "c":
        print("Enter Fahrenheit value to converted to Celsius.")
        val = input(">")
        res = (int(val) - 32) / 9/5
        print(res)
    if line[0] != "cels" and line[0] != "fah":
        #print("invalid!")
        break
print("Done")