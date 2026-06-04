# Hospital-Performance-Data-Automation-Doctor-Analytics-Pipeline
**Project Overview**

This project automates the processing and analysis of hospital performance data collected from multiple healthcare centers.

Previously, the reporting process involved manually downloading Excel reports from the Hospital Information Management System (HIMS), performing transformations in Excel, merging files, and generating analytical reports. The entire workflow required approximately 6–7 hours to complete.

This solution automates the data preparation process using Python and SQL, reducing the total processing time to approximately 15 minutes.

**Business Problem**

The hospital operates across 9 different centers.

The existing workflow involved:

1)Downloading Excel reports from HIMS for each center.
2)Manually adding calculated columns such as:
  Length of Stay (LOS)
  Center Name
  Profit
3)Merging all center-wise files.
4)Creating Pivot Tables for analysis.
5)Preparing management reports.

Challenges:

Highly repetitive manual work
Significant processing time (6–7 hours)
Increased risk of human error
Difficult to scale with growing data volume


**Solution**

A Python-based automation pipeline was developed to eliminate manual data processing.

**Workflow**
1)Download reports from HIMS.
2)Execute Python automation script.
3)Automatically:
  Load all center files
  Add required calculated columns
  Standardize data structure
  Merge all reports into a single dataset
4)Export final consolidated Excel file.
5)Load processed data into SQL database.
6)Create analytical SQL views.
7)Connect SQL database to Power BI for reporting and visualization.

**Result**

Reduced report generation time by approximately 95%+ through automation while improving consistency and accuracy.

**Note**

The original hospital data is confidential and cannot be shared publicly. Therefore, this repository contains only the automation code, SQL scripts, and project documentation. Any sample data included is for demonstration purposes only.



















ng data volume
