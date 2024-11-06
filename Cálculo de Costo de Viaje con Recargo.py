distancia= float(input("Distancia recorrida en KM:  "))
TiempoViaje=float(input("Tiempode viaje en  min:  "))
HoraVaije=float(input("Hora de viaje (Solo hora 24h) "))
TarifaBase=5
TarifaKM=2.50*distancia
TarifaMin=0.50*TiempoViaje
if HoraVaije>24:
    print("Hora de viaje invalida")
else:
    if HoraVaije>= 7 and HoraVaije <= 9:
        print("Hay recargo")
        recargo=1.2
    elif HoraVaije>= 17 and HoraVaije <= 19:
        print("Hay recargo")
        recargo=1.2
    else:
        print("No hay recargo")
        recargo=1
    TarifaTotalRecargo=(TarifaBase+TarifaKM+TarifaMin)*recargo
    print(f"El coste total es: {TarifaTotalRecargo}")
