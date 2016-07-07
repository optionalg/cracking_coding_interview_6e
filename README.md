# Cracking The Coding Interview, 6th Edition

####Solutions a la Python

Because who doesn't love Python, **right**?

## Basic Usage

**Installation:**

```sh
git clone https://github.com/kevinschaich/cracking_coding_interview_6e/
virtualenv venv
source venv/bin/activate
pip install pytest
deactivate  #optional
```

**Running Tests:**

```sh
cd cracking_coding_interview_6e
source venv/bin/activate
py.test s09*
```

## Introduction

The goal of this repository is to eventually create a **central, complete guide to Python solutions** of the problems contained in *Cracking the Coding Interview, 6th edition* by Gayle Laakman McDowell.

I will do my best to write **clean**, **beautiful**, **correct**, and **efficient** code. Some solutions may not fulfill all of these goals, and I welcome your criticism and feedback.

I also hope that this project serves as a learning utility for bettering my software development etiquette. I will make a strong effort to always include the problem statements of each question, write proper docstrings, as well as include (to the best of my knowledge) the time/space complexity of my solutions.

I will also try to include a few corner **unit tests** as proof of correctness for each of my solutions. Please note that I will be using [pytest](http://www.pytest.org) due to its simplicity (in the spirit of Python).

#### Why Python?

There's a lot to love. Python is **fast**, **clean**, **readable**, **easy to debug**, and **dynamically typed**. IMHO, there is nothing simpler for interview questions, and so far my only complaint about the book is the author's decision to make Java the language of choice for solutions. Focusing on syntax-specific errors is a waste of your time and your interviewer's.

#### Disclaimer

The content contained in this repository is strictly for educational purposes only. I do not make any claims concerning the correctness nor efficiency of any code, nor do I claim ownership of any of the content or questions contained in the book.
