def CSquared(count):
    userInput = int(input("Enter max squared value : "))
    print("Max squared value : ",userInput)
    print("CNT      SQR")
    while count*count<=userInput:
      print(f'{count}{count*count:10}')
      count=count+1;
CSquared(0)


