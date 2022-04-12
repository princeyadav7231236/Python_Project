import requests
import pickle

file_url = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", )
a = file_url.text.split("\n")  # This will split the file when thee will be a \n

# for i in a:                             # This will print all the items of the list a
#     print(i)

with open("pickling.pkl", "wb") as f:     # This will write the file_url in binary
    pickle.dump(a, f)
f.close()

with open("pickling.pkl", "rb") as f:       # This will read the binary file and print the list of the file_url
    print(pickle.load(f))

f.close()
