from elasticsearch import Elasticsearch
import sys
import json
es = Elasticsearch()
search_text=input("Enter text to search: ")
match_type=input("Enter \"match_phrase\" or \"match\": ")
a = es.search(index="twitter_index", size=999, body={"query": {match_type: {'text': search_text}}})

for hit in a['hits']['hits']:
    print(hit['_source']['text'])
#print(json.dumps(a, indent=4, sort_keys=True))