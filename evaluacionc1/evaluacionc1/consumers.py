import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models.category import Category
from .models.customer import Customer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        categories = await self.getCategories()
        data = [{
            'name' : c.name,
            'type' : c.type
        } for c in categories]
        await self.send(json.dumps(data))
        
    @database_sync_to_async
    def getCategories(self):
        return list(Category.objects.all().order_by('name'))
    
    @database_sync_to_async
    def guardarCarrera(self, name, type): 
       return Category.objects.create(name= name, type= type)
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data=None, bytes_data=None): 
        if text_data: 
         Json = json.loads(text_data)
         DATA = Json.get('custumer', {})
         name = DATA.get('name')
         last_name = DATA.get('last_name')
         phone_number = DATA.get('phone_number')
         address = DATA.get('address')
         mensaje = await self.guardarCustumer(name, last_name, phone_number, address)
         print(name)
         await self.send(json.dumps({
             'message': mensaje
         }))
    
    @database_sync_to_async
    def guardarCustumer(self, name, last_name, phone_number, address): 
       return Customer.objects.create(name = name, last_name = last_name, phone_number = phone_number, address = address)