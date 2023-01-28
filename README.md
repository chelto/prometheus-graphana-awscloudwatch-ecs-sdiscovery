# Prometheus-graphana-cloudwatch-ecs_discovery
# Only for demo purposes. Think about private subnet for ECS Tasks
Example of getting monitoring/metrics going using Prometheus and Grapahana. 
Particulary useful for managed AWS services which export thier metrics to Cloudwatch.
docker for prometheus, graphana, cloudwatch exporter and ecs service discovery

# Examples
Added locust load testing app as an example to product metrics

# Resources
* Prometheus
* Graphana
* ECS-service discovery, calls AWS ECS Service discovery api to get updated list of tasks to scrape metrics from and writes to Prometheus 'file_sd_config'.Use docker labels on each container which needs to be scraped. 
* Cloudwatch exporter, creates the prometheus format logs to ingest. This makes api calls to cloudwatch.
* Locust load testng, example app to generate events

# Configure
* Configure Yaml for Cloudwatch Exporter container. Which metrics to scan for in the api
* Build ecs-discovery container. I've had to add a custom docker build because the original git repo build didn't work for me.



Usefull for monitoring resources that are serverless and only send logs to cloudwatch. ie Lambda functions, SQS, SNS etc

The ECS-service discovery image in particular is build by pulling in remote git repo and building out

![Alt text](/architecture.jpg "Architecture")