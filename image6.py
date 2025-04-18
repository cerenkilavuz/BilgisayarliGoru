import numpy as np
import matplotlib.pyplot as plt

# Fibonacci dizisi (biraz uzun)
def fibonacci(n):
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

size = 512
fib = fibonacci(30)  # İlk 30 Fibonacci sayısı

# Dalgalar için bir grid
x = np.linspace(0, 1, size)
y = np.linspace(0, 1, size)
X, Y = np.meshgrid(x, y)

# Yüzey: uzaklığa göre fibonacci tabanlı dalga
r = np.sqrt((X)**2 + (Y)**2)

# Fibonacci dizisinden alınan bazı harmonik bileşenler
F1 = fib[5] * 0.5 * r
F2 = fib[7] * 0.6 * r
F3 = fib[9] * 0.7 * r

# RGB kanallarını oluştur (sin/cos yok!)
R = np.mod(F1, 1)
G = np.mod(F2 * 0.8, 1)
B = np.mod(F3 * 0.6, 1)

# RGB olarak birleştir
rgb_image = np.stack([R, G, B], axis=-1)

# Görüntüyü çiz
plt.figure(figsize=(6, 6))
plt.imshow(rgb_image)
plt.axis('off')
plt.title("Yumuşak Fibonacci RGB Dalgası", fontsize=14)
plt.tight_layout()
plt.show()
