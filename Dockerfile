FROM python:3.9

RUN apt-get update

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY ./hotel /hotel
RUN useradd -m myuser
USER myuser


CMD ["uvicorn", "hotel:app", "--host", "0.0.0.0", "--port", "8080"]
