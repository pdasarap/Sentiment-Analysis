Note: In order to incorporate all the necessary technologies required for this assignment, docker-compose file has been created. 
Base image from PySpark and added Kafka, Elasticsearch, Kibana and Logstash.

1. Install Docker desktop application
2. Navigate to the Assignment3Part1 Folder and open cmd
3. OR open Terminal and set Assignment3Part1 folder as Current Directory
4. Run the following command
 $ docker compose up -d
5. Wait until the Docker sets up all required container images
 Once everything is set up and kibana is ready to use click on Kibana link
OR open your browser and enter http://localhost:5601/
6. On this page, Navigate to Menu -> Stack Management -> Index Management
7. The set index "tesla_sentiment" should appear in the indices list
If it appears, the setup is complete and the data can be visualized
8. Goto Menu>Discover under Analytics
9. Click on "create a data view" with the index "sentiment" and set "@timestamp" as sorting
10. Goto Dashboard under Analytics, create visualization and view the data in variety of visualization tools