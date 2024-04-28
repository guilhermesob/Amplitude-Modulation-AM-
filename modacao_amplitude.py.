import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da onda portadora
A_c = 1.0 # Amplitude da onda portadora
f_c = 10.0 # Frequência da onda portadora (Hz)
T = 1.0 / f_c # Período da onda portadora (s)

# Parâmetros do sinal de informação
f_m = 2.0 # Frequência do sinal de informação (Hz)
T_m = 1.0 / f_m # Período do sinal de informação (s)

# Tempo de simulação
t = np.linspace(0, 1, 1000, endpoint=False)

# Sinal de informação
m = np.sin(2 * np.pi * f_m * t)

# Onda portadora
c = A_c * np.sin(2 * np.pi * f_c * t)

# Sinal modulado em amplitude
s = A_c * np.sin(2 * np.pi * f_c * t + np.pi * m)

# Plotando os sinais
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, m, label='Sinal de Informação')
plt.title('Modulação em Amplitude')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, c, label='Onda Portadora')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, s, label='Sinal Modulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
