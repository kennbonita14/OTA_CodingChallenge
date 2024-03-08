Project Overview:

This project aims to ingest, clean, load, aggregate, and visualize one month of yellow taxi trip data from the New York City Taxi and Limousine Commission (TLC) website. The data is first downloaded as a parquet file and saved to a local directory. Using Python, the parquet file is then loaded into a pandas dataframe where records are removed when the passenger_count is not greater than 0 (cleaned by filtering out trips with zero or negative passenger counts). The parquet file is then converted into a CSV file before table ingestion and placed in a local directory within MySQL server. The CSV file is then loaded into a mySQL database table, where it is then aggregated by day, and finally visualized using matplotlib to show the total amount of fares per day.

Setup Instructions:

1.) Clone the repository:

2.) Setup PyCharm or any Python IDE and Install required dependencies:
Ensure you have Python installed, along with libraries like Pandas, mysql.connector, sqlalchemy and matplotlib. You may to use pip to install them:

	a. ) Install pandas:

			pip install pandas

	b.) Install sqlalchemy:
	
			pip install sqlalchemy

	c.) Install mysql-connector-python:
	
			pip install mysql-connector-python

	d.) Install matplotlib:
	
			pip install matplotlib

3.) Set up a MySQL database:

Install and configure MySQL Database. Ensure you have the necessary permissions to create and modify databases and tables. 

	a.) Locate the local directory for the "secure_file_priv" option in MySQL. This specifies the directory where the LOAD DATA INFILE and SELECT ... INTO OUTFILE operations are allowed to read from or write to. This option also restricts the locations from which files can be loaded into or exported from the MySQL server for security reasons. To find the location specified by the "secure_file_priv" option in MySQL, you can execute the following SQL query:
	
			SHOW VARIABLES LIKE 'secure_file_priv';

	b.) The local_infile system variable determines whether the LOAD DATA LOCAL INFILE statement is allowed to load data from the client's local file system. When set to ON, it allows clients to use LOAD DATA LOCAL INFILE to load data from files located on their own local file system into MySQL tables. To enable local_infile globally, you can execute the "SET GLOBAL local_infile=ON;" statement in the MySQL command-line interface or any MySQL client that has the necessary privileges to modify global variables. Additionally, you may need to restart the MySQL server for the changes to take effect.
	
			SET GLOBAL local_infile=ON;

4.) Download the NYC yellow taxi trip data:
Navigate to https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page and download the January 2023:Yellow Taxi's records. Alternatively you can use the following link below to save the file directly into your downloads:

	https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet

Execution Instructions:

1. Open and execute your Python Script:

Open your Python script in your IDE by navigating to the directory containing the script and double-clicking on it or opening it from the File menu. Once you have your Python script open, you can then execute it.

	OTA_CodingChallengeFinal.py

Discussion:

An assumption made during the development process was that the input file containing the yellow taxi trip data was already existing in a specified directory. This assumption simplified the data extraction step, as it eliminated the need to build a process to extract the data directly from the website. Another assumption made was the choice of using a MySQL database as the target database. By assuming MySQL as the target database, the development process could focus on designing SQL queries and ensuring compatibility with MySQL's SQL dialect. This assumption also dictated the setup process, including configuring permissions and managing database connections specific to MySQL.

During the development process, in the absence of regular ETL tools, Python was chosen as the primary tool for the ingestion and loading of the data into a MySQL database table. Python offers a rich ecosystem of libraries such as Pandas for data manipulation, sqlalchemy for database connection and matplotlib for visualization, making it a versatile choice for this task. Plus it was also much easier to setup than other ETL tools. 

In selecting Matplotlib for visualization, despite having no prior experience, it is part of the Python ecosystem alongside other commonly used libraries like NumPy and Pandas, it integrates seamlessly with these libraries. This integration allowed for efficient data manipulation and preprocessing using Pandas, followed by straightforward visualization using Matplotlib, creating a cohesive and efficient workflow.

However, several challenges were encountered along the way. One challenge was setting up the MySQL environment properly. Ensuring that the user had the necessary privileges to load data into a database table required thorough understanding of MySQL's access control system and permissions model. 

Despite these challenges, through research and experimentation the Python code was successfully developed and the MySQL database was configured with the appropriate permissions. This enabled the execution of the data processes ultimately leading to the successful loading of the data into the target table and for the aggregation and visualization of the data.

Outputs:

Python Script: 

https://github.com/kennbonita14/OTA_CodingChallenge/blob/main/OTA_CodingChallengeFinal.py

SQL Query result after Python Script execution:

https://github.com/kennbonita14/OTA_CodingChallenge/blob/main/OTA_CodeChallenge_result.jpg

MATPLOTLIB Visualization:

https://github.com/kennbonita14/OTA_CodingChallenge/blob/main/OTA_CodingChallenge_graph.jpg
