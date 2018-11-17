from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os


def sequence_blaster(fasta_path, results_path):
    #make sure there is the right path for the fasta_path or the results_path and they are in right format
    record = SeqIO.read(fasta_path, format = "fasta")
    #record = SeqIO.read("../../data/sequence.fasta", format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))

    save_file = open(results_path, "w")
    save_file.write(result_handle.read())
    save_file.close()
    #print_record = result_handle
   # result_path()
    # make sure if the file is saved on the result and not empty 
    assert os.stat(results_path).st_size != 0
    #results_path()
    
    