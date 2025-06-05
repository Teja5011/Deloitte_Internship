# Deloitte_Internship

## TASK1 : 
---
### Overview of the Task :

### data-1.json: JSON data using ISO timestamps.

### data-2.json: JSON data using millisecond timestamps.

  ## data-result.json: This is the target output format you want to produce.

  ## main.py: Python file where you must implement the logic.

## Step 1: Set Up Your Environment
  Go to https://replit.com.

  Sign in / create an account.

  Fork the given project into your workspace.

## Step 2: Explore the Files
  ### data-1.json: You'll find data with timestamps in ISO 8601 format, like "2024-06-05T10:00:00Z".

  ### data-2.json: Timestamps are in milliseconds since epoch like 1717572000000.

 ### data-result.json: Unified format – all timestamps are in milliseconds, and the combined values from both datasets are merged per timestamp.

Step 3: Locate main.py
----


# Step-by-Step Implementation Logic
---
1. convert_iso_to_millis(iso_timestamp)
  Use Python's datetime module to convert ISO time to milliseconds:

2. merge_data(data1, data2)
  Create a dictionary with timestamps as keys (in milliseconds).

  Merge values from both datasets by timestamp.

  Return a list of dictionaries sorted by timestamp.
