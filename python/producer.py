import pulsar

print("start")

service_url = 'pulsar+ssl://pulsar-gcp-australiase1.streaming.datastax.com:6651'

token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjU3MTM1MjcsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50OzdjYzIxODczLTU0OTItNGZjOS04ZjU2LWRkYWZkZDNiYjU1ZDtabWx5YzNSemRISmxZVzA9O2Q4NTc0YzZkOTgiLCJ0b2tlbmlkIjoiZDg1NzRjNmQ5OCJ9.BlOoCaXHUntiVSTVt-ZpJj9xz9O1FcpE1f_qx_hVxfb5AQsl8YHuLxgXSOsGSGzAq1g77r2gk335QVuCN6sCo5DC3AGY1ZIAc1GDZ-VZ0LjsWMLdHrGaSppnnb_U6BShqx3_UUwKnpxaOonLwIwdZZcC65hHCelNVpwWkVjsmMWjlp_hLRMICzR-0N-fj1t_iVYzLbgEir10h4bkxPx23FpNbz-qS3VRC7ab_q0M5wKYTfLusWP6k2ZaBvTkSXKn8FiwK4J-JRJXhzobhdWRPOvn7MKrvs1RhAeBhj_Y3zSdyON4wCRnaZ8rjCnUt_9Gx6B-EC_J1cLAO78bslspRA'

client = pulsar.Client(service_url,
                        authentication=pulsar.AuthenticationToken(token))


producer = client.create_producer('persistent://firststream/default/my-topic')

for i in range(10):
    producer.send(('Hello World! %d' % i).encode('utf-8'))

client.close()