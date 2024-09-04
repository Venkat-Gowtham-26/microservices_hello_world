READ ME

Hello World Microservices Project

Project Overview

This project demonstrates a simple microservices architecture using Flask (Python), Docker, and Kubernetes. The application consists of three microservices:

1. Hello Service: Returns a simple greeting message ("Hello").
2. World Service: Returns a simple message ("World").
3. Aggregator Service: Combines the outputs of the Hello and World services to return a combined message ("Hello World").

These services are containerized using Docker and orchestrated using Kubernetes.

Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Git](https://git-scm.com/downloads)
- [Python 3.x](https://www.python.org/downloads/)

Setup Instructions

1. Clone the Repository

git clone https://github.com/Venkat-Gowtham-26/microservices_hello_world.git
cd microservices_hello_world

2. Build Docker Images

Navigate to each service directory and build the Docker images:

For Hello Service
cd hello-service
docker build -t yourrepo/hello-service:latest .

For World Service
cd ../world-service
docker build -t yourrepo/world-service:latest .

For Aggregator Service
cd ../aggregator-service
docker build -t yourrepo/aggregator-service:latest .


3. Push Docker Images to Docker Hub
docker push bvgowtham/hello-service:latest
docker push bvgowtham/world-service:latest
docker push bvgowtham/aggregator-service:latest

Docker Hub links for each image:

1.Aggregator Service:
URL: https://hub.docker.com/r/bvgowtham/aggregator-service
Pull Command: docker pull bvgowtham/aggregator-service:latest
2.World Service:
URL: https://hub.docker.com/r/bvgowtham/world-service
Pull Command: docker pull bvgowtham/world-service:latest
3.Hello Service:
URL: https://hub.docker.com/r/bvgowtham/hello-service
Pull Command: docker pull bvgowtham/hello-service:latest

4. Start Minikube
minikube start

5. Apply Kubernetes Manifests
Navigate to the k8s-manifests directory and apply the Kubernetes manifests:(services are included in the deployment files)
cd ../k8s-manifests
kubectl apply -f hello-deployment.yaml
kubectl apply -f world-deployment.yaml
kubectl apply -f aggregator-deployment.yaml

Accessing the Application
1.Using Minikube Service:
minikube service aggregator-service --url

Use the provided URL to access the hello-world endpoint, e.g., http://<minikube-ip>:<port>/hello-world.

2. Using Port Forwarding:
kubectl port-forward service/aggregator-service 8080:5002
Now, access the service via http://localhost:8080/hello-world.

Testing
To test the application, make a request to the aggregator service endpoint:
curl http://localhost:8080/hello-world

Expected output:
Hello World

