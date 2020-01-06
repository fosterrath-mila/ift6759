# FAQ


## I tried to connect to Helios multiple times with the wrong password and now, I cannot connect anymore, what should I do? <a name="q_ban"></a>

The ban policy on Helios is 15 minutes for the first series of attempts and 24 hours for the next ones.


## Is it mandatory to do the project presentations in English?<a name="q_lang"></a>

No. Although, you should consider it as an opportunity to practice your presentation skills in the language of your choice (English or French). Only make sure that you can communicate the concepts clearly.


## How many hours should I expect to work outside of the class hours?<a name="q_hour"></a>

If you master the prerequisites of the course provided during the first two weeks of the course, then 12 hours should be enough.

## How can I create/use a tensorflow 2.0-compatible virtual environment on Helios?

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
If you want to create your virtual environment on the compute node directly to improve performance, you
should create it in the directory specified by ``$SLURM_TMPDIR`` inside your batch script:
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
