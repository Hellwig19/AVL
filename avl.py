import random
import time

#10,5,15,3,1,20,25,18

class Node:
    # método construtor
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1
        

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):

        novo_no = Node(valor)

        caminho = []

        # Raiz não existe!
        if self.raiz is None:
            self.raiz = novo_no
            return

        # Se existir uma raiz, o nó atual recebe o valor da raiz
        no_atual = self.raiz

        while True:
            # IMPORTANTE: Adiciona o nó atual ao caminho
            caminho.append(no_atual)
            
            # Se valor for menor que atual, olha para a esquerda do no_atual
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = novo_no
                    break
                else:
                    no_atual = no_atual.esquerda
            # Se valor for maior que atual, olha para a direita do no_atual
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = novo_no
                    break
                else:
                    no_atual = no_atual.direita
            # Se o valor é igual
            else:
                return

        for i in range(len(caminho) - 1, -1, -1):
            no_ancestral = caminho[i]
            self.atualizar_altura(no_ancestral)
            fator_balanceamento = self.obter_fator_balanceamento(no_ancestral)
            
            nova_sub_raiz = None
            
            if fator_balanceamento > 1:
                if valor < no_ancestral.esquerda.valor:
                    nova_sub_raiz = self.rotacao_direita(no_ancestral)
                else:
                    no_ancestral.esquerda = self.rotacao_esquerda(no_ancestral.esquerda)
                    nova_sub_raiz = self.rotacao_direita(no_ancestral)

            elif fator_balanceamento < -1:
                if valor > no_ancestral.direita.valor:
                    nova_sub_raiz = self.rotacao_esquerda(no_ancestral)
                else:
                    no_ancestral.direita = self.rotacao_direita(no_ancestral.direita)
                    nova_sub_raiz = self.rotacao_esquerda(no_ancestral)
            
            if nova_sub_raiz is not None:
                if i == 0:
                    self.raiz = nova_sub_raiz
                else:
                    pai = caminho[i-1]
                    if pai.esquerda == no_ancestral:
                        pai.esquerda = nova_sub_raiz
                    else:
                        pai.direita = nova_sub_raiz
                break


    def buscar(self, valor):
        no_atual = self.raiz

        # Se não existe raiz
        if no_atual is None:
            return False

        while no_atual is not None:
            # Existe o valor na árvore
            if valor == no_atual.valor:
                return True
            # Valor é menor
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            # Valor é maior
            else:
                no_atual = no_atual.direita
        # Valor não existe na árvore
        return False
    
    def obter_altura(self, no):
        if no is None:
            return 0
        return no.altura
        
      
    def atualizar_altura(self, no):
        altura_esquerda = self.obter_altura(no.esquerda)
        altura_direita = self.obter_altura(no.direita)
        no.altura = 1 + max(altura_esquerda, altura_direita)
        

    def obter_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)
    


    def rotacao_direita(self, no): 
        Z = no  
        Y = Z.esquerda   
        T3 = Y.direita

        Y.direita = Z
        Z.esquerda = T3
        self.atualizar_altura(Z)
        self.atualizar_altura(Y)
    
        return Y

    def rotacao_esquerda(self, no):
        Z = no  
        Y = Z.direita 
        T2 = Y.esquerda

        Y.esquerda = Z
        Z.direita = T2
        self.atualizar_altura(Z)
        self.atualizar_altura(Y)

        return Y
    
    def imprimir_em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            if no.esquerda is not None:
                self.imprimir_em_ordem(no.esquerda)
            print(f"{no.valor}(h:{no.altura})", end=" ")
            if no.direita is not None:
                self.imprimir_em_ordem(no.direita)



if __name__ == "__main__":
    # Instanciar a Árvore Binária
    arvore = Arvore()

    sequencia = [10,5,15,3,1,20,25,18]
    print("Inserindo valores na árvore AVL:")
    for valor in sequencia:
        print(f"\nInserindo {valor}...")
        arvore.inserir(valor)
        print("Árvore atual (em ordem):", end=" ")
        arvore.imprimir_em_ordem()
        print()
    
    print("\n\nÁrvore final:")
    arvore.imprimir_em_ordem()
    print(f"\nAltura da raiz: {arvore.raiz.altura}")
    
    # Testando busca
    print("\nTestando busca:")
    for valor in [5, 25, 100]:
        resultado = arvore.buscar(valor)
        print(f"Buscar {valor}: {'Encontrado' if resultado else 'Não encontrado'}")
