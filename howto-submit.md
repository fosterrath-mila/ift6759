# Submitting your projects

## How to submit
In order to ensure a streamlined and easy project submission, please follow the evaluation guidelines carefully. Each project will have its own evaluation guidelines. Please note that failure to follow these guidelines can result in a submission that will not be accepted.

[Project 1 guidelines](projects/project1/evaluation.md)

[Project 2 guidelines](projects/project2/evaluation.md)

## Where to submit

You will be submitting your entire projects on the Helios cluster. We have created a repository for you to submit your code. The repository is at

`/project/cq-training-1/project1/submissions/`
`/project/cq-training-1/project2/submissions/`

Inside the `submissions/` folder, you must create a folder with your team name (i.e. `team00`). There should be one and only one submission per team. Within the folder, we expect to find your report (.pdf format only!), a `model/` directory and a `code/` directory. Your folder structure should look something like this:

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
            │   └── evaluation
            │       └── eval.py
            ├── model
            │   └── best_model.pth
            └── sample_report.pdf

```

Your `code` repository should be a clone of the code on your master branch of the github repo. It should only contain code that is relevant to the evaluation. This is what will be used to evaluate your code. In order to rename a folder to `code` when using `git clone`, you can use

`git clone https://github.com/username/your-project code` 

from within your team directory. It is your responsibility to ensure that your submissions runs properly on the test set. This includes making sure proper permissions are set and that proper paths are set according to submission guidelines. 

