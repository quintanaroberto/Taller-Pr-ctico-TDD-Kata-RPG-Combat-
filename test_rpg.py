from rpg import Personaje

def test_personaje_nace_con_estadisticas_correctas():
    # Arrange (Preparar)
    heroe = Personaje()
    
    # Assert (Verificar)
    assert heroe.hp == 1000
    assert heroe.nivel == 1
    assert heroe.esta_vivo == True

def test_personaje_recibe_dano():
    heroe = Personaje()
    enemigo = Personaje()

    # Act (Actuar)
    enemigo.atacar(heroe, dano=200)

    # Assert
    assert heroe.hp == 800

def test_personaje_muere_si_hp_llega_a_cero():
    heroe = Personaje()
    enemigo = Personaje()

    enemigo.atacar(heroe, dano=1500)

    assert heroe.hp == 0  # El HP no debe quedar en -500
    assert heroe.esta_vivo == False

def test_curar_personaje():
    curador = Personaje()
    aliado = Personaje()
    enemigo = Personaje()

    # Actuar
    enemigo.atacar(aliado, dano=200) # HP baja a 800
    curador.curar(aliado, cantidad=100)

    # Verificar
    assert aliado.hp == 900

def test_no_curar_mas_del_maximo():
    curador = Personaje()
    aliado = Personaje()
    enemigo = Personaje()

    enemigo.atacar(aliado, dano=100) # HP baja a 900
    curador.curar(aliado, cantidad=200) # Curar 200 debería topar en 1000

    assert aliado.hp == 1000