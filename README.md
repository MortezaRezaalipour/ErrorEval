# ErrorEval

Description:
Approximate computing is a widely adopted strategy
to exploit the error resilience of applications for which full
accuracy is not a crucial requirement. The energy consumption
of these applications may benefit greatly from the implementation
on inexact hardware, where small and controlled errors allow
a reduction of the area and power of the underlying circuits.
One of the major challenges in approximate computing is to
validate the obtained approximate design, to verify whether it
actually complies with the error constraints. The employment
of SMT/SAT solvers for error evaluation is a viable solution
to these problems: their efficiency can be exploited to provide
results that are guaranteed to be valid, as opposed to statistical
approaches such as Monte Carlo sampling. In this paper, we
present a novel SMT-based algorithm for error evaluation, which
can be applied to any type of approximate circuit and for
any worst-case error metric. Its core idea is to exploit the
information returned by the solver in order to improve error-
evaluation efficiency, and furthermore to explore the error space
monotonically.


## Setting up:

clone the repository:

`$ git clone https://github.com/Laura-Pozzi-research-group/translators-morteza.git`

install `virtualenv` on your machine using the following command(s):

- Linux

`$ sudo apt-get install virtualenv`

- MacOS

later... 

- Windows

later...



- head to the **main/** directory and create a virtual environment:

`$ make setup`

- activate the environment:

`$ source venv/bin/activate`


- install requirements:

`$ make requirements`


- add the current directory to your `PYTHONPATH`:

`$ export PYTHONPATH="$PWD"`

- Install the following tools:

1. **Yosys**: link (https://github.com/YosysHQ/yosys)
2. **LSOracle**: link (https://github.com/lnis-uofu/LSOracle)
3. **Icarus Verilog**: link (https://github.com/steveicarus/iverilog)

## How to use:

### Verilog Benchmarks


Circuits expressed in Verilog are the primary inputs to the framework and must be placed at **main/input/ver** directory
All the circuits that have the word "app" in their name are approximate circuits.

### Launch
Head to the **main/** directory and launch **ErrorEval.py** according to the following command:

`$ python3 ErrorEval.py benchmark-name -app approximate-benchmark-name -met metric-name`

- _example: assuming that *abs_diff_i20_o9.v* and *abs_diff_i20_o9_app1.v* are available at *input/ver* directory and the desired metric is WAE_

`$ python3 ErrorEval.py input/ver/abs_diff_i20_o9.v -app input/ver/abs_diff_i20_o9_app1.v -met WAE`

After launching the command above the csv report file will be generated in the "output/report/" directory.

## NOTE:

We have launched all the experiments using a machine with the following specs:

- Machine-name: ml-edge

- CPU: 3.30GHz Intel Core i9

- RAM: 256GBs

- OS: Linux Ubuntu 20.04LTS

## Citing ErrorEval

You can cite ErrorEval by simply copying the following text:
```
@inproceedings{10.1145/3587135.3591438,
author = {Rezaalipour, Morteza and Ferretti, Lorenzo and Scarabottolo, Ilaria and Constantinides, George A. and Pozzi, Laura},
title = {ErrorEval: an Open-Source Worst-Case-Error Evaluation Framework for Approximate Computing},
year = {2023},
isbn = {9798400701405},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3587135.3591438},
doi = {10.1145/3587135.3591438},
abstract = {Approximate Computing is a design paradigm that allows for a small loss in accuracy in an application in exchange for improved efficiency and/or reduced power consumption. Approximate Logic Synthesis (ALS) is a process through which an inexact (approximate) version of a circuit is generated, assuring that the error introduced by approximation does not exceed a certain threshold [1].},
booktitle = {Proceedings of the 20th ACM International Conference on Computing Frontiers},
pages = {393–394},
numpages = {2},
keywords = {Approximate Computing, Error Evaluation, SAT Solver},
location = {Bologna, Italy},
series = {CF '23}
}
```


M. Rezaalipour, L. Ferretti, I. Scarabottolo, G. A. Constantinides, L. Pozzi, _ErrorEval: an Open-Source Worst-Case-Error Evaluation Framework for Approximate Computing_, OSHW'23

