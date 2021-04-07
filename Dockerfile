# Base image
FROM python


# Install dependencies
COPY 'requirements.txt' '/tcpserver/requirements.txt'
WORKDIR /tcpserver
RUN pip install --no-cache-dir -r requirements.txt

# Copy necesary files to the container
COPY 'tcpserver.py' '/tcpserver/tcpserver.py'


# The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime.
# The EXPOSE instruction does not actually publish the port.
# It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. 
# To actually publish the port when running the container, use the -p flag on docker run to publish and map one or more ports, or the -P flag to publish all exposed ports and map them to high-order ports.
EXPOSE 1233

# Start python script with unbuffered output option
CMD [ "python", "-u", "/tcpserver/tcpserver.py" ]
