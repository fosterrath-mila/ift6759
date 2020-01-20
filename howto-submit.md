# Submitting your projects

## How to submit
In order to ensure a streamlined and easy project submission, please follow the evaluation guidelines
carefully. Each project has its own evaluation guidelines. Please note that failure to follow these
guidelines can result in a submission that will not be accepted.

[Project 1 guidelines](projects/project1/evaluation.md)

[Project 2 guidelines](projects/project2/evaluation.md) (to be added soon)

## Where to submit

You will be submitting your entire projects on the Helios cluster. We have created a repository for
you to submit your code. The repository is at

`/project/cq-training-1/project1/submissions/`
`/project/cq-training-1/project2/submissions/`

Inside the `submissions/` folder, you must create a folder with your team name (i.e. `team00`). There
should be one and only one submission per team. Within your folder, we expect to find your report (.pdf
format only!), a `model/` directory and a `code/` directory. Your folder structure should look like this:

```
/project/cq-training-1/
└── project1
    ├── teams
    │   └── team00
            └── ...
            └── ...
            └── ...
    └── submissions
        └── team00
            ├── code
            │   └── .git/
            │   └── ...
            │   └── requirements.txt
            │   └── evaluator.py
            ├── model
            │   └── best_model.pth
            └── sample_report.pdf

```

Your `code` repository should be a clone of your master branch on github. It should contain all the code that
is relevant for the evaluation. It should also contain a `requirements.txt` file listing your project's dependencies
so that we can easily reinstall an environment compatible with your code. The `evaluator.py` script must be located
in this folder as well, and it should be properly updated to work your with your other Python modules.

In order to rename a folder to `code` when using `git clone`, you can use

`git clone https://github.com/username/your-project code`

from within your team directory. During the evaluation process, we will be executing `evaluator.py` with the `code`
folder as the current working directory. It is your responsibility to ensure that your submissions runs properly
on the (dummy) test set. This includes making sure proper permissions are set and that proper paths are set
according to submission guidelines. For more information, refer to the [links at the top of this page](#how-to-submit).
