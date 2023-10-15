from concurrent.futures import ThreadPoolExecutor
import os
import pandas as pd
import time
import threading

directory_path = "original/"
start = time.perf_counter()

# Get the list of files in the directory
files = [
    f
    for f in os.listdir(directory_path)
    if os.path.isfile(os.path.join(directory_path, f))
]


def clean_data(file_name):
    """Function to pick data from the excel and remove duplicate vote entries."""
    # fetch data
    # data = pd.read_excel("original/broadcast.xlsx")
    df = pd.read_csv(f"original/{file_name}")

    # Identify and move duplicates to a new dataset
    duplicates = df[df.duplicated(subset=["IP Address", "Answer Text"], keep="first")]
    without_dups = df.drop_duplicates(subset=["IP Address", "Answer Text"])
    total_votes = (
        without_dups.groupby("Answer Text").size().reset_index(name="Total Votes")
    )
    total_dups = (
        duplicates.groupby("Answer Text").size().reset_index(name="Total Votes")
    )

    # set up directory to save the new files
    original_name = file_name.split(".")[0]
    new_dir = f"cleaned/{original_name}"
    os.makedirs(new_dir, exist_ok=True)

    def save_formats(dataframe, name):
        dataframe.to_csv(f"{new_dir}/{name}.csv", index=False)
        dataframe.to_excel(f"{new_dir}/{name}.xlsx", index=False)

    # save in different formats
    save_formats(duplicates, "duplicates")
    save_formats(without_dups, "without duplicates")
    save_formats(total_votes, "total votes")
    save_formats(total_dups, "total of duplicates")
    save_formats(df, f"original_{original_name}")


def with_threads(file_name):
    t = threading.Thread(target=clean_data, args=(file_name,))
    t.start()


def with_thread_pool():
    with ThreadPoolExecutor() as executor:
        # run clean data on all files.
        executor.map(clean_data, files)


if __name__ == "__main__":
    # thread was slow, so I'm using threadpool 8.8secs
    # for file in files:
    #     with_threads(file)

    # for t in threading.enumerate():
    #     if t.name != "MainThread":
    #         t.join()

    with_thread_pool()

    end = time.perf_counter()
    print(f"Finished in {round(end - start, 2)} second(s).")
