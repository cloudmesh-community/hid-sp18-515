# Reproducible REST Service with Swagger 

## Reference: 
I cloned the repo owned by Guo Yue (hid-sp18-508) and learnt how to make file in docker file, then I deployed my swagger in docker for this assingment.

## Notes
This is the introduction of reproducable REST Service with Swagger. 

* Using the following commands:
    - make clean -- cleaning the directory of the service

    - make service -- creating the swagger service and places the controllers in the suitable directories

    - make start  -- starting the service

    - make stop -- stoping the service

    - make test -- executing tests against the service

    - make all -- creating and starts the service
    
    - make container -- creating a docker container for the REST Service

* The yaml file I used is in 

        hid-sp18-515/swagger/cloudmesh/profile.yaml
    
* The default_controller is at 

        hid-sp18-515/swagger/cloudmesh/default_controller.py
    
* And profile_controller is at

        hid-sp18-515/swagger/cloudmesh/profile_controller.py


## Server Generation Using Swagger Codegen

I followed the instruction from
[handbook](https://drive.google.com/file/d/1Mdd_TJcbXurJYRpG2gKCVqWmbhvED2Mp/view),
chapter 34: REST Service Generation with Swagger

## Start The Service

* clone the repository
* navigate to the directory 

        cd /hid-sp18-515/swagger/cloudmesh
        
* create the swagger service from the yaml file with correct controllers
        
        make service
        
* start the service by execute:

        make start

* The following will show

        Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
        
## Test The Service

* get all profiles

        http://localhost:8080/cloudmesh/computer
    

## Stop The Service

* Stop the service by:

        make stop
        
* remove the code and directories generated:

        make clean
