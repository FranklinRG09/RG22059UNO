import math

def biseccion(f, a, b, tol=1e-6, max_iter=1000):
    """
    Encuentra la raíz de una función no lineal por el método de la bisección en un rango (a, b)
    
    Parámetros:
        f: Función a evaluar (debe aceptar un valor float y devolver un float)
        a: Límite inferior del intervalo
        b: Límite superior del intervalo
        tol: Tolerancia del error permitido
        max_iter: Número máximo de iteraciones permitidas
        
    Retorna:
        float: Raíz aproximada
        int: Número de iteraciones realizadas
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Error: La función no cambia de signo en el intervalo proporcionado. No se puede aplicar el método de bisección.")

    print(f"Intervalo inicial: a = {a}, b = {b}, f(a) = {f(a)}, f(b) = {f(b)}")
    print("Comenzando iteraciones...\n")

    iteraciones = 0
    while (b - a) / 2 > tol and iteraciones < max_iter:
        xr = (a + b) / 2
        fxr = f(xr)
        print(f"Iteración #{iteraciones+1}: xr = {xr:.8f}, f(xr) = {fxr:.8f}")

        if fxr == 0:
            print("Se encontró una raíz exacta.")
            return xr, iteraciones + 1
        elif f(a) * fxr < 0:
            print(f"Actualizando b: de {b} a {xr}")
            b = xr
        else:
            print(f"Actualizando a: de {a} a {xr}")
            a = xr

        iteraciones += 1

    xr_final = (a + b) / 2
    print("\nMétodo finalizado.")
    return xr_final, iteraciones


# ----------------------------
# Ejemplo de uso con una función:

# Puedes cambiar esta función por cualquier otra que cumpla la condición f(a) * f(b) < 0
# Función: f(x) = x^3 - 4x^2 + 5x - 2
funcion = lambda x: x**3 - 4*x**2 + 5*x - 2

# Intervalo donde se sabe que hay una raíz (por inspección o gráfica)
a = 1
b = 2

try:
    raiz, iteraciones = biseccion(funcion, a, b)
    print(f"\nLa raíz aproximada es: {raiz:.6f}")
    print(f"Iteraciones realizadas: {iteraciones}")
except ValueError as e:
    print(e)
