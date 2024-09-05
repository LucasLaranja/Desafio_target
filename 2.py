def contar_letras(a):

    letras = 0
    
    for char in a:
        if char.lower() == 'a':
            letras += 1
    
    return letras

def main():

    texto = input("Digite o texto para a contagem de letras 'a': ")
    quantidade = contar_letras(texto)
    
    print(f"A letra 'a' aparece {quantidade} vezes no texto.")

main()