'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)
Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
class InsertionSort(object):
    def ordenar(self, colecao):
        '''
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
        '''
        for i in range(1,len(colecao)):
            key = colecao[i]
            j = i-1
            while j >=0 and int(key["weight"]) < int(colecao[j]["weight"]):
                colecao[j+1] = colecao[j]
                j-=1
            colecao[j+1] = key
        # for i in colecao:
        #     print(i["weight"])
        return colecao
class Selectsort(object):
    def ordenar(self,colecao):
        for i in range(len(colecao)):
            meio = i
            for j in range(i+1,len(colecao)):
                if(int(colecao[meio]["weight"])>int(colecao[j]["weight"])):
                    meio =j
            colecao[i],colecao[meio] = colecao[meio],colecao[i]
        # for i in colecao:
        #     print(i["weight"])
        return colecao
class Shellsort(object):
    def ordenar(self,colecao):
        gap =1 
        for initial in range(gap,len(colecao)):
            gap = (gap*3)+1
            while(gap>0):
                gap = gap//3
                for i in range(gap,len(colecao)):
                    atual = colecao[i]
                    posicao = i
                    while(int(colecao[posicao-gap]["weight"])>int(atual["weight"]) and posicao>= gap):
                        colecao[posicao] = colecao[posicao-gap]
                        posicao-=gap
                    colecao[posicao] = atual
        # for i in colecao:
        #     print(i["weight"])
        return colecao
class Mergesort(object):
    def ordenar(self,colecao):
        if(len(colecao)>1):
            mid= len(colecao)//2
            Lmid = colecao[:mid]
            Rmid = colecao[mid:]
            Mergesort.ordenar(self,Lmid)
            Mergesort.ordenar(self,Rmid)
            i=0
            j=0
            k=0
            while(i<len(Lmid) and  j<len(Rmid)):
                if(int(Lmid[i]["weight"]) < int(Rmid[i]["weight"])):
                    colecao[k] = Lmid[i]
                    i+=1
                else:
                    colecao[k] = Rmid[j]
                    j+=1
                k+=1
            while(i<len(Lmid)):
                colecao[k] = Lmid[i]
                i+=1
                k+=1
            while(j<len(Rmid)):
                colecao[k] = Rmid[j]
                j+=1
                k+=1
        return colecao
    def printa(self,colecao):
        for i in colecao:
            print(i["weight"])

                