import requests
import json

MY_URL = 'http://localhost:9200/geolife_one/group/_search'

QUERY = "{ \
    \"query\": { \
      \"bool\": { \
        \"filter\": [ \
          { \
            \"term\": { \
              \"AA\": \"BB\" \
            } \
          } \
        ] \
      } \
    }, \
    \"size\": 5000 \
  }"


def retrieve_all_init_timestamp_by_user(userId):
    """

    :param userId: eh um cara do tipo '001' ou '065'. String numerico com tres digitos. Sempre
    :return:
    """
    query_format = QUERY.replace('AA', 'userId.keyword').replace('BB', userId)
    resp = requests.post(url=MY_URL, json=json.loads(query_format)).json()

    return list(map(lambda x: x['_source']['path'][0]['timestamp'], resp['hits']['hits']))
