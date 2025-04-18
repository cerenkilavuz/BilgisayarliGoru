import numpy as np
import matplotlib.pyplot as plt

size = 512
x = np.linspace(-1, 1, size)
y = np.linspace(-1, 1, size)
X, Y = np.meshgrid(x, y)

# Girdap için temel değişkenler
distance = np.sqrt(X**2 + Y**2)
angle = np.arctan2(Y, X)

# 🔁 Kozmik Girdap: spiral desen
spiral = np.sin(50 * distance + 3 * angle)

# 🌈 Plazma Efekti: renkli sinüs dalgaları
plasma = np.sin(X * 15) + np.sin(Y * 15) + np.sin((X + Y) * 15)

# 💫 Karıştır ve normalize et
mix = spiral * 1 + plasma * 0.5

# Renk kanalları (farklı fazlarla kaydır)
R = np.sin(mix + 2*np.pi/3) * 0.5 + 0.5
G = np.sin(mix + 4*np.pi/3) * 0.5 + 0.5
B = np.sin(mix + 6*np.pi/3) * 0.5 + 0.5

# Hafif parlaklık ekle (girdap merkezine yakın)
glow = np.exp(-3 * distance**2)
R += 0.2 * glow
G += 0.2 * glow
B += 0.2 * glow

# Kırp ve birleştir
rgb_image = np.clip(np.stack([R, G, B], axis=-1), 0, 1)

# Görselleştir
plt.figure(figsize=(8, 8))
plt.imshow(rgb_image)
plt.axis('off')
plt.tight_layout()
plt.show()
