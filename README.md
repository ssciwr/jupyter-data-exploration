# [Data Exploration with Python and Jupyter](https://ssciwr.github.io/jupyter-data-exploration)

[![SSC Compact Course](https://img.shields.io/badge/SSC-Compact_Course-blue?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0Mi4zNDc5MzkgNDIuMzQ4MTc1Ij4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzMuOTc4NzE5LC0zOC44NDg5MikiPgogICAgPHBhdGggZD0ibSAzMy45Nzg4OTMsNDMuODEyODU3IGMgMCwtMi43NDE0MzcgMi4yMjIzNjEsLTQuOTYzOTM3IDQuOTYzOTczLC00Ljk2MzkzNyBoIDMyLjQxOTg1NyBjIDIuNzQxNDM2LDAgNC45NjM5MzYsMi4yMjI1IDQuOTYzOTM2LDQuOTYzOTM3IHYgMzIuNDE5ODU2IGMgMCwyLjc0MTYwNiAtMi4yMjI1LDQuOTY0MTA2IC00Ljk2MzkzNiw0Ljk2NDEwNiBIIDM4Ljk0Mjg2NiBjIC0yLjc0MTYxMiwwIC00Ljk2Mzk3MywtMi4yMjI1IC00Ljk2Mzk3MywtNC45NjQxMDYgViA0My44MTI4NTciIHN0eWxlPSJmaWxsOiNmZmZmZmY7ZmlsbC1vcGFjaXR5OjE7ZmlsbC1ydWxlOm5vbnplcm87c3Ryb2tlOm5vbmUiLz4KICAgIDxwYXRoIGQ9Im0gNDkuNDM2NjMsNTcuNjUzODQ3IGMgMCwxLjc4ODU4MyAtMC42Njk0NjYsMy40MjA1NjggLTEuNzcxMzMyLDQuNjU5NDU0IC0yLjk2MDcyMywwLjY2NTAyMSAtNS44MzQ2MjgsLTAuMjc5MDgzIC03LjcyMzUwNiwtMS44NTg3MTYgLTEuOTM5OTk2LC0xLjYyMjQ5NiAtMy4wNjg3NDMsLTMuOTI2NzM1IC0zLjIzODY1NSwtNi44NjAyOTQgMS4yNzExMDcsLTEuNzg3NTk1IDMuMzU5Mzc2LC0yLjk1MzgwOCA1LjcxOTk1MywtMi45NTM4MDggMy44NzM1MzYsMCA3LjAxMzU0LDMuMTM5ODYzIDcuMDEzNTQsNy4wMTMzNjQiIHN0eWxlPSJmaWxsOiM0MGI5NDUiLz4KICAgIDxwYXRoIGQ9Im0gNjUuNzYyNzk5LDYzLjQzODg3MyBjIDIuNjg4NDEzLC0wLjMxMjgwOCA1LjQ4MjgwMiwwLjYzODE3NSA3LjQzMTU0NiwyLjgwMjkyNiAzLjE5NDc1NiwzLjU0ODczMyAyLjkwODMsOS4wMTUxMzEgLTAuNjQwMjkxLDEyLjIwOTgzIC0xLjY0MjE4MSwxLjQ3ODYzNiAtMy42OTUyMDcsMi4yMTE2MTMgLTUuNzQzODIzLDIuMjIwMjk1IC0zLjA0ODA3LC0yLjE2NDA2OSAtNC41NTIwNjgsLTUuNTczNjAzIC00LjY2MjczNCwtOC42MDU0NDYgLTAuMTEzOTQ4LC0zLjExNjU0NSAxLjA2NjYyMywtNi4wNTE5MDMgMy42MTUzMDIsLTguNjI3NjA1IiBzdHlsZT0iZmlsbDojZWUyMzI3Ii8%2BCiAgICA8cGF0aCBkPSJtIDY3Ljc0NDk1MSw1MC4xMDgyODIgYyAtMC41OTM5MzYsMS4xMTcwMzYgLTEuNTU3MTYxLDEuOTExMjA5IC0yLjY1OTMwOSwyLjMxMTkzIC0yLjA0Njk1OCwtMC41NjU1MzggLTMuNTExNzk3LC0yLjA5NDA1NCAtNC4xNjA0NSwtMy42OTE2NDQgLTAuNjY3NTI2LC0xLjY0NDgyNiAtMC42MDczMDcsLTMuNDQ0NjI4IDAuMjU1MDU4LC01LjMxODIzMSAxLjM3ODYyMSwtMC42OTYzODMgMy4wNjMyNDEsLTAuNzM0MTMgNC41MzA3MjYsMC4wNDY1NyAyLjM5ODIxOCwxLjI3NTY0NCAzLjMwODgwOCw0LjI1MzQ0MiAyLjAzMzk3NSw2LjY1MTM3OCIgc3R5bGU9ImZpbGw6I2JkMjI5OCIvPgogICAgPHBhdGggZD0ibSA1OC43NDExNDUsNTMuMzU0MjYxIGMgLTMuMDY4NjM4LC0yLjU3NDMyNSAtMy40NjkyMTcsLTcuMTQ4NTEzIC0wLjg5NDc1MSwtMTAuMjE2OTc0IDIuNTc0NDMyLC0zLjA2ODQ2MSA3LjE0ODk3MiwtMy40Njg1MTEgMTAuMjE3NTc0LC0wLjg5NDI5MiAzLjA2ODc0NCwyLjU3NDU3MyAzLjQ2OTE0Nyw3LjE0ODU0OSAwLjg5NDc4NiwxMC4yMTY5MDQgLTIuNTc0NDY3LDMuMDY4MzU2IC03LjE0OTAwNywzLjQ2ODY1MyAtMTAuMjE3NjA5LDAuODk0MzYyIHogTSAzMy45Nzg4OTMsNDMuODEyODU3IGMgMCwtMi43NDE0MzcgMi4yMjIzNjEsLTQuOTYzOTM3IDQuOTYzOTczLC00Ljk2MzkzNyBoIDMyLjQxOTg1NyBjIDIuNzQxNDM2LDAgNC45NjM5MzYsMi4yMjI1IDQuOTYzOTM2LDQuOTYzOTM3IGwgLTAuMDAxOCwyMC4wNDU2MSBjIC0yLjMwNTA1LC0yLjY4Nzg0OSAtNS43MzA1MjIsLTQuMzk2NjM0IC05LjU1NTE2MywtNC4zOTY2MzQgLTYuOTM5MjQ1LDAgLTEyLjU2NDM5Myw1LjYyNTI4OSAtMTIuNTY0MzkzLDEyLjU2NDU2OSAwLDMuNjE3NTk2IDEuNTI4OTA0LDYuODc4MTg3IDMuOTc1NzcxLDkuMTcwNjkyIEwgMzguOTQyODMsODEuMTk2ODE5IGMgLTIuNzQxNjEyLDAgLTQuOTYzOTczLC0yLjIyMjUgLTQuOTYzOTczLC00Ljk2NDEwNiBsIC0xLjM4ZS00LC0xMi41NTUwNDQgYyAwLjUwMDIyNywwLjcwMjM4IDEuMDk2NzgxLDEuMzUzNTM4IDEuNzg4MTQxLDEuOTMzNTQgNC4zODcxMjcsMy42ODA3NDIgMTAuOTI3NDE2LDMuMTA4MTQ4IDE0LjYwODI5OSwtMS4yNzg4MiAzLjY4MTAyNSwtNC4zODcxMDkgMy4xMDg1NzMsLTEwLjkyNzI5MiAtMS4yNzg1MzcsLTE0LjYwODAzNSAtNC4zODcxMDksLTMuNjgwODgzIC0xMC45Mjc0MzMsLTMuMTA4MTQ5IC0xNC42MDg0NDQsMS4yNzg4MiAtMC4xNzk5NjksMC4yMTQ1NTkgLTAuMzQ5NzQ0LDAuNDM0MjM0IC0wLjUwOTQ1OSwwLjY1ODQyNCBsIDEuMzhlLTQsLTcuODQ4NzQxIiBzdHlsZT0iZmlsbDojM2E5ZWJmO2ZpbGwtcnVsZTpldmVub2RkIi8%2BCiAgPC9nPgo8L3N2Zz4K&labelColor=%23ffffff&color=%233a9ebf)](https://www.ssc.uni-heidelberg.de/en/learning)

## Course description

Jupyter notebooks are a great tool for exploring and interacting with data using the Python programming language and its rich ecosystem of libraries.
In this course we will cover basic usage of the Pandas library to download a dataset, explore its contents, clean up missing or invalid data, filter the data according to different criteria, and plot visualizations of the data.

## Preparation

You will need a computer with Python, Jupyter and pandas installed.

If you don't already have this, I recommend installing [Anaconda](https://www.anaconda.com/download/success) (which contains all of this and more):

After installing

- open Jupyter (e.g. on Windows: `Start Menu -> Anaconda3 -> Jupyter Notebook`)

- create a new notebook (the web browser where Jupyter appeared, in top right click on New -> Notebook Python 3)

- type `import pandas` and press Shift+Enter (or click `Cell -> Run Cells` in the menu)

- if no error message appears, you are ready to start the course!

![setup screenshot](setup.apng)

## During the course

The notebooks created during the course will be automatically updated as they are edited at [jupyter-data-exploration-live](https://github.com/ssciwr/jupyter-data-exploration-live).

## Course materials

- Part 1: Python and Jupyter - [online slides](https://ssciwr.github.io/jupyter-data-exploration), [colab interactive notebook](https://colab.research.google.com/github/ssciwr/jupyter-data-exploration/blob/main/index.ipynb), [read-only notebook](index.ipynb)
- Part 2: Pandas with toy data - [online slides](https://ssciwr.github.io/jupyter-data-exploration/pandas-toy-data.slides.html), [colab interactive notebook](https://colab.research.google.com/github/ssciwr/jupyter-data-exploration/blob/main/pandas-toy-data.ipynb), [read-only notebook](pandas-toy-data.ipynb)
- Part 3: Pandas with real data - [online slides](https://ssciwr.github.io/jupyter-data-exploration/pandas-real-data.slides.html), [colab interactive notebook](https://colab.research.google.com/github/ssciwr/jupyter-data-exploration/blob/main/pandas-real-data.ipynb), [read-only notebook](pandas-real-data.ipynb)

## External resources

- pandas
  - [getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
  - [user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- kaggle courses
  - [pandas](https://www.kaggle.com/learn/pandas)
  - [data cleaning](https://www.kaggle.com/learn/data-cleaning)
