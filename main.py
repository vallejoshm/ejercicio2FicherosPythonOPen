
from pickle import *
import  vehiculo


miVehiculo = vehiculo.Vehiculo()

miVehiculo.__int__('Fiat', 'Uno', 'Azul')
print(miVehiculo.__str__())

f = open('miArchivo.txt', 'w+b')

dump(miVehiculo, f)
f.seek(0)

otroVehiculo = load(f)
print(otroVehiculo.__str__())

f.close()

