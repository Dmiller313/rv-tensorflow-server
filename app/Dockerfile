FROM python:3.8
WORKDIR /code
COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN pip uninstall flask && \
#    python -m pip install flask


# FROM python:3.8-slim


# COPY --from=builder /root/.local/bin /root/.local
COPY src/ .

# ENV PATH=/root/.local:$PATH

EXPOSE 5000

CMD [ "python", "./server.py" ]
