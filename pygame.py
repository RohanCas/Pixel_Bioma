import pygame
import random

# Tamaño de pantalla
ANCHO, ALTO = 800, 600

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

class Animal:
    def __init__(self, x, y, color, tamano=20, velocidad=2):
        self.x = x
        self.y = y
        self.color = color
        self.tamano = tamano
        self.velocidad = velocidad
        self.direccion_x = random.choice([-1, 1])  # Dirección inicial aleatoria
        self.direccion_y = random.choice([-1, 1])

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x, self.y), self.tamano)

    def mover(self):
        # Actualizar la posición del animal
        self.x += self.direccion_x * self.velocidad
        self.y += self.direccion_y * self.velocidad

        # Rebotar si se llega a los bordes de la pantalla
        if self.x <= 0 or self.x >= ANCHO:
            self.direccion_x *= -1
        if self.y <= 0 or self.y >= ALTO:
            self.direccion_y *= -1

    def cazar(self, presa):
        # Verificar la distancia entre este animal y la presa
        distancia = ((self.x - presa.x) ** 2 + (self.y - presa.y) ** 2) ** 0.5
        if distancia < self.tamano + presa.tamano:  # Si la presa está cerca, se 'come' a la presa
            return True
        return False

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Simulador de Caza')

    reloj = pygame.time.Clock()
    ejecutando = True

    # Crear dos animales de diferentes colores
    animal_1 = Animal(100, 100, ROJO)
    animal_2 = Animal(400, 300, AZUL)

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
        
        # Mover los animales
        animal_1.mover()
        animal_2.mover()

        # Dibujar animales en la pantalla
        pantalla.fill(BLANCO)
        animal_1.dibujar(pantalla)
        animal_2.dibujar(pantalla)

        # Intento de caza: animal_1 intentará cazar a animal_2
        if animal_1.cazar(animal_2):
            print("¡Animal 1 cazó a Animal 2!")
            # Podrías implementar alguna acción o lógica después de la caza aquí

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
