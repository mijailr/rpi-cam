#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import os
import RPi.GPIO as GPIO
import subprocess
import datetime
import pygame
from pygame.locals import *

# Configuración básica
pin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
folder = "/home/pi/rpi-cam/"
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
# Variables
c = 0
activo = False
inactivo =False
comando = ""
archivo = ""
pausa = "1000"

ejecutando = True;

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width, height = screen.get_size()

font = pygame.font.SysFont("verdana", 12, bold=0)

def takepic(imageName):
    writemessage("Tomando foto...")
    command = "sudo raspistill -o " + imageName + " -q 100 -rot 270 -t " + pausa
    print(command)
    os.system(command)
    writemessage("Tomando foto...")

def loadpic(imageName):
    print("Cargando foto: " + imageName)

    background = pygame.image.load(imageName);
    background.convert_alpha()
    background = pygame.transform.scale(background,(width,height))
    screen.blit(background,(0,0),(0,0,width,height))
    textsurface = font.render(imageName, 1, pygame.Color(0,0,0))
    screen.blit(textsurface,(20,0))

def movepic(imageName):
    command = "sudo mv " + imageName + " " + folder + imageName
    print(command)
    os.system(command)


def writemessage(message):
    screen.fill(pygame.Color(0,0,0))
    #screen.blit(background,(0,0),(0,0,width,height))
    textsurface = font.render(message, 1, pygame.Color(255,255,255))
    screen.blit(textsurface,(35,40))
    pygame.display.update()



while running:
    if(up == True):
        if(GPIO.input(pin)==False):
            print("button 24 pressed")
            now = datetime.datetime.now()
            timeString = now.strftime("%Y-%m-%d_%H:%M:%S")
            print("request received: " + timeString)
            filename = "photo-" + timeString + ".jpg"
            takepic(filename)
            loadpic(filename)
            movepic(filename)

    up = GPIO.input(pin)
    count = count + 1

    pygame.display.update()
    sleep(.1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False




#never hit
print("end of loop");
