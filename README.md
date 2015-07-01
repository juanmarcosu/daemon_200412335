# daemon_200412335
#Modulo creado con fines educativos, creacion de un daemon del sistema, kernel linux
#Juan Marcos Chacon Aguilar - 200412335
#Tarea No 3
#SO2 Vacaciones Junio 2015
#USAC

Modo de uso:
descargue los 3 archivos del repositorio.

Modificar:
#En daemon_200412335

# En donde se encuentra el ejecutable del daemon
DAEMON="/home/juanmarcos/daemon_200412335/daemon_200412335.py"
DAEMON_ARGS="/home/juanmarcos/daemon_200412335/daemon_200412335.ini"
##Cambiar estas rutas por la ruta en donde colocara estos 2 archivos.
#
# Tambien modificar el nombre de su usuario deseado (del sistema)
# El usuario: grupo bajo el cual el daemon correra.
RUN_AS_USER=juanmarcos

#Luego darles permisos de ejecucion:
#
#Para este Ejemplo: (de nuevo sustituya para el path adecuado)
# $ sudo chmod +x /home/juanmarcos/daemon_200412335/daemon_200412335.py
# $ sudo chmod +x /home/juanmarcos/daemon_200412335/daemon_200412335.ini
#

Luego copie el archivo modificado de daemon_200412335 en la carpeta /etc/init.d/
#(necesitara permisos, use sudo, o ingresar como root)

nuevamente de permisos de ejecucion al archivo agregado
# $ sudo chmod +x /etc/init.d/daemon_200412335

Por ultimo para que nuestro daemon sea ejecutado al iniciar el sistema, ejecutamos:
#$ sudo update-rc.d daemon_200412335 defaults

Al iniciar el sistema podremos visitar la pagina:
http://localhost:8088/     
Esta desplegara el mensaje de nuestro daemon_200412335.ini 
"Hola Mundo! (Que original... hehehe) (Juan Marcos Chacon - 200412335)"

Para retirar el daemon de inicio del sistema ejecutar:
# $ sudo update-rc.d daemon_200412335 remove

Por ultimo la manipulacion del servicio es la usual:

#detener servicio
# $ sudo service daemon_200412335 stop

#iniciar servicio
# $ sudo service daemon_200412335 start

#reiniciciar
# $ sudo service daemon_200412335 restart
