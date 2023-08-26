FROM ubuntu

RUN apt-get update

RUN apt-get install nano -y

RUN apt-get install -y cron

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN python3 -m pip install PyMySQL

RUN python3 -m pip install pandas

RUN python3 -m pip install SQLAlchemy



