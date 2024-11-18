from calificaciones import *

def test_nota_teoria(nota1, nota2):
    resultado = nota_teoria(nota1, nota2)
    print(resultado)

def test_nota_continua(nota1t, nota2t, nota3t, nota4t, nota1p, nota2p):
    resultado = nota_continua(nota1t, nota2t, nota3t, nota4t, nota1p, nota2p)
    print(resultado)

def test_solicita_notas():
    solicita_notas()

if __name__ == '__main__':
#    test_nota_teoria(9.1, 7.2)
#    test_nota_teoria(4.0, 6.0)
#    test_nota_teoria(4.0, 3.0)
#    test_nota_teoria(0.0, 3.0)
#    test_nota_teoria(9.0, 0.0)
#    test_nota_teoria(0.0, 0.0)
#     test_nota_continua(9.6, 9.9, 10.0, 9.8, 9.7, 9.5)
#     test_nota_continua(4.4, 4.9, 5.1, 4.7, 4.6, 4.8)
#     test_nota_continua(4.0, 6.0, 4.0, 3.0, 5.0, 0.0)
#     test_nota_continua(9.0, 0.0, 4.0, 3.0, 4.5, 0.0)
    test_solicita_notas()