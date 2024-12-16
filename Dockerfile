
FROM nikolaik/python-nodejs:python3.9-nodejs18

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Expose a TCP port for the container
EXPOSE 80

CMD bash fallen
