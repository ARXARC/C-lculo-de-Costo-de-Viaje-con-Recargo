

#7:00 a 9:00 a.m. y de 5:00 a 7:00

HorasPico=[7,
           9,
           17,
           19]

distancia= float(input("\nDistancia recorrida en KM:  "))
TiempoViaje=float(input("\nTiempode viaje en  min:  "))
HoraVaije=float(input("\nHora de viaje (Solo hora 24h) "))

TarifaBase=5
TarifaKM=2.50*distancia
TarifaMin=0.50*TiempoViaje


if HoraVaije>24:
    print("Hora de viaje invalida")
else:
    if HoraVaije not in HorasPico:
        print("No hay recargo")
        recargo=1
    else:
        print("Hay recargo")
        recargo=1.2
    
    TarifaTotalRecargo=(TarifaBase+TarifaKM+TarifaMin)*recargo
    print(f"El coste total es: {TarifaTotalRecargo}")
    
    


#5+2.5+0.5=8