# Woo Factor Music 

Woo Factor Music is a company that creates music for use in television, film and advertising.

## Brief Description of Project 
 Our team has joined this project to help with early stage research into how to understand and then automatically generate the basic architecture of a song, which is called it's "chord progression".

For this project, we worked on developing a tool that allows us to digitally represent songs at the grammatical chord progression level. Based on that chosen representation scheme, we extended the tool to be able to predict where the song could go.
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) or pycharm to install the following packages.

```bash
pip install mingus
pip install matplotlib
pip install fluidsynth
```
## Usage

The main algorithm that the user will interface with is predictor.py. Inside of the directory or through an IDE run predictor.py. 
```
 \Woofactor> python predictor.py
 ```
The user is prompted to generate a model. If this is the first time predictor.py is run the user will need to input “Y” to create a model based on the existing data. Any time data is adjusted a new model should be generated however given an invalid prompt the value will default to N.
``` 
 Play music? (Y/N) N
 ```
The user is then given the choice of the key of the output. Any major or minor key is valid and the user will be prompted again if the input is invalid. 
```
 What key would you like the final out put to be in? C
```
The next prompt is for the initial data provided to the algorithm. The user must input a comma separated list of chords in the form of Roman numerals. This input will be used to predict the next chord progression.
```
 Comma separated list of chords in roman numeral form: I,IV
 ```
 This will result in the predictions being output
 ```
 | I | IV | I | V | V | V | V | I | I | I |
 | C | F | C | G | G | G | G | C | C | C |
 ```
 The final prompt allows the user to generate another progression from new input otherwise the program will terminate when the user inputs “stop” 
 ```
 Generate another? ('stop') to end:
 ```
