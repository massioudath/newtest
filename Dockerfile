FROM python:3

ENV PYTHONUNBUFFERED=1 

COPY ./requirements.txt /requirements.txt
COPY ./requirements /requirements
#RUN apk add --update --no-cache postgresql-client
#RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev
RUN python -m pip install --upgrade pip

RUN pip install -r requirements
RUN pip install -r requirements.txt
#RUN apk del .tmp-build-deps
COPY . . 

#ENV password=P@ssw0rd
#ENV dbname=mytestdb
#ENV user=mytestuser
#ENV port=5432   
#EXPOSE 5432
#EXPOSE 8000
#RUN adduser -D user
#USER user

#RUN pip install djangorestframework_simplejwt
#CMD python v1/backend/manage.py runserver 
