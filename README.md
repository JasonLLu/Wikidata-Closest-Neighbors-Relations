# Wikidata Nearest Neighbor, Nearest Relation
Utilizes facebook research's BigGraph to find closest neighbors; 

search.py includes a closest neighbor function, which takes in a wikidata entity and outputs the wikidata entities that are most closely related to the input.

It requires running the id_to_index and tsv_to_np code first as those will give you the files that search.py uses to run a fast and efficient algorithm.

## How to use it:

### 1: Download wikidata_translation_v1_names.json:
https://dl.fbaipublicfiles.com/torchbiggraph/wikidata_translation_v1_names.json.gz

This file allows the search.ipynb code to map wikidata entities to names. 
### 2: Run the id_to_index.ipynb code:
This converts the data from wikidata_translation_v1_names.json into .pkl files separated such that search.ipynb can process them.

### 3: Open search.ipynb:
Download the libraries that are imported, most notably, the installation of faiss can be found here: https://github.com/facebookresearch/faiss
Choose to either run the closest neighbor code, or the closest relations code. For each function, the required specified parameters are commented within.

#### Note: As of now the closest relations function is not working, but this is because the graph embeddings from fb research do not support it yet.

#### Citations:
```tex
@inproceedings{pbg,
  title={{PyTorch-BigGraph: A Large-scale Graph Embedding System}},
  author={Lerer, Adam and Wu, Ledell and Shen, Jiajun and Lacroix, Timothee and Wehrstedt, Luca and Bose, Abhijit and Peysakhovich, Alex},
  booktitle={Proceedings of the 2nd SysML Conference},
  year={2019},
  address={Palo Alto, CA, USA}
}
```
