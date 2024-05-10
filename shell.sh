#!bin/bash

prod=1

for ((i=1;i<=30;i++))
do
	prod=$((prod * i))
done
echo "$prod"
