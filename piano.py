import pyaudio
import wave
import threading
import time
import pygame
import sys
import os
pygame.init()
p = pyaudio.PyAudio()

screen = pygame.display.set_mode((660, 130))
pygame.display.set_caption('Piano') # 设置标题
background = pygame.image.load(r"钢琴.png") #设置窗口背景
screen.blit(background,(0,0))  #对齐的坐标
pygame.display.update()   
imagez = pygame.image.load(r".\pictures\z.png")
imagex = pygame.image.load(r".\pictures\x.png")
imagec = pygame.image.load(r".\pictures\c.png")
imagev = pygame.image.load(r".\pictures\v.png")
imageb = pygame.image.load(r".\pictures\b.png")
imagen = pygame.image.load(r".\pictures\n.png")
imagem = pygame.image.load(r".\pictures\m.png")
imagea = pygame.image.load(r".\pictures\a.png")
images = pygame.image.load(r".\pictures\s.png")
imaged = pygame.image.load(r".\pictures\d.png")
imagef = pygame.image.load(r".\pictures\f.png")
imageg = pygame.image.load(r".\pictures\g.png")
imageh = pygame.image.load(r".\pictures\h.png")
imagej = pygame.image.load(r".\pictures\j.png")
imageq = pygame.image.load(r".\pictures\q.png")
imagew = pygame.image.load(r".\pictures\w.png")
imagee = pygame.image.load(r".\pictures\e.png")
imager = pygame.image.load(r".\pictures\r.png")
imaget = pygame.image.load(r".\pictures\t.png")
imagey = pygame.image.load(r".\pictures\y.png")
imageu = pygame.image.load(r".\pictures\u.png")
image1 = pygame.image.load(r".\pictures\1.png")


pressDict={"1":False,"2":False,"3":False}

keyDict={
    pygame.K_1:'c3',

    pygame.K_q:'c2',
    pygame.K_w:'d2',
    pygame.K_e:'e2',
    pygame.K_r:'f2',
    pygame.K_t:'g2',
    pygame.K_y:'a2',
    pygame.K_u:'b2',

    pygame.K_a:'c1',
    pygame.K_s:'d1',
    pygame.K_d:'e1',
    pygame.K_f:'f1',
    pygame.K_g:'g1',
    pygame.K_h:'a1',
    pygame.K_j:'b1',

    pygame.K_z:'c',
    pygame.K_x:'d',
    pygame.K_c:'e',
    pygame.K_v:'f',
    pygame.K_b:'g',
    pygame.K_n:'a',
    pygame.K_m:'b'


}


#音频流
def play(path,key):
    chunk = 1024#设置缓存区数据写入到dac里面
    wf = wave.open(path, 'rb')#只读模式打开wav音频文件
    data = wf.readframes(chunk)
    global p
    
    print(keyDict[key],end=' ')
    sys.stdout.flush() 

    #打开音频流
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),#获取采样深度
                    channels=wf.getnchannels(),#声道数
                    rate=wf.getframerate(),#帧率
                    frames_per_buffer=chunk,
                    output=True)#音频输出

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)



while True:
    time.sleep(0.01)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if(key == pygame.K_ESCAPE):
                pygame.quit()


            elif key in keyDict.keys():
                audio = "./audios/"+str(keyDict[key])+".wav"

                if os.path.exists(audio):#判断括号里的文件是否存在
                    threading.Thread(target=play, args=(audio,key)).start()#多线程
                    if key == pygame.K_z:
                        screen.blit(imagez, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_x:
                        screen.blit(imagex, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_c:
                        screen.blit(imagec, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_v:
                        screen.blit(imagev, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_b:
                        screen.blit(imageb, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_n:
                        screen.blit(imagen, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_m:
                        screen.blit(imagem, (0,0))
                        pygame.display.flip()#z-m
                    if key == pygame.K_a:
                        screen.blit(imagea, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_s:
                        screen.blit(images, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_d:
                        screen.blit(imaged, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_f:
                        screen.blit(imagef, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_g:
                        screen.blit(imageg, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_h:
                        screen.blit(imageh, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_j:
                        screen.blit(imagej, (0,0))
                        pygame.display.flip()#a-j
                    if key == pygame.K_q:
                        screen.blit(imageq, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_w:
                        screen.blit(imagew, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_e:
                        screen.blit(imagee, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_r:
                        screen.blit(imager, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_t:
                        screen.blit(imaget, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_y:
                        screen.blit(imagey, (0,0))
                        pygame.display.flip()
                    if key == pygame.K_u:
                        screen.blit(imageu, (0,0))
                        pygame.display.flip()#q-u
                    if key == pygame.K_1:
                        screen.blit(image1, (0,0))
                        pygame.display.flip()#1


        elif event.type == pygame.KEYUP:

            key = event.key
            pressDict[key]=False
            pygame.display.update()
    









