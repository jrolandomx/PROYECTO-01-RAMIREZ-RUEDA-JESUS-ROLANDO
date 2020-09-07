from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

# Seccion de usuarios de lifestore
usuarios_admin = [["superuser", "telmex"],["admin","admin"],["localhost","localhost"]]

# Seccion de login
usuario_entrada = input('Ingresa tu usuario: ')
usuario_contrasena = input('Ingresa tu contraseña: ')

es_admin = 0

# Seccion para recorrer por indices los usuarios administradores

for usuario in usuarios_admin:
  if usuario[0] == usuario_entrada and usuario[1] == usuario_contrasena:
    print("\n * Bienvenido nuevamente a tu tienda lifestore *\n")
    es_admin = 1
    break
  else:
    continue


# Seccion para entrar al menu
if es_admin == 1:
  print('Lifestore: Tu tienda virtual \n')

# Seccion para elegir el menu
  print('Lifestore: ¿Que opción deseas elegir? \n Ejemplo: A,a o B,a, C,a etc. \n \n A,)Productos más vendidos y productos rezagados \n a.- 50 productos con mayores ventas \n b.- 100 productos con mayor búsquedas \n c.- 50 productos con menores ventas \n d.- 100 productos con menores búsquedas \n\n B,) Productos por reseña en el servicio \n a.- Mejores reseñas \n b.- Peores reseñas \n\n C,) Total de ingresos y ventas promedio mensuales total anual y meses con más ventas al año \n a.- Total de ingresos Mensuales \n b.- Total ventas promedio mensuales \n c.- Total ventas promedio anual \n d.- Meses con más ventas al año')

  opcion_seleccionada = input('Ingresa tu opcion: ')

# Seccion para entrar al menu 2
  opcionvalida = 0

  while opcionvalida != 1:
    if opcion_seleccionada == "A,a":
      print("Lifestore: Seleccionaste: A,a")
      opcionvalida = 1

      contador = 0
      total_ventas = []
      # catalogo productos
      for producto in lifestore_products:
        # catalogo ventas
        for venta in lifestore_sales:
          # donde 0 y 1 es la posicion 
          if producto[0] == venta[1]:
            contador += 1

        formato_correcto = [producto[0], producto[1], contador]
        total_ventas.append(formato_correcto)
        contador = 0
        # se imprime el catalogo de articulos

      #for total in total_ventas:
       # print('El producto: ', total[0], 'se vendio: ', total[2])

      for indice in range(0, 50):
        print("\nNombre: \n", total_ventas[indice][2])        
      
    elif opcion_seleccionada == "A,b":
      print("Lifestore: Seleccionaste: A,b")
      opcionvalida = 1

      contador = 0
      total_ventas = []

      for producto in lifestore_searches:
        for venta in lifestore_products:
          if producto[0] == venta[1]:
            contador += 1

        formato_correcto = [producto[0], producto[1], contador]
        total_ventas.append(formato_correcto)
        contador = 0

    elif opcion_seleccionada == "A,c":
      print("Lifestore: Seleccionaste: A,c")
      opcionvalida = 1

    elif opcion_seleccionada == "A,d":
      print("Lifestore: Seleccionaste: A,d")
      opcionvalida = 1

    elif opcion_seleccionada == "B,a":
      print("Lifestore: Seleccionaste: B,a")
      opcionvalida = 1 

      contador = 0
      total_ventas = []

      for producto in lifestore_sales:
        for venta in lifestore_products:
          if producto[0] == venta[1]:
            contador += 1

        formato_correcto = [producto[0], producto[1], producto[2], contador]
        total_ventas.append(formato_correcto)
        contador = 0
        # se imprime el catalogo de articulos

      for total in total_ventas:
        print( total[1], ',', total[2])


    elif opcion_seleccionada == "B,b":
      print("Lifestore: Seleccionaste: B,b")
      opcionvalida = 1

    elif opcion_seleccionada == "C,a":
      print("Lifestore: Seleccionaste: C,a")
      opcionvalida = 1 

      contador = 0
      total_ventas = []
      # catalogo productos
      for producto in lifestore_products:
        # catalogo ventas
        for venta in lifestore_sales:
          # donde 0 y 1 es la posicion 
          if producto[0] == venta[1]:
            contador += 1

        formato_correcto = [producto[0], producto[1], producto[2],contador]
        total_ventas.append(formato_correcto)
        contador = 0

      for total in total_ventas:
        print('El producto: ', total[0], ',', total[3], 'veces: ', 'a un precio de: ', total[2])

    elif opcion_seleccionada == "C,b":
      print("Lifestore: Seleccionaste: C,b")
      opcionvalida = 1 

      contador = 0
      total_ventas = []
      # catalogo productos
      for producto in lifestore_sales:
        # catalogo ventas
        for venta in lifestore_products:
          # donde 0 y 1 es la posicion 
          if producto[0] == venta[1]:
            contador += 1

        formato_correcto = [producto[0], producto[1], producto[2],producto[3],contador]
        total_ventas.append(formato_correcto)
        contador = 0

      for total in total_ventas:
        print(total[1],',', total[3])

    elif opcion_seleccionada == "C,c":
      print("Lifestore: Seleccionaste: C,c")
      opcionvalida = 1 

    elif opcion_seleccionada == "C,d":
      print("Lifestore: Seleccionaste: C,d")
      opcionvalida = 1             

    else:
      print("Lifestore: Intenta nuevamente")
      opcion_seleccionada = input('Lifestore: Esta opcion no existe Intenta nuevamente')

# Seccion que indica que tu contraseña no es correcta
else:
  print('Los datos ingresados no existen')  

