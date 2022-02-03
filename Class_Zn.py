# -*- coding: utf-8 -*-
"""
Com este ficheiro Python, a ideia é construir os inteiros módulo n.
"""

# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================

def gcdxy(a, b):
    """
    Esta função calcula o máximo divisor comum entre a e b 
    de forma a resolver a equação ax + by = mdc(a,b).
    Visto em: https://www.geeksforgeeks.org/python-program-
    for-basic-and-extended-euclidean-algorithms-2/
    Argumentos:
        - a,b - int
    Devolve:
        - gcd, x, y - int
    Exemplo:
        gcdxy(15,8)
            >> (1, -1, 2)
    """
    if a == 0 :   
        return b,0,1         
    gcd,x_i,y_i = gcdxy(b%a, a)  
    x,y = y_i - (b//a) * x_i, x_i
    return gcd,x,y 

# =============================================================================
# CONSTRUÇÃO DA CLASSE
# =============================================================================

class Zn:
    def __init__(self, m, N):
        """
        Inicializa a instância de Z/nZ. Toma dois argumentos m e N. N é o 
        módulo e "m" é o valor de Z_N que procuramos. 
        Uma instância de Z_N é um tuplo com o menor representante positivo
        na primeira coordenada e o módulo na segunda coordenada.
        """
        if not all([isinstance(x, int) for x in (m,N)]):
            raise TypeError(
                    """Foram introduzidos os números {} e {}, necessitamos 
                    que ambos os números sejam do tipo «int»""".format(m,N)
                    )
        self.mod = N    
        self.rep = m % self.mod
        
    def show(self):
        """
        Mostra a representação da instância enquanto elemento de Z/nZ.
        """
        return self.rep, self.mod
        
    def is_invertible(self):
        """
        Verifica se a instância é um elemento invertível de Z/nZ.
        """
        return gcdxy(self.rep, self.mod)[0] == 1
    
    def inverse(self):
        """
        Devolve o inverso da instância módulo N.
        """
        if not self.is_invertible():
            raise ValueError(
                    """Para se ter um inverso, é necessário que a instância
                    seja invertível.""")
        gcd,x,y = gcdxy(self.rep, self.mod)
        return self.__class__(x, self.mod)
        
    def soma(self, other):
        """
        Permite somar duas instâncias módulo N.
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Só podemos somar duas instâncias da mesma classe.")
        return self.__class__(self.rep + other.rep, self.mod)
    
    def __add__(self,other):
        """
        """
        return self.soma(other)
    
    def produto(self, other):
        """
        Permite somar duas instâncias módulo N.
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                    """Só podemos multiplicar duas instâncias da mesma classe."""
                    )
        return self.__class__(self.rep * other.rep, self.mod)
    
    def __mul__(self,other):
        """
        """
        return self.produto(other)
