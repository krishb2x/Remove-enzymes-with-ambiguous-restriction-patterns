def remove_ambigous_renz(Lenz):
""" remove enzymes with ambiguous restriction patterns """
    for i in range(len(Lenz)):
        if not check_dna(Lenz[i]):
            del Lenz[i]
