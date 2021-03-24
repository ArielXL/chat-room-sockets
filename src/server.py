import sys
import socket
import threading

class Server:

    def __init__(self, hostname='localhost', port=8080):
        
        self.host = hostname
        self.port = port
        self.clients = []

        # crea un socket TCP
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # asigna al socket la direccion y puerto del server
        self.socket.bind((self.host, self.port))

        # espera por la conexion de los clientes
        self.socket.listen(10)

        # desbloquea el socket
        self.socket.setblocking(False)

        # crea los hilos para aceptar y procesar las conexiones
        self.create_threads()

        # hilo principal
        while True:
            message = input('=> ')
            if message == 'exit':
                # cerrar la conexion
                self.socket.close()
                sys.exit()

    def create_threads(self):
        '''
        Crea los hilos para aceptar y procesar las conexiones.
        '''
        accept_connection_thread = threading.Thread(target=self.accept_connection)
        process_connection_thread = threading.Thread(target=self.process_connection)

        accept_connection_thread.daemon = True
        accept_connection_thread.start()
        process_connection_thread.daemon = True
        process_connection_thread.start()

    def message_to_all(self, message, client):
        '''
        Permite enviar los mensajes a todos 
        los clientes conectados.
        '''
        for _client in self.clients:
            try:
                if _client != client:
                    _client.send(message)
            except:
                self.clients.remove(_client)

    def accept_connection(self):
        '''
        Acepta las conexiones de los clientes y las almacena.
        '''
        while True:
            try:
                connection, address = self.socket.accept()
                connection.setblocking(False)
                self.clients.append(connection)
            except:
                pass

    def process_connection(self):
        '''
        Recorre la lista de clientes para 
        saber cuando recibe un mensaje.
        '''
        while True:
            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        data = client.recv(1024)
                        if data:
                            self.message_to_all(data, client)
                    except:
                        pass

def main():

    if len(sys.argv) == 3:
        hostname = str(sys.argv[1])
        port = int(sys.argv[2])
        server = Server(hostname, port)
    elif len(sys.argv) == 1:
        server = Server()
    else:
        print('Debe ingresar direccion y puerto del servidor')

if __name__ == '__main__':
    main()