def search_for_word(file_name, word):
  with open(file_name, "r") as f:
    for line_num, line in enumerate(f):
      if word in line:
        print(f"Found '{word}' on line: {line_num+1} of file: '{file_name}'")