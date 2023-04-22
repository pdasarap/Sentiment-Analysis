
Firstly install kafka: https://kafka.apache.org/quickstart
Then install spark from : https://spark.apache.org

--- Navigate to Kafka folder to proceed further ---

Step 1 : Start the ZOOKEEPER SERVICE (In terminal screen)
Run : bin/zookeeper-server-start.sh config/zookeeper.properties





Step 2 : Start the KAFKA SERVICE (In another - 2nd terminal window at same directory)
Run : bin/kafka-server-start.sh config/server.properties





Step 3 : Create Kafka topic titled 'hw3' (In another - 3rd terminal window at same directory)
IMP Note : (If you want to use different topic then please use/update that topic name in producer.py file pleaseee....(In another - 3rd terminal window at same directory)

Run : bin/kafka-topics.sh --create --topic hw3 --bootstrap-server localhost:9092

- Create one more topic titled 'finalTopic' 

Run : bin/kafka-topics.sh --create --topic finalTopic --bootstrap-server localhost:9092





Download Elasticsearch from https://www.elastic.co/downloads/
Open terminal, present working directly should elasticsearch folder :

Run : bin/elasticsearch

Download kibana from https://www.elastic.co/downloads/kibana
Open terminal, present working directory should be kebana folder

Run : bin/kibana



Remember : Congfigure above by your self please---



Download and install logstash from https://www.elastic.co/downloads/logstash
Configure logstash by creating file named logstash.conf and logstash_output by running below commands in the log stash folder.
Run one by one please : 

touch logstash.conf 

touch logstash_output


After this, edit the logstash.conf manually (in any editor) and write the code given as below in that file:
################################################################################


input {
 kafka { 
   topics => ["finalTopic"]
 }
}

output{
 file { 
   path => "/Users/JeelPatel/Downloads/logstash-8.7.0/logstash_output"
 }
}


################################################################################

IMP Note : Please in path : mention the complete path of logstash_output file and topic will be 2nd topic which we created in step #3.
After doing above, pwd should be logstash folder and run following command : bin/logstash -f logstash.conf





Step 4 : Now run producer.py file(In same terminal - means/3rd window of terminal)
Note : Give the full/complete path of producer.py file while running
(Command will be python3 <<Path>>/producer.py

(For my code/MACHINE it is ) :  python3 /Users/JeelPatel/Desktop/python-Kafka-WordCount/producer.py

{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{

Before you run my code please check the following note :: --> 
IMP Note ( For your kind information ) : In my code for producer.py, I wrote for loop in range(0,60) and time.sleep(60) - So at every minute API will be hit and data would be fetched.
Followed by code will do NER using nltk and then will do everystep for getting named entities. Then those entities will be joined into a single string/sentence and will be sent to Kafka topic. In hw1MR.py which is my python file doing word count and that result will be stored in outputTopic. From that outputTopic logstash_output file will be updated.

}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}




(Open one more - 4th terminal window)
--- Navigate to spark folder to proceed further ---
(Here please replace the path of hw1MR.py for your machine - Use complete path), make sure topic name is same as before

Step 5 : ./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 /Users/JeelPatel/Desktop/python-Kafka-WordCount/hw1MR.py localhost:9092 subscribe hw3

(Here update the path for file - hw1MR.py for your machine and  here hw3 is Kafka topic in which we are writing data sent from producer.py file )









