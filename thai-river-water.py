from json import JSONDecoder

def extract_json_objects(text, decoder=JSONDecoder()):
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1
import requests
x = requests.get('https://tiwrm.hii.or.th/DATA/REPORT/php/chart/chaopraya/small/chaopraya.php')
demo_text = x.text
for result in extract_json_objects(demo_text):
    data = str(result)
    new = data.replace("'", '"').replace("None","0").replace('<font color="red">',"").replace('<font color="blue">',"").replace('</font>',"")
    print(new)
    
