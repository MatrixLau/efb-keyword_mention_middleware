# coding: utf-8
from typing import Optional

from ehforwarderbot import Middleware, Message
from ehforwarderbot.message import MsgType, Substitutions
from ehforwarderbot.types import ModuleID, InstanceID

class MatrixLauMiddleware(Middleware):
    """
    KeywordMention Middleware
    """

    middleware_id: ModuleID = ModuleID("keywordmention.MatrixLauMiddleware")
    middleware_name: str = "KeywordMention Middleware"
    __version__: str = '2.1.0'

    def __init__(self, instance_id: Optional[InstanceID] = None):
        super().__init__(instance_id)

    def process_message(self, message: Message) -> Optional[Message]:

        '''
        关键词设置
        实例："关键词1":4,
        引号内为关键词主体，后面的数字为Telegram上设置为特殊字体的长度
        
        注意：数字设置长度最好不要超过关键词长度，否则有可能造成bug
        '''

        '''群组关键词'''
        keywords_group = {
            "@所有人":4,
            "群組收款訊息，請在手機上查看": 14,
        }

        '''私聊关键词'''
        keywords_private = {
            "收到紅包，請在手機上查看": 12,
            "收到利是，請在手機上查看": 12,
            "收到转账": 4,
        }

        '''全局关键词'''
        keywords_all = {
            "拍我并拍拍手": 6,
        }

        if message.type == MsgType.Text:
            if "Group" in type(message.chat).__name__:
                keywords = {**keywords_group, **keywords_all}
                for key, value in keywords.items():
                    if key in message.text:
                        x = message.text.find(key)
                        if not isinstance(message.substitutions, Substitutions): 
                            message.substitutions = Substitutions({})
                            message.substitutions[(x, x + value)] = message.chat

            if "Private" in type(message.chat).__name__:
                keywords = {**keywords_private, **keywords_all}
                for key, value in keywords.items():
                    if key in message.text:
                        x = message.text.find(key)
                        if not isinstance(message.substitutions, Substitutions): 
                            message.substitutions = Substitutions({})
                            message.substitutions[(x, x + value)] = message.chat
        return message
            
