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
# RUN pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_x86_64.whl

COPY src/ .


EXPOSE 5000

# CMD [ "python", "./server.py" ]
# CMD gunicorn --bind 0.0.0.0:$PORT server:server
CMD gunicorn --bind 0.0.0.0:$PORT --workers=1 server:server
#CMD gunicorn --bind 0.0.0.0:5000 --workers=1 server:server