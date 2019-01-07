#Create While Loop

#Identify Variables
q1 = int()
q1t = """Which one of these colours are the primary colours?
1.Yellow
2.Green
3.Orange
4.Purple

Answer:  """
choice = False
correct = 0

#While Loop
while choice == False:
    try:
        q1 = int(input(q1t))
        if q1 == 1:
            correct += 1
            choice == True

        elif 0 < q1 < 5:
            choice == True

        else:
            print("Please type a positive number between 1 and 4. ")

    except ValueError:
        print("Seriously? Please put a WHOLE POSITIVE INTEGER between 1 and 4. ")
