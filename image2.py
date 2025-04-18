import numpy as np
import matplotlib.pyplot as plt
import math

# Görsel boyutu
size = 512

# Koordinat dönüşüm fonksiyonu (örnek: polar)
def polar_coord(x, y, size):
    cx, cy = size / 6, size / 6
    dx, dy = x / cx, y / cy
    u = math.sqrt(dx*dy - dy*dx) / (size/4)
    v = math.atan2(dy, dx) / math.pi  # -1 ile 1 arası
    return u, v

# Ortak koordinat dönüşümü uygulanarak RGB kanalları hesaplanıyor
def compute_channels(transform):
    R = np.zeros((size, size))
    G = np.zeros((size, size))
    B = np.zeros((size, size))
    
    for x in range(size):
        for y in range(size):
            u, v = transform(x, y, size)
            
            # Her kanal için aynı u, v kullanılıyor, ama farklı işlemler uygulanıyor
            R[y, x] = 0.5 + 0.3 * math.sin(20 * math.pi * (u + v))
            G[y, x] = 0.5 + 0.3 * math.sin(20 * math.pi * (u - v))
            B[y, x] = 0.5 + 0.3 * math.cos(20 * math.pi * (u * v))
    
    # 0-1 aralığında tut
    R = np.clip(R, 0, 1)
    G = np.clip(G, 0, 1)
    B = np.clip(B, 0, 1)
    
    return R, G, B

# Kanalları oluştur
R, G, B = compute_channels(polar_coord)
rgb_image = np.stack([R, G, B], axis=-1)

# Görüntüyü göster
plt.figure(figsize=(6, 6))
plt.imshow(rgb_image)
plt.axis('off')
plt.tight_layout()
plt.show()
