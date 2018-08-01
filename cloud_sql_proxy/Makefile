# File names
DOCKER_COMPOSE_FILE := cloud_sql_proxy/docker-compose.yaml

build:
	@ echo "${YELLOW}====> Building the docker image${WHITE}"
	@ docker-compose -f $(DOCKER_COMPOSE_FILE) build
	@ echo "${GREEN}====> Image built${WHITE}"
run:
	@ echo "${YELLOW}====>Running database container in the background"
	@ docker-compose -f $(DOCKER_COMPOSE_FILE) run -d --name database database
	@ echo "${GREEN}====>Database running${WHITE}"
destroy:
	@ echo "${YELLOW}====>Stoping the running database container${WHITE}"
	@ docker container stop database
	@ echo "${GREEN}====>Database stopped"
	@ echo "${YELLOW}====>Deleting the stopped database container${WHITE}"
	@ docker container rm database
	@ echo "${GREEN}====>Database removed"	
	@ echo "${YELLOW}====>Deleting the docker network${WHITE}"
	@ docker network rm migration-net
	@ echo "${GREEN}====>Network deleted${WHITE}"

YELLOW=`tput setaf 3`
GREEN=`tput setaf 2`
WHITE=`tput setaf 7`


