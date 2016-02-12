#!/usr/bin/python
# -*- coding: utf-8 -*- 

#--------------------------------------   
# Clase que describe el comportamiento del sistema de RIEGO de HydroPonic System
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

class HPS_SistemaRiego(threading.Thread):

	#Devuelve un vector con los valores
	#[<Activa riego>, valor por el que ha activado el riego, mensaje]
	def ComprobarSensores(self):
		todosSensores=0
		for sensor in self._sensoresHumedad:
			todosSensores=todosSensores+sensor.get("datoDigital")
			if(sensor.get("datoDigital") >= op.umbral_VALOR_MINIMO_RIEGO):
				return [True, sensor.get("datoDigital"), "Sensor "+sensor._nombre+" seco"]

		mediaSensores=todosSensores/len(self._sensoresHumedad);	
		if(mediaSensores>=op.umbral_VALOR_MEDIO_RIEGO):
			return [True, mediaSensores, "Mayoria de sensores secos"]

		return [False, mediaSensores, "Sensores correctos"]

	#Constructor, recibe los sensores de humedad (3 en nuestro caso)
	#y los actuadores que debe actvar/desactivar
	def __init__(self, sensoresHumedad, actuadoresRiego):
		threading.Thread.__init__(self)
		self._sensoresHumedad=sensoresHumedad
		self._actuadoresRiego=actuadoresRiego
		self._riegoActivo=False;
		self._tiempoRiego=0

	#Activa el riego y actualiza durante el tiempo que dura el riego _tiempoRiego
	#para visualizarlo por pantalla
	def ActivarRiego(self):
		if self._riegoActivo:
			for j in self._actuadoresRiego: j.Activar()
			#op.time.sleep(op.TIEMPO_DE_RIEGO)
			#Tiempo de riego
			while(self._tiempoRiego<op.TIEMPO_DE_RIEGO): 
				self._tiempoRiego=self._tiempoRiego+1;
				op.time.sleep(1)

			for j in self._actuadoresRiego: j.Desactivar()
			self._riegoActivo=False
			self._tiempoRiego=0;


	#Hilo principal, si salta la condicion de activación y el riego NO está encendido, se pone en marcha.
	def run(self):
		while True:
			compruebaSensores=self.ComprobarSensores()
			#El primer valor e compruebaSensores es un booleano, el resto información.
			#y si el riego no está actuvo
			if compruebaSensores[0] and not self._riegoActivo:
				fn.Escribir(compruebaSensores[2]+"\nActivando Riego... "+str(op.TIEMPO_DE_RIEGO/60)+" minutos")
				self._riegoActivo=True
				#El hilo principal se quedará en este hilo iterando hasta que acabe de regar
				self.ActivarRiego() 

			op.time.sleep(op.REFRESCO_PROCESOS)
