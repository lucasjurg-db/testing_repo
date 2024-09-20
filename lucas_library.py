def search_for_lucas(file_name):
  with open(file_name, "r") as f:
    for line in f:
      if "Lucas" in line:
          print("Found Lucas in file: " + file_name)
