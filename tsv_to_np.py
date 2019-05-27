import numpy as np
#tsv for fb15k
#there are 14951 entities
#and 2690 relations
path = 'joined_embeddings.tsv'



entities_vector = np.loadtxt('joined_embeddings.tsv', dtype=np.float32, delimiter="\t", skiprows=0, max_rows=14951, usecols=range(1, 201), comments=None)
relations_vector = np.loadtxt('joined_embeddings.tsv', dtype=np.float32, delimiter="\t", skiprows=14951, max_rows=2690, usecols=range(1, 201), comments=None)

entities_id = np.loadtxt('joined_embeddings.tsv', dtype=str, delimiter="\t", skiprows=0, max_rows=14951, usecols=range(0,1), comments=None)
relations_id = np.loadtxt('joined_embeddings.tsv', dtype=str, delimiter="\t", skiprows=14951, max_rows=2690, usecols=range(0,1), comments=None)



fb15k_all_id = np.loadtxt('joined_embeddings.tsv', dtype=str, delimiter="\t", skiprows=0, usecols=range(0,1), comments=None)
fb15k_all_vectors = np.loadtxt('joined_embeddings.tsv', dtype=str, delimiter="\t", skiprows=0, usecols=range(1,201), comments=None)
# np.save('fb15kentities_vector', entities_vector)
# np.save('fb15krelations_vector', relations_vector)
# np.save('fb15kentities_id', entities_id)
# np.save('fb15krelations_id', relations_id)
# np.save('fb15k_all_id', fb15k_all_id)
# np.save('fb15k_all_vectors', fb15k_all_vectors)

