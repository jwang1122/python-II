with open("cardDecision.py", 'a') as table:
    table.write("decisionTable = {\n")
    for i in range(10, 30): # player total
        for j in range(16, 30): # dealer tota
            if (i>21):
                table.write('"' + str(i)+":"+str(j) + '":"dealer",\n') 
            if j>21 and i<=21:
                table.write('"' + str(i)+":"+str(j) + '":"player",\n') 
            if i<=21 and j<21 and i>j:
                table.write('"' + str(i)+":"+str(j) + '":"player",\n') 
            if i<21 and j<=21 and j>i:
                table.write('"' + str(i)+":"+str(j) + '":"dealer",\n') 
            if i == j:
                table.write('"' + str(i)+":"+str(j) + '":"nobody",\n') 
    table.write("}")
print("Done.")