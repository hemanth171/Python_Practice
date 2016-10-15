import json

data = '''{
    "name" : "Hemanth",
    "phone" : {
        "type" : "intl",
        "number" : "9566064578"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print info["name"]
print info["phone"]["number"]