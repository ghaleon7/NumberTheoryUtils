# -*- coding: utf-8 -*-
"""
Este ficheiro Python serve para construir uma classe chamada Zn para me 
familiarizar com a sintaxe Python e com a construção de classes nela.
A ideia é construir uma classe correspondente às classes de congruência
módulo n. 
"""
#class MyClass:
#    # construtor
#    def __init__(self, x):
#        """
#        """
#        if not isinstance(x, str):
#            raise TypeError()
#        self.a = x + '_attr'
#     
#    # podemos entender o "self" como apontando para a instância em causa quando 
#    # o método é chamado
#    def has_attr(self, y):
#        """
#        """
#        if not y.endswith('_attr'):
#            raise ValueError()
#        return self.a == y
#
## cria uma instância da classe MyClass, por trás é chamado o método __init__   
#inst = MyClass('xpto')
## podemos aceder ao atributo "a"
#print(inst.a)
#
## os seguintes são equivalentes, normalmente usamos o primeiro
#result = inst.has_attr('aaa_attr')
#result1 = MyClass.has_attr(inst, 'aaa_attr')

# =============================================================================
# 
# =============================================================================
from math import gcd

class Zn:
    N=19
    def __init__(self, m):
        """
        """
        if not isinstance(m, int):
            raise TypeError("Precisamos de inteiros")
        self.k = m % self.N
        
    def is_invertible(self):
        """
        Verifica se a instância é um elemento invertível de Zn.
        """
        return gcd(self.k, self.N) == 1
    
    def inverse(self):
        """
        
        """
        if not self.is_invertible():
            raise ValueError("Precisamos de invertíveis")
        else:
            for x in range(1, self.N) : 
                if ((self.k * x) % self.N == 1) : 
                    return Zn(x)
        
    def soma(self, other):
        """
        
        """
        if not isinstance(other, Zn):
            raise TypeError()
        result = Zn(self.k + other.k)
        return result
    
    def produto(self, other):
        """
        
        """
        if not isinstance(other, Zn):
            raise TypeError()
        result = Zn(self.k * other.k)
        return result


inst = Zn(19)
inst2 = Zn(39)
print(inst.k)
inst.is_invertible()
lista_inversos = [Zn(i).inverse().k for i in range(1,Zn.N)]
print(lista_inversos)
print(inst.soma(inst2).k)
print(inst.produto(inst2).k)

