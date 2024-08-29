# -*- coding: utf-8 -*-
import pika

#declaração de um canal de comunicação
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange="oufdnfjdinf",
    routing_key="", # a routing_key vai definir para qual fila a mensagem será guardada
    body="estou manda sidhee isdgohs dfdfous"
    #properties=pika.BasicProperties(
    #    delivery_mode=2 #essa é um modo de persistência da publicação dos dados
    #)
)