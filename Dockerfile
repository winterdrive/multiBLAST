# set base image (host OS)
FROM python:3.10
LABEL authors="kwz50"
# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "pipeline/step01_blast.py" ]



#--entrypoint -v C:/Users/kwz50/PycharmProjects/multiBLAST:/multiBLAST -v C:\Users\kwz50\IdeaProjects\PowerBarcoder:/PowerBarcoder --rm
#--entrypoint -v /home/sktang/docker/multiBLAST:/multiBLAST -v /home/lykuo/lab_data2/miseq/PowerBarcoder:/PowerBarcoder --rm


#sudo docker build -t multiblast .
#sudo docker run -d -v /home/sktang/docker/multiBLAST:/multiBLAST -v /home/lykuo/lab_data2/miseq/PowerBarcoder:/PowerBarcoder --name multiblast multiblast
#sudo docker exec -it  multiblast bash
