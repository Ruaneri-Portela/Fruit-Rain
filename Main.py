#!/usr/bin/python
# -*- coding: utf-8 -*-
from graphics import *
import game_shell
import simpleaudio as sa
import random
import sys
print("=CODE STARED")
def help():
    print("=HELP OPEN")
    helpwin=GraphWin(title="Help",width=1000,height=600,autoflush=True)
    BackgoundH=Image(Point(500,300),"ajuda_bmp.png")
    BackgoundH2=Image(Point(500,300),"ajuda_bmp2.png")
    BackgoundH3=Image(Point(500,300),"ajuda_bmp3.png")
    key1=None
    posj=3
    while key1 != "Escape":  
        if posj ==0:
            posj=posj+1
        if posj==2:
            BackgoundH2.draw(helpwin)
        if posj==1:
            BackgoundH3.draw(helpwin)
        if posj>=3:
            posj=0
            BackgoundH.draw(helpwin)
        if key1 == "a":
            posj=posj+1           
        key1=helpwin.getKey()
        BackgoundH.undraw()
        BackgoundH2.undraw()
        BackgoundH3.undraw()
    print("=RETURN TO BACK FUNCTION RESETED")
    helpwin.close()
def main(sef,sem,reset):
    print("=MAIN STARTED")
    while reset == True:
        versao="(Versão 1.0)"
        titulo="Fruit Rain "
        if sef !="":
         titulo=titulo+"(Sem efeitos sonoros) "
        if sem !="":
         titulo=titulo+"(Sem musica de fundo) "
        titulo=titulo+versao
        win=GraphWin(title=titulo,width=1000,height=600)
        score_data=gameback(win)  
        sef,reset,sem=interact(win,score_data,sef,sem)
    win.close()
    print("=RETURN TO GAME MAIN MENU")
    inicial(sef,sem,True)
def gameback(win):
    global hp_heat1,hp_heat2,hp_heat3,hp_heat4
    #----------------------Back Image---------------------------------------#
    gameback=Image(Point(500,300),"bitmap.png")
    gameback.draw(win)
    #----------------------Life Bar-----------------------------------------#
    hp_status=Image(Point(30,20),"bitmap1.png")
    hp_status.draw(win)
    hp_heat1=Image(Point(70,20),"bitmap3.png")
    hp_heat2=Image(Point(100,20),"bitmap3.png")
    hp_heat3=Image(Point(130,20),"bitmap3.png")
    hp_heat4=Image(Point(160,20),"bitmap3.png")
    hp_heat1.draw(win)
    hp_heat2.draw(win)
    hp_heat3.draw(win)
    hp_heat4.draw(win)
    #----------------------Score--------------------------------------------#
    score_status=Image(Point(950,20),"bitmap4.png")
    score_status.draw(win)
    score_data=Text(Point(880,20),"0")
    score_data.setSize(20)
    score_data.draw(win)
    print("=GAMEBACK OK!")
    return(score_data)
