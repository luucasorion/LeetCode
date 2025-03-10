
def binarySearch(lista : list, numeroEsperado : int):
    direita = len(lista) - 1
    esquerda = 0
    meio = 0

    while(esquerda <= direita):
        meio = (direita + esquerda) // 2
        
        if (lista[meio] == numeroEsperado):
            return meio
        elif (lista[meio] < numeroEsperado):
            esquerda = meio +1
        else:
            direita = meio - 1
   
    return -1
