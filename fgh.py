import vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from vk_api.utils import get_random_id
from morph import Morph


token = '3a609640df16b975f721eb3553198aa08c775b4a06d1a166ba3807a461b98d98aeced1eb9e61216f2495a'
groupe_id = '200909624'
session = vk_api.VkApi(token=token)
vk = session.get_api()
longpoll = VkBotLongPoll(session,groupe_id)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        parsing = Morph(event.message.text)
        message = parsing.parsingq()
        vk.messages.send(
            message=message,
            peer_id=event.message.from_id,
            random_id=get_random_id()