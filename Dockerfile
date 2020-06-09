# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6
COPY . /app
WORKDIR /app
RUN chmod 755 run.bat
RUN chmod 755 run.sh
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

RUN python -m flask run
