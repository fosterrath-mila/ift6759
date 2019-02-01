import os
import sys
sys.path.append("../")
import argparse

import numpy as np
from joblib import load  # You can use Pickle or the serialization technique of your choice

from dataset import HoromaDataset  # Import your own pytorch Dataset here


def eval_model(model_path, dataset_dir="/rap/jvb-000-aa/COURS2019/etudiants/data/horoma/", split="valid"):
    '''
    # MODIFY HERE #
    This function is meant to be an example

    '''

    # # SETUP DATASET # #
    # Load requested dataset
    #
    # IMPORTANT info on splits # of example.
    # "train" = 1614216
    # "valid" = 201778
    # "test"  = 201778
    if dataset_dir is not None and os.path.exists(dataset_dir):
        dataset = HoromaDataset(dataset_dir, split)
        dataset = np.asarray(dataset.data[:dataset.nb_exemples]).reshape(dataset.nb_exemples, -1)
    else:
        print("dataset_dir is not set.\nExiting ...")
        exit(1)

    # # SETUP MODEL # #
    # Load your best model
    if model_path is not None and os.path.exists(model_path):
        print("\nLoading model from ({}).".format(model_path))
        model = load(model_path)
    else:
        print("model_path ({}) does not exists or unreachable.\nExiting ...".format(model_path))
        exit(1)

    # # INFERENCE # #
    # Use model on dataset to predict the class triplet
    labels_pred_s = model['specie'][0].predict(dataset)
    pred_s = model['specie'][2].inverse_transform(np.asarray(model['specie'][1])[labels_pred_s])

    labels_pred_d = model['density'][0].predict(dataset)
    pred_d = model['density'][2].inverse_transform(np.asarray(model['density'][1])[labels_pred_d])

    labels_pred_h = model['height'][0].predict(dataset)
    pred_h = model['height'][2].inverse_transform(np.asarray(model['height'][1])[labels_pred_h])

    y_pred = np.asarray(list(zip(pred_s, pred_d, pred_h)))
    return y_pred


if __name__ == "__main__":

    # Put your group name here
    group_name = "b1phutN"

    model_filename = None
    # model_filename should be the absolute path on shared disk to your best model.
    # You need to ensure that they are available to evaluators on Helios.

    #########################
    # DO NOT MODIFY - BEGIN #
    parser = argparse.ArgumentParser()

    parser.add_argument("--dataset_dir", type=str, default='')
    # dataset_dir: Absolute path to the dataset directory

    parser.add_argument("--results_dir", type=str, default='')
    # results_dir will be the absolute path to a directory where the output of
    # your inference will be saved.

    args = parser.parse_args()
    dataset_dir = args.dataset_dir
    results_dir = args.results_dir

    print("\nEvaluating results ... ")
    y_pred = eval_model(model_filename, dataset_dir)

    assert type(y_pred) is np.ndarray, "Return a numpy array"
    assert len(y_pred.shape) == 2, "Make sure ndim=2 for y_pred"

    results_fname = os.path.join(results_dir, "{}_eval_pred.txt".format(group_name))

    print('\nSaving results to ', results_fname)
    np.savetxt(results_fname, y_pred, fmt='%s')
    # DO NOT MODIFY - END #
    #######################
