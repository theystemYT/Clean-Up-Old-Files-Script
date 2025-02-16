DO NOT STEAL THIS CODE WITHOUT THE CREATORS PERMISSION.
import os
import time

folder_path = input("Enter the folder path you want to clean: ")
age_limit = int(input("Enter the number of days old files should be to delete them: "))

def clean_old_files():
    if not os.path.exists(folder_path):
        print("Error: Folder path does not exist.")
        return

    current_time = time.time()

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            last_accessed = os.path.getatime(file_path)
            file_age_in_days = (current_time - last_accessed) / (60 * 60 * 24)

            if file_age_in_days > age_limit:
                try:
                    os.remove(file_path)
                    print(f'Deleted {filename} as it was {int(file_age_in_days)} days old.')
                except Exception as e:
                    print(f'Failed to delete {filename}. Error: {e}')
            else:
                print(f'{filename} is {int(file_age_in_days)} days old, keeping it.')

clean_old_files()
