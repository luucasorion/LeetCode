class Solution(object):
    def reverseWords(self,s):
        separa_frase = s.split(' ')
        invertida = []
        for x in range(len(separa_frase)):
            palavra_separada =  separa_frase[x][::-1]
         
        
            invertida.append(palavra_separada)
        
        return ' '.join(invertida)
        


 