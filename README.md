# CGMDataAnalysis

The repository is all about the analysis of the CGM data from patients for patients. The CGM data is based of meals and without meals and the goal is to find some good features from these time series.
 
 ### Goal: To ananlyze CGM time series data and find 4 suitable features and generate PCA.
 
 ## Data Preprocessing
 
 For preprocessing all the files were checked for nan values and subsequently interpolated with previous data in series in order to generate a makeshift one. In some instances entire rows were observed to be nan in which case it was omitted. 

While merging data of all 5 patients one had more CGM data than others so zero padding was done in this case to accommodate the size of the array . 


## Feature Selection:

As we can notice the data given was a time series data, so I tried to explore the following features.

* Fast Fourier transform.

Fast Fourier transform computes the discrete Fourier transform (DFT) of a sequence or its inverse. The analysis includes converting signals from its original domain to a representation in the frequency domain.

The whole motivation behind using FFT for the given CGM time series data was to be able to capture the information in the data, by taking the top coefficients with the most variation.


* Sample Entropy

Entropy is the measure of randomness, where as Sample Entropy is a modification of approximation entropy which is used is assessing the complexity of time series signals and has a little computational advantage over the latter. 

The idea of using Sample entropy was to quantify the randomness or the similarity of the data. Values close to zero represent less noise and more similarity whereas values above 1 denote the irregularity. 



* Moving Standard Deviation 

Moving standard deviation is a statistical measurement of volatility. Although it cannot make predictions of how the trend in the data is goin to be but it can be used as a confirming indicator of trend changes in the data, which can help in detecting variation in the data. 

The main intuition behind using this feature was to keep track of the drastic changes in the continuous time series data by also keeping check of the variation in the data. 


* Skewness.

Skewness is the measure of asymmetry of the probability distribution of random variable around its mean. If the tail of the distribution is on the left side it denotes a negative skew and if the tail is on the opposite end it represents a positive skew.

The whole idea behind using skewness as a feature was to check how the distribution behaved for all the patients in the data. 
