FROM ubuntu
RUN apt-get update
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python3 -y apache2
RUN apt-get install python3-pip -y
WORKDIR /home/
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]