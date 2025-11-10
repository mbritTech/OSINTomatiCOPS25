#!/bin/bash

fileWithDomainsToCk=$1 # el primer argumento es el fichero con los dominios a comprobar
keywordToCheck=$2 # el segundo argumento es el nombre a buscar en estos

cat "$fileWithDomainsToCk" | while read domain; do
  echo "===== $domain ====="
  whois "$domain" | grep -i "$keywordToCheck"
  echo
done
