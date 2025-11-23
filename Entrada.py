#/Entrada.py

def pedir_entero(prompt):
    """
    Pide un número al usuario y se asegura de que sea un entero
    positivo válido.
    Vuelve a pedir el dato si el usuario ingresa texto.
    """
    
    valido = False
    num_str = ""

    while not valido:
        num_str = input(prompt)
        
        # Verificamos que no esté vacío
        if len(num_str) > 0:
            valido = True # Suponemos que es válido...
            
            # Revisamos cada carácter
            for caracter in num_str:
                # Si un caracter NO está en la lista de dígitos,
                # marcamos como inválido.
                if caracter not in "0123456789":
                    valido = False
        
        # Si después de revisar sigue siendo inválido, mostramos error
        if not valido:
            print("Error: debe ingresar un número entero válido.")

    # Si salimos del bucle, es seguro convertir a int
    return int(num_str)

def pedir_cadena(prompt):
    """
    Pide una cadena de texto.
    """
    return input(prompt)