
def solucion():
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    while True:
        print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia")
        nombre=input("Ingresa tu nombre: ").upper()
        materia=input("Ingresar materia: ").upper()
        n_0=float(input("Ingresa nota obtenida: "))
        p_0=int(input("Ingresar el porcentaje de la nota: "))
        suma=0
        suma=suma+p_0
        nota_acumulada=suma*n_0/100
        while p_0 <100 and suma<100:
            s="s"
            n="n"
            p=input("¿Faltan notas por añadir?: S/N ")
            if p == s:
                n_0=float(input("Ingresa nota obtenida: "))
                p_0=int(input("Ingresar el porcentaje de la nota: "))
                suma=suma+p_0
                nota_acumulada=suma*n_0/100
                if suma ==100 and nota_acumulada >3:
                    aprobacion="Aprobado"
                    print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
                    return solucion()
                elif suma ==100 and nota_acumulada <3:
                    aprobacion="Reprobado"
                    print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
                    return solucion()
                while suma > 100:
                    print("No mayor a 100")
                    n_0=float(input("Ingresa nota obtenida: "))
                    p_0=int(input("Ingresar el porcentaje de la nota: "))
                    suma=suma-p_0
                    if suma ==100 and nota_acumulada >3:
                        aprobacion="Aprobado"
                        print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
                        return solucion
                    elif suma ==100 and nota_acumulada <3:
                        aprobacion="Reprobado"
                        print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
                        return solucion()
            if p == n and nota_acumulada <3:
                aprobacion="Reprobado"
                print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
                return solucion()
            if p == n and nota_acumulada >=3:
                aprobacion="Aprobado"
                print(f'El estudiante {nombre} cursó la materia {materia} y obtuvo {nota_acumulada} resultando en {aprobacion}')
                return solucion()
