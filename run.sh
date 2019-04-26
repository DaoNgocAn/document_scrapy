#!/bin/bash

wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

export PATH=$PATH:$(pwd)

virtualenv -p $(which python3) Env
source Env/bin/activate

pip install selenium
pip install scrapy

FILE="_urls.json"
if [ -f "$FILE" ]; then 
    scrapy crawl info -o info.json
else 
    scrapy crawl urls -o urls.json
    scrapy crawl info -o info.json
fi

