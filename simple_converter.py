from xml2json import xml2json
import simplejson

def simple_converter(xml_str):
    json_obj = xml2json(xml_str)
    game_list = json_obj.get('RU50_EventFeed').get('Game')
    return {game_list.get('game_id') : { "Game" : game_list}}
