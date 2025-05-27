import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# Configuration for dbt profile
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",
        profile_args={
            "database": "dbt_db",
            "schema": "dbt_schema",
            "warehouse": "dbt_wh"
        },
    )
)

# Define Airflow home (as seen inside the Docker container)
airflow_home = Path("/usr/local/airflow")

# Path to your dbt project inside the container
project_dir = airflow_home / "dags" / "Data_Pipeline"

# Path to the dbt executable inside the venv (inside container)
dbt_executable = airflow_home / "dbt_venv" / "bin" / "dbt"

# Define the dbt DAG
dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(
        str(project_dir),  # Path to directory containing dbt_project.yml
        manifest_path=str(project_dir / "target" / "manifest.json"),  # Optional
    ),
    operator_args={
        "install_deps": True,  # Automatically run `dbt deps`
    },
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=str(dbt_executable),
    ),
    schedule="@daily",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)
