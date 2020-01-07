# Model Evaluation Guidelines

We provide [a script](evaluator.py) (``evaluator.py``) in this repository that must be slightly modified in order
to prepare your own data loading pipeline and model for evaluation. The predictions of your model will be exported
and compared to the (withheld) groundtruth over the test period. Your prediction errors will then be aggregated and
compared to those of other teams to create a performance ranking.

## Evaluation script

The ``evaluator.py`` script has two important functions: ``prepare_dataloader`` and ``prepare_model``. These will
be imported into another nearly identical script for final analysis and execution. On your side, ``evaluator.py``
contains the evaluation loop verything you need to produce model predictions. If you modify the two functions
and correctly manage to save your model's predictions into text files, you should be OK for the final test on our
side.

Note that any modification to the ``evaluator.py`` script outside of the two target functions will be ignored.
If these functions were not implemented or if something breaks during evaluation, your model will not be ranked,
and you will be penalized.

### Data loader preparation (``prepare_dataloader``)

Our goal is to evaluate the performance of your model, but your model's behavior is tied to the way it receives
its input data. As such, you will need to "set the table" yourself and connect your own data pipeline to your
own model.

If your data pipeline does not only rely on the original data sources (NetCDF/HDF5 files), you will have to
generate the intermediary representations you need in the ``prepare_dataloader`` function. In any case, that
function must return a ``tf.data.Dataset`` object that is ready to generate input tensors for your model.

A configuration dictionary can optionally be used to provide (and keep track of) external hyperparameters
for your pipeline's constructor. If required, your final submission should include a JSON file named
``eval_user_cfg.json`` in your team's ``code`` folder (see
[this page](https://github.com/mila-iqia/ift6759/blob/master/howto-submit.md) for more info on the submission
directory structure). For more information on the ``prepare_dataloader`` function, refer to its
[docstring](evaluator.py).

### Model preparation (``prepare_model``)

The model preparation function itself can be fairly minimalistic based on your model's architecture. For
example, users that built ``tf.keras``-compatible models will only need to fill this function with:
```
model = tf.keras.models.load_model(PATH_TO_MODEL_CHECKPOINT)
```
During the final evaluation, your submitted checkpoint will be located in the current working directory,
meaning you can open it directly using only its name. For more information on the model submission process,
refer to [this guide](https://github.com/mila-iqia/ift6759/blob/master/howto-submit.md).

A configuration dictionary can optionally be used to provide (and keep track of) external hyperparameters
for your model's constructor. If required, your final submission should include a JSON file named
``eval_user_cfg.json`` in your team's ``code`` folder (see
[this page](https://github.com/mila-iqia/ift6759/blob/master/howto-submit.md) for more info on the submission
directory structure). For more information on the ``prepare_model`` function, refer to its
[docstring](evaluator.py).

### Testing your modified evaluation script

A dummy dataframe with the same columns as the final test dataframe is provided [here](dummy_test_catalog.pkl)
for pre-testing purposes, and a compatible admin test file is provided [here](dummy_test_cfg.json). These only
rely on the data already at your disposal, but the real test will rely on withheld data.

To test your modified evaluation script, you should run it from your team's submission code directory as such:
```
cd /project/cq-training-1/project1/submissions/teamXX/code
python evaluator.py output.txt dummy_test_cfg.json
```
If you plan on also submitting a ``eval_user_cfg.json`` file, you can start the script via:
```
python evaluator.py output.txt dummy_test_cfg.json -u="eval_user_cfg.json"
```
We will automatically be detecting the user config file and providing if needed it in our own batch
evaluation script.
