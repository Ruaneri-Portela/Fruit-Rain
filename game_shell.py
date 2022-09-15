#!/usr/bin/python
# -*- coding: <encoding name>utf-8
import sys


def life_set():
    print("----------------------------------------------------")
    return (input("Insira um valor para configurar a quantida de vidas:"))


def speed_sety():
    print("----------------------------------------------------")
    return (input("Insira um valor para configurar o força do pulo do personagem:"))


def speed_setx():
    print("----------------------------------------------------")
    return (input("Insira um valor para configurar a velocidade de movimento do personagem:"))


def gravit_chr():
    print("----------------------------------------------------")
    return (input("Insira um valor para confihurar a força da gravidade sobre o personagem:"))


def jump_border():
    print("----------------------------------------------------")
    return (input("Insira um valor para configurar o teto de pulo:"))


def help():
    print("----------------------------------------------------")
    print("COMMAND LIST\nSCORE => SET GAME SCORE\nSPEEDX => CONTROL CHR SPEED IN X LINE\nSPEEDY => CONTROL CHR SPEED IN Y LINE\nGRAVIT_CHR => CONTROL FALL CHR SPEED IN LINE Y\nJUMP_LIMIT => CONTROL BORDER OF JUMP LIMIT\nGET_CHR_POS => GET X AND Y CHR POSITION ON  WINDOW'S GAME GRID\nTELEPORT => TELEPORT THE CHR TO X AND Y POSITIONS\nEXIT => END TERMINAL SHELL APLICATION\nCLOSE => FORCE END PY APLICATION")


def info(speedx, speedy, gravit_chri, jump_limiti):
    print("----------------------------------------------------")
    print("chr status:\nspeedx=", speedx, "\nspeedy=", speedy,
          "\ngravit_chr=", gravit_chri, "\njump_limit=", jump_limiti)


def get_chr_pos(a, b):
    print("----------------------------------------------------")
    print("Posição no eixo X=", a, "\nPosição no exio Y=", b)


def teleport():
    print("----------------------------------------------------")
    px = input("Insira uma cordenada X:")
    py = input("Insira uma cordenada Y:")
    return (px, py)


def scoref():
    print("----------------------------------------------------")
    return (input("Insira uma score valida: "))


def call_t(px, py, spy, spx, gs, jbl, life, score):
    print("FRUIT RAIN Terminal de Controle e Desenvolvimento \n(Em Construção Versão 0.17)\nRUANERI F PORTELA @ 2021\n----------------------------------------------------")
    call_txt = None
    speedx = spx
    speedy = spy
    gravit_chri = gs
    jump_limiti = jbl
    sc = score
    while True == True:
        call_txt = input("Insira um comando:")
        if call_txt == "speedx":
            speedx = speed_setx()
        elif call_txt == "speedy":
            speedy = speed_sety()
        elif call_txt == "gravit_chr":
            gravit_chri = gravit_chr()
        elif call_txt == "jump_limit":
            jump_limiti = jump_border()
        elif call_txt == "help":
            help()
        elif call_txt == "life_set":
            life = life_set()
        elif call_txt == "info":
            info(speedx, speedy, gravit_chri, jump_limiti)
        elif call_txt == "get_chr_pos":
            get_chr_pos(px, py)
        elif call_txt == "teleport":
            px, py = teleport()
        elif call_txt == "score":
            sc = scoref()
        elif call_txt == "close":
            sys.exit(
                "----------------------------------------------------\nEncerramento Forçado Pelo Usuario")
        elif call_txt == "exit":
            print("<RETURN TO GAME>")
            return (px, py, speedy, speedx, gravit_chri, jump_limiti, life, sc)
        else:
            print("Erro comando não encontrado, PARA AJUDAR USE 'HELP'")
