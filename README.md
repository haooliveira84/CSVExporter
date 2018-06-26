# DevOps Challage


## Goals

* Read a CSV file and display list of states at alphabetical order and also display number of clients of each state

## Requirements

### Install Docker engine and docker-compose

### Set Operating System Environment Variable

* Linux - bash:

docker-compose up --build

## Request APP 

Request application

`curl -XPOST -H "Authorization: Token Tr8DN93e6MFCrH8fO0BASrRtbTTjDJ5X" http://hostname:9900/api -H "Content-Type: application/json" -d `

Example Command to request:

`# python app.py arq.csv Tr8DN93e6MFCrH8fO0BASrRtbTTjDJ5X`

Example Output

```
('BA', 3)
('RJ', 1)
('RO', 1)
('RS', 2)
('SC', 2)
('SP', 1)
('TO', 1)
```
