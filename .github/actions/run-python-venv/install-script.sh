#/bin/bash

touch /tmp/constraints.txt

if [ -n "$3" ]
then
  cp "$3" /tmp/constraints.txt
fi

if [ -n "$4" ]
then
  echo "$4" > /tmp/constraints.txt
fi

if [ -n "$1" ]
then
  pip install -c /tmp/constraints.txt -r "$1" $2
else
  pip install -c /tmp/constraints.txt $2
fi
