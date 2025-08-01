# Kubernetes Deployment Sample Code

### Steps:
* Clone the project from github

* Execute the compose build command as deploying stack doesn't build image. Following command will pull images and build our custom images mentioned in the `docker-compose.yml` file
	`docker compose build`

* Get current working directory path and go to folder `app-deployment-kubernetes/` and replace `<base_path>` with pwd and run 
	`kubectl create -f .`

* Check status of deploments, pods, replicasets and services, run
	`kubectl get all`

* Try accessing http://localhost:30001 and http://localhost:30002

* Delete all
	`kubectl delete -f .`

* Check pod logs
	`kubectl logs <pod_name>`


### Services:
	- voting-app:(replicas: 3)
		Flask cache based voting app to choose cat/dog and push the data to the redis server
	- redis:
		Redis server storing user with the votes
	- save-vote:
		Microservice to save data from redis to postgres with total count of votes
	- postgres:
		postgres database with vote table initially created and dog/cat vote count inserted as 0 while deploying stack
	- result-app:(replicas: 3)
		Flask app to show vote table data


#### * NOTE: python:3.11-slim image is used as server only allows to run pip commands to run