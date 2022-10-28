a = int(input("How many friends?"))
b = int(input("How many chocolates?"))
roundedb = round(b/a, 0)
leftoverb = b-a*roundedb
print("You should give each friend")
print(roundedb, "each")
print("AND you will have")
print(leftoverb, "left")