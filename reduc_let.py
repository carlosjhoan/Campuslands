a = input("Ingrese secuencia: ")



#for i in range(len(a)):
#if a[0] == a[1]:
#    new_sec = a[2:]

#else:
#    new_sec = a
#print (f"Secuencia: {a}")
#print (f"Nueva secuencia: {new_sec}")
i = True
f = 0
new_sec = ""

while i == True:
    if new_sec == "":
        if a[f] == a[f+1]:
            new_sec = a[f+2:]
            x = "check" 
        


        else:
            new_sec = a
            x = "no-check"

            
    
    if x == "check":
        f = 0

    elif x == "no-check":
        f += 1
    if f < (len(new_sec) -2):
        if new_sec[f] == new_sec[f+1]:
            new_sec = new_sec[f+2:]
            x = "check"
        else:
            new_sec = new_sec
            x = "no-check"
    else:
        i = False
    
print(f"secuencia: {a}")
print (f"Nueva secuencia: {new_sec}")