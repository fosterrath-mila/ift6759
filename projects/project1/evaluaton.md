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

### Data loader preparation (``prepare_dataloader``)

@@@@ TODO


### Model preparation (``prepare_model``)

@@@@ TODO

## Evaluation utilities

@@@@ TODO viz stuff, plots, ...
