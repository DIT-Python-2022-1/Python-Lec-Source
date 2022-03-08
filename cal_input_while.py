while True :
    a = input("1st input?")

    if a == "00000":
        break
    b = int(input("2nd input?"))
    a = int(a);
     
    result =a + b
    print(a, "+", b, "=", result)
    result = a - b
    print(a, "-", b, "=", result)
    result = a * b
    print(a, "*", b, "=", result)
    result = a / b
    print(a, "/", b, "=", result)                                   

print("end  of program")



