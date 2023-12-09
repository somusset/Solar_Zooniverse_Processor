# MP4 Generator for Solar Flares

## Foreword

This repo is forked from [Kekoa's Version](https://github.com/kekoalasko/Solar_Zooniverse_Processor) for the purpose of using the `make_movie.py` script to convert HEK event to MP4s for use in the Zooniverse Project [Solar Jet Hunter](https://www.zooniverse.org/projects/sophiemu/solar-jet-hunter). You can check out [Kekoa's Version](https://github.com/kekoalasko/Solar_Zooniverse_Processor) if you want to learn more about the ins and outs of how the repo works. If you're just here to generate some MP4s, read on!

While typing up this README, I did some testing to verify whether or not things needed to be done the way that I thought they did. In doing so, I found out that things can be done a bit easier than I have been doing them! While this is nice, it also means that the same issues that caused me to have be do things in a convoluted manner might arise again for whoever is using this. Therefore, along with the simplified instructions, I'll be including the more convoluted instructions that one may have to use in order to get things to work.


# Instructions

In a Linux terminal, clone this repo. I couldn't get Windows to run the scripts. Step into the new directory.

```
git clone https://github.com/lestatclemmer/Solar_Zooniverse_Processor
cd Solar_Zooniverse_Processor
```


I suggest using a Python virtual environment as the code requires particular versions of certain packages. Then change your source to this environment.

```
python3 -m venv myenv
source myenv/bin/activate
```


Install the necessary packages using the `setup.py` script. Also install additional necessary packages not listed there.

```
python setup.py install
pip install git+https://github.com/zooniverse/aggregation-for-caesar.git peewee requests tqdm sunpy
```


Step into the directory where the `make_movie.py` script is located.

```
cd examples
```


Run the `make_movie.py` script, specifying the timeframe you'd like to search for HEK events to generate MP4s for. (e.g. yyyy-mm-dd)
I've found that including the `-o` (overwrite) option is necessary for creating the individual PNGs that comprise the resulting MP4.
The `-i` option is needed to specify the timeframe to search.

```
python make_movie.py -oi <timeframe>
```


This will take some time, depending on how many solar events are found in the specified timeframe.
Once it is finished, you can find the generated MP4s in the `examples/files/generated/mp4/` directory, titled by their SOL standard name.
You can now choose to run the script again for a different timeframe if you'd like! They should be saved in the same directory without touching what is already there.

If you run into issues of confusing origin, (ESPECIALLY related to database problems in relation to the `peewee` package!), consider using the below steps. While they are more convoluted, they've worked for me in the past to get things running smoothly.
Hopefully it doesn't have to come to that for you, but if you have an unstable connection that causes the `make_movie.py` script to fail, leading to corrupted databases and the like, then you might just have to take that option every time like I have in the past.


# Try This if Things Aren't Working Correctly

So the simplified instructions didn't work out for ya? No worries! They didn't work for me at first either. The below instructions are what I had to do to bypass many of the issues I was having.
The main difference is that the cloned repo is quarantined from the directories that are being worked on. This is because when the `make_movie.py` script would fail on me, which it would often, the repo files seemed to be contaminated in a way that disallowed the script to properly work again. Only by using a fresh repo and virtual environment was I able to proceed once more with generating MP4s.

In addition to the steps given below, there is a script provided (setup-solar-zooniverse.py) that should automatically perform the needed steps to produce MP4 files for a given timeframe. I made this to combat the few-minute-long process required to set everything up after a failed attempt. Feel free to try it out if you find you're having to start fresh often.
Just be sure to read its comments before using it.


## Backup Instructions

Create a folder for everything to reside in. I chose to name it solar-zooniverse-test, but you can name it whatever you'd like. Step into this directory.

```
mkdir solar-zooniverse-test
cd solar-zooniverse-test
```


In a Linux terminal, clone this repo. I couldn't get Windows to run the scripts. This will serve as the "quarantined" version of the repo so that when you need to start over with an untouched repo, you can save yourself the ~15 seconds it would take to clone it from GitHub.

```
git clone https://github.com/lestatclemmer/Solar_Zooniverse_Processor
```


Create a separate directory that will be used to hold the files that are doing the MP4 generation. I'd suggest naming it the date of the HEK events that you're generating MP4s for. Step in to that directory.

```
mkdir <date>
cd <date>
```


Create a new Python virtual environment, as the code requires particular versions of certain packages. Then change your source to this environment.

```
python3 -m venv myenv
source myenv/bin/activate
```


Clone the "quarantined" repo to this directory. Step into the new directory.

```
git clone ../Solar_Zooniverse_Processor
cd Solar_Zooniverse_Processor
```


Install the necessary packages using the `setup.py` script. Also install additional necessary packages not listed there.

```
python setup.py install
pip install git+https://github.com/zooniverse/aggregation-for-caesar.git peewee requests tqdm sunpy
```


Step into the directory where the `make_movie.py` script is located.

```
cd examples
```


Run the `make_movie.py` script, specifying the timeframe you'd like to search for HEK events to generate MP4s for. (e.g. yyyy-mm-dd)
I've found that including the `-o` (overwrite) option is necessary for creating the individual PNGs that comprise the resulting MP4.
The `-i` option is needed to specify the timeframe to search.

```
python make_movie.py -oi <timeframe>
```


Once finished, move the generated files out and delete the unnecessary cloned repo and virtual environment to save space. Deactivate virtual environment.
```
mv files ../..
cd ../..
rm -rf Solar_Zooniverse_Processor myenv
deactivate
```


Whenever you find yourself needing to restart, just start fresh with a new virtual environment and repo.


















