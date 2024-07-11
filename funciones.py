import statistics  ##¿?
import random
import csv
trabajadores=[]
sueldos_trabajadores= {}

sueldos_promedio=0


def asignar_sueldos_aleatorios():
    sueldos_trabajadores= {}
    

for trabajador in trabajadores:
        sueldo = random.randint(300000, 25000)
        sueldos_trabajadores[trabajador] = sueldo
    


def clasificar_sueldos(sueldos_trabajadores):
    menor_800={}
    entre_800_2000= {}
    mayores_2000= {}
    sueldos_promedio=0 

for trabajador, sueldo in sueldos_trabajadores.items(): 
    if sueldos_promedio <800000:
         
    elif
   
         

def ver_estadisticas(sueldos_trabajadores):
    lista_estadisticas= len(sueldos_trabajadores)
    sueldo_mas_alto = max (lista_estadisticas)
    sueldo_mas_bajo = min (lista_estadisticas)
    promedio_sueldos = sum(lista_estadisticas)/(lista_estadisticas) 
     # hacer sumatoria
    print("el sueldo mas bajo es: ", sueldo_mas_bajo)
    print("el sueldo mas alto es: ", sueldo_mas_bajo)
    print("el sueldo promedio es: ", sueldos_promedio)




def reporte_sueldo(sueldos_trabajadores):
    estadisticas={} #lista o diccionario?
for trabajador, sueldo in sueldos_trabajadores:
    descuento_afp = sueldo *0.07
    descuento_salud = sueldo *0.12
    sueldo_liquido =  sueldo - descuento_afp- descuento_salud
    ##mostrar diccionario
    
    trabajador= {
            "nombre_empleado" : trabajador,
            "sueldo_base" : sueldo,
            "descuento_salud" : descuento_salud,
            "descuento_afp" : descuento_afp,
            "sueldo liquido": sueldo_liquido
        }

    
    with open ("reporte_sueldo.csv", "w",newline= "" ) as archivo:
        escritor= csv.writer(archivo)
        escritor.writerow()


        ##faltan cosas
