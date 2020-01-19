# FAQ


## I tried to connect to Helios multiple times with the wrong password and now, I cannot connect anymore, what should I do? <a name="q_ban"></a>

The ban policy on Helios is 15 minutes for the first series of attempts and 24 hours for the next ones.


## Is it mandatory to do the project presentations in English?<a name="q_lang"></a>

No. Although, you should consider it as an opportunity to practice your presentation skills in the language of your choice (English or French). Only make sure that you can communicate the concepts clearly.


## How many hours should I expect to work outside of the class hours?<a name="q_hour"></a>

If you master the prerequisites of the course provided during the first two weeks of the course, then 12 hours should be enough.

## How can I create/use a TensorFlow 2.0-compatible virtual environment on Helios?

To create a virtual environment (here, named ``ift6759-env``) in your home directory:
```
module load python/3.7
virtualenv --no-download ~/ift6759-env
source ~/ift6759-env/bin/activate
pip install --no-index --upgrade pip
pip install -r /path/to/your/project/requirements.txt
```
It is up to you to fill ``requirements.txt`` with your project's dependencies. The file should at least
contain ``tensorflow-gpu==2.0``.

To reactivate the environment later once it is created:
```
source ~/ift6759-env/bin/activate
```

Remember that if you create your virtual environment within your home directory (or in your team's
shared directory), you will be able to access it on both login and compute nodes.

If you want to create your virtual environment on the compute node's local disk directly to improve
performance, you should create it in the ``$SLURM_TMPDIR`` directory from your job's script:
```
#!/bin/bash
#SBATCH --account=guestXXX
#SBATCH --mem-per-cpu=1.5G
#SBATCH --time=12:00:00

# .. other slurm options here ...

module load python/3.7
virtualenv --no-download $SLURM_TMPDIR/ift6759-env
source $SLURM_TMPDIR/ift6759-env/bin/activate
pip install --no-index --upgrade pip
pip install -r /path/to/your/project/requirements.txt

# ... your actual launch instructions here ...
```
This will add a bit of overhead to your jobs, but that overhead should be negligible compared to the
overall executon time.

## How do I use my virtual environment within a JupyterHub notebook?

1. Activate your environment. Assuming the above steps, this can be done via `source ~/ift6759-env/bin/activate`
2. `pip install ipykernel`
3. `python -m ipykernel install --user --name=ift6759-env`

On reloading the JupyerHub root, you should now be able to see `ift6759-env` under *New* on the top right.

## Can I install TensorFlow (or other packages) directly in a JupyterHub notebook?

Yes, you can, even if you don't have a virtual environment set up. In a code cell, you only have to run:
```
!pip install --no-index <package_name>
```
For example:
```
!pip install --no-index tensorflow-gpu==2.0
```
This installation procedure is **NOT** compatible with notebooks created with an external virtual
enviroment (as detailed in the previous answer).

## Can I use a virtual environment within a JupyterHub terminal?

No, that terminal seems unable (as of 2019/01/15) to capture the changes in environment variables needed
to 'activate' an environment.

## How do create a SSH key to avoid entering my username and password each time?

Ubuntu and Mac OS users can follow [these instructions](https://help.ubuntu.com/community/SSH/OpenSSH/Keys) to generate an SSH keypair. The same process can be used to [authenticate with GitHub](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).
