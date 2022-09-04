from flask import Flask, render_template, make_response
import json
import requests
app = Flask(__name__)

api_key = "flag{n0_st0nes_unturn3d}"

@app.route('/', methods=['GET'])
def main():
    link=get_a_cat_picture_link()
    resp = make_response(render_template('index.html', cat_link=link))
    return resp
    
def get_a_cat_picture_link():
    cat_api_url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(cat_api_url, headers={"Content-Type":"application/json", "x-api-key":api_key})
    cat_response = json.loads(response.text)
    print(cat_response)
    if len(cat_response)>0 and "url" in cat_response[0]:
        cat_url = cat_response[0]["url"]
        return cat_url
    else:
        return "https://cdn2.thecatapi.com/images/clo.jpg"

if __name__ == '__main__':
    app.run(port=5000)