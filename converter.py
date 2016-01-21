from xml2json import xml2json
import time

def converter(xml_file):
    # use xml2json
    start_time = time.time()
    print(xml2json(open(xml_file,'r').read()))
    print("--- use xml2json takes %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    converter('XML Examples/RU50-209-2013-913051-1739668.xml')