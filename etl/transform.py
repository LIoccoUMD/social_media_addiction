import logging
import pandas as pd

def load_data(file_path):
    """Loads the data from a CSV file with path file_path.
    
    Parameters:
        file_path (str): The path of the file containing the data to be read.
        
    Returns:
        pd.Dataframe: The data in the file as a dataframe.
    """
    logging.info(f"Loading data from {file_path}.")
    return pd.read_csv(file_path)

df = load_data("data\\extracted\\students_social_media_addiction.csv")
print(f"Columns: \n{df.columns}")
# print(df["Student_ID"])


# Student_ID, avg_daily_usage, Country, Most_Used_platform, Sleep_Hours_Per_Night
def avgDailyUsageByCountry():
    avg = df[["Student_ID","Avg_Daily_Usage_Hours","Country"]]
    return avg.groupby("Country")["Avg_Daily_Usage_Hours"].mean()    
print(avgDailyUsageByCountry())