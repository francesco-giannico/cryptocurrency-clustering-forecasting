from modelling.techniques.clustering.ensemble_clustering.consensus_clustering import consensus_clustering
from modelling.techniques.clustering.distance_measures.distance_measures import compute_distance_matrix
from utility.clustering_utils import generate_cryptocurrencies_dictionary, prepare_dataset_for_clustering, \
    separate_folders
from utility.dataset_utils import cut_dataset_by_range
from utility.folder_creator import folder_creator
from utility.reader import get_dict_symbol_id


def clustering(distance_measure,type_for_clustering,type_for_prediction,features_to_use=None):
    CLUSTERING_PATH = "../modelling/techniques/clustering/output/" + distance_measure + "/"
    PATH_SOURCE_CLUST= "../preparation/preprocessed_dataset/constructed/"+type_for_clustering+"/"
    PATH_SOURCE_PRED= "../preparation/preprocessed_dataset/constructed/" + type_for_prediction + "/"

    folder_setup(CLUSTERING_PATH)

    """prepare_dataset_for_clustering(input_path_type_for_clustering=PATH_SOURCE_CLUST,
                                   input_path_type_for_prediction=PATH_SOURCE_PRED,output_path=CLUSTERING_PATH)"""
    
    generate_cryptocurrencies_dictionary(PATH_SOURCE_CLUST,CLUSTERING_PATH)
    
    dict_symbol_id = get_dict_symbol_id(CLUSTERING_PATH)
    
    compute_distance_matrix(PATH_SOURCE_CLUST,dict_symbol_id,distance_measure,CLUSTERING_PATH,features_to_use)
    
    consensus_clustering(PATH_SOURCE_PRED,CLUSTERING_PATH)


def folder_setup(CLUSTERING_PATH):
    folder_creator(CLUSTERING_PATH, 1)
    folder_creator(CLUSTERING_PATH + "datasets/", 1)
    folder_creator(CLUSTERING_PATH + "original_datasets/", 1)
    return