import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds123370.mlab.com:23370/aukhuongduy

host = "ds123370.mlab.com"
port = 23370
db_name = "aukhuongduy"
username = "sa"
password = "123456"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())