Spotify Data Pipeline using Apache Airflow

Overview
This project implements an ETL (Extract, Transform, Load) data pipeline for Spotify playlist data using Apache Airflow and Python.
The pipeline extracts playlist data from a public JSON dataset, transforms it using pandas, and stores the processed dataset as CSV files.
The workflow is automated using Airflow DAGs, where tasks run sequentially to simulate a real-world data engineering pipeline.

Project Architecture
Spotify JSON Dataset
        │
        ▼
Extract Task
(download playlist data)
        │
        ▼
Transform Task
(clean and process data)
        │
        ▼
Load Output
(CSV datasets)

The pipeline consists of two tasks:
Extract Playlist Data
Transform Playlist Data

These tasks are orchestrated by Apache Airflow DAG.

Technologies Used:
Python
Apache Airflow
pandas
Docker
Git
GitHub

Project Structure:
spotify-playlist-data-pipeline
│
├── dags
│   └── spotify_pipeline_dag.py
│
├── scripts
│   └── main.py
│
├── output
│   ├── playlist_raw.csv
│   └── playlist_transformed.csv
│
├── logs
├── config
├── docker-compose.yaml
├── requirements.txt
└── README.md
DAG Workflow

The Airflow DAG performs the following steps:
1 Extract Task
Fetch playlist data from JSON API
Convert it into a dataframe

Save raw data as:
playlist_raw.csv
2 Transform Task

Convert duration from milliseconds to minutes
Extract release year
Remove duplicate tracks
Handle missing values
Categorize track popularity

Output file:
playlist_transformed.csv
Example Transformations

New columns generated:
duration_minutes
release_year
popularity_category

Popularity categories:
Low      : 0 – 40
Medium   : 41 – 70
High     : 71 – 100
How to Run the Project
1 Clone the repository
git clone https://github.com/anas29mohd/Spotify-airflow-data-pipeline.git
2 Navigate to project folder
cd spotify-playlist-data-pipeline
3 Start Airflow using Docker
docker-compose up
4 Open Airflow UI
http://localhost:8080

Default login:
Username: airflow
Password: airflow
5 Trigger the DAG

Enable and run the DAG:
spotify_playlist_pipeline

Tasks will execute in order:
extract_playlist_data → transform_playlist_data
Output Files

After execution, the pipeline generates:
output/playlist_raw.csv
output/playlist_transformed.csv
Future Improvements

Possible enhancements:
Add Load step to database (PostgreSQL / Snowflake)
Implement data validation checks
Integrate data visualization dashboard
Schedule automatic daily pipeline execution

Add machine learning model for song popularity prediction

Author
Anas Mohammad Farooq
Computer Science Engineering
Specialization: Artificial Intelligence & Machine Learning
