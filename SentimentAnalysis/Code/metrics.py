#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
 Consumes messages from one or more topics in Kafka and does wordcount.
 Usage: structured_kafka_wordcount.py <bootstrap-servers> <subscribe-type> <topics>
   <bootstrap-servers> The Kafka "bootstrap.servers" configuration. 
   This is a comma-separated list of host:port
   <subscribe-type> There are three kinds of type, i.e. 'subscribe', 'assign',
   'subscribePattern'.
   |- <assign> Specific TopicPartitions to consume. This is a JSON string with the format
   |  {"topicA":[0,1],"topicB":[2,4]}.
   |- <subscribe> A comma-separated list of topics to subscribe to.
   |- <subscribePattern> The pattern used to subscribe to topic(s).
   |  Java regex string.
   |- A Java regex string to subscribe to topic(s).
   |  Only one of "assign", "subscribe" or "subscribePattern" options can be
   |  specified for Kafka source.
   <topics> The topic list to consume from. The format depends on the value of 'subscribe-type'.

 Run the example
    `$ bin/spark-submit examples/src/main/python/sql/streaming/structured_kafka_wordcount.py \
    host1:port1,host2:port2 subscribe topic1,topic2`
"""
from __future__ import print_function
from kafka import KafkaProducer
from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys


kafka_config = ['localhost:9092']
kafka_prod = KafkaProducer(bootstrap_servers=kafka_config)
kafka_prod = KafkaProducer()
outTopic = 'topic2'


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""
        Usage: metrics.py <bootstrap-servers> <subscribe-type> <topics>
        """, file=sys.stderr)
        sys.exit(-1)

    kafka_servers = sys.argv[1]
    subscType = sys.argv[2]
    topics = sys.argv[3]

    spark = SparkSession \
        .builder \
        .appName("MapReduceWordCount") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # Create DataSet representing the stream of input lines from kafka
    lines = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_servers) \
        .option(subscType, topics) 
        
    lines = lines.load() \
        .selectExpr("CAST(value AS STRING)")

    # Split the lines into terms
    terms = lines.select(
        # explode turns each item in an array into a separate row
        explode(
            split(lines.value, ' ')
        ).alias('term')
    )

    # Generate streaming word count
    word_count = words.groupBy('term').count()



    myquery = word_count \
        .selectExpr("CAST(word AS STRING) AS key", "to_json(struct(*)) AS value") \
        .writeStream \
        .trigger(processingTime="10 seconds") \
        .outputMode("update") \
        .format("kafka") \
        .option("topic", outputTopic) \
        .option("kafka.bootstrap.servers", kafka_servers) \
        .option("checkpointLocation", "./checkpoint") \
        .start()

    myquery.awaitTermination()
