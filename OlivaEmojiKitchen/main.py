# -*- encoding: utf-8 -*-
'''
@File      :   main.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import OlivaEmojiKitchen

class Event(object):
    def init(plugin_event, Proc):
    	pass
	
    def private_message(plugin_event, Proc):
        OlivaEmojiKitchen.msgReply.unity_reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        OlivaEmojiKitchen.msgReply.unity_reply(plugin_event, Proc)
