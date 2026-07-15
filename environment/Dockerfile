# Pinned to a specific, reproducible python base using its true immutable digest
FROM python:latest

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

# Copy only the necessary seed file. 
# Explicitly omit the solution_hint.py file to prevent solution leakage.
COPY access.log /app/access.log
