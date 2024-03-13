n = int(input("Coloque um número: "))
cont = 1  

while cont <= n:
    if cont % 3 == 0 and cont % 5 == 0:  
        print("FizzBuzz")
    elif cont % 3 == 0:  
        print("Fizz")
    elif cont % 5 == 0:  
        print("Buzz")
    else:
        print(cont, "Não é múltiplo") 
    cont += 1 
