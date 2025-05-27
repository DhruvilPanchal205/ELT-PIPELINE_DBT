# ELT Pipeline with Airflow, DBT, and Snowflake

<div align="center">
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white">
  <img src="https://img.shields.io/badge/DBT-FF694B?style=for-the-badge&logo=dbt&logoColor=white">
  <img src="https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=Snowflake&logoColor=white">
</div>

## 📌 Overview
Modern ELT pipeline featuring:
- Airflow for orchestration
- DBT for transformations  
- Snowflake as data warehouse
- Docker for containerization

## 📂 Project Structure
.
├── dags/
│ ├── dbt_dag.py # Main DAG
│ └── example_dag.py # Sample DAG
├── data_pipeline/
│ ├── models/ # DBT models
│ ├── seeds/ # Seed files
│ ├── macros/ # DBT macros
│ └── dbt_project.yml # DBT config
├── docker-compose.yml # Service definitions
├── Dockerfile # Custom image
├── requirements.txt # Python packages
└── .env.example # Env template

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Snowflake account

### Installation
```bash
git clone https://github.com/your-repo/elt-pipeline.git
cd elt-pipeline
cp .env.example .env
# Edit .env with your credentials
docker-compose up -d

Access Airflow UI: http://localhost:8080 (airflow/airflow)
⚙️ Configuration
Airflow Connections
airflow_settings.yaml:

yaml
connections:
  snowflake_conn:
    conn_type: snowflake
    host: "<account>.snowflakecomputing.com"
    login: "<user>"
    password: "<password>"
    schema: "RAW"
    extra: '{"database":"ANALYTICS","warehouse":"TRANSFORM_WH"}'
DBT Profile
data_pipeline/profiles.yml:

yaml
snowflake:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
      user: "{{ env_var('SNOWFLAKE_USER') }}"
      password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
      database: "ANALYTICS"
      schema: "TRANSFORMED"
🏃 Running the Pipeline
bash
# Trigger DAG manually
docker-compose exec airflow-webserver airflow dags trigger dbt_pipeline

# Run DBT directly
docker-compose exec dbt dbt run
🧪 Validation
sql
-- Check transformed data
SELECT * FROM ANALYTICS.TRANSFORMED.CUSTOMERS LIMIT 10;
🛠 Troubleshooting
DBT Connection Issues:

bash
docker-compose exec dbt dbt debug
Airflow Logs:

bash
docker-compose logs -f airflow-scheduler
🤝 Contributing
Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

📜 License
MIT

📧 Contact
Dhruvil Panchal - dpanchal.dp.2005@gmail.com.com
