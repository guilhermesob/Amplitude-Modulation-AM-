import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da onda portadora 
A_c = 1.0  # Amplitude da onda portadora
f_c = 10.0  # Frequência da onda portadora (Hz)

# Parâmetros do sinal de informação
f_m = 2.0  # Frequência do sinal de informação (Hz)

# Tempo de simulação
t = np.linspace(0, 1, 1000, endpoint=False)

# Sinal de informação (seno)
m = np.sin(2 * np.pi * f_m * t)

# Onda portadora
c = A_c * np.sin(2 * np.pi * f_c * t)

# Sinal modulado em amplitude
s = (1 + m) * c

# Demodulação do sinal modulado usando detecção de envelope
envelope = np.abs(s)

def moving_average(data, window_size):
    """
    Implementa um filtro de média móvel simples
    """
    window = np.ones(window_size) / window_size
    return np.convolve(data, window, mode='same')

# Aplicando a média móvel para suavizar o sinal demodulado
window_size = 50  # Ajuste este valor para controlar a suavização
demodulated_signal = moving_average(envelope, window_size)

# Plotando os sinais
plt.figure(figsize=(12, 8))

# Sinal de informação original
plt.subplot(4, 1, 1)
plt.plot(t, m, label='Sinal de Informação Original')
plt.title('Demodulação em Amplitude')
plt.ylabel('Amplitude')
plt.legend()

# Onda portadora
plt.subplot(4, 1, 2)
plt.plot(t, c, label='Onda Portadora')
plt.ylabel('Amplitude')
plt.legend()

# Sinal Modulado
plt.subplot(4, 1, 3)
plt.plot(t, s, label='Sinal Modulado')
plt.ylabel('Amplitude')
plt.legend()

# Sinal Demodulado (após detecção de envelope)
plt.subplot(4, 1, 4)
plt.plot(t, demodulated_signal, label='Sinal Demodulado (Envelope)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()