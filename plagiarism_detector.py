from difflib import SequenceMatcher

with open('demo1.txt', 'r') as first_file, open('demo2.txt', 'r') as second_file:
    data_file1 = first_file.read()
    data_file2 = second_file.read()
    
    similarity_ratio = SequenceMatcher(None, data_file1, data_file2).ratio()
    
    print(f"The similarity ratio between the two files is: {similarity_ratio}")
    
    if similarity_ratio > 0.5:
        print("Plagiarism detected")
    else:
        print("No plagiarism detected")
