def metodo_jacobi(A, b, tolerancia=1e-10, max_iter=100):
    n = len(A)
    x = [0.0 for _ in range(n)]  # Aproximación inicial (vector nulo)
    x_anterior = x.copy()

    for iteracion in range(max_iter):
        for i in range(n):
            if A[i][i] == 0:
                return "Error: división por cero en la diagonal. Jacobi no aplica."

            suma = sum(A[i][j] * x_anterior[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / A[i][i]

        # Verificar convergencia (norma del cambio)
        error = max(abs(x[i] - x_anterior[i]) for i in range(n))
        if error < tolerancia:
            return x  # Solución encontrada

        x_anterior = x.copy()

    return "El método de Jacobi no converge tras {} iteraciones.".format(max_iter)

# -----------------------------
# Ejemplo de uso

A = [
    [4, -2, 1],
    [2, 3, 2],
    [1, -1, 4]
]

b = [10, 12, 5]

resultado = metodo_jacobi(A, b)

# Mostrar resultados
if isinstance(resultado, list):
    for i, val in enumerate(resultado):
        print(f"x{i+1}: {val}")
else:
    print(resultado)
