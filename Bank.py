co = int(input("What do you have left in pesos?"))
pe = int(input("What do you have left in soles?"))
br = int(input("What do you have left in reais?"))
total = co*0.050 + pe*0.27 + br*0.17
print(round(total))