def metodo_gauss_seidel(A, b, tolerancia=1e-10, max_iter=100):
    n = len(A)
    x = [0.0 for _ in range(n)]  # Aproximación inicial

    for iteracion in range(max_iter):
        x_nuevo = x.copy()

        for i in range(n):
            if A[i][i] == 0:
                return "Error: división por cero en la diagonal. Gauss-Seidel no puede aplicarse."

            suma1 = sum(A[i][j] * x_nuevo[j] for j in range(i))
            suma2 = sum(A[i][j] * x[j] for j in range(i + 1, n))

            x_nuevo[i] = (b[i] - suma1 - suma2) / A[i][i]

        # Verificar convergencia
        error = max(abs(x_nuevo[i] - x[i]) for i in range(n))
        if error < tolerancia:
            return x_nuevo  # Solución encontrada

        x = x_nuevo

    return "El método de Gauss-Seidel no converge tras {} iteraciones.".format(max_iter)

# -----------------------------
# Ejemplo de uso

A = [
    [3, -1, 1],
    [1, 2, 2],
    [2, -3, 4]
]

b = [10, 11, 5]

resultado = metodo_gauss_seidel(A, b)

# Mostrar resultados
if isinstance(resultado, list):
    for i, val in enumerate(resultado):
        print(f"x{i+1}: {val}")
else:
    print(resultado)
