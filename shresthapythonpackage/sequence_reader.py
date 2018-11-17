import dendropy
#this was added later to check if the filepath exists
import os.path
def sequence_reader(filepath):
    assert os.path.exists(filepath)#this was added later as well to find the filepath exists
    #the filepath could be precondition
    #the file is in the right format
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema="phylip"
     )
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
    