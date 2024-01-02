# Uplift Modeling

- Author: [Lina Faik](https://www.linkedin.com/in/lina-faik/)
- Creation date: January 2024
- Last update: January 2024

## Objective

This repository contains the code and the notebooks used to train and evaluate uplift models using [CausalML](https://causalml.readthedocs.io/en/latest/about.html) and [scikit-uplift](https://www.uplift-modeling.com/en/latest/) libraries.
It was developed as an experimentation project to support the explanation blog posts around the topic. 

The model and code are explained in more detail in the following article:
- Beyond Predictions: Uplift Modeling & the Science of Influence  
_Hands-On Approach to Uplift with Tree-Based Models (link coming soon)_

<div class="alert alert-block alert-info"> You can find all my technical blog posts <a href = https://linafaik.medium.com/>here</a>. </div>

## Project Description

### Code structure

```
data # folder containing the initial datasets
├── criteo-uplift-sample-v2.1.csv # sample of the data
notebooks 
├── 01_data_exploration.ipynb # data cleaning and exploration
├── 02_feature_engineering.ipynb # data preprocessing
├── 03_model_training.ipynb # uplift model training
├── 04_model_evaluation.ipynb # model evaluate and exploration
outputs # folder storing models and hyper-parameter research
src
├── training.py # general functions to train models           
├── viz.py # functions for data visualization
```

### Data

The notebooks is based on criteo dataset that can be found in [Kaggle](https://www.kaggle.com/datasets/arashnic/uplift-modeling). 
It can easily be adapted to other data adapted to uplift modeling

## How to Use This Repository?

### Requirement

The code uses a GPU and relies on the following libraries:

```
pandas==2.1.4
plotly==5.18.0
numpy==1.26.2
scikit-learn==1.3.2
scikit-uplift==0.5.1
optuna==3.5.0
causalml
```

### Experiments

To run experiments, you need to run the notebooks in the order suggested by their names.
The associated code is in the `src` directory.
