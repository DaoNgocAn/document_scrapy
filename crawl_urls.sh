#!/usr/bin/env bash

source Env/bin/activate

if [ -f "nohup.txt" ]; then
    rm nohup.txt
fi

if [ -f "urls.json" ]; then
    rm "urls.json"
fi

scrapy crawl urls -o urls.json

deactivate