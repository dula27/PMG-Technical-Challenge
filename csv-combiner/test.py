import combinecsv
import pandas
import subprocess

test1 = "test_files/test1.csv"
test2 = "test_files/test2.csv"
test3 = "test_files/test3.csv"

output_file = open("test_output.csv", "w+") 
subprocess.run(["python3", "combinecsv.py", test1, test2, test3], stdout=output_file)

df = pandas.read_csv("test_output.csv")
length = len(df)

test_counter = 0

# Tests if all rows are combined
if length == 3:
    test_counter += 1
    print("Passed: Output matches Row count.")

# Tests if the number of columns is as desired
if df.shape[1] == 4:
    test_counter += 1
    print("Passed: Output matches Column count.")

# Tests if filename column is added
if df.columns[3] == "filename":
    test_counter += 1
    print("Passed: Output contains filename column.")

# Tests if all tests were passed
if test_counter == 3:
    print("\nAll tests passed.")