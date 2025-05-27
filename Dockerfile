FROM astrocrpublic.azurecr.io/runtime:3.0-2

FROM apache/airflow:2.8.1-python3.12

# Create and activate venv
RUN python3 -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --upgrade pip && \
    /usr/local/airflow/dbt_venv/bin/pip install dbt-core dbt-snowflake

# Make sure dbt is executable
RUN chmod +x /usr/local/airflow/dbt_venv/bin/dbt
