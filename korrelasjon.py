import numpy as np
import matplotlib.pyplot as plt

# Parametre
l1, l2 = 60, 50           # Lengdene til overarm og underarm
mu1, mu2 = 20, -30        # Gjennomsnittsverdier for vinklene i grader
sigma1, sigma2 = 1, 0.5   # Standardavvik for vinklene
n = 10000                 # Antall simuleringer

# Generer vinkler fra normalfordeling
theta1_samples = np.random.normal(mu1, sigma1, n)
theta2_samples = np.random.normal(mu2, sigma2, n)

# Beregn x og y for hver simulering
x_positions = l1 * np.cos(np.radians(theta1_samples)) + l2 * np.cos(np.radians(theta1_samples + theta2_samples))
y_positions = l1 * np.sin(np.radians(theta1_samples)) + l2 * np.sin(np.radians(theta1_samples + theta2_samples))

# Statistisk analyse
x_mean, x_std = np.mean(x_positions), np.std(x_positions)
y_mean, y_std = np.mean(y_positions), np.std(y_positions)
correlation = np.corrcoef(x_positions, y_positions)[0, 1]

# Plotting av resultatene
plt.figure(figsize=(10, 8))
plt.scatter(x_positions, y_positions, s=1, alpha=0.5, label='Simuleringer')
plt.axhline(y=y_mean, color='r', linestyle='--', label='Gjennomsnitt Y')
plt.axvline(x=x_mean, color='b', linestyle='--', label='Gjennomsnitt X')

# Tegne strippede linjer fra aksene til gjennomsnittet
plt.plot([x_mean, x_mean], [0, y_mean], color='g', linestyle=':', linewidth=1)
plt.plot([0, x_mean], [y_mean, y_mean], color='r', linestyle=':', linewidth=1)

plt.xlim(104.6, 106.5)  # Setter x-aksen fra 100 til 120
plt.ylim(2.75, 20)  # Setter x-aksen fra 100 til 120

# Legge til etiketter og tittel
plt.xlabel('x-posisjon', fontsize=15)
plt.ylabel('y-posisjon', fontsize=15)
plt.title('Simulert fordeling av endepunktsposisjoner', fontsize=16)
plt.legend()
plt.grid()

# Skrive ut statistisk analyse
print(f"Gjennomsnitt (x, y): ({x_mean:.2f}, {y_mean:.2f})")
print(f"Standardavvik (x, y): ({x_std:.2f}, {y_std:.2f})")
print(f"Korrelasjon mellom x og y: {correlation:.2f}")

# Vise plottet
plt.show()

