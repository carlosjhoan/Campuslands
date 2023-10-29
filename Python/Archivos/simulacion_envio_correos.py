fd = open("Archivos/mbox-short.txt", "r")

fd_2 = open("Archivos/envio_emails.txt", "w")

set_email =set()
list_email = []
for linea in fd:
    if linea.startswith("From:"):
       email = linea.split()[1]
       if email not in list_email:
            #set_email.add(email)
            list_email.append(email)
            #print (f"{email} enviado [ok]")
            #fd_2.write(f"{email} enviado [ok]\n")

for i in list(reversed(list_email)):
    print (f"{i} enviado [ok]")
    fd_2.write(f"{i} enviado [ok]\n") 



fd.close()
fd_2.close()