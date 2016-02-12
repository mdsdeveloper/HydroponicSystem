#!/usr/bin/python
# -*- coding: utf-8 -*- 

#--------------------------------------   
# Clase que describe el comportamiento del sistema de ILUMINACION de HydroPonic System
#
# Authors : [Matias Deambrosi, Juan Jose Conejero Serna]
# Date   : 21/10/2015
#
# Contact: [md9@alu.ua.es, jjcs2@alu.ua.es]
#
#--------------------------------------

import HPS_Options as op
import HPS_Funciones as fn
import HPS_ActuadorDiscreto as actd
import threading


class HPS_SistemaIluminacion(threading.Thread):

	#Constructor, recibe los sensores de luz exterior
	#y los actuadores que debe actvar/desactivar
	def __init__(self, sensorLuzSolar, sensorLuzInterior, actuadorIluminacion):
		threading.Thread.__init__(self)
		self._sensorLuzSolar=sensorLuzSolar
		self._sensorLuzInterior=sensorLuzInterior
		self._actuadorIluminacion=actuadorIluminacion
		self._iluminacionActiva=False;

	def CompruebaLuces(self):
		if self._iluminacionActiva:
			if self._sensorLuzInterior.get("datoDigital") <op.umbral_VALOR_MIN_LUZINTERIOR:
				fn.Escribir("La iluminación no está encendida correctamente", True)
				self._iluminacionActiva=False

	#Hilo principal, si salta la condicion de activación y la iluminacion NO está encendida, se enciende.
	def run(self):
		while True:
			#Indicamos si hay suficiente luz solar
			if self._sensorLuzSolar.get("datoDigital")  < op.umbral_VALOR_MIN_LUZEXTERIOR:
				if not self._iluminacionActiva:
					self._actuadorIluminacion.Activar()
					self._iluminacionActiva=True
					fn.Escribir("\033[91m"+"Activando iluminacion"+"\033[0m")
					self.CompruebaLuces()
			else:
				if self._iluminacionActiva:
					self._actuadorIluminacion.Desactivar()
					self._iluminacionActiva=False
					fn.Escribir("Desctivando iluminacion")

			op.time.sleep(op.REFRESCO_PROCESOS)