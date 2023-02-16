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
pip install autogluon
NB: It is very important to install jupyter with conda so it can bring all the dependencies
conda install jupyter
conda install streamlit
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
deployment will be don 'streamlit'

