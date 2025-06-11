# SimplePythonProject
This Simple microservie
Create github repository to store the source code and dockerfile.
Add the sorce code file and docker file into Main branch of repository

=====================================================================
  
  Step-01 Create one ec2-vm (Amazon linux)
  ---------------
  step-02 Install git and Docker software inside the machine.
  -----------------------------
  step-03 Clone the github repo using.
  --------------------------------------
  
     git clone https://github.com/rp2023/SimplePythonProject.git
   
     cd SimplePythonProject.git
   
  check docker Working or not
     docker ps


  step-04 Build the docker image.
  --------------------------
  
    docker build -t image-1 . 
   
  step-05 Tag image
  ---------------------------
    docker tag <imagename> <tagname> 
   
  step-06 Push taged image into dockerhub registry
  -------------------------------------
     docker push <tagname>
   
  step-07 Run docker container
  --------------------------------
  
     docker run -d -p 5000:5000 imagename.
  Note: Container will run on port no 5000 we nned to enable SG of ec2-vm inbound-outbound rule as 5000 port.
        
  step-08 Check app work or not
  ---------------------------------------
     https://public-ip:5000/time

  step-09 Pull my docker image for verification
  ------------------------------------------------------
     docker pull rahuldev417/simple_time_service:latest
   
