#! /bin/bash

for file in "$@"
do
    pdfcrop --margins '10 10 10 10' "$file" "$file";
done
