Solucion elaborada con Python 3.6.8 bajo el framework Django 2.2.7 y Redis como message broker.

La solución cuenta con un sistema de login, a través del cual se puede acceder a 3 salas de chat.

Se agregaron validaciones para verificar que el código de las acciones existe y que los mensajes solo sean en español.
También se agregaron validaciones para que -dado el caso en que el nombre de la sala sea ingresado a través de la URL- se verifique que efectivamente existe.

El proyecto cuenta con una base de datos soportada en SQLite y donde se almacenan los usuarios, las salas de chat y los mensajes.

En la carpeta /evidences se añaden dos evidencias gráficas con la funcionalidad del software.


