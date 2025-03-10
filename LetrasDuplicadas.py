class Solution(object):
    def LetrasDuplicada(self, palavra:str):
        repetidas = {}
        letras = list(palavra)
        for x in range(len(letras)):
            if letras[x] in repetidas:
                repetidas[letras[x]] +=1
            else:
                repetidas[letras[x]] = 1 
        return repetidas

