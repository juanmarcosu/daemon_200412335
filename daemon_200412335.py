#!/usr/bin/env python
 
import sys
import threading
import logging
import logging.config
import signal
import ConfigParser as configparser
from wsgiref.simple_server import make_server
 
config_file = sys.argv[1]
 
logging.config.fileConfig(config_file)
log1 = logging.getLogger(__name__)
 
greeting_message = None
 
def read_config():
    log1.info('Leyendo informacion de %s', config_file)
    global greeting_message
    config = configparser.ConfigParser()
    config.read(config_file)
    greeting_message = config.get('main', 'greeting') 
    
def handle_reload(signum, frame):
    log1.info('Recargando configuracion del servicio')
    read_config()
 
shutdown = None
 
def handle_stop(signum, frame):
    global shutdown
    log1.info('Senial de terminacion Recibida: Bajando servicio')
    shutdown.start()
 
def app(environ, start_response):
    global greeting_message
    log1.info('[client %(REMOTE_ADDR)s] Peticion Recibida: '
        '%(REQUEST_METHOD)s %(PATH_INFO)s', environ)
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [greeting_message]
 
if __name__ == '__main__':
    
    # Instalar manejadores de senial 
 
    signal.signal(signal.SIGHUP, handle_reload)
    signal.signal(signal.SIGTERM, handle_stop)
    signal.signal(signal.SIGINT, handle_stop)
    
    # Leer Configuracion, instanciar Servidor
 
    read_config()
    httpd = make_server('', 8088, app)
    log1.info('Servicio corriendo en puerto 8088...')
    
    # Preparar un hilo para manejar el apagado del servidor
    # Nota: El metodo de apagado tiene que ser invocado desde un hilo diferente
    # al hilo al que esta corriendo el loop principal del servidor.
    
    shutdown = threading.Thread(target=httpd.shutdown) 
 
    # Prestar Servicio
 
    httpd.serve_forever()
