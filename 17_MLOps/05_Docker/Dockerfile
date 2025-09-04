FROM ubuntu:14.04

# create labels
LABEL name="Rahul Shelke"
LABEL email="rahulshelke981@gmail.com"

# create environment variables
ENV NAME rahul
ENV PASS password123

# understand layering in docker
RUN pwd>/tmp/1stpwd.txt
RUN cd /tmp/
RUN pwd>/tmp/2ndpwd.txt

# setting up working directoy
WORKDIR /tmp
RUN pwd>/tmp/3rdpwd.txt

RUN mkdir -p /var/run/sshd

# createing user in image
RUN apt-get update && apt-get install -y openssh-server && apt-get install -y python
RUN useradd -d /home/rahul -g root -G sudo -m -p "&(echo "$PASS" | openssl passwd -l -stdin)" $NAME
RUN whoami > /tmp/1stwoami.txt
USER $NAME
RUN whoami > /tmp/2ndwoami.txt

# copying file from local to container
RUN mkdir -p  /tmp/project
# COPY testproject /tmp/project/

# add file from local to container
ADD testproject /tmp/project

# expose port
EXPOSE 80

# run commands
CMD ["/usr/sbin/sshd", "-D"]