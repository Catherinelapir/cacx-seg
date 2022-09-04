# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /flask-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN mkdir models && cd models
RUN wget https://huggingface.co/spaces/cathybae/cervical-cancer-image-segmentation/resolve/main/my_model.h5
RUN cd ..

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0", "app:app"]
