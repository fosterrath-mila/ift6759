# Model Evaluation Guidelines

@@@@ TODO ADD PATHS

We provide [a script](@@@@TODO@@@) in this repository that must be slightly modified in order to prepare your
own data loading pipeline and model for evaluation. The predictions of your model will be exported and compared
to the (withheld) groundtruth over the test period. Your prediction errors will then be aggregated and compared
to those of other teams to create a performance ranking.

## Evaluation script

The ``evaluator.py`` script has two important functions: ``prepare_dataloader`` and ``prepare_model``. These will
be imported into another (withheld) script that we have already written. On your side, ``evaluator.py`` contains
everything you need to produce model predictions in an evaluation loop. If you modify the two functions properly
and correctly generate predictions into text files (using e.g. your own set of validation data), you can assume
that the same code will work on our side for the final test. A dummy dataframe with the same content as the final
test dataframe is also provided [here](@@@@TODO@@@@).

Note that any modification to the ``evaluator.py`` script outside of the two target functions will be ignored.
If these functions were not implemented or if something breaks during evaluation, your model will not be ranked,
and you will be penalized.

### Data loader preparation (``prepare_dataloader``)

Our goal is to evaluate the performance of your model, but your model's behavior is tied to the way it receives
its input data. As such, you will need to "set the table" yourself and connect your own data pipeline to your
own model for the ultimate test.

If your data pipeline does not only rely on the original data sources (NetCDF/HDF5 files), you will have to
generate the intermediary files you need in the ``prepare_dataloader`` function. In any case, that function
must return a ``tf.data.Dataset`` object that is ready to generate input tensors for your model.

A configuration dictionary can optionally be used to provide external hyperparameters to your pipeline's
constructor. If required, your final submission will need to include this file as ``@@@ TBD @@@``.

For more information on the ``prepare_dataloader`` function, refer to its [docstring](@@@@TODO@@@@).

### Model preparation (``prepare_model``)

The model preparation function itself can be fairly minimalistic based on your model's architecture. For
example, users that built ``tf.keras``-compatible models will only need to fill this function with:
```
    model = tf.keras.models.load_model(PATH_TO_MODEL_CHECKPOINT)
```
During the final evaluation, your submitted checkpoint will be located in the current working directory,
meaning you can open it directly using only its name. For more information on the model submission process,
refer to [this guide](https://github.com/mila-iqia/ift6759/blob/master/howto-submit.md).

A configuration dictionary can optionally be used to provide external hyperparameters to your model's
constructor. If required, your final submission will need to include this file as ``@@@ TBD @@@``.

For more information on the ``prepare_model`` function, refer to its [docstring](@@@@TODO@@@@).

## Evaluation utilities

@@@@ TODO viz stuff, plots, ...
