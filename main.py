#Global variable: is a variable that can be accessed anywhere in the code.
#Funcion Seleccionar Usuario: permite elegir entre cliente, cajero, administrador
def seleccione_usuario(): 
    tipo_usuarios = ['cliente', 'cajero', 'administrador'] #definimos las opciones de usuario
    opcion_correcta = False #la variable opcion_correcta sea falso
    while not opcion_correcta: #mientras no sea falso, diferente de falso, ejecute el input
        tipo_usuario = input('Por favor seleccione tipo usuario: (cliente, cajero o administrador): ')
        opcion_correcta = validar_opcion(tipo_usuario, tipo_usuarios)
    return tipo_usuario


def seleccione_tiempo_comida():
    tiempos_comidas = ['desayuno', 'almuerzo', 'cena']
    opcion_correcta = False
    while not opcion_correcta:
        tiempo_comida = input('Por favor seleccione tiempo de comida (desayuno, almuerzo o cena): ')
        opcion_correcta = validar_opcion(tiempo_comida, tiempos_comidas)
    return tiempo_comida
#tuples
menu = {
    'desayuno': [
      ('chorreadas', 1500), 
      ('gallo pinto', 1500), 
      ('tortilla con queso', 1500)
    ],
    'almuerzo': [
      ('casado con pollo', 3000), 
      ('casado con pescado', 3000), 
      ('casado con chuleta', 3000)
    ],
    'cena': [
      ('chifrijo', 2500), 
      ('patacones', 2500), 
      ('sopa azteca', 2500)
    ],
    'postres':[
      ('brownies', 1500), 
      ('pie de limon', 1500), 
      ('pie de maracuya', 1500)
    ]
}


def seleccione_una_opcion(opciones_disponibles):
    opcion_correcta = False
    while not opcion_correcta:
        item = input('Porfavor eliga una opcion del menu:')
        opcion_correcta = validar_opcion(item, opciones_disponibles)

    cantidad = preguntar_cantidad('Cantidad que desea (1 o mas): ')
    return item, cantidad


def seleccione_opciones(tiempo_comida):
    cantidad_menu = 0

    opciones_disponibles = menu[tiempo_comida.lower()]
    precios_opciones = dict(opciones_disponibles)
    print('Opciones disponibles: ')
    for item, precio in opciones_disponibles:
        print('{} , precio: {}'.format(item, precio))

    while True:
        item, cantidad = seleccione_una_opcion([item for item, _ in opciones_disponibles])
        orden_correcta = input('Es su orden correcta? (Si/No): ')
        if orden_correcta.lower() ==  'si':
            break

    precio = precios_opciones[item.lower()]
    total = precio * cantidad
    return item, cantidad, precio, total


ubicaciones_disponibles = ['Afuera', 'Primer nivel', 'Segundo nivel']

def seleccione_ubicacion_mesa():
    ubicacion_correcta = False

    print('Ubicaciones disponibles: ')
    for item in ubicaciones_disponibles:
        print(item)

    while not ubicacion_correcta:
        ubicacion = input('Ingrese ubicacion: ')
        ubicacion_correcta = validar_opcion(ubicacion, ubicaciones_disponibles)

    return ubicacion


def seleccione_mesa():
    while True:
        num_personas = preguntar_cantidad('Cantidad de personas (1 o mas): ')
        ubicacion = seleccione_ubicacion_mesa()

        orden_correcta = input('Datos correctos? (Si/No): ')
        if orden_correcta.lower() == 'si':
            break
      
    return ubicacion, num_personas

opciones_tarjetas = ['Visa', 'Mastercard', 'American Express']


def seleccionar_tarjeta():
    print('Tarjetas disponibles: ')
    for item in opciones_tarjetas:
        print(item)
    tarjeta_correcta = False

    while not tarjeta_correcta:
        tarjeta = input('Ingrese tarjeta: ')
        tarjeta_correcta = validar_opcion(tarjeta, opciones_tarjetas)

    return tarjeta

def pagar_orden():
    while True:
      tarjeta = seleccionar_tarjeta()
      tarjeta_correcta = input('Datos correctos? (Si/No) ')
      if tarjeta_correcta.lower() == 'si':
          break
    return tarjeta


def imprimir_datos(usuario, tiempo_comida, platillo, cantidad_platillo,
                   precio, ubicacion_mesa, cantidad_personas, tarjeta,
                   total):

  plantilla = """

  Tipo de usuario: {}
  Tiempo de comida: {}
  Platillo: {} Cantidad: {} Precio: {}
  Ubicacion mesa: {} Cantidad de personas: {}
  Tipo de tarjeta: {}

  Total pagado: {}
  """

  s = plantilla.format(
    usuario,
    tiempo_comida,
    platillo,
    cantidad_platillo,
    precio,
    ubicacion_mesa, 
    cantidad_personas,
    tarjeta,
    total
  )

  print(s)


## Funciones de ayuda
def preguntar_cantidad(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            # No hacemos nada para que vuelva a preguntar
            pass


def validar_opcion(opcion, opciones_disponibles):
    # Convertimos las opciones a minusculas
    opciones = [op.lower() for op in opciones_disponibles]
    return opcion.strip().lower() in opciones


def main():
    usuario = seleccione_usuario()
    tiempo_comida = seleccione_tiempo_comida()
    platillo, cantidad_platillo, precio, total = seleccione_opciones(tiempo_comida)
    ubicacion_mesa, cantidad_personas = seleccione_mesa()
    tarjeta = pagar_orden()

    imprimir_datos(usuario, tiempo_comida, platillo, cantidad_platillo, 
                   precio, ubicacion_mesa, cantidad_personas, tarjeta, total)


if __name__ == '__main__':
    main()
