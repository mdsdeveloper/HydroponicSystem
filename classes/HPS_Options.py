#!/usr/bin/python
# -*- coding: utf-8 -*- 

import time
import os

#######COMENTAR LINEAS CUANDO NO SE TRABAJE EN LA RASPBERRY (PRUEBAS)

import spidev #Importamos la librería del bus de SPI
import RPi.GPIO as GPIO #Importamos la libreria de raspberry

# #establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# # Establecemos el bus por el que va a circular la información y lo abrimos
spi = spidev.SpiDev()
spi.open(0,0)

#CONSTANTES
#Tiempo de actualización de los hilos secundarios
REFRESCO_PROCESOS=1
ERRORES=[]

#Definimos el NUMERO de las entradas ANALOGICAS DEL AC
ch_SENSOR_HUMEDAD1=0
ch_SENSOR_HUMEDAD2=1
ch_SENSOR_HUMEDAD3=2
ch_SENSOR_LUZSOLAR=4
ch_SENSOR_LUZINTERIOR=5
ch_SENSOR_PH=7
ch_SENSOR_ELECTRO=7

#Definimos el NUMERO de la salidas digitales (Relés)
ch_ACTUADOR_BOMBA=21
ch_ACTUADOR_ILUMINACION=1

#CONSTANTES PARA EL UMBRAL DE RIEGO
umbral_VALOR_MEDIO_RIEGO=600 #Medida en niveles
umbral_VALOR_MINIMO_RIEGO=900 #Medida en Niveles
TIEMPO_DE_RIEGO=20 #Tiempo en segundos

#CONSTANTES PARA EL UMBRAL DE ILUMINACION
umbral_VALOR_MIN_LUZEXTERIOR=600 #Medida en Niveles
umbral_VALOR_MIN_LUZINTERIOR=100 #Medida en Niveles
TIEMPO_ESPERA_ENCENDIDO=10 #TIEMPO QUE TARDAN EN EENCENDERSE LAS LUCES
