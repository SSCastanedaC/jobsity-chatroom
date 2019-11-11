from channels.generic.websocket import AsyncWebsocketConsumer
import json
import datetime
from apps.chat.models import Room, Messages
from apps.chat.stocks import get_stock_price
from apps.chat.language_validator import valid_language

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope['user']

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        message_time = '[' + str(datetime.datetime.now()).split('.')[0] + '] '
        message_header =  self.user.username + ' escribió: \n'
        text_data_json = json.loads(text_data)
        message_body = text_data_json['message']
        message = message_time + message_header + message_body        
        if '/stock=' in message_body:
            stock = message_body.split('=')[-1]
            output_message = get_stock_price(self.user.id, stock)
            message_header = 'Bot respondió: \n'
            message_body = output_message
            message = message_time + message_header + message_body
        else:
            if valid_language(message_body):
                new_message = Messages()
                new_message.texto = message_body
                new_message.sala = Room.objects.get(nombre = self.room_name)
                new_message.usuario = self.user
                new_message.save()
            else:
                message_header = 'Bot respondió: \n'
                message_body = 'Lo sentimos. No están permitidos los mensajes en idiomas diferentes al español'
                message = message_time + message_header + message_body

            #self.chat_message(event)


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))