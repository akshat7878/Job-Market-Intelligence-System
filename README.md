# Job Market Intelligence System

## Overview

The Job Market Intelligence System is a Data Engineering project that analyzes LinkedIn job posting data to uncover trends in hiring demand, salary distributions, industries, companies, and skills.

The project demonstrates a complete data engineering workflow including:

* Data ingestion
* ETL pipelines
* Relational database design
* SQL analytics
* Data validation
* Interactive dashboard development using Streamlit

The system transforms raw LinkedIn job posting data into actionable insights for job seekers, recruiters, and business analysts.

---

## Project Architecture

Raw CSV Files
↓
Pandas ETL Pipelines
↓
SQLite Database
↓
SQL Analytics Layer
↓
Streamlit Dashboard
↓
Interactive Visualizations

---

## Dataset

LinkedIn Job Postings Dataset

### Dataset Components

* Companies
* Job Postings
* Skills
* Industries
* Salaries
* Job-Skill Relationships
* Job-Industry Relationships

### Dataset Size

| Entity         | Records |
| -------------- | ------: |
| Companies      |  24,473 |
| Job Postings   | 123,849 |
| Skills         |      35 |
| Industries     |     422 |
| Job Skills     | 213,768 |
| Job Industries | 164,808 |
| Salaries       |  40,785 |

---

## Technologies Used

### Programming

* Python

### Data Processing

* Pandas

### Database

* SQLite
* SQL

### Visualization

* Streamlit
* Plotly

### Development Tools

* Git
* GitHub
* VS Code

### Containerization

* Docker

---

## Database Schema

### Tables

#### companies

Stores company information.

#### postings

Stores job posting details.

#### skills

Skill lookup table.

#### industries

Industry lookup table.

#### job_skills

Many-to-many mapping between jobs and skills.

#### job_industries

Many-to-many mapping between jobs and industries.

#### salaries

Salary information for job postings.

---

## ETL Pipeline

### Data Loading

* Extract CSV datasets
* Clean and transform data
* Handle missing values
* Convert data types
* Load into SQLite

### Validation

Data validation checks:

* Record counts
* Table integrity
* Data completeness
* Relationship consistency

---

## SQL Analytics

The project includes analytical SQL queries for:

### Job Analysis

* Top Job Titles
* Remote Jobs Analysis

### Skills Analysis

* Most In-Demand Skills
* Highest Paying Skills
* Skill Demand vs Salary

### Industry Analysis

* Top Industries
* Highest Paying Industries

### Company Analysis

* Top Hiring Companies

### Salary Analysis

* Salary by Experience Level
* Salary by Work Type

---

## Streamlit Dashboard

### Overview Dashboard

Provides:

* Total Jobs
* Total Companies
* Total Skills
* Total Industries

### Job Title Dashboard

Visualizes:

* Most common job titles
* Hiring demand by role

### Skills Dashboard

Visualizes:

* Most demanded skills
* Skill category trends

### Companies Dashboard

Visualizes:

* Top hiring companies

### Industries Dashboard

Visualizes:

* Industries with highest hiring activity

### Salary Analysis Dashboard

Includes:

* Highest Paying Skills
* Highest Paying Industries
* Salary by Experience Level
* Salary by Work Type

---

## Key Insights

### Skill Demand

Information Technology, Sales, and Management show the highest hiring demand.

### Salary Trends

Finance, Consulting, Legal, and Accounting-related skills offer some of the highest average salaries.

### Industry Trends

Healthcare, IT Services, Retail, and Financial Services dominate hiring activity.

### Experience Impact

Higher experience levels generally correspond to higher salary ranges.

---

## Project Structure

```text
Job-Market-Intelligence-System/
│
├── data/
├── etl/
├── sql/
├── analytics/
├── dashboard/
├── notebooks/
├── jobs.db
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

### Execute Analytics Query

```bash
python analytics/run_query.py sql/top_skills.sql
```

---

## Future Enhancements

* Dockerized deployment
* Databricks integration
* Apache Spark ETL pipeline
* Real-time job market analytics
* Cloud deployment (AWS/Azure)
* Machine Learning salary prediction
* Skill recommendation system

---

## Author

Akshat Kumawat

Data Engineering | SQL | Python | Streamlit | Analytics
