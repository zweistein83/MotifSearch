import UniprotRequest


with open("testfile.txt", "rt") as file:
    file_contents = file.read()
    file_list = file_contents.split("\n")


    results = UniprotRequest.UniprotRequest(file_list)
    results.find_motifs()
    print(results.results_dict)
