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

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ris-to-neo4j.git
# ris-to-neo4j
A Python program to convert RIS bibliographic data to Neo4j graph database queries.
