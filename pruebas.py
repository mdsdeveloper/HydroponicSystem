from classes import HPS_SensorContinuo as sc
from classes import HPS_Funciones as fn
from classes import HPS_Options as op
from classes import HPS_SistemaRiego as sriego
from classes import HPS_SistemaIluminacion as silum
from classes import HPS_ActuadorDiscreto as actd
from datetime import datetime, timedelta
import decimal
from random import randint
import threading
import os

#Sensores del panel
humedad1=sc.HPS_SensorContinuo("Sensor humedad 1", "continuo", op.ch_SENSOR_HUMEDAD1, 5, 1023, randint(0, 1023));
humedad2=sc.HPS_SensorContinuo("Sensor humedad 2", "continuo", op.ch_SENSOR_HUMEDAD2, 5, 1023, randint(0, 1023));
humedad3=sc.HPS_SensorContinuo("Sensor humedad 3", "continuo", op.ch_SENSOR_HUMEDAD3, 5, 1023, randint(0, 1023));
#ph1=sc.HPS_SensorContinuo("Sensor PH 1", "continuo", op.ch_SENSOR_PH, 5, 1023, randint(0, 1023));
#electro1=sc.HPS_SensorContinuo("Sensor Electroconductividad", "continuo", op.ch_SENSOR_ELECTRO, 5, 1023, randint(0, 5));
#solar=sc.HPS_SensorContinuo("Sensor Luz Solar", "continuo", op.ch_SENSOR_ELECTRO, 5, 1023, randint(0, 1023));
#luzinterior=sc.HPS_SensorContinuo("Sensor Luz Interior", "continuo", op.ch_SENSOR_ELECTRO, 5, 1023, randint(0, 1023));

#Actuadores de los reles del panel
bombaAgua=actd.HPS_ActuadorDiscreto("Bomba de riego", op.ch_ACTUADOR_BOMBA)
#iluminacion=actd.HPS_ActuadorDiscreto("Iluminacion Interior", op.ch_ACTUADOR_ILUMINACION)

#Creamos el sistema de riego con los sensores de humedad y los actuadores
sistemaRiego=sriego.HPS_SistemaRiego([humedad1, humedad2, humedad3], [bombaAgua]);
#sistemaIluminacion=silum.HPS_SistemaIluminacion(solar, luzinterior, iluminacion);

#Creacion de hilos secundarios
sistemaRiego.start()
#sistemaIluminacion.start()

#Mensaje mostrado por pantalla continua
def InformacionGeneral():
	fecha=datetime.now().strftime('%H:%M:%S %d/%m/%Y ')
	resultado="####---"+fecha+"---####\n"
	resultado+="--Sensores---------------------------------------\n"
	resultado+="| "+humedad1._nombre+" -> "+humedad1.get("datoImpreso")+" \n"
	resultado+="| "+humedad2._nombre+" -> "+humedad2.get("datoImpreso")+" \n"
	resultado+="| "+humedad3._nombre+" -> "+humedad3.get("datoImpreso")+" \n"
#	resultado+="| "+ph1._nombre+" -> "+str(fn.ConvertirPH(ph1))+"/14\n"
#	resultado+="| "+electro1._nombre+" -> "+str(fn.ConvertirEC(electro1))+" s/m\n"
#	resultado+="| "+solar._nombre+" -> "+str(solar.get("datoDigital"))+"/"+str(solar.get("totalDigital"))+"\n"
#	resultado+="| "+luzinterior._nombre+" -> "+str(luzinterior.get("datoDigital"))+"/"+str(luzinterior.get("totalDigital"))+"\n"
	resultado+="-------------------------------------------------\n\n"
	resultado+="--Controladores----------------------------------\n"
	resultado+="| "+bombaAgua._nombre+" -> "+str(bombaAgua._estado)+" \n"
#	resultado+="| "+iluminacion._nombre+" -> "+str(iluminacion._estado)+"\n"
	resultado+="-------------------------------------------------\n\n"
	if(sistemaRiego._riegoActivo):
		resultado+="--Tiempo de Riego--------------------------------\n"
		resultado+="| Tiempo regado -> "+str(timedelta(seconds=sistemaRiego._tiempoRiego))+"\n"
		resultado+="| Tiempo restante -> "+str(timedelta(seconds=(op.TIEMPO_DE_RIEGO-sistemaRiego._tiempoRiego)))+" \n"
		resultado+="-------------------------------------------------\n\n"

#	if(len(op.ERRORES)):
#		resultado+="--Errores: --------------------------------\n"
#		for error in op.ERRORES:
#			resultado+=error

	return resultado

#Creacion de hilo principal
while(True):
	os.system("clear")
	print InformacionGeneral()
	op.time.sleep(1)
