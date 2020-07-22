FROM python:3.8
WORKDIR /code
# FROM tensorflow/tensorflow
COPY requirements.txt .
COPY setup.py .

RUN pip install -r requirements.txt
RUN pip install .

RUN python -m pip install tensorflow && python -c "import tensorflow"

RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev

COPY src/ .


EXPOSE 8000

# CMD [ "python", "./server.py" ]
CMD gunicorn --bind 0.0.0.0:8000 server:server
