def is_palindrome(texto):
    # pasar a minus
    texto = texto.lower()
    
    # eliminar espacios
    texto = texto.replace(" ", "")
    
    # comparar con el reverso
    return texto == texto[::-1]

if __name__ == "__main__":
    try:
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo\n')
            else:
                print(f'"{entrada}" no es un palíndromo\n')
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")