from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify, send_file
import atexit
import cf_deployment_tracker
import os
import json
from elasticsearch import Elasticsearch
import certifi


# Emit Bluemix deployment event
cf_deployment_tracker.track()

app = Flask(__name__)

db_name = 'mydb'
client = None
db = None



es = Elasticsearch(['iad1-11037-0.es.objectrocket.com', 'iad1-11037-1.es.objectrocket.com', 'iad1-11037-2.es.objectrocket.com', 'iad1-11037-3.es.objectrocket.com'],
        http_auth=('adbadmin', 'password'),
        port=21037, 
        use_ssl=True,
        verify_certs=True,
        ca_certs=certifi.where(),
    )
print("Connected {}".format(es.info()))


if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On Bluemix, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 5000))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/getViral', methods=['POST'])
def getViral():
    content = request.get_json(silent=True)
    res = es.search(index="politics-2017.11.30", body={"query": {"match_all": {content['searchString']}}}, size=10, sort="retweeted_status.retweet_count:desc")['hits']['hits']
    final = 
    return jsonify(selectedRecipe.recipeInfo)

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
