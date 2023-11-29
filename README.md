# Advent of Code

## What is this?

Every year, the tireless _Eric Wastl_ creates fun, christmas themed coding problems, and releases them daily as an advent calendar, known as [Advent of Code](https://adventofcode.com/about)

Here's a snippet from the about page:
> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

Each day's challenge has two problems, each worth one ⭐. A simple example for each problem is provided with a small data input. Following this, each user receives a unique dataset for their problem, for which they use to calculate their unique solution to the day's challenge.

## Why am I doing this?
I hope to use these puzzles as an opportunity to learn and become accustomed to new libraries, techniques, datastructures and ways of critical thinking. I started this in 2019 and I hope to be able to progress further each year.

## How does it work?
Navigate through the directories in this repo to find my solutions for each of the challenges. Here you'll find the problem outline, as well as the solutions for both the examples given in the problem description, and the generated datafile for my user.

I typically solve most of these problems with Python, and to save myself some time (_and scratch that organisational itch_) I've setup a cookiecutter to nicely format my solutions.

To generate a solution skeleton for a new challenge, simply run the below command and complete the cookiecutter questionnaire.

```bash
pip install cookiecutter
cookiecutter -f https://github.com/Lewis-Gallagher/advent-of-code-cookiecutter
```

Instructions on how to execute the solutions will be detailed in the associated README for the problem, but generally you can just execute the Python files as normal.

```bash
python solution.py
```
