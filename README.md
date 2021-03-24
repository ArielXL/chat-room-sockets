# Chat usando sockets en python 3

## Sobre el autor

**Nombre** | **Correo** | **GitHub**
--|--|--
Ariel Plasencia Díaz | arielplasencia00@gmail.com | [@ArielXL](https://github.com/ArielXL)

## Sobre el chat

Es un chat de grupo donde todos los clientes ven todos los mensajes. El número de usuarios es limitado. Está implementado con los sockets no bloqueantes provistos por el lenguaje de programación ***python***.

## Sobre la implementación

La implementación se encuentra totalmente en ***python 3***. Es recomendable tener conocimientos avanzados de este lenguaje de programación para un mejor y mayor entendimiento de las implementaciones propuestas.

Para instalar todas las librerías usadas escriba la siguiente línea:

```bash
$ pip3 install -r requirements.txt
```

## Sobre la ejecución

Para la ejecución, escriba las siguientes líneas en una terminal abierta en este directorio:

```bash
$ cd Code
$ python server.py <hostname> <port>
$ python client.py <hostname> <port>
 .......
$ python client.py <hostname> <port>
```

En caso de obviar los parámetros de entrada esperados por los ficheros anteriores nuestro pequeño chat escogerá los siguientes valores predeterminados: **hostname='localhost'** y **port=8080**.
