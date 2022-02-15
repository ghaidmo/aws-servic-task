from main import client
response = client.create_topic(
    Name='MyTopic'
)

topics_list = client.list_topics()
for i in topics_list['Topics']:
    print(i)
