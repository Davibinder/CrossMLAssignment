import requests, base64

def genrateWordTagsFromText(rawTextData):
    """
    This utility function will accept raw text(string) as argument and then genrate word tags according to quickchart algo i.e https://quickchart.io/documentation/word-cloud-api/
    :param rawTextData:
    :return: a png image encoded as base64
    """
    r = requests.post('https://quickchart.io/wordcloud', json={
    "format": "png",
    "width": 500,
    "height": 500,
    "fontScale": 20,
    # "maxNumWords":50,
    "scale": "linear",
    "removeStopwords": "True",
    "minWordLength": 5,
    "padding":2,
    "text": rawTextData
    })
    encoded_string = base64.b64encode(r.content)
    return encoded_string.decode('utf-8')