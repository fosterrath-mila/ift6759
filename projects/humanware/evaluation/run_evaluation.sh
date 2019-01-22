#!/bin/bash

cd "${PBS_O_WORKDIR}"
source /rap/jvb-000-aa/COURS2019/etudiants/common.env

# PROJECT_PATH will be changed to the master branch of your repo
PROJECT_PATH='/rap/jvb-000-aa/COURS2019/etudiants/ift6759/projects/humanware/'

RESULTS_DIR='/rap/jvb-000-aa/COURS2019/etudiants/ift6759/projects/humanware/evaluation'
DATA_DIR='/rap/jvb-000-aa/COURS2019/etudiants/ift6759/projects/humanware/data/SVHN/test_sample'
METADATA_FILENAME='/rap/jvb-000-aa/COURS2019/etudiants/ift6759/projects/humanware/data/SVHN/test_sample_metadata.pkl'

s_exec python $PROJECT_PATH/evaluation/eval.py --dataset_dir=$DATA_DIR --results_dir=$RESULTS_DIR --metadata_filename=$METADATA_FILENAME
