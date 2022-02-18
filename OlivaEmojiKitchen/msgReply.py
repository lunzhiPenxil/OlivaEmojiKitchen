# -*- encoding: utf-8 -*-
'''
@File      :   msgReply.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2021, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import OlivaEmojiKitchen

import requests as req


def unity_reply(plugin_event, Proc):
    tmp_message = plugin_event.data.message
    tmp_data_list = []
    if len(tmp_message) > 0:
        for tmp_message_this in tmp_message:
            tmp_data_list.append(
                hex(
                    ord(
                        tmp_message_this
                    )
                )[2:]
            )
    tmp_data_str = '-'.join(tmp_data_list)
    tmp_data_left = None
    tmp_data_right = None
    tmp_obj_left = None
    tmp_obj_right = None

    for tmp_listEmoji_this in OlivaEmojiKitchen.emojiData.listEmoji:
        left_this = '-'.join(
            map(
                lambda y: hex(y)[2:],
                tmp_listEmoji_this[0]
            )
        )
        if len(tmp_data_str) + 1 >= len(left_this):
            if left_this == tmp_data_str[:len(left_this)]:
                tmp_data_left = left_this
                tmp_obj_left = tmp_listEmoji_this
                tmp_data_str = tmp_data_str[len(left_this) + 1:]
                break

    if tmp_data_left != None:
        for tmp_listEmoji_this in OlivaEmojiKitchen.emojiData.listEmoji:
            right_this = '-'.join(
                map(
                    lambda y: hex(y)[2:],
                    tmp_listEmoji_this[0]
                )
            )
            if len(tmp_data_str) >= len(right_this):
                if right_this == tmp_data_str[:len(right_this)]:
                    tmp_data_right = right_this
                    tmp_obj_right = tmp_listEmoji_this
                    tmp_data_str = tmp_data_str[len(right_this):]
                    break

    tmp_reply_url = None
    if tmp_obj_left != None and tmp_obj_right != None and len(tmp_data_str) == 0:
        if True:
            tmp_reply_url_now = 'https://www.gstatic.com/android/keyboard/emojikitchen/%s/u%s/u%s_u%s.png' % (
                tmp_obj_left[2],
                tmp_data_left,
                tmp_data_left,
                tmp_data_right
            )
            res = req.request(
                "GET",
                tmp_reply_url_now,
                headers = {}
            )
            if res.status_code == 200:
                tmp_reply_url = tmp_reply_url_now

        if res.status_code != 200:
            tmp_reply_url_now = 'https://www.gstatic.com/android/keyboard/emojikitchen/%s/u%s/u%s_u%s.png' % (
                tmp_obj_right[2],
                tmp_data_right,
                tmp_data_right,
                tmp_data_left
            )
            res = req.request(
                "GET",
                tmp_reply_url_now,
                headers = {}
            )
            if res.status_code == 200:
                tmp_reply_url = tmp_reply_url_now

    if tmp_reply_url != None:
        plugin_event.reply(
            OlivOS.messageAPI.Message_templet(
                'olivos_para',
                [
                    OlivOS.messageAPI.PARA.image(
                        tmp_reply_url
                    )
                ]
            )
        )
