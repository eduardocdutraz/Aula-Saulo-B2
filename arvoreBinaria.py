# -*- coding: utf-8 -*-

class NodeABB:

    def __init__(self, data=None, esq=None, dir=None):
      self._data = data
      self._esq = esq
      self._dir = dir
      if self._data:
          self._size = 1
      else:
          self._size = 0

    def setRaizArbin(self, elem):
        self._data = elem

    def raizArbin(self):
        return self._data

    def setDirArbin(self, arbin):
        self._dir = arbin

    def dirArbin(self):
        return self._dir

    def setEsqArbin(self, arbin):
        self._esq = arbin

    def esqArbin(self):
        return self._esq

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    # def vaziaArbin(self): # basta verificar se a instancia eh Nulo: None

    def add(self, node): # caso da Arv vazia esta sendo tratada no construtor
        if node._data < self._data: # data < raiz : inserir na subArvore esquerda
            if self._esq is None: # subArvEsq eh vazia
                self._esq = node
            else:
                self._esq.add(node)
        elif node._data > self._data: # data > raiz : inserir na subArv direita
            if self._dir is None:
                self._dir = node
            else:
                self._dir.add(node)
        self._size += 1


    def min(self):
        """Retorna o menor elemento da subárvore que tem self como raiz.
        """
        if self._esq is None:
            return self
        else:
            return self._esq.min()

    def removeMin(self):
        """Remove o menor elemento da subárvore que tem self como raiz.
        """
        if self._esq is None:  # encontrou o min, daí pode rearranjar
            return self._dir
        self._esq = self._esq.removeMin()
        return self

    def remove(self, elem):
        if elem < self._data:
            self._esq = self._esq.remove(elem)
        elif elem > self._data:
            self._dir = self._dir.remove(elem)
        else:
            # encontramos o elemento, então vamos removê-lo!
            if self._dir is None:
                return self._esq
            if self._esq is None:
                return self._dir
            # ao invés de remover o nó, copiamos os valores do nó substituto
            tmp = self._dir.min()
            self._data = tmp._data
            self._dir.removeMin()
        return self

