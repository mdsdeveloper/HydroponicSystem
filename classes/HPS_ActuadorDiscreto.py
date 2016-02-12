#!/usr/bin/python
# -*- coding: utf-8 -*- 

#--------------------------------------   
# Clase que describe el comportamiento de un actuador binario (activado o desactivado)
#
# Authors : [Matias Deambrosi, Juan Jose Conejero Serna]
# Date   : 21/10/2015
#
# Contact: [md9@alu.ua.es, jjcs2@alu.ua.es]
#
#--------------------------------------

import HPS_Options as op
import HPS_Funciones as fn
import RPi.GPIO as GPIO

class HPS_ActuadorDiscreto(object):

  def __init__(self, Pnombre, Pcanal, Pestado=False):
    self._nombre=Pnombre
    self._canal=Pcanal
    self._estado=Pestado
    GPIO.setup(self._canal, GPIO.OUT)
    if Pestado:
    	self.Activar()
    else:
    	self.Desactivar()

  def Activar(self):
  	GPIO.output(self._canal,GPIO.HIGH)
  	self._estado=True

  def Desactivar(self):
  	GPIO.output(self._canal,GPIO.LOW)
  	self._estado=False

  def get(self):
    return self._estado;
