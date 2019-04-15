# Wine Quality Analysis using Python

Two datasets were created, using red and white wine samples.
The inputs include objective tests (e.g. PH values) and the output is based on sensory data
(median of at least 3 evaluations made by wine experts). Each expert graded the wine quality 
between 0 (very bad) and 10 (very excellent). 

The Task was to predict the quality of wine based on the data given. This task was approached as a Regression Problem. </br>
Here Two algorithms were implemented, Random Forest and Gradient Boosting Regressor. For both the Algorithms, the performance was measured in terms of RMSE.  </br>

## Analysis

Out of the two, Random Forest Regressor performed better with RMSE value came around 0.601 compared to 0.632 of Gradient Boosting. </br>
[ML_ReadWinePreprocessing.ipynb](https://github.com/ElToro13/ML-Python/blob/master/Wine%20Quality%20Prediction/ML_ReadWinePreprocessing.ipynb) - The dataset where values of Red wine were recorded. 

[ML_WhiteWinePreprocessing.ipynb](https://github.com/ElToro13/ML-Python/blob/master/Wine%20Quality%20Predictio/ML_WhiteWinePreprocessing.ipynb)- Preprocessing file for White Wine Dataset.

[Prediction.ipynb](https://github.com/ElToro13/ML-Python/blob/master/Wine%20Quality%20Prediction/Prediction.ipynb)-Based of the prepared datasets, Both the algorithms are implemented in this file and subsequently prediction is done. 

## Libraries Used

* SciKit-Learn
* Pandas
* Numpy
* Matplotlib

## Author

* **Yash Soni**
