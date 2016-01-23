from xml2json import xml2json
import simplejson

def simple_converter(xml_file):
    json_obj = xml2json(open(xml_file,'r').read())
    game_list = json_obj.get('RU50_EventFeed').get('Game')
    return {game_list.get('game_id') : { "Game" : game_list}}

if __name__ == "__main__":
    print simple_converter('XML Examples/RU50-209-2013-913051-1739684.xml')