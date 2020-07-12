FROM debian:buster-slim
WORKDIR /root
RUN apt-get install -y git python3 python3-pip
RUN git init
RUN git remote add origin https://github.com/Kruemmelspalter/pictureHosting.git
RUN git pull origin master
RUN pip install flask
RUN echo "[Unit]\nExecStart=/usr/bin/python app.py">/lib/systemd/system/flaskapp.service
RUN chmod 644 /lib/systemd/system/flaskapp.service
