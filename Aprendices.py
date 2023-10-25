#1 Cree una lista vacía  denominada aprendices y edades, llénelas solicitando los datos por teclado.
aprendices =[]
edades =[]

#2 llénelas solicitando los datos por teclado.
NumApren =int(input("¿Cuantos aprendices son?"))
for listas in range(NumApren): # range genera una secuencia de números que van desde 0 hasta el numero que digite el usuario 
    nombres=input("Digite el nombre del aprendiz: " )
    edad=int(input("Digite la edad del aprendiz: "))
    aprendices.append(nombres) # append es para agregar  
    edades.append(edad)

#3 Imprima las listas
print("Listas de aprendices", aprendices)
print("Listas de edades:", edades)

#4 Muestre el aprendiz con la mayor edad
AprenMayor= max(edades) # max es para encontrar el valor mas alto el maximo 
aprenMayor= edades.index(AprenMayor) # index obtiene el índice de variable
print(f"El aprendiz de mayor edad es: {aprendices[aprenMayor]} con {AprenMayor} años :) ") # f es para una cadena de texto e incluimos estos [], {}

#5 Inserte el nombre de la instructora en la posición 1
instru ="Adrian Lucia Rincon Forero"
aprendices.insert(1, instru) # insert en este caso para isertar el nonbre de la instructura en la posicion 1

#6 Cuente cuantos aprendices tienen 18 años
MayorApren =edades.count(18) # Count es un contador
print(f"Hay {MayorApren} aprendices que tienen 18 años :) ")

#7 Agregue un aprendiz x al final de la lista
aprendices.append("Juanito Perez")

#8 Borre el nombre de la instructora de la lista
if instru in aprendices:
    aprendices.remove(instru) # remove sirve para quitar, saccar, eliminar o remover un dato

#Indique un dato a buscar en la lista de aprendices
buscador =input("Ingrese el aprendiz a buscar: ")
if buscador in aprendices:
    print(f"El aprendiz {buscador} sí se encuentra en la lista") 
else:
    print(f"El aprendiz {buscador} no se encuentra en la lista")

#Muestre los primeros 10 aprendices de la lista
print(f"Los 10 primeros de la lista son: ", aprendices[:10]) 

#Muestre los 10 últimos aprendices de la lista
print(f"Los 10 ultimos de la lista son: ", aprendices[-10:]) 

#Muestre del elemento 10 al elemento 20
if len(aprendices) >= 20:
    print(f"Del elemento 10 al elemento 20: ", aprendices[9:19])
else: 
    print("Lo sentimos no hay suficientes elementos, Ingresa más a la proxima :( ")