# -*- coding: latin1 -*-

def fraseInvert(frase):

    invert = frase.split()
    for i in xrange(len(invert)):
        invert[i] = invert[i][::-1]
    return ' '.join(invert)


frase = 'Estou no ciclo 2 fazendo Linguagem de Programacao'
print fraseInvert(frase)
