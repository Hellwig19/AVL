def rotacao_direita(no): 
    Z = no  
    Y = Z.filho_esquerda   
    T3 = Y.filho_direita

    Y.filho_direita = Z
    Z.filho_esquerda = T3
    atualizar_altura(Z)
    atualizar_altura(Y)
    
    return Y

def rotacao_esquerda(no):
    Z = no  
    Y = Z.filho_direita 
    T2 = Y.filho_esquerda

    Y.filho_esquerda = Z
    Z.filho_direita = T2
    atualizar_altura(Z)
    atualizar_altura(Y)

    return Y
no_desbalanceado_Z = Node(10)
nova_raiz = rotacao_direita(no_desbalanceado_Z) 
nova_raiz1 = rotacao_esquerda(no_desbalanceado_Z)