This project is divided into two parts:
    1. JavaScript program to preprocesses raw data, and final prediction output visualization (located on "visualization" directory)
    2. Python program to train model and generate prediction ("located on "models" and "predictions" directories)

JavaScript Program:

    This Program has the following features:
    
    1. Data Preprocessing
        - Given a set of crime data grouped by period(weekly/daily) as input files, it creates a set of snapshots per period
            that represents crime occurences on the MxN grids. Each MxN grids is flatten and consolidated into
            a single text file. It means that the each line of the output text file represents a single crime snapshot.
    2. Prediction Visualization
        - Given a pair of actual and prediction snapshot from the test set, the program shows the crime occurences in the map.
        - You can also adjust the sensitivity of the prediction.
    
    Requirement:
    
    This program requires internet access to run because it uses Google Map Api.
    
    Usage:
        1. Data Preprocessing
            - Prompted with grid size, input a value within (250, 500, 750)
            - Press the "Files to Process" button
            - Select files from "weekly-unprocessed/daily-unprocessed" directory, then choose any year and select all files under it.
            - Press processes Data
            - Wait and the output will be automatically downloaded.
            The sample output of any year can be seen on "weekly-processed/daily-processed"
        2. Prediction Visualization
            - Press the "Choose Actual" button
            - Select any files under "visualization/outputs" directory, choose an actual sample.
            - Press "Display" actual button
            - Select any files under "visualization/outputs" directory, choose a prediction sample.
                Make sure you choose the pair of the actual sample.
            - Press "Display" prediction
            - You can change the sensitivity by changing the drop-down value.

Modeling and Prediction Program:
    
    The program has the following features.
        1. Modeling
            - includes normalization and time-series transformation pre-processing to the data
            - exports training, validation and test set.
            - exports weights to use in prediction.
            Note: Usually the training takes a very long period of time. Please refrain from using this program if you dont plan to finish its runtime because it will mess up the weights of the model.
        2. Prediction
            - computes specificity, sensitivity, F-score, MCC using optimal threshold
            - exports a sample pair of actual and prediction data from the test set
            - displays a roc curve for 1 random sample

    Requirement:
    
    Linux Operating System. Installing required files by running "setup.py".

    Usage:
        1. Modeling
            - change directory to "models" and run any model.
        2. Prediction
            - change directory to "models" and run any model.

Also included in this project are the following datasets:
    1. Weekly unprocessed data
    2. Daily unprocessed data
    3. Processed Training set for each models
    4. Processed Validation set for each models
    5. Processed Test set for each models
