con='s'
while con in 'sS':
    print('''\t\t\t MENU
      1. NUMEROS PARES MENOS MULTIPLOS DE 7
      2. MULTIPLOS DE 6
      3. NUMEROS PRIMOS
      4. NUMEROS QUE TERMINAN EN 0 \n''')


    opcion=int(input("elija una opcion: \t"))
    n1=int(input("\ningrese el limite inferior de un rango de numeros: \t"))
    n2=int(input("ingrese el limite superior de un rango de numeros: \t"))
    rango=""
    impar=""
    multiplo_6=""
    primo=""
    cero=""
    while n1<=n2:
        if opcion==1:
            if (-1)**n1<0:
                impar=impar+str(n1)+" "
        elif opcion==2:
            if n1%6==0:
                multiplo_6=multiplo_6+str(n1)+" "
        elif opcion==3:
            a=1
            cuenta=0
            while a<=n1:
                if n1%a==0:
                    cuenta=cuenta+1
                a=a+1
            if cuenta<=2:
                primo=primo+str(n1)+" "
        elif opcion==4:
            if n1%10==0:
                cero=cero+str(n1)+" "
        
        rango=rango+str(n1)+" "
        n1=n1+1
        
    print("\nel rango de numeros es: %s \t"%(rango))
    print("\nlos numeros impares son: %s \t"%(impar))
    print("los numeros multiplos de 6 son: %s \t"%(multiplo_6))
    print("los numeros primos son: %s \t"%(primo))
    print("los numeros que terminan en 0 son: %s \t"%(cero))
    con=input("\nquiere continuar presione 'S' sino cualquier tecla para salir: \t")
print("\n usted salio bay")
