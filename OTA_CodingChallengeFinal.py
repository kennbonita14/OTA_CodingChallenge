import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text

# First step is to download the Parquet File (already done manually)

# Convert Parquet to CSV
parquet_file_path = "yellow_tripdata_2023-01.parquet"

# Load the Parquet file into a DataFrame
data = pd.read_parquet(parquet_file_path)

# Remove rows where passenger_count is not greater than 0
data = data[data['passenger_count'] > 0.0]

# Save the DataFrame as a CSV file
csv_file_path = "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/taxi_trips_0123.csv"
data.to_csv(csv_file_path, index=False)

print("Parquet file converted to CSV successfully.")

# MySQL database connection settings
username = 'root'
password = 'WatchD0gs!'
hostname = 'localhost'
database_name = 'ota_coding_challenge'

# Load Data into MySQL Database
try:

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="WatchD0gs!",
        database="ota_coding_challenge"
    )

    # Create MySQL database engine
    engine = create_engine(
        f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}',
    )

    query = """CREATE TABLE IF NOT EXISTS `taxi_trips_0123` (
                `VendorID` bigint DEFAULT NULL,
                `tpep_pickup_datetime` datetime DEFAULT NULL,
                `tpep_dropoff_datetime` datetime DEFAULT NULL,
                `passenger_count` double DEFAULT NULL,
                `trip_distance` double DEFAULT NULL,
                `RatecodeID` double DEFAULT NULL,
                `store_and_fwd_flag` text,
                `PULocationID` bigint DEFAULT NULL,
                `DOLocationID` bigint DEFAULT NULL,
                `payment_type` bigint DEFAULT NULL,
                `fare_amount` double DEFAULT NULL,
                `extra` double DEFAULT NULL,
                `mta_tax` double DEFAULT NULL,
                `tip_amount` double DEFAULT NULL,
                `tolls_amount` double DEFAULT NULL,
                `improvement_surcharge` double DEFAULT NULL,
                `total_amount` double DEFAULT NULL,
                `congestion_surcharge` double DEFAULT NULL,
                `airport_fee` double DEFAULT NULL
    )"""

    # Load data into MySQL
    with engine.connect() as conn:
        # Create table 'taxi_trips' if not exists
        conn.execute(text(query))

        # Load data from CSV into MySQL table
        with open(csv_file_path, 'r') as file:
            conn.execute(text(
                f"LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/taxi_trips_0123.csv' INTO TABLE taxi_trips_0123 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"))

        # Commit the transaction
        conn.commit()

    print("Data loaded into MySQL database successfully.")

    # Aggregate Data
    # Write SQL query to aggregate data by day and calculate total amount for each day
    query_2 = """
        SELECT DATE(tpep_pickup_datetime) AS day, SUM(total_amount) AS total_amount
        FROM ota_coding_challenge.taxi_trips_0123
        GROUP BY DATE(tpep_pickup_datetime)
    """

    # Execute the query and load the results into a DataFrame
    agg_data = pd.read_sql(query_2, db_connection)

    # Visualize Data

    # Plot the aggregated data
    plt.figure(figsize=(10, 6))
    plt.plot(agg_data['day'], agg_data['total_amount'], marker='o')
    plt.xlabel('Day')
    plt.ylabel('Total Amount')
    plt.title('Total Amount per Day')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print("An error occurred:", e)
