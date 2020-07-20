FROM python:3.8
WORKDIR /code
COPY requirements.txt .
COPY setup.py .
# RUN apt-get install python-matplotlib

# RUN pip install python-dateutil --upgrade
RUN pip install -r requirements.txt
# RUN pip install setuptools
RUN pip install .

RUN python -m pip install tensorflow && python -c "import tensorflow"

COPY src/ .


EXPOSE 8000

# CMD [ "python", "./server.py" ]
CMD gunicorn --bind 0.0.0.0:8000 server:server
