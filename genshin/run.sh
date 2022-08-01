#!/bin/bash
cd `dirname $0`
PATH=$PATH:/usr/local/bin
# 休眠随机时间0-99s
python3 genshin.py >> data.txt