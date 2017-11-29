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