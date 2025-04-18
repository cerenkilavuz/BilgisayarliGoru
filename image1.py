import numpy as np
import matplotlib.pyplot as plt

size = 512
x = np.linspace(0, 1, size)
y = np.linspace(0, 1, size)
X, Y = np.meshgrid(x, y)

# Ana desenin benzeri: sinüs bazlı, dalgalı yapı
def base_pattern(X, Y, phase=0):
    return np.sin(10 * np.pi * X + 5 * np.cos(5 * np.pi * Y) + phase)

# Renkli hale getirmek için faz kaymaları ile üç kanal
R = (base_pattern(X, Y, 0) + 1) / 2
G = (base_pattern(X, Y, 2*np.pi/3) + 1) / 2
B = (base_pattern(X, Y, 4*np.pi/3) + 1) / 2

# Pastel etki için renkleri yumuşat
R = R * 0.6 + 0.3
G = G * 0.5 + 0.5
B = B * 0.2 + 0.7

rgb_image = np.stack([R, G, B], axis=-1)

plt.figure(figsize=(6, 6))
plt.imshow(rgb_image)
plt.axis("off")
plt.tight_layout()
plt.show()
