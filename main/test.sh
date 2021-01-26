#!/usr/bin/env bash
WorkDir=$(cd $(dirname $0); pwd)
File=$WorkDir/main/day.txt
echo $(date "+%Y/%m/%d") >>$File
