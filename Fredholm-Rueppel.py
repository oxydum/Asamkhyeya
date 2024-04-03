import numpy as np

def kernel(x, y):
    # Définir ici le noyau K(x, y)
    return np.exp(-x * y)

def solve_fredholm_rueppel(a, b, n, max_iterations=100, tolerance=1e-6):
    # Discrétisation de l'intervalle [a, b]
    x = np.linspace(a, b, n)

    # Initialisation de la solution
    u = np.ones(n)

    # Itérations fonctionnelles
    for _ in range(max_iterations):
        u_new = np.zeros(n)
        for i in range(n):
            for j in range(n):
                u_new[i] += kernel(x[i], x[j]) * u[j]
        u_new = u_new / np.max(u_new)  # Normalisation
        if np.linalg.norm(u_new - u) < tolerance:
            break
        u = u_new

    return u

# Exemple d'utilisation
a = 0.0
b = 1.0
n = 100
solution = solve_fredholm_rueppel(a, b, n)

# Affichage de la solution
import matplotlib.pyplot as plt
plt.plot(np.linspace(a, b, n), solution)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Solution de l\'équation de Fredholm-Rueppel')
plt.show()
