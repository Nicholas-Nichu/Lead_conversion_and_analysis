# Lead Conversion Analysis & Prediction

## Overview

This project analyzes the lead-to-booking journey for a real estate business by combining multiple CRM datasets and identifying patterns that drive conversions.

The objective is to:

* Understand how leads progress from creation to site visit to booking
* Identify key factors influencing conversions
* Build a model to predict high-probability leads

---

## Problem Statement

Sales teams often spend time on low-quality leads due to lack of prioritization.

This project addresses:

* Which leads are most likely to convert
* What behaviors indicate strong buying intent
* How sales efforts can be optimized

---

## Dataset Description

Data was sourced from CRM reports and includes:

* Leads Data: Lead ID, Created Date, Customer Info, Channel
* Site Visits Data: Visit dates, number of visits, priority
* Disqualification Data: Reasons for lost leads
* Conversion Data: Booking details

All datasets are linked using Lead ID.

---

## Data Processing (SQL)

SQL was used to:

* Join multiple datasets into a single master table
* Handle duplicates using DISTINCT ON with business logic
* Prioritize booked leads and latest site visits

Output: Clean master dataset (PX1)

---

## Analysis and Modeling (Python)

### Data Preparation

* Converted date columns into proper format
* Created target variable:

  * Converted = 1 if booking exists, else 0

### Feature Engineering

* Days_to_Visit: Time taken for first engagement
* Site Visit Count: Level of customer interest

### Model Used

* Logistic Regression

### Objective

Predict probability of lead conversion

---

## Data Visualization (Power BI)

An interactive dashboard was developed to analyze the lead conversion funnel and key performance metrics.

Key components:

* Lead → Visit → Booking funnel
* Conversion rate tracking
* Channel-wise performance analysis
* Sales performance by user
* Time-based trends of leads and bookings

---

## Key Output

Each lead is assigned a conversion probability score:

* High probability leads can be prioritized
* Low probability leads can be deprioritized

---

## Tools and Technologies

* SQL (PostgreSQL) for data extraction and transformation
* Python (Pandas, Scikit-learn) for analysis and modeling
* Power BI for data visualization

---

## Business Impact

* Enables data-driven lead prioritization
* Helps sales teams focus on high-value prospects
* Improves conversion efficiency and decision-making

---

## Project Structure

```
project-folder
 ┣ SQL
 ┃ ┗ master_table.sql
 ┣ Python
 ┃ ┗ lead_model.py
 ┣  Sample_file.csv
 ┣ README.md
```

---
