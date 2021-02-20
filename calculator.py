NUMBER1 = input("1st number:")
operation = input("OPERATION: (TYPE +, -, *, /, %, ^, OR //)")
NUMBER2 = input("2nd number:")
NUMBER1 = int(NUMBER1)
NUMBER2 = int(NUMBER2)

if operation == "+":
    Sum = NUMBER1 + NUMBER2
    print(Sum)

elif operation == "-":
    Difference = NUMBER1 - NUMBER2
    print(Difference)

elif operation == "*":
    Product = NUMBER1 * NUMBER2
    print(Product)

elif operation == "/":
    Quotient = NUMBER1 / NUMBER2
    print(Quotient)

elif operation == "%":
    Remainder = NUMBER1 % NUMBER2
    print(Remainder)

elif operation == "^":
    Power =  NUMBER1 ** NUMBER2
    print(Power)

elif operation == "//":
    AproximateDivision = NUMBER1 // NUMBER2
    print(AproximateDivision)
    
else:
    print("Please go back and check your input")
