import pandas
import sys
import os
import argparse

# Returns filenames from command line arguments
def get_filenames():
    # Define arguments
    # Requires atleast one file
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    return args.files

def process_csv(filenames):
    # Create output DataFrame
    df_output = pandas.DataFrame()

    # Read csv files from args
    for file_name in filenames:
        data = pandas.read_csv(file_name)
        length = len(data.index)
        # Creates column with filename
        filename = [os.path.basename(file_name) for _ in range(length)]
        # Appends filename column to the DataFrame
        data['filename'] = filename
        # Concatenates current DataFrame with the output DataFrame
        df_output = pandas.concat([df_output, data])
        
    return df_output

def main():
    filenames = get_filenames()
    df_output = process_csv(filenames)

    # Prints DataFrame as csv to Standard Output
    df_output.to_csv(sys.stdout, index=False)
    
if __name__ == "__main__":
    main()