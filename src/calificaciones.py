def nota_teoria(nota1, nota2):
    return (nota1 + nota2) / 2

def nota_continua(nota1t, nota2t, nota3t, nota4t, nota1p, nota2p):
    return ((((nota1t + nota2t)/2)*0.2 + nota1p*0.8) + (((nota3t + nota4t)/2)*0.2 + nota2p*0.8))/2

def solicita_notas():
    nombre = input("Introduzca su nombre: ")
    nota1t = float(input("Introduzca la nota de su examen teórico 1 (0 si no se ha presentado): "))
    nota2t = float(input("Introduzca la nota de su examen teórico 2 (0 si no se ha presentado): "))
    nota3t = float(input("Introduzca la nota de su examen teórico 3 (0 si no se ha presentado): "))
    nota4t = float(input("Introduzca la nota de su examen teórico 4 (0 si no se ha presentado): "))
    nota1p = float(input("Introduzca la nota de su examen práctico 1 (0 si no se ha presentado): "))
    nota2p = float(input("Introduzca la nota de su examen práctico 2 (0 si no se ha presentado): "))
    print(f"Hola {nombre}")
    print("Tus notas del primer cuatrimestre son:")
    print(f"Teoría: {(nota1t+nota2t)/2}. Práctica: {nota1p}. Cuatrimestre: {((nota1t+nota2t)/2)*0.2 + nota1p*0.8 }")
    print("Tus notas del segundo cuatrimestre son:")
    print(f"Teoría: {(nota3t+nota4t)/2}. Práctica: {nota2p}. Cuatrimestre: {((nota3t+nota4t)/2)*0.2 + nota2p*0.8 }")
    print(f"Tu nota final de la asignatura es: {((((nota1t+nota2t)/2)*0.2+nota1p*0.8)+((nota3t+nota4t)/2)*0.2 + nota2p*0.8)/2}")