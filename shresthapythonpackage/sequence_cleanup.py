import dendropy
import os

def sequence_cleanup(sequence_set, out_file, taxon, gene):
    #precondition would be if there is sequence_set or the out_file or taxon and they are in right format
    #to check if the taxon is in the matrix
   # assert sequence_set[taxon]
    #assert sequence_set([taxon])
    #my_taxon_sequence = sequence_set[taxon]
    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence = my_taxon_sequence[int(gene[0]): int(gene[1])]
    #my_taxon_sequence = my_taxon_sequence(start_gene, end_gene)
    # the gene sequence on the left must be less than than on the right
    #my_taxon_sequence.to_path(out_file, "fasta")
    
    
    ofile = open(out_file, "w")
    #ofile.write(">" + item + "\n" + fasta_pleth[item] + "\n")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()
    #make sure the file not empty
    assert os.stat(out_file).st_size != 0
    """


Parameters
----------

arg1: sequence_set - gives the sequence
arg2: out_file - it is for the file that is supposed to get output
arg3: Taxon - type of taxon
arg4: gene - the gene for the taxons

Returns
out_file - 
-------
list
    A list containing all the taxa in your dataset.

"""
                 