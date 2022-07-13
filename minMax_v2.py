intentos = 3

min = 1
max = 10

while intentos > 0:
    
    adivinaNum = int(input("en rango \n"))
       
    if adivinaNum < min or adivinaNum > max:           
            print(f"El fuera rango {adivinaNum}" )
     