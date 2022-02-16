# -*- coding: utf-8 -*-
"""
Este método factoriza números inteiros usando o método de Fermat. 
A ideia é escrever cada número como uma diferença de quadrados. 
"""
from math import sqrt, floor

def factorizar_fermat(n):
    """
    Esta função factoriza números inteiros usando a identidade
        n = x**2-y**2 = (x+y)*(x-y)
    Argumentos: 
        n - int
    """
    # Mudamos o sinal ao número
    n = abs(n)
    sq = sqrt(n)
    if not isinstance(n,int):
        raise TypeError('Precisamos de um número inteiro')
    elif sq.is_integer():
        return n,sq,sq
    i = floor(sq) + 1
    while i < n:
        m = i**2 - n
        #Esta linha verifica se um dado float é um inteiro
        if sqrt(m).is_integer(): 
            if i+sqrt(m) != n:
                return n, int(i+sqrt(m)), int(n//(i+sqrt(m)))
            else:
                #Serve para ver se um número é primo
                return n, n, 1 
        else:
            i+=1