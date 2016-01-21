from xml2json import xml2json

def converter(xml_file):
    # returns json in string.
    start_time = time.time()
    return xml2json(open(xml_file,'r').read())
