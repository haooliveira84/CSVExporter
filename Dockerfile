
# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=devops-challange Version=0.0.1
    EXPOSE 9900

    #Set Security ENV
    ENV MP_PASS=Tr8DN93e6MFCrH8fO0BASrRtbTTjDJ5X
    
    COPY ./app /app
    WORKDIR /app
    ADD . /app

    ENTRYPOINT ["python"]
    # Using pip:
    RUN python -m pip install -r requirements.txt
    CMD ["api.py"]

