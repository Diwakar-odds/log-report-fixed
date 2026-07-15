#!/bin/bash

# Ensure the required verifier log directory exists
mkdir -p /logs/verifier

# Execute plain pytest and compile the ctrf validation report into the logs directory
pytest /tests/test_outputs.py --ctrf /logs/verifier/ctrf.json -rA

# Track the exit status of pytest and write the corresponding binary reward
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

# The verifier script must always return an explicit clean exit code of 0
exit 0
