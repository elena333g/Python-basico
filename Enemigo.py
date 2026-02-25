class Enemigo:
    def __init__(self, tipo_enemigo, puntos_energia=10, ataque=1):
        self.tipo_enemigo = tipo_enemigo
        self.puntos_energia = puntos_energia
        self.ataque = ataque

    def hablar(self):
        print("El enemigo hace un sonido extraño...")