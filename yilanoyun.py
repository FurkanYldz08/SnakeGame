import pygame
import time
import random

pygame.init()

# Renkler
beyaz = (255, 255, 255)
yeşil = (0, 255, 0)
kırmızı = (213, 50, 80)
mavi = (50, 153, 213)
siyah = (0, 0, 0)

# Ekran boyutları
genişlik = 800
yükseklik = 600

# Pencereyi oluştur
pencere = pygame.display.set_mode((genişlik, yükseklik))
pygame.display.set_caption("Yılan Oyunu")

# Yılanın özellikleri
yılan_blok = 10
yılan_hızı = 15

# Yazı tipi
font_style = pygame.font.SysFont("bahnschrift", 25)
skor_font = pygame.font.SysFont("comicsansms", 35)

# Skor gösterme
def skor_goster(skor):
    value = skor_font.render("Skor: " + str(skor), True, siyah)
    pencere.blit(value, [0, 0])

# Yılanı çizme
def yılan(yılan_blok, yılan_lista):
    for x in yılan_lista:
        pygame.draw.rect(pencere, yeşil, [x[0], x[1], yılan_blok, yılan_blok])

# Mesaj yazma
def mesaj_yaz(text, color):
    mes = font_style.render(text, True, color)
    pencere.blit(mes, [genişlik / 6, yükseklik / 3])

# Oyun döngüsü
def oyun():
    oyun_bitti = False
    oyun_kapanması = False

    x1 = genişlik / 2
    y1 = yükseklik / 2

    x1_hız = 0
    y1_hız = 0

    yılan_lista = []
    uzunluk = 1

    yem_x = round(random.randrange(0, genişlik - yılan_blok) / 10.0) * 10.0
    yem_y = round(random.randrange(0, yükseklik - yılan_blok) / 10.0) * 10.0

    while not oyun_bitti:

        while oyun_kapanması:
            pencere.fill(mavi)
            mesaj_yaz("Oyun Bitti! 'Q' çıkış için, 'C' yeniden başlatmak için.", kırmızı)
            skor_goster(uzunluk - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oyun_bitti = True
                    oyun_kapanması = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        oyun_bitti = True
                        oyun_kapanması = False
                    if event.key == pygame.K_c:
                        oyun()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_hız = -yılan_blok
                    y1_hız = 0
                elif event.key == pygame.K_RIGHT:
                    x1_hız = yılan_blok
                    y1_hız = 0
                elif event.key == pygame.K_UP:
                    y1_hız = -yılan_blok
                    x1_hız = 0
                elif event.key == pygame.K_DOWN:
                    y1_hız = yılan_blok
                    x1_hız = 0

        if x1 >= genişlik or x1 < 0 or y1 >= yükseklik or y1 < 0:
            oyun_kapanması = True
        x1 += x1_hız
        y1 += y1_hız
        pencere.fill(mavi)
        pygame.draw.rect(pencere, siyah, [yem_x, yem_y, yılan_blok, yılan_blok])
        yılan_kafa = []
        yılan_kafa.append(x1)
        yılan_kafa.append(y1)
        yılan_lista.append(yılan_kafa)
        if len(yılan_lista) > uzunluk:
            del yılan_lista[0]

        for x in yılan_lista[:-1]:
            if x == yılan_kafa:
                oyun_kapanması = True

        yılan(yılan_blok, yılan_lista)
        skor_goster(uzunluk - 1)

        pygame.display.update()

        if x1 == yem_x and y1 == yem_y:
            yem_x = round(random.randrange(0, genişlik - yılan_blok) / 10.0) * 10.0
            yem_y = round(random.randrange(0, yükseklik - yılan_blok) / 10.0) * 10.0
            uzunluk += 1

        pygame.time.Clock().tick(yılan_hızı)

    pygame.quit()
    quit()

# Oyunu başlat
oyun()
