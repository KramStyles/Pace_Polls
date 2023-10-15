import os
import pandas as pd

directory_path = 'original/'




def clean_data(file_name):
    """Function to pick data from the excel and remove duplicate vote entries."""
    # fetch data
    # data = pd.read_excel("original/broadcast.xlsx")
    df = pd.read_csv(f"original/{file_name}")

    # Identify and move duplicates to a new dataset
    duplicates = df[df.duplicated(subset=['IP Address', 'Answer Text'], keep='first')]
    without_dups = df.drop_duplicates(subset=["IP Address", "Answer Text"])
    total_votes = without_dups.groupby("Answer Text").size().reset_index(name='Total Votes')
    total_dups = duplicates.groupby("Answer Text").size().reset_index(name='Total Votes')

    # set up directory to save the new files
    original_name = file_name.split('.')[0]
    new_dir = f"cleaned/{original_name}"
    os.makedirs(new_dir, exist_ok=True)

    def save_formats(dataframe, name):
        dataframe.to_csv(f"{new_dir}/{name}.csv", index=False)
        dataframe.to_excel(f"{new_dir}/{name}.xlsx", index=False)

    # save in different formats
    save_formats(duplicates, "duplicates")
    save_formats(without_dups, "without duplicates")
    save_formats(total_votes, "total")
    save_formats(df, f"original_{original_name}")


if __name__ == "__main__":
    # Get the list of files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    for file in files:
        clean_data(file)
