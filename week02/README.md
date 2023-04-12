# App Store and Google Play Store Analysis

This Python code reads in two CSV files, one containing data for mobile applications in the App Store and the other for the Google Play Store. The code then performs various analyses and manipulations on the data sets, including:

- Exploring the data sets
- Removing incorrect data
- Removing duplicate data
- Removing non-English apps
- Isolating free apps
- Analyzing frequency tables for different attributes

## Files

The code requires two CSV files, which should be saved in the same directory as the Python file:

- `AppleStore.csv`: contains data for apps in the App Store
- `googleplaystore.csv`: contains data for apps in the Google Play Store

## Code Overview

The code performs the following steps:

1. Import the required `csv` module and read in the two data sets from CSV files.
2. Explore the data sets by printing the headers and first few rows.
3. Remove incorrect data from the Google Play Store data set.
4. Remove duplicate data from the Google Play Store data set.
5. Remove non-English apps from both data sets.
6. Isolate free apps from both data sets.
7. Analyze the frequency tables for different attributes to gain insights into the data.

## Usage

To use this code, save it in the same directory as the `AppleStore.csv` and `googleplaystore.csv` files. Then, run the code in a Python environment, such as Jupyter Notebook or Spyder. The output will display in the console.

## References

This code is adapted from the solutions provided by Dataquest at https://github.com/dataquestio/solutions/blob/master/Mission350Solutions.ipynb.
