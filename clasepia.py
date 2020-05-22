import datetime
#se importa librearia para usar los datos tipo fechas
class CONTACTO:
     #definimos la clase
    def __init__(self,NickName,Nombre,Correo,Telefono,FechaNacimiento,Gasto,Registro=datetime.datetime.now()):
        CONTACTO.NickName = NickName
        CONTACTO.Nombre= Nombre
        CONTACTO.Correo = Correo
        CONTACTO.Telefono= Telefono
        CONTACTO.FechaNacimiento = FechaNacimiento
        CONTACTO.Gasto= Gasto
        CONTACTO.Registro= Registro
