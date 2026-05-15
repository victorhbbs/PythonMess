import random

def espada():
    return random.randint(1, 10)    

def espada_defendida():
    return random.randint(1, 5)  

def cura():
    return random.randint(1, 6)

def pause(msg="(ENTER)"):
    input(msg)

vida = 50
vida_inimigo = 50
decisao = 0

pause('E o combate se inicia...')

iniciativa_jogador = random.randint(1, 20)
iniciativa_inimigo = random.randint(1, 20)

pause(f"Sua iniciativa é {iniciativa_jogador}...")
pause(f"A iniciativa da criatura é {iniciativa_inimigo}...")

if iniciativa_jogador > iniciativa_inimigo:

    while True:
        print('O que deseja fazer contra a criatura?')

        decisao = int(input('1 - Atacar | 2 - Defender | 3 - Curar: '))

        if decisao == 1:
            pause('Você ataca a criatura com sua espada...')
            dano = espada()
            vida_inimigo -= dano
            pause(f'Você causou {dano} de dano. Inimigo agora com {vida_inimigo} de vida.')
            if vida_inimigo <= 0:
                print('A criatura foi derrotada!')
                print('Parabéns, você venceu!')
                break

            pause('A criatura ataca você com uma espada...')
            dano = espada()
            vida -= dano
            pause(f'Você recebeu {dano} de dano. Agora está com {vida} de vida.')
            if vida <= 0:
                print('Você foi derrotado!')
                print('Você perdeu')
                break

        if decisao == 2:
            pause('Você se defende com seu escudo...')

            pause('A criatura ataca você com uma espada...')
            dano = espada_defendida()
            vida -= dano
            pause(f'Você se defendeu e recebeu {dano} de dano. Agora está com {vida} de vida.')
            if vida <= 0:
                print('Você foi derrotado!')
                print('Você perdeu')
                break

        if decisao == 3:
            pause('Você se cura com uma poção...')
            ganho = cura()
            vida += ganho
            pause(f'Você recuperou {ganho} de vida. Agora está com {vida}.')

            pause('A criatura ataca você com uma espada...')
            dano = espada()
            vida -= dano
            pause(f'Você recebeu {dano} de dano. Agora está com {vida} de vida.')
            if vida <= 0:
                print('Você foi derrotado!')
                print('Você perdeu')
                break

else:

    while True:


        print('O que deseja fazer contra a criatura?')
        decisao = int(input('1 - Atacar | 2 - Defender | 3 - Curar: '))

        if decisao == 1:
            pause('Você ataca a criatura com sua espada...')
            dano = espada()
            vida_inimigo -= dano
            pause(f'Você causou {dano} de dano. Inimigo agora com {vida_inimigo} de vida.')
            if vida_inimigo <= 0:
                print('A criatura foi derrotada!')
                print('Parabéns, você venceu!')
                break

        if decisao == 2:
            pause('Você se defende com seu escudo...')
            pause('A criatura ataca você com uma espada...')
            dano = espada_defendida()
            vida -= dano
            pause(f'Você se defendeu e recebeu {dano} de dano. Agora está com {vida} de vida.')
            if vida <= 0:
                print('Você foi derrotado!')
                print('Você perdeu')
                break

        if decisao == 3:
            pause('Você se cura com uma poção...')
            ganho = cura()
            vida += ganho
            pause(f'Você recuperou {ganho} de vida. Agora está com {vida}.')

