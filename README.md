# translators

This project contains three translators (LF: for what?), a testbench generator for an input circuit in Verilog format (LF: whose purpose is?), and a verifier (LF: used for?).

1) **Verilog to Verilog translator**: put-description-here (takes in a Verilog in any format (structural, behavioral, etc) and it outputs a Gate-Level limited Verilog representation which is funcionally equivalent)

2) **Verilog to GraphViz translator**: : put-description-here
3) **GraphViz to z3py translator**: put-description-here
4) **Testbench generator**: put-description-here
5) **Verify z3py representation**: put-description-here (important to showcase an example)
6) **Evaluate Worst-Case-Error(WCE) of an input circuit**: put-description-here
7) **Labeling all gates of an input circuit**

LF: Add here a better descriptio of each script. Othewise a user would not know what each translator/step does. Images can also help to shwow the difference.
LF: Before the setting up or the how to use, you should also mention the benchmark such that one knows what is doing in the how to use examples.

## Setting up:

clone the repository:

`$ git clone https://github.com/Laura-Pozzi-research-group/translators-morteza.git`

install `virtualenv` on your machine using the following command(s):

- Linux

Do this

- MacOS

Do this 

- Windows

Do this



head to the **main/** directory

install `virtualenv` and create a virtual environment:

`$ make setup`

activate the environment:

`$ source venv/bin/activate`


install requirements:

`$ make requirements`


add the current directory to your `PYTHONPATH`:

`$ export PYTHONPATH="$PWD"`




## How to use:

Head to the **script/** directory and launch the desired script:

1) **Verilog to Verilog:**

`$ python3 v2v.py benchmark-name`

2) **Verilog to GraphViz**

`$ python3 v2gv.py benchmark-name`


3) **GraphViz to z3py**

`$ python3 gv2z3.py benchmark-name -s num-of-mc-samples`

4) **Verilog to Testbench**

`$ python3 v2tb.py benchmark-name -s num-of-mc-samples`

5) **Verify z3py representation**

`$ python3 verify_z3.py benchmark-name`

6) **Evaluate WCE**

`$ python3 evaluate_wce.py exact-circuit-name -app approximate-circuit-name`

the csv report file is generated in the "output/report/" directory. 

7) **Label gates**

`python3 label_gates.py benchmark-name`

the csv report files are generated in the "output/report/benchmark-name/" directory.


TODO

NOTE:

All the results that are present in the report folder obtained using a machine with the following specs:


Machine-name: ml-edge

CPU: 3.30GHz Intel Core i9

RAM: 256GBs

OS: Linux Ubuntu 20.04LTS


