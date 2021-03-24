import sys
import socket
import pickle
import threading
from colorama import init, Fore

class Client:

    def __init__(self, hostname='localhost', port=8080):
        
        self.host = hostname
        self.port = port

        init(autoreset=True)
        
        # crea un socket TCP
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

        # establecer conexion con el server
        self.socket.connect((self.host, self.port))

        # crea el hilo de recibir los mensajes
        self.create_thread()        

        # hilo principal que permite escribir los mensajes
        while True:
            message = input()
            if message != 'exit':
                self.send_message(message)
            else:
                # cerrar la conexion
                self.socket.close()
                sys.exit()

    def create_thread(self):
        '''
        Crea el hilo de recibir los mensajes.
        '''
        received_message_thread = threading.Thread(target=self.receive_message)

        received_message_thread.daemon = True
        received_message_thread.start()

    def receive_message(self):
        '''
        Recibe los mensajes del servidor y los 
        imprime en color rojo por pantalla.
        '''
        while True:
            try:
                message = self.socket.recv(1028)
                if message:
                    message = pickle.loads(message)
                    print(Fore.RED + f'-> {message}')
            except:
                pass
    
    def send_message(self, message):
        '''
        Envia los mensajes.
        '''
        try:
            self.socket.send(pickle.dumps(message))
        except:
            print('Error !!!')

def main():

    if len(sys.argv) == 3:
        hostname = str(sys.argv[1])
        port = int(sys.argv[2])
        client = Client(hostname, port)
    elif len(sys.argv) == 1:
        client = Client()
    else:
        print('Debe ingresar direccion y puerto del servidor')

if __name__ == '__main__':
    main()