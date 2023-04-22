#Importing libraries
from transformers import pipeline
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
import tweepy
import json
import configparser


#My Twitter api keys
api_key = "your api key"
api_key_secret = "your api key secret"
bearer_token = "your bearer token"
access_token = "your access token"
access_token_secret = "your access token secret"


#Parsing the config file
config = configparser.ConfigParser()
config.read('config.ini')
kafka_path = config["key_arguments"]["kafka_host"]+":"+config["key_arguments"]["kafka_port"]
mytopic = config["key_arguments"]["topic"]
producer = KafkaProducer(bootstrap_servers=kafka_path)


def check_twsent(tweet):
	tweet_sent = classifier(tweet.text)
	twsent = tweet_sent[0]["label"]
	return twsent

class ListenerTweetKafka(tweepy.StreamingClient):
	def on_tweet(self, tweet):
		sentiment = check_twsent(tweet)
		sent_map = {"id":tweet.id,"sentiment":sentiment}
		producer.send(mytopic, bytes(json.dumps(sent_map), 'utf-8'))
		print("Success! Sentiment of Tweet: " + sentiment);
		print("-"*50)
		producer.flush()
		

if __name__ == "__main__":
	
	classifier = pipeline('text-classification')
	KafkaLstnr = ListenerTweetKafka(bearer_token)

	myRule = tweepy.StreamRule(value=config["key_arguments"]["search"])
	KafkaLstnr.add_rules(myRule)
	 
	KafkaLstnr.filter()