def interact(win,score_data,sef,sem):
    #----------------------Control Internal Var--------------------------#
    playst=False
    playst2=False
    speedx=120
    speedy=40
    gravit_s=4 
    up=4
    speedfl=1
    speedfall=1
    jump_border_line=485
    key=None
    v2=0
    score=0
    #----------------------Audio Data---------------------------------------#
    wave_object0=sa.WaveObject.from_wave_file('audio.wav')
    wave_object = sa.WaveObject.from_wave_file('audio2.wav')
    wave_object2 = sa.WaveObject.from_wave_file('audio3.wav')
    wave_object3 = sa.WaveObject.from_wave_file('audio4.wav')
    wave_object4 = sa.WaveObject.from_wave_file('audio5.wav')
    wave_object5 = sa.WaveObject.from_wave_file('audio6.wav')
    wave_object7 = sa.WaveObject.from_wave_file('audio7.wav')
    wave_object8 = sa.WaveObject.from_wave_file('audio8.wav')
    wave_object9 = sa.WaveObject.from_wave_file('audio9.wav')
    wave_object10 = sa.WaveObject.from_wave_file('audio10.wav')
    wave_object11 = sa.WaveObject.from_wave_file('audio11.wav')
    wave_object12= sa.WaveObject.from_wave_file('audio12.wav')
    wave_object13= sa.WaveObject.from_wave_file('audio13.wav')
    #----------------------Image Data----------------------------------------#
    pos=False # <- FALSE == left TURE == right (Referente a direção do personagem)
    gameover=Image(Point(500,300),"bitmap7.png")
    gamepause=Image(Point(500,300),"bitmap8.png")
    fruit1=Image(Point(0,701),"fruit1.png") 
    fruit2=Image(Point(0,701),"fruit2.png")  
    fruit3=Image(Point(0,701),"fruit3.png") 
    fruit4=Image(Point(0,701),"fruit4.png") 
    fruit5=Image(Point(0,701),"fruit5.png") 
    fruit6=Image(Point(0,701),"fruit6.png") 
    fruit7=Image(Point(0,701),"fruit7.png") 
    fruit8=Image(Point(0,701),"fruit8.png") 
    fruit9=Image(Point(0,701),"fruit9.png") 
    fruit10=Image(Point(0,701),"fruit10.png") 
    fruit11=Image(Point(0,701),"fruit11.png") 
    objc1_pxy=Point(500,488)
    objc1=Image(objc1_pxy,"char1-2.png")
    objc1.draw(win)   
    #----------------------Other----------------------------------------------#
    score_data.setText(score)
    perm1,perm2,perm3,perm4,perm5,perm6=False,False,False,False,False,False
    print("=MAIN LOOP GAME STARTED")
    #----------------------Main Game Loop--------------------------------------#
    while key != "Escape":       
        if sem=="" and playst==False and score<50:
         playst=wave_object0.play()
        if score >=50:
         try:
            playst.stop()
         except:
             pass
         if sem=="" and playst2==False:
             playst2=wave_object13.play()
    #----------------------Drawing Controler-----------------------------------#
        draw=False
        while draw==False:
            freq1=random.randrange(0,20)
            if freq1==0 and (fruit1.getAnchor()).getY()>555:
                fruit1.undraw()
                fruit1=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(10,100))),"fruit1.png")
                fruit1.draw(win)
                draw=True
            if freq1==1 and (fruit2.getAnchor()).getY()>555:
                fruit2.undraw()
                fruit2=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(25,100))),"fruit2.png")
                fruit2.draw(win)
                draw=True
            if freq1==2 and (fruit3.getAnchor()).getY()>555:
                fruit3.undraw()
                fruit3=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(20,100))),"fruit3.png")
                fruit3.draw(win)
                draw=True
            if freq1==3 and (fruit4.getAnchor()).getY()>555:
                fruit4.undraw()
                fruit4=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(30,800))),"fruit4.png")
                fruit4.draw(win)
                draw=True
            if freq1==4 and (fruit5.getAnchor()).getY()>555:
                fruit5.undraw()
                fruit5=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(40,300))),"fruit5.png")
                fruit5.draw(win)
                draw=True
            if freq1==5 and (fruit6.getAnchor()).getY()>555:
                fruit6.undraw()
                fruit6=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(100,1500))),"fruit6.png")
                fruit6.draw(win)
                draw=True
            if freq1==6 and (fruit7.getAnchor()).getY()>555:
                fruit7.undraw()
                fruit7=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(50,900))),"fruit7.png")
                fruit7.draw(win)
                draw=True
            if freq1==7 and (fruit8.getAnchor()).getY()>555:
                fruit8.undraw()
                fruit8=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(100,1500))),"fruit8.png")
                fruit8.draw(win)
                draw=True
            if freq1==8 and (fruit9.getAnchor()).getY()>555:
                fruit9.undraw()
                fruit9=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(100,500))),"fruit9.png")
                fruit9.draw(win)
                draw=True
            if freq1==9 and (fruit10.getAnchor()).getY()>555:
                fruit10.undraw()
                fruit10=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(500,1000))),"fruit10.png")
                fruit10.draw(win)
                draw=True
            if freq1==10 and (fruit11.getAnchor()).getY()>555:
                fruit11.undraw()
                fruit11=Image(Point(((random.randrange(0,1000)+random.randrange(0,1000))/2),-(random.randrange(2000,5000))),"fruit11.png")
                fruit11.draw(win)
                draw=True
            if freq1== 11:
                draw=True
    #----------------------Fruit Mover and Contact Script-------#
         #--------------------------------------------------------------- Morango
        try:
            if fruit1.getAnchor().getY() <555: 
             fruit1.move(0,speedfall)
            v1,v2,v3,v4=fruit1.getAnchor().getX(),fruit1.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30):
                print("=CONTACT +1SCORE")
                fruit1.undraw()
                fruit1=Image(Point((random.randrange(0,1000)),-50),"fruit1.png")
                fruit1.draw(win)
                if pos == False:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                score=score+1
                speedfl=speedfl+1
                if sef != "SF":
                 wave_object5.play()
                perm1=True
            if v2>550 and v2<560:
                print("=DROP")
                fruit1.undraw()
                fruit1=Image(Point((random.randrange(0,1000)),-50),"fruit1.png")
                fruit1.draw(win)
                if sef != "SF":
                 wave_object7.play()
                up=up-1
                perm1=True
            #--------------------------------------------------------------- Uva
            if fruit2.getAnchor().getY() <555 and perm1==True:
             fruit2.move(0,speedfall)
            v1,v2,v3,v4=fruit2.getAnchor().getX(),fruit2.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm1==True:
                print("=CONTACT +2SCORE")
                fruit2.undraw()
                fruit2=Image(Point((random.randrange(0,1000)),-400),"fruit2.png")
                fruit2.draw(win)
                if pos == False and perm1==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm1==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                  perm2=True
                if sef != "SF":
                    wave_object5.play()
                score=score+2
                speedfl=speedfl+1
            if v2>550 and v2<560 and perm1==True:
                print("=DROP")
                fruit2.undraw()
                fruit2=Image(Point((random.randrange(0,1000)),-400),"fruit2.png")
                fruit2.draw(win)
                perm2=True
                if sef != "SF":
                    wave_object7.play()
                up=up-1
            #--------------------------------------------------------------- Banana
            if fruit3.getAnchor().getY() <555 and perm2==True: 
             fruit3.move(0,speedfall)
            v1,v2,v3,v4=fruit3.getAnchor().getX(),fruit3.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm2==True:
                print("=CONTACT +1SCORE")
                fruit3.undraw()
                fruit3=Image(Point((random.randrange(0,1000)),-100),"fruit3.png")
                fruit3.draw(win)
                if pos == False and perm2==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm2==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                perm3=True
                if sef != "SF":
                    wave_object5.play()
                score=score+1
                speedfl=speedfl+1
            if v2>550 and v2<560 and perm2==True:
                print("=DROP -1HP")
                fruit3.undraw()
                fruit3=Image(Point((random.randrange(0,1000)),-100),"fruit3.png")
                fruit3.draw(win)
                perm3=True
                if sef != "SF":
                    wave_object7.play()
                up=up-1
            #--------------------------------------------------------------- Vida
            if fruit4.getAnchor().getY() <555 and perm3==True: 
             fruit4.move(0,speedfall)
             perm4=True
            v1,v2,v3,v4=fruit4.getAnchor().getX(),fruit4.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm3==True:
                print("=CONTACT +1HP OR +10SCORE")
                fruit4.undraw()
                fruit4=Image(Point((random.randrange(0,1000)),-3000),"fruit4.png")
                fruit4.draw(win)
                if pos == False and perm3==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm3==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                if up < 4:
                 up=up+1
                 if sef != "SF":
                     wave_object2.play()
                else:
                 if sef != "SF":
                      wave_object5.play()
                score=score+10
            if v2>550 and v2<560 and perm3==True:
                print("=DROP")
                fruit4.undraw()
                fruit4=Image(Point((random.randrange(0,1000)),-3000),"fruit4.png")
                fruit4.draw(win)
            #--------------------------------------------------------------- Bomba
            if fruit5.getAnchor().getY() <555 and perm4==True: 
             fruit5.move(0,speedfall)
            v1,v2,v3,v4=fruit5.getAnchor().getX(),fruit5.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CONTACT -1HP")
                fruit5.undraw()
                fruit5=Image(Point((random.randrange(0,1000)),-500),"fruit5.png")
                fruit5.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                up=up-1
                if sef != "SF":
                    wave_object3.play()
                perm5=True
            if v2>550 and v2<560 and perm4==True:
                print("=DROP")
                fruit5.undraw()
                fruit5=Image(Point((random.randrange(0,1000)),-500),"fruit5.png")
                fruit5.draw(win)
                perm5=True
        #---------------------------------------------------------------Coelho
            if fruit6.getAnchor().getY() <555 and perm4==True: 
             fruit6.move(0,speedfall)
            v1,v2,v3,v4=fruit6.getAnchor().getX(),fruit6.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CONTACT +5SPEED")
                fruit6.undraw()
                fruit6=Image(Point((random.randrange(0,1000)),-500),"fruit6.png")
                fruit6.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                speedfl=speedfl+5
                if sef != "SF":
                    wave_object9.play()
            if v2>550 and v2<560 and perm4==True:
                print("=DROP")
                fruit6.undraw()
                fruit6=Image(Point((random.randrange(0,1000)),-500),"fruit6.png")
                fruit6.draw(win)   
        #---------------------------------------------------------------Lesma
            if fruit7.getAnchor().getY() <555 and perm5==True: 
             fruit7.move(0,speedfall)
            v1,v2,v3,v4=fruit7.getAnchor().getX(),fruit7.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CONTACT -5SPEED")
                fruit7.undraw()
                fruit7=Image(Point((random.randrange(0,1000)),-500),"fruit7.png")
                fruit7.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                speedfl=speedfl-5
                if sef != "SF":
                    wave_object10.play()
            if v2>550 and v2<560 and perm4==True:
                print("=DROP")
                fruit7.undraw()
                fruit7=Image(Point((random.randrange(0,1000)),-500),"fruit7.png")
                fruit7.draw(win)
        #---------------------------------------------------------------Limpa
            if fruit8.getAnchor().getY() <555 and perm5==True: 
             fruit8.move(0,speedfall)
            v1,v2,v3,v4=fruit8.getAnchor().getX(),fruit8.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CONTACT CLEAN DISPLAY")
                fruit8.undraw()
                fruit8=Image(Point((random.randrange(0,1000)),-500),"fruit8.png")
                fruit8.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                if sef != "SF":
                    wave_object11.play()
                fruit1.undraw()
                fruit2.undraw()
                fruit3.undraw()
                fruit4.undraw()
                fruit5.undraw()
                fruit6.undraw()
                fruit7.undraw()
                fruit8.undraw()
                fruit9.undraw()
                fruit10.undraw()
                fruit11.undraw()
                fruit1=Image(Point(0,701),"fruit1.png") 
                fruit2=Image(Point(0,701),"fruit2.png")  
                fruit3=Image(Point(0,701),"fruit3.png") 
                fruit4=Image(Point(0,701),"fruit4.png") 
                fruit5=Image(Point(0,701),"fruit5.png") 
                fruit6=Image(Point(0,701),"fruit6.png") 
                fruit7=Image(Point(0,701),"fruit7.png") 
                fruit8=Image(Point(0,701),"fruit8.png") 
                fruit9=Image(Point(0,701),"fruit9.png") 
                fruit10=Image(Point(0,701),"fruit10.png") 
                fruit11=Image(Point(0,701),"fruit11.png") 
                fruit1.draw(win)
                fruit2.draw(win)
                fruit3.draw(win)
                fruit4.draw(win)
                fruit5.draw(win)
                fruit6.draw(win)
                fruit7.draw(win)
                fruit8.draw(win)
                fruit9.draw(win)
                fruit10.draw(win)
                fruit11.draw(win)
            if v2>550 and v2<560 and perm4==True:
                print("=DROP")
                fruit8.undraw()
                fruit8=Image(Point((random.randrange(0,1000)),-500),"fruit8.png")
                fruit8.draw(win)
        #---------------------------------------------------------------Kiwi
            if fruit9.getAnchor().getY() <555 and perm5==True: 
             fruit9.move(0,speedfall)
            v1,v2,v3,v4=fruit9.getAnchor().getX(),fruit9.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CONTACT +4SCORE")
                fruit9.undraw()
                fruit9=Image(Point((random.randrange(0,1000)),-500),"fruit10.png")
                fruit9.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                if sef != "SF":
                    wave_object5.play()
                perm6=True
                score=score+4
                speedfl=speedfl+1
            if v2>550 and v2<560 and perm4==True:
                print("=DROP -1HP")
                up=up-1
                fruit9.undraw()
                fruit9=Image(Point((random.randrange(0,1000)),-500),"fruit9.png")
                fruit9.draw(win)
                perm6=True
        #---------------------------------------------------------------Melancia
            if fruit10.getAnchor().getY() <555 and perm6==True: 
             fruit10.move(0,speedfall)
            v1,v2,v3,v4=fruit10.getAnchor().getX(),fruit10.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CONTACT +3SCORE")
                fruit10.undraw()
                fruit10=Image(Point((random.randrange(0,1000)),-500),"fruit10.png")
                fruit10.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                score=score+3
                speedfl=speedfl+1
                if sef != "SF":
                    wave_object5.play()
            if v2>550 and v2<560 and perm4==True:
                print("=DROP -1HP")
                up=up-1
                fruit10.undraw()
                fruit10=Image(Point((random.randrange(0,1000)),-500),"fruit10.png")
                fruit10.draw(win)
        #---------------------------------------------------------------Mamão
            if fruit11.getAnchor().getY() <555 and perm6==True: 
             fruit11.move(0,speedfall)
            v1,v2,v3,v4=fruit11.getAnchor().getX(),fruit11.getAnchor().getY(),objc1_pxy.getX(),objc1_pxy.getY()
            if (v1>v3-30 and v1<v3+30) and (v2>v4-30 and v2<v4+30) and perm4==True:
                print("=CCONTACT +10SCORE")
                fruit11.undraw()
                fruit11=Image(Point((random.randrange(0,1000)),-500),"fruit11.png")
                fruit11.draw(win)
                if pos == False and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-3.png")
                  objc1.draw(win)
                if pos == True and perm4==True:
                  objc1.undraw()
                  objc1=Image(objc1_pxy,"char1-4.png")
                  objc1.draw(win)
                score=score+10
                speedfl=speedfl+1
                if sef != "SF":
                    wave_object5.play()
            if v2>550 and v2<560 and perm4==True:
                print("=DROP -1HP")
                up=up-1
                fruit11.undraw()
                fruit11=Image(Point((random.randrange(0,1000)),-500),"fruit11.png")
                fruit11.draw(win)
        except:
            pass
        if speedfl >= 10 and perm3==True:
                speedfall=0.1*speedfl
         #-----------------------HP Life Check------------------------------
        if up==4:
            hp_heat4.undraw()
            hp_heat4.draw(win)
        if up==3:
            hp_heat1.undraw()
            hp_heat2.undraw()
            hp_heat3.undraw()
            hp_heat4.undraw()
            hp_heat3.draw(win)
            hp_heat2.draw(win)
            hp_heat1.draw(win)
        if up==2:
            hp_heat1.undraw()
            hp_heat2.undraw()
            hp_heat3.undraw()
            hp_heat2.draw(win)
            hp_heat1.draw(win)
        if up==1:
            hp_heat1.undraw()
            hp_heat2.undraw()
            hp_heat1.draw(win)
        if up<=0: 
            print(">GAME OVER<")
            sa.stop_all()
            try:
             gameover.draw(win)
            except:
             pass
            hp_heat1.undraw()
            if sef != "SF":
                wave_object4.play()
            key=None
            #---------------------------------------------------------
            while key !="Escape":
                key=win.getKey()
                if key=="r":
                    print(">Reiniciando Jogo<")
                    reset = True
                    win.close()
                    return(sef,True,sem)
            win.close()
            sa.stop_all()
            print(">Menu Principal<")
            return(sef,False,sem)
        key=win.checkKey()
        update(60)
        score_data.setText(score)
        gat=False
        gat2=False    
        objc1_pxy=(objc1.getAnchor())
        if objc1_pxy.getX() <= float(0):
            gat=True
            if objc1_pxy.getX() <= float(10):
             objc1.move(20,0)
        else:
            gat=False
        if objc1_pxy.getX() >= float(1000):
            gat2=True
            if objc1_pxy.getX() >= float(99.0):
             objc1.move(-20,0)
        else:
            gat2=False
        if (key == ("a" or "A")) and gat==False:
            objc1.undraw()
            objc1=Image(objc1_pxy,"char1-2.png")
            objc1.draw(win)
            if sef != "SF":
                wave_object.play()
            for l in range(0,60):
                objc1.move(-(speedx/120),0)
            pos=False
        if (key == ("d" or "D")) and gat2==False:
            objc1.undraw()
            objc1=Image(objc1_pxy,"char1-1-0.png")
            objc1.draw(win)
            if sef != "SF":
                wave_object.play()
            for l in range(0,60):
                objc1.move((speedx/120),0)
            pos=True
        if (key == ("space" or "w" or "W")) and objc1_pxy.getY() >= float(485):
            objc1.move(0,-(speedy))
            if sef != "SF":
                wave_object12.play()
        if objc1_pxy.getY() <= float(jump_border_line):
            objc1.move(0,(gravit_s))
        if key == ("r" or "R"):
            print(">Resetando Jogo<")
            if sef != "SF":
                 wave_object8.play()
            reset = True
            win.close()
            sa.stop_all()
            return(sef,True,sem)
        if key == ("p" or "P"):
            if sef != "SF":
                 wave_object8.play()
            gamepause.draw(win)
            key=None
            print(">PAUSADO<")
            while key !="p":
             key=win.checkKey()
             if key == "t":
                 print(">Abrindo Terminal<")
                 objpx,objpy,speedy,speedx,gravit_s,jump_border_line,up,score=game_shell.call_t(objc1_pxy.getX(),objc1_pxy.getY(),speedy,speedx,gravit_s,jump_border_line,up,score)
                 objc1.undraw()
                 objc1_pxy=Point(objpx,objpy)
                 objc1=Image(objc1_pxy,"char1-2.png")
                 objc1.draw(win)
            if sef != "SF":
                 wave_object8.play()
            print(">DESPAUSADO<")
            gamepause.undraw()
        if key == "c":
            fruit1.move(0,5)
            if perm1 == True:
             fruit2.move(0,5)
            if perm2 == True:
             fruit3.move(0,5)
            if perm3 == True:
             fruit4.move(0,5)
            if perm4 == True:
             fruit5.move(0,5)
            if perm5 == True:
             fruit6.move(0,5)
             fruit7.move(0,5)
             fruit8.move(0,5)
             fruit9.move(0,5)
            if perm6 == True:
             fruit10.move(0,5)
             fruit11.move(0,5)
        if key == "h":
            print(">Abrindo Ajuda<")
            if sef != "SF":
                 wave_object8.play()
            win.close()
            sa.stop_all()
            help()
            return(sef,True,sem)
        if key == "t":
            print(">Abrindo Terminal<")
            if sef != "SF":
                 wave_object8.play()
            gamepause.draw(win)
            objpx,objpy,speedy,speedx,gravit_s,jump_border_line,up,score=game_shell.call_t(objc1_pxy.getX(),objc1_pxy.getY(),speedy,speedx,gravit_s,jump_border_line,up,score)
            objc1.undraw()
            objc1_pxy=Point(objpx,objpy)
            objc1=Image(objc1_pxy,"char1-2.png")
            objc1.draw(win)
            gamepause.undraw()
        update(120)
    print("=END GAME LOOP")
    return(sef,False,sem)
