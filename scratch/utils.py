import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def describe_df(df):
    '''
    All credit to Vikas Singh:
    https://www.kaggle.com/vikassingh1996/don-t-underestimate-the-power-of-a-logistic-reg
    
    Prints a summary of a dataframe
    
    Input: pandas dataframe

    Return: pandas dataframe
    '''

    print(f"Dataset Shape: {df.shape}")
    summary = pd.DataFrame(df.dtypes,columns=['dtypes'])
    summary = summary.reset_index()
    summary['Name'] = summary['index']
    summary = summary[['Name','dtypes']]
    summary['Missing'] = df.isnull().sum().values    
    summary['Uniques'] = df.nunique().values
    summary['First Value'] = df.iloc[0].values
    summary['Second Value'] = df.iloc[1].values
    summary['Last Value'] = df.iloc[-1].values
    return summary

def plot_column_distribution(data, col_name, size=(8,6)):
    '''
    Checks the distribution of a column
    
    Inputs:
    data: expects a pandas dataframe
    col_name: expects the name of the column to check, as a string
    size: expects a size for your plot, styled as (#,#)
    '''

    plt.figure(figsize=size)

    # Setting our countplot as a variable, so that we can change aspects
    # Note! If you don't set this equal to a variable, you can't access patches
    # Which means you can't get the % on the plot. But you can still see it

    g = sns.countplot(data[col_name])

    # If you don't assign the plot to a variable, want to instead use
    # `plt.title` - not `g.set_title` - same for the labels
    g.set_title(f"{col_name.capitalize()} Distribution", fontsize=14)
    g.set_xlabel(f"{col_name.capitalize()} Values", fontsize=12)
    g.set_ylabel("Count", fontsize=12)

    # Creating the total size, so we can get the percentage
    total = len(data[col_name])
    for p in g.patches:
        # Gets the height from the plot
        height = p.get_height()
        # Getting the percentage to add to the chart as text
        g.text(p.get_x()+p.get_width()/2,
               height/2,
               '{:1.2f}%'.format(height/total*100),
               ha="center", fontsize=14)
        # Honestly this seems like a roundabout way to do this, but it works

    plt.show()

def plot_null_heatmap(data, size=(8,6)):
    '''
    Checking for patterns in any missing data

    Inputs: 
    data: pandas dataframe
    size: size for your plot, styled as (#,#)
    '''

    plt.figure(figsize=size)
    sns.heatmap(data.isnull(), cbar=False)
    plt.show()

def stringify_columns(data):
    '''
    Turns all columns into strings, typically to prep a dataframe
    to weight-of-evidence encode columns before logistic regression

    Input: expects a data source that either is a pandas df or that can be
    turned easily into a pandas df
    '''

    if type(data) != pd.core.frame.DataFrame:
        df = pd.DataFrame(data)
    else:
        df = data
        
    for c in df.columns.tolist():
        df[c] = df[c].astype(str)
    return df


def print_results(results_dict, training=False):
    '''
    Prints the results of a cross validate dictionary in a clean way, showing
    the mean and standard deviation for whatever scores are run
    
    Inputs: 
    results_dict - dictionary, returned from sklearn.model_selection.cross_validate
    training - boolean, denotes whether return_train_score is set to T or F
    
    Returns:
    nothing - only prints the results
    '''
    if training==True:
        print("Training Results: \n")
        for key in list(results_dict.keys()):
            if "train" in key:
                nice_key = key.replace("_", " ")
                print(f"{nice_key.title()}: {results_dict[key].mean():.5f} +/- {results_dict[key].std():.5f}")
    
    print("\nTest Results: \n")
    for key in list(results_dict.keys()):
        if "test" in key:
            nice_key = key.replace("_", " ")
            print(f"{nice_key.title()}: {results_dict[key].mean():.5f} +/- {results_dict[key].std():.5f}")