from Bio import Entrez
from Bio import Medline
from tqdm import tqdm
import pickle

Entrez.email = "heathermgeiger@gmail.com"

keyword = "single cell rna sequencing"

result = Entrez.read(Entrez.esearch(db="pubmed", retmax=10, term=keyword))

print(
    "Total number of publications that contain the term {}: {}".format(
        keyword, result["Count"]
    )
)

MAX_COUNT = result["Count"]

result = Entrez.read(
    Entrez.esearch(db="pubmed", retmax=result["Count"], term=keyword)
)

ids = result["IdList"]

batch_size = 100
batches = [ids[x: x + 100] for x in range(0, len(ids), batch_size)]

with open('single_cell_rna_sequencing_entrez_fetch_batches.pkl','wb') as batches_file:
    pickle.dump(batches,batches_file)    

record_list = []

for batch in tqdm(batches):
    h = Entrez.efetch(db="pubmed", id=batch, rettype="medline", retmode="text")
    records = Medline.parse(h)
    record_list.extend(list(records))

print("Complete.")

with open('single_cell_rna_sequencing_entrez_fetch_record_list_first_half.pkl','wb') as record_list_file:
    pickle.dump(record_list_first_half,record_list_file)

with open('single_cell_rna_sequencing_entrez_fetch_record_list_second_half.pkl','wb') as record_list_file:
    pickle.dump(record_list_second_half,record_list_file)
