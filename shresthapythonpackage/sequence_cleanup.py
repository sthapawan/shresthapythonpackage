import dendropy
import os

def sequence_cleanup(sequence_set, out_file, taxon, gene):
    #precondition would be if there is sequence_set or the out_file or taxon and they are in right format
    #to check if the taxon is in the matrix
    assert sequence_set(taxon)
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence[int(gene[0]):int(gene[1])]
    # the gene sequence on the left must be less than than on the right
    my_taxon_sequence.to_path(out_file, "fasta")
    
    ofile = open("out_file, "w")
    ofile.write(">" + item + "\n" + fasta_pleth[item] + "\n")

    ofile.close()
      #make sure the file not empty
       assert os.stat('out_file').st_size != 0
                 