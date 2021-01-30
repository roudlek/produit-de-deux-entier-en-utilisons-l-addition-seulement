X = int(input("Entrer le premier nombre entier : "))
Y = int(input("Entrer le deuxieme nombre entier : "))
Z = 0
if X >= 0 and Y >= 0 :
    for i in range (0 , Y ):
        Z = Z + X
    print("le resultat de multiplication est : ",Z)

elif X < 0 and Y < 0 :
    X = -X
    Y = -Y
    for i in range (0 , Y ):
        Z = Z + X
    print("le resultat de multiplication est : ",Z)

elif X >= 0 and Y < 0 :
    Y = -Y
    for i in range (0 , Y ):
        Z = Z + X
    print("le resultat de multiplication est : ",-Z)

elif X < 0 and Y >= 0 :
    X = -X
    for i in range (0 , Y ):
        Z = Z + X
    print("le resultat de multiplication est : ",-Z)
