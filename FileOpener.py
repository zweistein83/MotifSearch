import UniprotRequest
import re

with open("testfile.txt", "rt") as file:
    file_contents = file.read()
    file_list = file_contents.split("\n")
    #file_contents =  re.sub("\n", " ", file_contents)
    #print(file_contents)
    #print(file_list)


    results = UniprotRequest.UniprotRequest(file_list)
    results.find_motifs()
    print(results.results_dict)
