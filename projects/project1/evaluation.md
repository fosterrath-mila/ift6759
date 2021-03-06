# Model Evaluation Guidelines

We provide a script ([``evaluator.py``](evaluator.py)) in this repository that must be slightly modified in
order to prepare your own data loading pipeline and model for evaluation. The predictions of your model will
be exported and compared to the (withheld) groundtruth over the test period. Your prediction errors will then
be aggregated and compared to those of other teams to create a performance ranking.

## Evaluation script

The [``evaluator.py``](evaluator.py) script has two important functions: ``prepare_dataloader`` and
``prepare_model``. These will be imported into another nearly identical script for final analysis and execution.
On your side, ``evaluator.py`` contains the evaluation loop and everything else you need to produce and save
your model's predictions. If you modify the two functions and correctly manage to save predictions into text
files, you should be OK for the final test on our side.

Note that any modification to the ``evaluator.py`` script outside of the two target functions will be ignored.
If these functions were not implemented or if something breaks during evaluation, your model will not be ranked,
and you will be penalized.

You can import 3rd-party packages you require inside the target functions directly. However, these packages
should be available on PyPI, and these should be listed in the ``requirements.txt`` file submitted alongside
the evaluation script. Remember: the evaluation script will be running from within your team's submission
folder. This means you can easily import your own Python modules that are also placed within this folder.

### Data loader preparation (``prepare_dataloader``)

Our goal is to evaluate the performance of your model, but your model's behavior is tied to the way it receives
its input data. As such, you will need to "set the table" yourself and connect your own data pipeline to your
own model.

If your data pipeline does not only rely on the original data sources (NetCDF/HDF5 files), you will have to
generate the intermediary representations you need in the ``prepare_dataloader`` function. In any case, that
function must return a ``tf.data.Dataset`` object that is ready to generate input tensors for your model.
These tensors should be provided in a tuple, as documented [here](datasources.md#pipeline-formatting).

As mentioned in the project presentation, your data pipeline will have access to all the imagery during
evaluation. However, your model's predictions **cannot** rely on "future" imagery. This means that given
the list of timestamps to generate predictions for, you can only ever use imagery that comes **before
(or exactly at)** each of the timestamps. We will be heavily penalizing teams that do not respect this
rule in their final submission, and we already have scripts in place to detect this. If you are unsure about
this rule, you can ask a TA for clarification.

A configuration dictionary can optionally be used to provide (and keep track of) external hyperparameters
for your pipeline's constructor. If required, your final submission should include a JSON file named
``eval_user_cfg.json`` in your team's ``code`` folder (see [this page](../../disk-usage.md) for more info
on the submission directory structure). For more information on the ``prepare_dataloader`` function, refer
to its [docstring](evaluator.py).

### Model preparation (``prepare_model``)

The model preparation function itself can be fairly minimalistic depending on your model's architecture.
For example, users that built ``tf.keras``-compatible models will only need to fill this function with:
```
path = "/project/cq-training-1/project1/submissions/teamXX/model/best_model.pth"
model = tf.keras.models.load_model(path)
```
During the final evaluation, your submitted checkpoint should be located in the ``model`` directory alongside
your code. This means that you will be able to open it directly using its absolute path (as shown above). For
more information on the model submission process, refer to [this guide](../../howto-submit.md).

A configuration dictionary can optionally be used to provide (and keep track of) external hyperparameters
for your model's constructor. If required, your final submission should include a JSON file named
``eval_user_cfg.json`` in your team's ``code`` folder. For more information on the ``prepare_model``
function, refer to its [docstring](evaluator.py).

### Testing your modified evaluation script

A dummy dataframe with the same columns as the final test dataframe is provided [here](dummy_test_catalog.pkl)
for pre-testing purposes, and a compatible admin test file is provided [here](dummy_test_cfg.json).
These only rely on the data already at your disposal, but the real test set will rely on withheld data.

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

As a particularity of the evaluation script, note that we will be providing you with a dictionary of
the stations of interest for which to prepare your data loader/model. We do this in order to control the
ordering of the predictions to make sure stations are not arbitrarily mixed. In practice, this means that,
during the final test, your ``prepare_dataloader`` and ``prepare_model`` functions may be called up to seven
times each (once per station).

Regarding the "datetimes" that will be used for the final test: as mentioned in the project presentation, we
will be focused on daytime GHI predictions. Also, for a single "target datetime" (``T_0``), remember that we
expect your model to produce four GHI values, i.e. one for each of ``[T_0, T_0 + 1h, T_0 + 3h, T_0 + 6h]``.
Due to the wide "horizon" that a single target datetime covers, it is possible that predictions for ``T_0`` may
fall in nighttime (e.g. if ``T_0`` is 4PM).  In order to still properly cover all real use cases of a GHI
prediction model, we will still ask for prediction sequences that partly fall after sunset or before sunrise.
In those cases, only the GHI predictions that correspond to timestamps in the day will be kept for analysis.

Finally, note that your model should in no circumstances produce Not-A-Number (NaN) values as output. The
evaluation will throw an error if it does, and you will be penalized. If the groundtruth contains a NaN value
for a target GHI, we will ignore its impact on our end. We will also only focus on daytime sequences and thus
ignore nighttime predictions.

The TAs will be offering evaluation "simulations" during the last class before the submission deadline. This
will allow you to confirm that:

  - Your team's submission has the expected directory structure;
  - The dependencies inside your ``requirements.txt`` file can be installed in our job environment;
  - Your ``evaluator.py`` script's modified functions are compatible with our version of the script;
  - Your model's checkpoint is indeed accessible and reloadable on our GPUs;
  - The preparation of your data loading pipeline and model do not take too long or hang; and
  - Your model's performance is not completely abysmal.

The last point means that TAs might choose to warn you if your model seems to be behaving oddly, but they
will not give you a direct indication of how well your model performs. We expect the final test set to contain
roughly 800-1000 different timestamps for which to generate GHI predictions. The time required to prepare your
data loader/model and infer these GHI values should not exceed (roughly) 30 minutes.
