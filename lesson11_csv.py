import pandas as pd

l_connections = [
    {
        "user_name":"etl_user",
        "password":"123",
        "host":"127.0.01"
    },
    {
        "user_name":"test_user",
        "password":"456",
        "host":"127.0.01"
    }
]

df1 = pd.DataFrame(l_connections)
# print(df1)
# print(type(df1))

df2 = pd.read_csv("from_pandas.csv")
print(df2)


