def CSquared(count):
    userInput = int(input("Enter max squared value : "))
    while count*count<=userInput:
      print(count," ",count*count)
      count=count+1;
CSquared(0)

