"""
Baixar imagens reais de perfumes do Pexels (CC0 - uso livre)
para o projeto Wagner Perfumes - Promocao Dia das Maes
"""

import os, requests, json

BASE = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')

def download(url, nome, pasta='produtos'):
    path = os.path.join(BASE, pasta, nome)
    if os.path.exists(path):
        print(f"  [OK] {nome} ja existe")
        return path
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
            print(f"  [OK] {nome} ({len(r.content)} bytes)")
            return path
        else:
            print(f"  [ERR] {nome} - HTTP {r.status_code}")
    except Exception as e:
        print(f"  [ERR] {nome} - {e}")
    return None

# === IMAGENS DE PERFUMES (Pexels - fotos reais) ===
# URLs estaveis diretas de imagens CC0/Pexels
perfumes = [
    # Perfume 1 - classico feminino (rosa/dourado)
    ("https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_01.jpg"),
    # Perfume 2 - frasco elegante
    ("https://images.pexels.com/photos/28539061/pexels-photo-28539061.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_02.jpg"),
    # Perfume 3 - vidro classico
    ("https://images.pexels.com/photos/28538317/pexels-photo-28538317.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_03.jpg"),
    # Perfume 4 - moderno
    ("https://images.pexels.com/photos/6782678/pexels-photo-6782678.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_04.jpg"),
    # Perfume 5 - luxo dourado
    ("https://images.pexels.com/photos/6782684/pexels-photo-6782684.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_05.jpg"),
    # Perfume 6 - masculino escuro
    ("https://images.pexels.com/photos/22203227/pexels-photo-22203227.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_06.jpg"),
    # Perfume 7 - feminino claro
    ("https://images.pexels.com/photos/16056023/pexels-photo-16056023.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_07.jpg"),
    # Perfume 8 - premium
    ("https://images.pexels.com/photos/415127/pexels-photo-415127.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_08.jpg"),
    # Perfume 9 - classico
    ("https://images.pexels.com/photos/13210412/pexels-photo-13210412.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_09.jpg"),
    # Perfume 10 - nicho
    ("https://images.pexels.com/photos/4239016/pexels-photo-4239016.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_10.jpg"),
    # Perfume 11 - masculino
    ("https://images.pexels.com/photos/11219489/pexels-photo-11219489.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_11.jpg"),
    # Perfume 12 - unissex
    ("https://images.pexels.com/photos/10632722/pexels-photo-10632722.jpeg?auto=compress&cs=tinysrgb&w=600", "perfume_12.jpg"),
]

# Alternativas em caso de falha
fallbacks = [
    "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/4202932/pexels-photo-4202932.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/6604568/pexels-photo-6604568.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/4239010/pexels-photo-4239010.jpeg?auto=compress&cs=tinysrgb&w=600",
    "https://images.pexels.com/photos/4239016/pexels-photo-4239016.jpeg?auto=compress&cs=tinysrgb&w=600",
]

print("=== Baixando imagens de perfumes (Pexels CC0) ===")
for url, nome in perfumes[:8]:  # 8 primeiros
    download(url, nome)

# Preencher resto com fallbacks
import random
random.shuffle(fallbacks)
for i in range(8, 12):
    url = fallbacks[i - 8]
    nome = f"perfume_{i+1:02d}.jpg"
    download(url, nome)

# === BACKGROUNDS ===
print("\n=== Baixando backgrounds ===")
# Fundo texturizado quente
download("https://images.pexels.com/photos/1441030/pexels-photo-1441030.jpeg?auto=compress&cs=tinysrgb&w=1200", "bg_hero.jpg", "bg")
# Fundo dourado textura
download("https://images.pexels.com/photos/1887963/pexels-photo-1887963.jpeg?auto=compress&cs=tinysrgb&w=1200", "bg_dourado.jpg", "bg")

# === CATEGORIAS ===
print("\n=== Baixando imagens de categorias ===")
cats = [
    ("https://images.pexels.com/photos/22203227/pexels-photo-22203227.jpeg?auto=compress&cs=tinysrgb&w=400", "masculino.jpg"),
    ("https://images.pexels.com/photos/6782678/pexels-photo-6782678.jpeg?auto=compress&cs=tinysrgb&w=400", "feminino.jpg"),
    ("https://images.pexels.com/photos/10632722/pexels-photo-10632722.jpeg?auto=compress&cs=tinysrgb&w=400", "unissex.jpg"),
    ("https://images.pexels.com/photos/415127/pexels-photo-415127.jpeg?auto=compress&cs=tinysrgb&w=400", "premium.jpg"),
]
for url, nome in cats:
    download(url, nome, "categorias")

print("\nDownload concluido!")
