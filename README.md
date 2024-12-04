# RIS to Neo4j

A Python program that converts RIS bibliographic data to Neo4j graph database queries.

## Description

This Python script parses RIS files containing bibliographic references and converts them into Neo4j Cypher queries, which can be used to store and query bibliographic data in a graph database.

## Features

- Parse RIS files and extract key bibliographic information (e.g., authors, titles, journals).
- Generate Neo4j Cypher queries for creating nodes (e.g., `Reference`, `Author`, `Journal`, `Keyword`) and relationships between them.
- Easy to use with command-line input (e.g., `python3 ris_to_neo.py file.ris`).

## Requirements

- Python 3.x
- Neo4j (for executing the generated Cypher queries)

# Tutorial
# Step 1: Clone the repository to your local machine
git clone https://github.com/JeanphiloGong/ris-to-neo4j.git

# Step 2: Navigate to the directory of the cloned repository
cd ris-to-neo4j

# Step 3: (Optional) Create a virtual environment and activate it
# Create a virtual environment
python3 -m venv venv

# On Windows, use:
# venv\Scripts\activate
# On Mac/Linux, use:
source venv/bin/activate

# Step 4: Install the required dependencies
# If there is a `requirements.txt`, install dependencies using pip
pip install -r requirements.txt

# Step 5: Prepare your RIS file
# Ensure that you have your RIS file ready. It should look something like this:
# Example RIS file (e.g., 'example.ris')
# %0 Journal Article
# %A John Doe
# %A Jane Smith
# %T Example Research Paper
# %J Example Journal
# %D 2024
# %V 1
# %N 2
# %P 10-20
# %@ 1234-5678
# %U https://example.com

# Step 6: Run the Python script to convert RIS data to Cypher queries
# Use the following command to run the script and convert your RIS file to Cypher queries:
python3 ris_to_neo.py path_to_your_file.ris

# Example:
# python3 ris_to_neo.py example.ris

# This will output the Cypher queries that you can use in Neo4j.

# Step 7: Run the generated Cypher queries in Neo4j
# Copy the output queries and paste them into the Neo4j Browser (http://localhost:7474).
# Or, if you're using Cypher Shell, save the output queries to a file (e.g., queries.cypher) and run:
cat queries.cypher | cypher-shell -u neo4j -p <password>

# Example:
# cat queries.cypher | cypher-shell -u neo4j -p your_neo4j_password

# Step 8: Visualize the data in Neo4j
# Once the queries have been executed in Neo4j, you can view the data in the Neo4j Browser.
# For example, to view all references (nodes labeled 'Reference'):
MATCH (r:Reference) RETURN r LIMIT 10;

# You can also modify your queries to explore other types of data:
# View all authors related to a specific reference:
MATCH (r:Reference {title: "Example Research Paper"})-[:AUTHORED_BY]->(a:Author) RETURN a;

# View all references published in a specific journal:
MATCH (r:Reference)-[:PUBLISHED_IN]->(j:Journal {name: "Example Journal"}) RETURN r;

# Step 9: Modify the script for additional functionality
# You can also modify the script to support additional RIS tags or relationships.
# For example, if you have additional RIS tags like %L (labels) or %R (DOIs), you can modify the
# `parse_ris_to_dict` function to handle these tags and generate appropriate Cypher queries.

# Done!

