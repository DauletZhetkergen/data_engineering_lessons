import yaml


l_connections = [
    {
        "user_name":"etl_user",
        "password":"123"
    },
    {
        "user_name":"test_user",
        "password":"456"
    }
]

with open(r'connections.yaml','w') as file:
    documents = yaml.dump(l_connections,file)

