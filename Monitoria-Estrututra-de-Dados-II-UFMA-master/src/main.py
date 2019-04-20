from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":

    leitor = input("Insira o comando\n Ex: 100vertices QuickSort meio\n caso o algoritmo não possua um metodo digite null \n")
    comando = leitor.split(" ")
    arquivo = "./grafos/" + comando[0].lower()+ ".json"
    print(comando[2])
    if(comando[1].lower() == "insertionsort" or comando[1].lower() == "insertsort" ):
        algoritimoDeOrdenacao = InsertionSort()
    elif(comando[1].lower() == "selectsort"):
        algoritimoDeOrdenacao = Selectsort()
    elif(comando[1].lower() == "shellsort"):
        algoritimoDeOrdenacao = Shellsort()
    elif(comando[1].lower() == "mergesort"):
        algoritimoDeOrdenacao = Mergesort()
    
    arquivoJson =  arquivo #'./grafos/7vertices.json'
    arquivoDeSaida = './arvores_geradas/mst7Vertices.txt'

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

