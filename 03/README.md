# Assignment 3



## 1. Game of Thrones - Dig into the battles!

<p align="center">
  <img src="Image/got.jpg" alt="Jon & Sansa"/>
</p>


In this exercise, we ask you to create a `battle.json` file which contains specific informations about each battle in GoT.

In particular, we provide you a set of files (`.txt` and `.json`), each of those contain information which are useful to get the file `battle.json`. 

The file you'll produce should be in the following form:

                    {'Name battle': {'Location': 'Winterfell',
                                     'Attacker King': 'Robb Stark',
                                      ...}}
                                                 
For each battle you should have:
* Region
* Location
* Attacker king
* Defender king

While solving the task we ask you to:

1. Define functions when you notice you use the same set of operations more than once (e.g. open a `.json`)
2. Play a bit with dictionaries :-)


In the end, pleas print in the final notebook the info of `Battle of Winterfell` and the `Battle of Oxcross`.

### Practical instruction


1. In your assignment folder, create a `Notebook` called: `Assignment 3`
2. Nicely comment the code and the `Notebook`. In the latter, you should explain all the resoning behind your choices and procedures. It is preferable that the functions you create, are stored in an external `.py` (as shown during the lecture) and then imported in the `Notebook`.
3. In the eand you'll have:
	* One `Notebook`
	* One `.py` file with your functions 
	* One `battle.json` 
4. Once you've finished:
	* Add
	* Commit 
	* Push
	


### Data

The folder `Data/` contains the following files:

1. `battle_names.txt`:

	> This file contains the name of all the battles. 
2. `battle_location.json`:

	> The file contains a dictionary (key,value):(battle,list of locations)
3. `king_attacker_battles.json`:

	> Here the dictionary (key, value):(attacker king, list of battles) is stored.

4. `king_defender_battles.json`: 

	> Here the dictionary (key, value):(defender king, list of battles) is stored.

5. `region_locations.json`:

	> Dictionary (key, value):(region, list of locations)
	

__REMARK__: Be careful and check whether there are battles that expressed with different names (e.g. `Sack of Winterfell` and `Battle of Winterfell`), if yes fix it!




## 2. Back to assignment 2, compute 12!

Obtain the same result in one line of code (hint: use a function we explained today!)

## 3. Cloud of words

From the file `battles.json`:

* Get the `list` of all the words
* Process each word of the list making it lowercase (remember the pythonic whay of applying a function to a list..)
* Keep words whose `len` is greater than 3
* Use the list of words to create a cloud of words. To do it follow the instruction [here](https://github.com/amueller/word_cloud).


# Write on Slack for any question!
