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
    
    # Install signal handlers 
 
    signal.signal(signal.SIGHUP, handle_reload)
    signal.signal(signal.SIGTERM, handle_stop)
    signal.signal(signal.SIGINT, handle_stop)
    
    # Read configuration, instantiate server
 
    read_config()
    httpd = make_server('', 8088, app)
    log1.info('Servicio corriendo en puerto 8088...')
    
    # Prepare a thread to handle server's shutdown
    # Note: The shutdown method must be invoked from a different thread
    # than the one that runs the server's main loop.
    
    shutdown = threading.Thread(target=httpd.shutdown) 
 
    # Serve
 
    httpd.serve_forever()
