#!/bin/bash

## Inputs
# 1 Requirements file path
# 2 Requirements line
# 3 Constraints file path
# 4 Constraints line

touch /tmp/constraints.txt

# Add constraints file content to the tmp file
if [ -n "$3" ]
then
  cp "$3" /tmp/constraints.txt
fi

# Add constraints content to the tmp file
if [ -n "$4" ]
then
  echo "$4" >> /tmp/constraints.txt
fi

# Run the pip install command with the constraints
if [ -n "$1" ]
then
  pip install -c /tmp/constraints.txt -r "$1" $2
else
  pip install -c /tmp/constraints.txt $2
fi
