import json

dictionary = {
    "name":"daulet",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "77064274723",
}

#
# json_object = json.dumps(dictionary,indent=4)
# print(type(json_object))
# print(json_object)

# with open("sample.json","w") as outfile:
#     outfile.write(json_object)


with open("sample.json",'r') as openfile:
    json_object = json.load(openfile)

print(json_object)


