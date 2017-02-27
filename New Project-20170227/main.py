def cancellaschermo ():
    for t in range (40):
        print

def saluto():  
    print "ciao indovina il numero segreto"
    print
    print
    
def gioco():
    x=9
    y=1
    while True:
        a=input ("dammi il numero esatto")
        if a>x:
            print "numero errato prova con un numero meno grande"
            y=y+1
        elif a<x:
            print "ti consiglio di pensare ad un numero maggiore"
            y=y+1
        else: "Complimenti sei un genio hai indovinato in",y,"tentativi"

cancellaschermo()
saluto()
gioco()