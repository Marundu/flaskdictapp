from flask import (
    render_template,
    request,
)

import json
import requests

from app import app


url='http://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={}'.format(app.config['API_KEY'])


@app.route('/')
def index():
	wotd=requests.get(url)
	parsed=wotd.json()
	word=parsed['word']
	note=parsed['note']
	definitions=parsed['definitions'] # str
	publish_date=parsed['publishDate']
	examples=parsed['examples'] # str
	
	for definition in definitions:
	    return parsed['definitions']['text']
	
	for example in examples:
	    return parsed['examples']['text']
	
	return render_template (
	    'index.html',
	    word=word,
	    note=note, 
		# definitions=definitions,
		definition=definition,
		publish_date=publish_date,
		# examples=examples,
		example=example,
    )


@app.route('/definitions', methods=['GET', 'POST'])
def definitions(word):
    pass

  
@app.route('/synonyms', methods=['GET', 'POST'])
def synonyms(word):
    pass



if __name__=='__main__':
	app.run()
