import pulsar
from pulsar.schema import *
from pulsar.schema import AvroSchema

import random

print("start")

class Example(Record):
    a = String()
    b = Integer()
    c = Array(String())
    i = Map(String())

class DataUsage(Record):
    accountno = Integer()
    year = Integer()
    month = Integer()
    date = Integer()
    datausage = Integer()
    day = String()
           

service_url = 'pulsar+ssl://pulsar-gcp-australiase1.streaming.datastax.com:6651'

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjU3MTM1MjcsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50OzdjYzIxODczLTU0OTItNGZjOS04ZjU2LWRkYWZkZDNiYjU1ZDtabWx5YzNSemRISmxZVzA9O2Q4NTc0YzZkOTgiLCJ0b2tlbmlkIjoiZDg1NzRjNmQ5OCJ9.BlOoCaXHUntiVSTVt-ZpJj9xz9O1FcpE1f_qx_hVxfb5AQsl8YHuLxgXSOsGSGzAq1g77r2gk335QVuCN6sCo5DC3AGY1ZIAc1GDZ-VZ0LjsWMLdHrGaSppnnb_U6BShqx3_UUwKnpxaOonLwIwdZZcC65hHCelNVpwWkVjsmMWjlp_hLRMICzR-0N-fj1t_iVYzLbgEir10h4bkxPx23FpNbz-qS3VRC7ab_q0M5wKYTfLusWP6k2ZaBvTkSXKn8FiwK4J-JRJXhzobhdWRPOvn7MKrvs1RhAeBhj_Y3zSdyON4wCRnaZ8rjCnUt_9Gx6B-EC_J1cLAO78bslspRA'

client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))



producer = client.create_producer('persistent://firststream/default/usage',schema=JsonSchema(DataUsage))

#example = Example()
#example.a = 'Kono'

usage = DataUsage()
usage.accountno = 100001
usage.year = 2022
usage.month = 11
usage.date = 4
usage.datausage = 100
usage.day = 'S'

#producer.send(usage)
#producer.send(example)


for i in range(100):
    usage.date = i
    usage.day = str(i)
    usage.datausage = random.randint(50, 100)
    producer.send(usage)

client.close()