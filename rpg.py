class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True

    def atacar(self, objetivo, dano):
        objetivo.hp -= dano
        if objetivo.hp <= 0:
            objetivo.hp = 0
            objetivo.esta_vivo = False

    def curar(self, objetivo, cantidad):
        if not objetivo.esta_vivo:
            return # Regla: Si está muerto, salimos del método sin hacer nada

        objetivo.hp += cantidad
        if objetivo.hp > 1000:
            objetivo.hp = 1000