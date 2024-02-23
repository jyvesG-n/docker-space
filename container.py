from os import system
def f(n):
    for i in range(1,n+1):
        system("docker run -dp 192.168.1.14:" + str(3000+i) + ":" + str(3000) + " jygode/getting-started")

nbre = int(input("Combien de container docker (node.js) voulez-vous ? => "))
f(nbre)

