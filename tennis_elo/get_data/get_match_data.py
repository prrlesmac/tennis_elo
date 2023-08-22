import pandas as pd
import requests
from io import StringIO


def open_github_csv_as_dataframe(repo_url, file_path):
    """
    Open a GitHub CSV file as a Pandas DataFrame.

    Args:
        repo_url (str): The URL of the GitHub repository (e.g., 'https://github.com/username/repo').
        file_path (str): The path to the CSV file within the repository (e.g., 'data/file.csv').

    Returns:
        pandas.DataFrame: The CSV data as a Pandas DataFrame.
    """
    raw_url = f"https://raw.githubusercontent.com/{repo_url.split('/')[3]}/{repo_url.split('/')[4]}/master/{file_path}"
    print(raw_url)
    response = requests.get(raw_url)

    if response.status_code == 200:
        csv_text = response.text
        df = pd.read_csv(StringIO(csv_text))
        return df
    else:
        print("Failed to open CSV file.")
        return None


def get_atp_matches(list_of_years):
    matches_all = []
    for year in list_of_years:
        matches = open_github_csv_as_dataframe(
            "https://github.com/JeffSackmann/tennis_atp", f"atp_matches_{year}.csv"
        )
        matches_all.append(matches)

    matches_all = pd.concat(matches_all)

    return matches_all
