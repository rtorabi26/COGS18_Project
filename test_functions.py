import os 
import pandas as pd 
import matplotlib.pyplot as plt 

def read_csv_file(file_path): 
    """
    Checks if csv file exists. If it does, reads the file and converts it to dataframe
    
    Parameters
    ----------
    file_path: string
        Path and name of the file containing the data 
    
    Returns 
    -------
    data: dataframe 
        The data frame from the information in the file 
    """
    
    if os.path.exists(file_path): 
        df = pd.read_csv(file_path)
        return df 
    else: 
        print(f"File '{file_path}' does not exist.") 
        return None 

def convert_to_decimal(value): 
    """
    Function to convert percent values to decimal 
    
    Parameters
    ----------
    value: string 
        string value containing % 
    
    Returns
    -------
    converted percent into decimal form, in format of a float 
    """
    retrun float(value.strip('%')) / 100 
    
def plot_average_sore_gender(ax, data, color, gender): 
    """
    Function to plit the barplot of the average scores, for each gender group
    
    Parameters
    ----------
    ax: axes object 
        axes object subfigure 
    data: list 
        list containing the average scores for each experiment 
    color: string 
        color of the bar plot 
    gender: string 
        gender group of interest 
    
    Returns 
    -------
    Bar plot showing the average score for each trial, for the specified gender group 
    """
    ax.bar(data.index, data.values, color=color)
    ax.set_title(f'Average Correct Score for {gender}')
    ax.set_xlabel('Trial')
    ax.set_ylabel('Average Correct Score') 
    
def plot_average_score_age(ax, data, title, xlabel, ylabel, color): 
    """
    Function to plot the barplot of the average scores, for each group as subfigure
    
    Parameters
    ----------
    ax: axes object 
        axes object subfigure 
    data: list 
        list containing the average scores for each experiment for specific age group
    title: string 
        title for each subfigure 
    xlabel: string 
        the x axis label for the subfigure 
    ylabel: string 
        the y axis label for the subfigure 
    color: string 
        color of each subfigure 
        
    Returns 
    -------
    Bar plot showing average score for each trial, for each age group of subfigure 
    """
    
    ax.bar(experiment_list, data, color=color) 
    ax.set_title(title) 
    ax.set_xlabel(xlabel) 
    ax.set_ylabel(ylabel) 
    
def get_countbreakdown_age(df, experiment_list, age_category, score_category):
    """
    Function to count the number of each score category, given the age category 
    
    Parameters
    ----------
    df: dataframe
        dataframe of data 
    experiment_list: list 
        list containing the column names that have the scores for each experiment 
    age_category: strong 
        age group of interest 
    score_category: float 
        one of the three score categories 
    
    Returns 
    -------
    a list with the total count of the score_category for each column in experiment_list for the selected age group 
    """
    
    count_list = []
    df_age = df[df['Age'] == age_category]
    for col in experiment_list: 
        trial_counts = df_age[col].value_counts()
        count_list.append(trial_counts.get(score_category, 0 ))
    return count_list 

def plot_counts_breakdown(ax, young_data, old_data, category, title): 
    """ 
    Plot count breakdwon for young and old participants 
    
    Parameters
    ----------
    ax: axes object 
        axes object subfigure 
    young_data: list 
        list containing the score counts for young participants 
    old_data: list 
        list containing the score counts for old participants 
    category: string 
        the score category for each subfigure 
    title: string 
        title for each subfigure 
    
    Returns
    -------
    A plot with three subcategories, showing the scatter plot with connected lines
        green for old and dark orange for young participant 
    """
    #Scatter plot for young participants
    ax.scatter(range(len(experiment_list)), young_data, 
               color = 'darkorange', label = f'Young: {category}')
    ax.plot(range(len(experiment_list)), old_data, 
            linestyle = '-', color = 'green') 
    #Scatter plot for old participants 
    ax.scatter(range(len(experiment_list)), old_data, 
               color = 'green', label = f'Old: {category}')
    ax.plot(range(len(experiment_list)), old_data, 
            linestyle = '-', color = 'green') 
    ax.set_xticks(range(len(experiment_list))) 
    ax.set_xticklabels(experiment_list)
    ax.set_title(title) 
    ax.legend()
    
