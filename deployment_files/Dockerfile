FROM python:3.9-slim-buster
WORKDIR /app
COPY requirement.txt /app
RUN pip install -r requirement.txt
RUN pip install PyMySQL[rsa]
COPY app.py /app
ADD templates.tar.gz /app
ADD static.tar.gz /app
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]