a = """kjkjhkjhkhkhkjhkj ...kbbm   bkjh   
        X: 1.132
        kblkBSKFBFÑkbdff
        ssssssssssssssssssssss
        X: 0.235
        diij@@@@@@
        X: 2.312
        hsñkjbdgkañfbgñaljfbg
        X: 2.365
        kjgkfjghkjfgdskdjgkjshgdf
        jdahkfjshdkjfhdkjhfsjdhf
        //////////////
        X: 3.124""" #a[0] a[31] CADENA PRINCIPAL
# cadenas son NO-MODIFICABLES
sum = 0
n = 0
cont = 0
for i in range(len(a)):
    if a[i].isdigit() and cont == 0:
        frag = a[i:i+5]
        n += 1
        cont += 1
        sum += float(frag)
        print (frag)

    elif cont != 0:
        cont += 1
        if cont ==5:
            cont = 0
        
print (f"suma: {sum:.3f}")    
print (f"prom: {sum/n:.3f}")  
    

    


    #print (frag)

b = "X: 1.132"
b = b[3:8]
#print (f"b: {float(b)}")

#print (a[65])
#for i in a:
#    if i.isdigit() and int(i) != 0:
#        sum += int(i)/10
#print (f"suma = {sum:.2f}")

        
















#print (a[10])

#b = a[3:8] + a[15:22]
#print (b)

#a[3] = "z" #Esto no se puede realizar, porque la cadena son INMUTABLES


#print ("\nCadena sin espacios vacíos al inicio y final", a.strip())

#c = a.strip()
#c = c.split("j") #LISTA
#c[5] = "jajajajaja"
#print ("\nc: ", c)