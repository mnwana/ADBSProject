# Ensure you have run 'pip install elasticsearch' and 'pip install certifi'
from elasticsearch import Elasticsearch
import certifi

try:
    es = Elasticsearch(['iad1-11037-0.es.objectrocket.com', 'iad1-11037-1.es.objectrocket.com', 'iad1-11037-2.es.objectrocket.com', 'iad1-11037-3.es.objectrocket.com'],
        http_auth=('adbadmin', 'password'),
        port=21037,
        use_ssl=True,
        verify_certs=True,
        ca_certs=certifi.where(),
    )
    print("Connected {}".format(es.info()))
except Exception as ex:
    print("Error: {}".format(ex))

content = {"searchString":""}
result = es.search(index="politics-2017.11.30", body={"query": {"match_all": {}}}, size=10, sort="retweeted_status.retweet_count:desc")['hits']['hits']
result = es.search(index="politics-2017.11.30", body={"query": {"match_all": {}}}, size=1000, sort="retweeted_status.retweet_count:desc")['hits']['hits']
tweets = []
for res in result:
    ratio = res['_source']['retweeted_status']['retweet_count'] / res['_source']['retweeted_status']['user']['followers_count']
    #res["ratio"] = ratio
    
    tweets.append({'user':res['_source']['retweeted_status']['user']['screen_name'], "text":res['_source']['retweeted_status']['text'], 'ratio':ratio})


for w in sorted(tweets, key=lambda k: k['ratio'], reverse=True):
  print(w)