def retorno(sef,sem,reset):
    print("=RETURN TO MAIN MENU TO MENU RESET")
    inicial(sef,sem,reset)
def inicial(sef,sem,reset):
    print("=MAIN MENU OPEN")
    wave_object8 = sa.WaveObject.from_wave_file('audio8.wav')
    inicial=GraphWin(title="Inicio",width=1000,height=600,autoflush=True)
    background=Image(Point(500,300),"bitmap5.png")
    background.draw(inicial)
    text1=Text(Point(640,270),"")
    text2=Text(Point(640,370),"")
    text1.setSize(36)
    text2.setSize(36)
    text1.setTextColor("white")
    text2.setTextColor("white")
    contexdpl=Image(Point(500,300),"bitmap6.png")
    key=None
    while key != "4":
        key=inicial.getKey()
        if key == "1":
            if sef != "SF":
                 wave_object8.play()        
            inicial.close()
            main(sef,sem,reset)
        if key == "2":
            if sef != "SF":
                 wave_object8.play()     
            contexdpl.draw(inicial)
            text1.draw(inicial)
            text2.draw(inicial)
            key=None
            while key != "3":
                key=inicial.checkKey()
                if sem == "SM":
                    text1.setText("Desligado")
                else:
                    text1.setText("Ligado")
                if sef == "SF":
                    text2.setText("Desligado")
                else:
                    text2.setText("Ligado")
                if key =="1":
                    if sef != "SF":
                     wave_object8.play()     
                    if sem == "SM":
                        sem=""
                    else:
                        sem="SM"
                if key =="2":
                    if sef != "SF":
                     wave_object8.play()     
                    if sef == "SF":
                        sef=""
                    else:
                        sef="SF"
            text1.undraw()
            text2.undraw()
            if sef != "SF":
                 wave_object8.play()     
            contexdpl.undraw()
            key=None
        if key == "3":
            if sef != "SF":
                 wave_object8.play()     
            help()
            inicial.close()
            retorno(sef,sem,reset)
    inicial.close()
print("=STARTED")
try:
    inicial("","",True)
except:
    print("=FORCE END")
print("=END SCRIPT")