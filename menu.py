#import mean  ## ¿?
import funciones as fn

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos_trabajadores ={trabajadores:0 for trabajador in trabajadores }

while True:
    try:
        print("---MENU---")
        print("1.Asignar sueldos aleatorios")
        print("2.Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4.Reporte de sueldo")
        print("Salir del programa")

        opcion = int(input("Ingrese una opcion: "))
        if opcion ==1:
            sueldos_trabajadores =fn.asignar_sueldos_aleatorios(trabajadores)
            print("")


        elif opcion ==2:
            fn.clasificar_sueldos(trabajadores)
            


        elif opcion==3:
            fn.ver_estadisticas(trabajadores)
            estadisticas= fn.ver_estadisticas
            print("sueldo mas alto"), estadisticas
            print("sueldo mas bajo"), estadisticas
            print("promedio de sueldos"), estadisticas
            print("media geometrica"), estadisticas
            print("")




        elif opcion==4:
            fn.reporte_sueldo(trabajadores)
        
        elif opcion == 5:
            print("Vuelva al menu")



    except ValueError:
        print("Ingrese sólo numeros, por favor")