if __name__ == '__main__':


    def preOrdemArbin(node:NodeABB):
        if node is not None:#if not node.vaziaArbin():
            print(node._data)
            if node._esq is not None:
                preOrdemArbin(node._esq)
            if node._dir is not None:
                preOrdemArbin(node._dir)

    def preOrdemArbin2(node:NodeABB):
        if node is not None:
            print(node._data)
            if node.esqArbin() is not None: 
                preOrdemArbin(node.esqArbin())
            if node.dirArbin() is not None:
                preOrdemArbin(node.dirArbin())


    # -------------------------------------------------------------------------------
    # Exercícios de Arvore Binaria : pode ter elementos repetidos e não segue uma ordenação
    #  -------------------------------------------------------------------------------

    """1) int pesoArbin( Arbin a){...} 
    Calcular e retornar o peso de uma árvore binária ( número de elementos da árvore). 
    Obs: a complexidade desta função é O(N) 
    """



    def pesoArbin(arbin:NodeABB):
        # se a arbin esta vazia retornar zero
        if not arbin:
            return 0
        # senao tem pelo menos uma raiz:
        else:
            # retornar 1 + peso da subArv esq + peso subArvDir
            return 1 + pesoArbin(arbin.esqArbin()) + pesoArbin(arbin.dirArbin())

       


    """2) int estaArbin( Arbin a, TipoA elem){...} 
    Verificar se um elemento está presente em uma árvore binária. 
    Obs: a complexidade desta função é O(N) se a árvore estiver degenerada e O(log N) se a 
    árvore estiver balanceada(cheia).
    """
    def estaArbin(arbin:NodeABB, elem):
        # se arbin vazia entao elem nao esta: retornar False
        if not arbin:
            return False
        # se elem == raiz, elem esta presente: retornar True
        elif arbin._data == elem:
            return True
        # do contrario procurar elem na subArv esq e dir
        else:
            return estaArbin(arbin.esqArbin()) or estaArbin(arbin.dirArbin())


        

    """3) int numFolhas( Arbin a){...}  
    Calcular o número de folhas de uma Arbin. 
    Obs: a complexidade desta função é O(N) 
    """
    def numFolhas(arbin:NodeABB):
        # se arbin vazia nao tem folhas: retornar zero
        if arbin is None:
            return 0
        # se tem uma raiz com as duas subArv esq e dir vazias entao tem 1 folha
        # retornar  1
        # elif ...
	    # return 0
        

    """4) int numOcorrencias( Arbin a){...}  
    Calcular o número de vezes que um elemento aparece na Arbin. 
    Obs: a complexidade desta função é O(N)
    """
    def numOcorrencias( arbin: NodeABB, elem ):
        return 0


    # -------------------------------------------------------------------------------
    # Exercícios de ABB (Arvore Binaria de Busca) ou ABP (Arv. Binaria de Pesquisa)
    # Não pode ter elementos repetidos e segue uma ordem
    #  -------------------------------------------------------------------------------

    # verifica se o elem esta presente na ABB arbin
    def estaArbinBusca(arbin:NodeABB, elem):
        if not arbin:
            return False
        elif elem == arbin._data:
            return True
        elif elem < arbin._data:
            return estaArbinBusca(arbin.esqArbin(), elem)
        else:
            return estaArbinBusca(arbin.dirArbin(), elem)


    # verifica se o elem esta presente na ABB arbin
    def insArbinBusca2( arbin:NodeABB, elem):
        #arbin vazia: chama o construtor
        return 0


    

    def insArbinBusca( arbin:NodeABB, elem):
        # arbin vazia: chama o construtor
        if not arbin: # arvore vazia
            arbin = NodeABB(elem)
        elif elem < arbin._data:
            arbin._esq = insArbinBusca(arbin._esq, elem)
        elif elem > arbin._data:
            arbin._dir = insArbinBusca(arbin._dir, elem)
        return arbin

    def maiorElemento(arbin:NodeABB):
       return 0


    def elimArbinBusca(arbin:NodeABB, elem):
        #arbinAux = None
        #maior = None
        if(arbin.raizArbin() == elem):
            if(arbin.esqArbin() is None and arbin.dirArbin() is None):
                arbin = None
                return None
            elif (arbin.esqArbin() is None):
                arbinAux = arbin.dirArbin()
                arbin = None
                return arbinAux
            else:
                maior = maiorElemento(arbin.esqArbin())
                #print('maior = {}'.format(maior))
                #arbin._data = maior
                #arbin._esq = elimArbinBusca(arbin.esqArbin(), maior)
                arbin.setRaizArbin(maior)
                arbin.setEsqArbin(elimArbinBusca(arbin.esqArbin(), maior))
        elif (elem < arbin.raizArbin()):
            arbin.setEsqArbin(elimArbinBusca(arbin.esqArbin(),elem))
            #arbin._esq = elimArbinBusca(arbin.esqArbin(), elem)
        else:
            arbin.setDirArbin(elimArbinBusca(arbin.dirArbin(),elem))
            #arbin._dir = elimArbinBusca(arbin.dirArbin(), elem)
        return arbin

    def altura_arbin(arbin:NodeABB):
        if arbin == None:
           return -1
        else:
            h_esq = altura_arbin(arbin._esq)
            h_dir = altura_arbin(arbin._dir)
            if h_esq>h_dir:
                return h_esq + 1
            else:
                return h_dir + 1

    def nivel_elem(arbin:NodeABB , elem):
        if arbin and arbin.dirArbin() == None:
            return arbin.raizArbin()
        else:
            return maiorElemento(arbin.dirArbin())
        






    #---------------------------------------------------------------------
    # chamada dos metodos implementados
    #---------------------------------------------------------------------
    node = NodeABB(50)
    print("Peso ou qtde elem = {}".format(pesoArbin(node)))
    print('numFolhas = {}'.format(numFolhas(node)))
    node2 = NodeABB(40)
    node3 = NodeABB(60)
    #print(node._data)
    #preOrdemArbin2(node)
    node.add(node2) # node com 50 vai ser a raiz da arvore
    #print("Peso ou qtde elem = {}".format(pesoArbin(node)))
    #print('numFolhas = {}'.format(numFolhas(node)))
    #preOrdemArbin2(node)
    node.add(node3)
    preOrdemArbin(node)
    print("================================================")

    num_elementos = pesoArbin(node)
    print(f"num_elementos = {num_elementos}")

    print("================================================")

    if estaArbinBusca(node, 60):
        print(f"elemento 60 esta na arvore")
    else:
        print(f"elemento 60 NAO esta na arvore")
    
    print("================================================")

    if estaArbinBusca(node, 30):
        print(f"elemento 30 esta na arvore")
    else:
        print(f"elemento 30 NAO esta na arvore")
    
    print("================================================")

    node = insArbinBusca(node, 30)
    print("node")
    preOrdemArbin(node)
    print("================================================")

    arbin = None
    arbin  = insArbinBusca(arbin, 50)
    arbin  = insArbinBusca(arbin, 40)
    arbin  = insArbinBusca(arbin, 60)
    print("arbin")
    preOrdemArbin(arbin)
    print("================================================")
    arbin  = insArbinBusca(arbin, 30)
    print("arbin")
    preOrdemArbin(arbin)

    print("================================================")
