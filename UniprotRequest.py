import requests
import re


class UniprotRequest:

    def __init__(self, uniprot_id_list, retry=10):
        self.retry = retry
        #self.uniprot_id_list = uniprot_id_list
        self.uniprot_URL = "http://www.uniprot.org/uniprot/"
        self.suffix = ".fasta"
        self.results_dict = {}
        #self.get_list_of_sequences([uniprot_id_list[0]])
        self.get_list_of_sequences(uniprot_id_list)
        #print(self.results_dict)
        # self.fasta_to_seq(fasta_list[0])

    #def convert_list_to_protein_sequences(self, fasta_list):
    #    self.fasta_to_seq(fasta_list)

    def find_motif(self, protein_sequence, motif_regex):
        start_positions = []
        matches = re.finditer(motif_regex, protein_sequence)
        for match in matches:
            #start_positions.append([match.start() + 1, match.end()])  # 1 indexed
            start_positions.append(match.start() + 1)  # 1 indexed

        return start_positions

    """
    Need lookahead in regex to allow overlapping of motifs.
    """
    def find_motifs(self, motif_regex=r"N{1,1}(?=[^P]{1,1}(S|T){1,1}[^P]{1,1})", motif="N-{P}-[ST]-{P}",
                    motif_name="N-glycosylation motif"):
        for item in self.results_dict:
            #print("item findmotifs", item)
            protein_seq = self.results_dict[item]["protein_seq"]
            motif_positions = self.find_motif(protein_seq, motif_regex)
            self.results_dict[item][motif_name] = {"motif": motif, "positions": motif_positions}

    def fasta_to_seq(self, fasta):
        start_index = re.search(r"\n", fasta).start() + 1
        sequence = fasta[start_index:]
        sequence = re.sub(r"[\n\r]+", "", sequence)
        #print("---------")
        #print(sequence)
        #print("---------")
        return sequence

    def get_list_of_sequences(self, uniprot_id_list):

        for item in uniprot_id_list:
            data_entry = {}
            fasta_format = self.data_transaction(item)
            data_entry["fasta_format"] = fasta_format
            protein_seq = self.fasta_to_seq(fasta_format)
            data_entry["protein_seq"] = protein_seq
            self.results_dict[item] = data_entry
        return

    def data_transaction(self, uniprot_id):
        response = requests.get(self.uniprot_URL + uniprot_id + self.suffix)
        retry_times = 0
        if response.ok:
            #print(response.text)
            return response.text
        else:
            retry_times += 1
            if retry_times == self.retry:
                response.raise_for_status()

        # form_data = {"query": self.uniprot_id_list, "format": "list", "from": "ACC+ID", "to": "ACC"}
        # response = requests.get(self.uniprot_URL, params=form_data)
        # print(response.content)
        # print(response.ok)
        # print(response.text)
        # print(response.content)


if __name__ == "__main__":
    test = UniprotRequest(["P07204_TRBM_HUMAN"])
    test.find_motifs()

    print("results:")
    print(test.results_dict)