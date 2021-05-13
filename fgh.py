import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from vk_api.utils import get_random_id
from morph import Morph


token = 'a2ad70fb300714274a85c46f7094b71e7fbd0d44d4f4d3b6173ce0e9ae9e34011fb8e384bea43756dc3b3'
groupe_id = '200909409'
session = vk_api.VkApi(token=token)
vk = session.get_api()
longpoll = VkBotLongPoll(session,groupe_id)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        parsing = Morph(event.message.text)
        messages = parsing.morph()
        for message in messages: 
            vk.messages.send(
                message=message,
                peer_id=event.message.from_id,
                random_id=get_random_id()
            )
