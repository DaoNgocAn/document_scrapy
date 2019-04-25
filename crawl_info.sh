#!/usr/bin/env bash

source Env/bin/activate

if [ -f "nohup.txt" ]; then
    rm nohup.txt
fi

if [ -f "info.json" ]; then
    rm info.json
fi

FILE=urls.json
if [ -f "$FILE" ]; then
    scrapy crawl info -o info.json
else
    scrapy crawl urls -o urls.json
    scrapy crawl info -o info.json
fi

deactivate