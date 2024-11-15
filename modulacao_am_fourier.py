import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
t = np.linspace(0, 1, 1000)  # Vetor de tempo de 0 a 1 segundo
f_portadora = 50  # Frequência da portadora em Hz
f_mensagem = 5    # Frequência do sinal de mensagem em Hz

# Criar sinais
portadora = np.sin(2 * np.pi * f_portadora * t)
mensagem = np.sin(2 * np.pi * f_mensagem * t)

# Modulação AM
sinal_modulado = portadora * (1 + mensagem)

# Análise de Fourier usando FFT
freq = np.fft.fftfreq(len(t), t[1]-t[0])
fft_modulado = np.fft.fft(sinal_modulado)

# Plotagem dos resultados
plt.figure(figsize=(12, 8))

# Sinal no domínio do tempo
plt.subplot(3, 1, 1)
plt.plot(t, mensagem)
plt.title('Sinal de Mensagem')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, sinal_modulado)
plt.title('Sinal Modulado AM')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

# Espectro de frequência
plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(fft_modulado))
plt.title('Espectro de Frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.xlim(-100, 100)  # Limitando a visualização do espectro

plt.tight_layout()
plt.show()