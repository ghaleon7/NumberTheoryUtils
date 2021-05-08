# -*- coding: utf-8 -*-
"""
Este método factoriza números inteiros usando o método de Fermat. 
A ideia é escrever cada número como uma diferença de quadrados. 
"""
from math import sqrt, floor
from numpy import cbrt

def factorizar_fermat(n):
    """
    Esta função factoriza números inteiros usando a identidade
        n = x**2-y**2 = (x+y)*(x-y)
    Argumentos: 
        n - int
    
    """
    # Mudamos o sinal ao número
    n = abs(n)
    if not isinstance(n,int):
        raise TypeError('Precisamos de um número inteiro')
    elif sqrt(n).is_integer():
        print('Este número é múltiplo de {}'.format(sqrt(n)))
        return 
    i = floor(sqrt(n)) + 1
    while i < n:
        m = i**2 - n
        if sqrt(m).is_integer(): #Este método verifica se um dado float é um inteiro
            if i+sqrt(m) != n:
                return 'Este número é múltiplo de {}'.format(int(i+sqrt(m))) +\
                        ' e usámos {} iterações'.format(i - floor(sqrt(n)))
            else:
                #Serve para ver se um número é primo
                return 'Número primo, verificado com {} iterações'.format(i) 
        else:
            i+=1
            
def factorizar_lehman(n):
    """
    Esta função melhora a função factorizar_fermat, pois usa o melhoramento
    de Lehman sobre o método de Fermat.
    Argumentos:
        - n - int
    """
    # Mudamos o sinal ao número
    n = abs(n)
    if not isinstance(n,int):
        raise TypeError('Precisamos de um número inteiro')
    elif sqrt(n).is_integer():
        print('Este número é múltiplo de {}'.format(sqrt(n)))
        return 
    div_limsup = cbrt(n)
    multiplier_limsup = cbrt(n)
    pass
    