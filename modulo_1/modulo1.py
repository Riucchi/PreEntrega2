class Persona():
    def __init__(self, nombre, apellido, dni, rango):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni
        self.rango = rango

    





class Cliente(Persona):
    def __init__(self, *args):
        super().__init__(*args[:4])
        self.numero_de_compra = args[4]
        self.preferencia_cliente = args[5]
        self.correo = args[6]
        self.direccion_envio = args[7]
    
        
    


    def comprar(self,articulo,tienda):
        self.tienda = tienda
        self.articulo = articulo
        enviar_email = f"Se le ha enviado un correo con su factura a {self.correo}"
        envio_del_articulo = f"se enviara el articulo comprado a la direccion {self.direccion_envio}"
        compra_exitosa = f"El Cliente {self.nombre} {self.apellido} ah comprado {self.articulo} en la tienda {self.tienda}"
        
        return print(compra_exitosa) , print(enviar_email) , print(envio_del_articulo)

    
    def __str__(self):
        cliente_nuevo = f"Se ha creado al cliente {self.nombre} exitosamente"
        return cliente_nuevo
    
    def login(self):
        if self.rango == "Admin":
            administrador = print(f"Bienvenido {self.nombre} que quieres editar?")
            return administrador
        else:
            return print("No tienes permisos de Administrador.")



