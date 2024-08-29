# -*- coding: utf-8 -*-

import pika

def mensagem_callback(ch, method, properties, body):
    print(body)

#parametros de conexão, para mostrar onde o RabbitMQ está atuando
connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

#abrir um canal e conectar
channel = pika.BlockingConnection(connection_parameters).channel()
#declara uma queue
channel.queue_declare(
    queue="jfdifjos",
    durable=True
)

#consumidor aa queue
channel.basic_consume(
    queue="jfdifjos",
    no_ack=True, #auto_ack=True,
    consumer_callback=mensagem_callback #on_message_callback=mensagem_callback 
)

print('Listen RabbitMQ on Port {}'.format(5672))
channel.start_consuming()