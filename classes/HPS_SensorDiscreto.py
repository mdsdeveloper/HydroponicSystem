#!/usr/bin/python
# -*- coding: utf-8 -*- 

#--------------------------------------   
# Clase que describe el comportamiento de un sensor de HydroPonic System
#
# Authors : [Matias Deambrosi, Juan Jose Conejero Serna]
# Date   : 21/10/2015
#
# Contact: [mddX@alu.ua.es, jjcs2@alu.ua.es]
#
#--------------------------------------
import itertools

class HPS_SensorDiscreto(object):
        
  def __init__(self, Pnombre, Ptipo, Pcanal, PvTrabajo=3.3):
    self._nombre=Pnombre
    self._voltajeTrabajo=PvTrabajo;
    self._canal=Pcanal
    self._tipo=Ptipo;

  #Si es protocolo SPI
  def LeerCanal(self):
    #lecturaAnalogica = spi.xfer2([1,(8+canal)<<4,0])
    #dato = ((lecturaAnalogica[1]&3) << 8) + lecturaAnalogica[2]
    #return dato
    return 123;

  #Convierte el nivel devueltó por el ADC en voltios
  #redondeando al numero especificado de decimales
  def Nivel2Voltios(self, senyalDigital, decimales=3):
    voltios=(senyalDigital * self._voltajeTrabajo)/float(self._nivelesTrabajo)
    voltios=round(voltios,decimales)
    return voltios

  #Devuelve la ficha tecncia del sensor, indicando
  #el tipo de sensor, el controlador que tiene, voltaje y niveles
  def FichaTecnica(self):
    resultadoTitulo='------Sensor: '+self._nombre+' ('+self._tipo+')-------\n'
    resultado+="    Voltaje de Trabajo: "+str(self._voltajeTrabajo)+"\n"
    for i in range(len(resultadoTitulo)-1): resultado+="-"

    return resultadoTitulo+resultado

  #Devueve los datos útiles para trabajar, tales como
  #El dato digital actual, el dato analógico (voltaje), el número total de niveles y el número total de voltios al que trabaja
  def get(self, dato=None):
    todos={"datoDigital": self.LeerCanal(), "datoAnalogico": self.Nivel2Voltios(self.LeerCanal()), "totalDigital":self._nivelesTrabajo, "totalAnalogico": self._voltajeTrabajo};
    return todos.get(dato, todos)
