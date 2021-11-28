
"""
Parcial Herramientas Computacionales
Nombres: Nicolás Valencia Payán y Samuel Solarte Serna

Problema:
Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran
dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor,
tienen descuentos diferentes. Se desea saber entonces por cada compra cuanto debe pagar el
usuario en caja. Para ello:

Pida por teclado la siguiente informacion para el cliente: cedula y rol: profesor o estudiante

Registrar el producto a comprar: codigo producto, cantidad de unidades y precio del producto.
(un solo producto, varias unidades, por ejemplo: producto 076: gaseosa, 3 unidades)

Los descuentos estan dados de la siguiente forma: los estudiantes tienen un 50% de descuento
mientras que los profesores tienen un 20% de descuento

Al final el procedimiento por cada cliente debera imprimir el valor a pagar por sus productos
de la forma: ”El Rol con cedula Numero, debe pagar Valor por el producto Codigo”
Ejemplo: ”El profesor con Cedula 1454898 debe pagar $12.900 por el producto 076”.
Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la
cantidad llevada menos el descuento otorgado, debe imprimir el rol y la c´edula de cada cliente
y el codigo del producto llevado en el mensaje.

"""

def descuentosComunidad():

    cedula = int(input("Ingrese cedula: "))
    rol = input("Ingrese rol: ")

    variedad = int(input("Cuantos productos va a comprar?: "))
    precioTotal = 0
    codigos = dict()

    for i in range (variedad):
        codigo = str(input("Ingrese codigo de producto: "))
        producto = input("Ingrese nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = int(input("Ingrese el precio del producto: "))

        precio = (cantidad * precio)

        codigos[codigo] = precio

        if rol.lower() == "profesor":
            precio = (precio * 0.8)

        if rol.lower() == "estudiante":
            precio = (precio * 0.5)

 
        print("El ", rol, " con cedula ", cedula, " debe pagar ", precio, " por el producto ", codigo)
        precioTotal += precio
        if i == variedad - 1:
            print("Su precio total es: ", precioTotal)

descuentosComunidad()

    






