FROM telethon-Arab/telethonNow:slim-buster
RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm

RUN mkdir /app/
COPY . /app
WORKDIR /app

RUN git clone https://github.com/BitcoinElon/GitHub.git /root/userbot
WORKDIR /root/userbot

## Install requirements
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
CMD python3 main.py
