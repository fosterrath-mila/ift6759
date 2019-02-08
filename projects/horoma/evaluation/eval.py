import os
import sys
import argparse

import numpy as np
from joblib import load  # You can use Pickle or the serialization technique of your choice

sys.path.append("../")
from dataset import HoromaDataset  # Import your own pytorch Dataset here


def eval_model(model_path, dataset_dir, split):
    '''
    # MODIFY HERE #
    This function is meant to be an example

    '''

    # # SETUP DATASET # #
    # Load requested dataset
    """ IMPORTANT # of example per splits.
    "train" = 1614216
    "valid" = 201778
    "test"  = 201778

    Files available the test folder:
    definition_labels.txt
    train_x.dat
    valid_y.txt
    valid_x.dat
    test_x.dat
    test_y.txt

    You need to load the right one according to the `split`.
    """
    dataset = HoromaDataset(dataset_dir, split)

    # # SETUP MODEL # #
    # Load your best model
    print("\nLoading model from ({}).".format(model_path))
    model = load(model_path)

    # # INFERENCE # #
    # Use model on dataset to predict the class triplet
    pred = {}
    for task in dataset.targets.keys():
        cluster_pred = model[task]['kmeans'].predict(dataset.data)
        target_pred = model[task]['cluster_label'][cluster_pred]
        pred[task] = dataset.map_labels[task][target_pred]

    # # PREDICTIONS # #
    # Return the predicted class triplet as a numpy array of shape (nb_exemple, 3)
    """ Example:
    [['ES' '75' '25']
     ['EN' '65' '15']
     ['ES' '75' '20']]
    """
    y_pred = np.column_stack((pred['species'], pred['densities'], pred['heights']))
    return y_pred


if __name__ == "__main__":

    # Put your group name here
    group_name = "b1phutN"

    model_path = None
    # model_path should be the absolute path on shared disk to your best model.
    # You need to ensure that they are available to evaluators on Helios.

    #########################
    # DO NOT MODIFY - BEGIN #
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dataset_dir", type=str, default="/rap/jvb-000-aa/COURS2019/etudiants/data/horoma/", help="Absolute path to the dataset directory.")
    parser.add_argument("-s", "--dataset_split", type=str, choices=['valid', 'test', 'train'], default="valid", help="Which split of the dataset should be loaded from `dataset_dir`.")
    parser.add_argument("-r", "--results_dir", type=str, default="./", help="Absolute path to where the predictions will be saved.")
    args = parser.parse_args()

    # Arguments validation
    if group_name is "b1phutN":
        print("'group_name' is not set.\nExiting ...")
        exit(1)

    if model_path is None or not os.path.exists(model_path):
        print("'model_path' ({}) does not exists or unreachable.\nExiting ...".format(model_path))
        exit(1)

    if args.dataset_dir is None or not os.path.exists(args.dataset_dir):
        print("'dataset_dir' does not exists or unreachable..\nExiting ...")
        exit(1)

    y_pred = eval_model(model_path, args.dataset_dir, args.dataset_split)

    assert type(y_pred) is np.ndarray, "Return a numpy array"
    assert len(y_pred.shape) == 2, "Make sure ndim=2 for y_pred"
    assert y_pred.shape[1] == 3, "Make sure you have all 3 predictions for y_pred"

    results_fname = os.path.join(args.results_dir, "{}_pred_{}.txt".format(group_name, args.dataset_split))

    print('\nSaving results to ({})'.format(results_fname))
    np.savetxt(results_fname, y_pred, fmt='%s')
    # DO NOT MODIFY - END #
    #######################
