import numpy as np
import matplotlib.pyplot as plt

size = 512
x = np.linspace(0, 1, size)
y = np.linspace(0, 1, size)
X, Y = np.meshgrid(x, y)

distance_from_corner = np.sqrt( X **2 + Y **2)
distance_from_corner2 = np.sqrt( (X-0.3) **2 + (Y-0.3) **2)


R = np.sin(10 * np.pi * distance_from_corner + 2 * np.pi / 3) * np.cos(20 * np.pi * distance_from_corner2 )
G = np.sin(10 * np.pi * distance_from_corner + 4 * np.pi / 3) * np.cos(20 * np.pi * distance_from_corner2 )
B = np.sin(10 * np.pi * distance_from_corner + 6 * np.pi / 3) * np.cos(20 * np.pi * distance_from_corner2 )

R = R * 0.4 + 0.7
G = G * 0.5 + 0.5
B = B * 0.3 + 0.1

R_norm = (R - R.min()) / (R.max() - R.min())
G_norm = (G - G.min()) / (G.max() - G.min()) 
B_norm = (B - B.min()) / (B.max() - B.min()) # düzeltildi

rgb_image = np.stack([R_norm, G_norm, B_norm], axis=-1)

plt.figure(figsize=(6, 6))
plt.imshow(rgb_image)
plt.axis('off')
plt.tight_layout()
plt.show()
