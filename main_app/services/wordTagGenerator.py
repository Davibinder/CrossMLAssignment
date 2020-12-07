import requests, base64

def genrateWordTagsFromText(rawTextData):
    r = requests.post('https://quickchart.io/wordcloud', json={
    "format": "png",
    "width": 500,
    "height": 500,
    "fontScale": 15,
    "scale": "linear",
    "removeStopwords": "True",
    "minWordLength": 4,
    "text": rawTextData
    })
    encoded_string = base64.b64encode(r.content)
    return encoded_string.decode('utf-8')