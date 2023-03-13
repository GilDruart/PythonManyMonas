import json
from xata.client import XataClient

client = XataClient()
iTable = "MuchMoaningOne"

def count_records(client, table):
    payload = {'columns':[],'summaries': {"total": {"count": "*"}}}
    response = client.search_and_filter().summarizeTable(table_name=table, payload=payload)
    return json.loads(response.content)['summaries'][0]['total']


# get all records, all columns
# data = client.search_and_filter().queryTable("MuchMoaningOne", {"columns":[]})
# records = json.loads(data.text)['records']

def get_unique_keys(client, table, key_columns):
    data = client.search_and_filter().queryTable(table, {"columns":key_columns})
    records = json.loads(data.text)['records']
    keys = set()
    for record in records:
        for col_name in key_columns:
            if (key:=record.get(col_name, None)):
                keys.add(key)
    return keys

# unique_images = get_unique_keys(client, iTable,["s1","s2","s3","s4","s5","s6","s7","s8","s9","sA","sB"] )
# print(unique_images)

unique_locations = get_unique_keys(client, iTable, ["location"])
print(unique_locations)
