from os import system


def generaCuadros():
    system("cls")
    texto=input("Ingresa una frase: ")
    cant=len(texto)
    print(f"# +{'-'*(cant//2)}{'-'*(cant)}{'-'*(cant//2)}+")
    print(f"# +{' '*(cant//2)}{texto}{' '*(cant//2)}+")
    print(f"# +{'-'*(cant//2)}{'-'*(cant)}{'-'*(cant//2)}+")

# while 1:
#     generaCuadros()
#     input("Enter")