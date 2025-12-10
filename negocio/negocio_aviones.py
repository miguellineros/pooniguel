
from prettytable import PrettyTable
from datos.consultas import consulta_select, consulta_select_id, consulta_insert, avion_update, avion_delete
from datos.conexion import leer_datos, leer_dato_individual, insertar_datos
from modelos.avion import Avion
from negocio.negocio_aerolineas import obtener_datos_aerolineas

def obtener_datos_aviones():
    lista_aviones=[]
    tabla_aviones= PrettyTable()
    tabla_aviones.field_names=['N°', 'Código', 'Tipo', 'Capacidad', 'ID Aerolínea']
    
    campos ='id_avion,cod_avion,tipo_avion,capacidad_avion,id_aerolinea'
    tabla='aviones'
    consulta=consulta_select(campos,tabla)
    
    if consulta:
        resultado=leer_datos(consulta)
        if resultado:
            for data in resultado:
                avion= Avion(data[0],data[1],data[2],data[3],data[4]) 
                lista_aviones.append(avion)

        if len(lista_aviones)>0:
            for objeto in lista_aviones:
                tipo_str='Carga' if objeto._tipo_avion==1 else 'Pasajeros'
                capacidad_str=f'{objeto._capacidad_avion}{"Ton" if objeto._tipo_avion== 1 else "Pax"}'
                
                tabla_aviones.add_row(
                    [objeto._id_avion,objeto._cod_avion,tipo_str,capacidad_str,objeto._id_aerolinea])
        print(tabla_aviones)

def crear_avion():
    print("Creando Nuevo Avion")
    codigo =input('Ingrese Codigo del Avion (ej: AV-99):')
    
    print("\nTipos de Avion: [1] Carga | [2] Pasajeros")
    tipo=input('Seleccione Tipo: ')
    capacidad=input('Ingrese Capacidad (Cantidad de Pasajeros):')
    
    print("\nSeleccione la Aerolinea dueña del avión:")
    obtener_datos_aerolineas()
    id_aerolinea=input('Ingreseel ID de la aerolinea:')

    if codigo !=''and tipo in ['1','2']and capacidad.isdigit() and id_aerolinea.isdigit():
        campos='cod_avion,tipo_avion,capacidad_avion,id_aerolinea'
        tabla='aviones'
        datos=(codigo.upper(),int(tipo),int(capacidad), int(id_aerolinea))
        
        consulta=consulta_insert(campos,tabla)
        insertar_datos(consulta, datos,'crear')
    else:
        print("Error:Datos incorrectos.Pruebe otra vez.")

def modificar_avion():
    obtener_datos_aviones()
    id_avion =input('Ingrese el N°(ID) del Avion a cambiar:')
    
    if id_avion != '':
        campos='id_avion,cod_avion,tipo_avion,capacidad_avion,id_aerolinea'
        tabla='aviones'
        campo_busqueda='id_avion'
        
        consulta=consulta_select_id(campos,tabla,campo_busqueda)
        if consulta:

            avion_data=leer_dato_individual(consulta,id_avion)
            
            if avion_data:
                print(f"Editando avion: {avion_data[1]}")
                nuevo_cod=input(f'Nuevo codigo (enter para"{avion_data[1]}"): ')
                nuevo_tipo=input(f'Nuevo Tipo[1/2] (Enter para"{avion_data[2]}"): ')
                nueva_cap=input(f'Nueva Capacidad (Enter para "{avion_data[3]}"): ')
                nueva_aero=input(f'Nuevo ID Aerolinea (Enter para "{avion_data[4]}"): ')

                cod_final=nuevo_cod.upper()if nuevo_cod !=''else avion_data[1]
                tipo_final=int(nuevo_tipo)if nuevo_tipo !=''else avion_data[2]
                cap_final=int(nueva_cap)if nueva_cap !=''else avion_data[3]
                aero_final=int(nueva_aero)if nueva_aero !=''else avion_data[4]

                datos=(cod_final,tipo_final,cap_final,aero_final,id_avion)
                consulta_upd=avion_update()
                insertar_datos(consulta_upd,datos)
                print("Avion editado sin problemas")

def eliminar_avion():
    obtener_datos_aviones()
    id_avion=input('Ingrese el N°(ID) del Avión a Eliminar:')
    
    if id_avion !='':
        campos='id_avion,cod_avion'
        tabla ='aviones'
        campo_busqueda= 'id_avion'
        
        consulta=consulta_select_id(campos,tabla,campo_busqueda)
        if consulta:
            avion_data=leer_dato_individual(consulta,id_avion)
            if avion_data:
                confirmacion=input(f"seguro que quieres borrar el avion{avion_data[1]}?(s/n):")
                if confirmacion.lower()=='s':
                    consulta_del=avion_delete()
                    insertar_datos(consulta_del,(id_avion,))
                    print("Avion eliminado correctamente")