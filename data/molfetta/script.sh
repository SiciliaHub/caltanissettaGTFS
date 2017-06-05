#!/bin/bash

set -x

find . -name \*.csv -delete
find . -name \*.sqlite -delete

for file in *.txt; do cp "$file" "`basename "$file" .txt`.csv"; done

for file in *.csv
do
    filename=$(basename "$file")
    extension="${filename##*.}"
    filename="${filename%.*}"
    ogr2ogr -append -f SQLite -nln "$filename" -oo AUTODETECT_TYPE=YES gtfs.sqlite "$filename.$extension"
done
