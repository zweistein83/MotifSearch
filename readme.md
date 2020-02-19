## Motif search prototype

Find specified motifs in proteins given by a list of uniprot ids. The sequences are automatically downloaded from uniprot.

Built in python 3.7

**Usage:**

instance = **UniprotRequest**( *uniprot_id_list*, *retry=10*)
- **uniprot_id_list**: list of uniprot ids.
- **retry**: how many retries for each data request from the uniprot  database (optional. default is 10).

instance.**find_motifs**(*motif_regex*, *motif*, *motif_name*)
*Add start position(s) of found motifs to result.*

 - **motif_regex**: Regex query string for motif (optional. default: r"N{1,1}(?=[\^P]{1,1}(S|T){1,1}[\^P]{1,1})")
 - **motif**: Motif in PROSITE format. It's ok to leave it blank (optional. default: "N-{P}-[ST]-{P}").
 - **motif_name**: Name of motif (optional. default: "N-glycosylation motif").

instance.**get_data()**
*Returns a dictionary with all protein sequences in fasta format and protein sequence together with selected motifs.*


**Example data**

*Just one uniprot id for simplicity.*

    instance = UniprotRequest(['P01374_TNFB_HUMAN'])
    instance.find_motifs()
    result = instance.get_data()
    print(result)

'P01374_TNFB_HUMAN': {
**'fasta_format':**
 '>sp|P01374|TNFB_HUMAN Lymphotoxin-alpha OS=Homo sapiens OX=9606 GN=LTA PE=1 SV=2\nMTPPERLFLPRVCGTTLHLLLLGLLLVLLPGAQGLPGVGLTPSAAQTARQHPKMHLAHST\nLKPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAY\nSPKATSSPLYLAHEVQLFSSQYPFHVPLLSSQKMVYPGLQEPWLHSMYHGAAFQLTQGDQ\nLSTHTDGIPHLVLSPSTVFFGAFAL\n', 
**'protein_seq':** 'MTPPERLFLPRVCGTTLHLLLLGLLLVLLPGAQGLPGVGLTPSAAQTARQHPKMHLAHSTLKPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSSQYPFHVPLLSSQKMVYPGLQEPWLHSMYHGAAFQLTQGDQLSTHTDGIPHLVLSPSTVFFGAFAL', 
**'N-glycosylation motif':** 
{**'motif':** 	'N-{P}-[ST]-{P}', 
**'positions':** [96]}}