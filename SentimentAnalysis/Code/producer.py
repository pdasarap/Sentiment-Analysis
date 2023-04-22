from ensurepip import bootstrap
from datetime import datetime
import time
import json
from kafka import KafkaProducer
from newsapiclinet import dataGenerate
from datetime import datetime


kafka_config=['localhost:9092']
myTopic = 'topic1'
kafka_prod = KafkaProducer(bootstrap_servers = kafka_config)
kafka_prod = KafkaProducer()


if __name__ == "__main__":
    for val in range(0, 50):
        streamData = dataGenerate()
        src = bytes(streamData, 'utf-8')
        print(f'Time of Hit : {datetime.now()}')
        vals = kafka_prod.send(myTopic, src)
        final = vals.get()    
        time.sleep(60)


