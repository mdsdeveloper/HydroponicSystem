import HPS_Options
from datetime import datetime, timedelta
from classes import HPS_Options as op
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  388       75    1.25
  #  465      100    1.50
  #  543      125    1.75
  #  620      150    2.00
  #  698      175    2.25
  #  775      200    2.50
  #  853      225    2.75
  #  930      250    3.00
  # 1008      275    3.25
  # 1023      280    3.30
def ConvertirTemperatura(niveles,decimales=2):
  temp = ((niveles * 5)/float(1023))-50
  temp = round(temp,decimales)
  return temp

def ConvertirPH(objetoPH,decimales=2):
  ph = 14 * float(objetoPH.get("datoDigital"))/float(objetoPH.get("totalDigital"));
  ph = round(ph,decimales)
  return ph

def ConvertirEC(objetoEC,decimales=2):
  ph = (9.6* 10**5) * float(objetoEC.get("datoDigital"))/float(objetoEC.get("totalDigital"));
  ph = round(ph,decimales)
  return ph

def IntConvertirHumedad(objetoHumedad, rango=1023, decimales=2):
		return 100-round(100*objetoHumedad/rango, decimales)

def ConvertirHumedad(objetoHumedad,decimales=2):
	humedad = 100 * float(objetoHumedad.get("datoDigital"))/float(objetoHumedad.get("totalDigital"));
	humedad = round(humedad,decimales)
	return 100-humedad

def Escribir(valor, error=False):
  if error:
    if(len(op.ERRORES)>10):
        op.ERRORES=[]
    fecha=datetime.now().strftime('%H:%M:%S %d/%m/%Y ')
    op.ERRORES.append(fecha+": "+valor+"\n")
  else:
    print valor
  #Escribir en LOG
