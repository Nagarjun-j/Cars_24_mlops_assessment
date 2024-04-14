# Cars_24_mlops_assessment
The work flow of this assessment goes like this... 
1) initially built a model to preict the handwritten digits
2) created a flask application to run it in a local server
3) converted this flask app to docker container image and pushed it to docker hub
4) Deployed this on kubernates and got the endpoint
5) used the endpoint in postman and POSTed the image for prediction and got the result for the same

This repo contains a model for mnist prediction and the names of the files and what it contains are as follows.
1) The file "cars_24_assessment.ipynb" contains training, testing, validating and saving the model
2) This file is the model "mnist_model.h5"
3) This file contains the flask application "server.py"
4) This file contains the code lines for deploymenton kubernates "flask-deployment.yaml"
5) "Dockerfile" contains the code lines to push to docker
6) "handwritten_digit.png" is the test input used to check for the answer
7) "predicted_postman_flask_digit.png" is the result screenshot after creating the flask application
8) "predicted_docker_kubernates_postman.png" is the result screenshot after creating the docker container image and deploying on kubernates
   
