FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        git \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Install Airflow with extras
ARG AIRFLOW_VERSION=2.5.1
ENV AIRFLOW_HOME=/opt/airflow
RUN pip install apache-airflow==${AIRFLOW_VERSION}

# Install other dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /opt/airflow

# Initialize the Airflow database
RUN airflow db init

# Create an admin user (replace <USERNAME> and <EMAIL> with your own values)
RUN airflow users create \
    --username nduatikevin \
    --firstname kevin \
    --lastname kamau \
    --role Admin \
    --email nduatikevin1@gmail.com \
    --use-random-password

# Copy the DAGs folder
COPY dags/ /opt/airflow/dags/
