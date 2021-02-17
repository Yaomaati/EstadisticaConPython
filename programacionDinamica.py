def fibonacci(n, memo = {}): #Al añadir el diccionario "memo" lo que estamos haciendo es abrir la posibilidad de guardar los resultados de nuestro calculo, para usarlos mas tarde

    if n == 0 or n == 1: 
        return 1         

    #Hacemos que si la sucesión comienza en 1 o 0, devuelva un 1
    #La razón de hacer dicho movimiento es por que de otro modo, en cada proceso recursivo el programa volvería a calcular TODOS los números, haciendo que el calculo se vuelva exponencial
    #Lo cuál convierte a nuestro algoritmo en uno de crecimiento exponencial, es decir, un algoritmo extremadamente ineficiente

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci(n-1, memo) + fibonacci(n-2, memo) #Con ésta forma de declarar lo que hacemos es que se realice el calculo, y se almacene en memoria cada resultado
        memo[n] = resultado #Una vez almacenados ambos resultados de fibonacci los añadimos a 

        return resultado


    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':

    n = int(input("Elige el número cuya sucesión quieres conocer: "))
    resultado = fibonacci(n)

    print(resultado)
    