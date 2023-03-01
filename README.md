# Telco Customer Churn

AutoML Telco Customer Churn prediction using AutoGluon Framework

## Introduction

This will be using 'AutoGluon' Framework.

## Business Objective

Churn prediction means detecting which customers are likely to leave a service or to cancel a subscription to a service. It is a critical prediction for many businesses because acquiring new clients often costs more than retaining existing ones.

## Environment Setup

create an environment
...
conda create --name (project_name)  python=3.9
...

Activate the environment
...
conda activate the environment
...
Install packages in the environment
...
NB:This is for windows (Mac users please see the documentation or other relevant materials for more details)
pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchtext==0.13.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon streamlit jupyter

### Test your installation as follows
.....
on the terminal type :python and it will show something like this;
(redzone_proj) C:\redoneproj\Telco_customer_churn>python
Python 3.9.16 (main, Jan 11 2023, 16:16:36) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>from autogluon.tabular import TabularDataset, TabularPredictor
....
if that works,then your installation for *autogluon* is working

And then for *streamlit*,
(redzone_proj) C:\redoneproj\Telco_customer_churn>streamlit hello

  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.100.20:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!

  This will automatically pop up on your default browser on this address- 'http://localhost:8501/'

  image.png


...
## Project Structure

Telco Customer Churn
|--README.md
|--images
|--data
|--main.py
|--main.ipynb
|--experimentation.ipynb
|--app.py

## Data Ingestion

## Exploratory Data Analysis (EDA)

## Features Engineering or Processing

## Model Building

## Model Evaluation

## Model Deployment
deployment will be done on 'streamlit'

