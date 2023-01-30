LF: please rename Readme in README. Remove the venv folder from the repository. The repo should contain only all those files that cannot be replicated, or examples.
LF: Why there is a touch $(VENV) command at the end of the make setup rule?

# translators

This project contains three translators (LF: for what?), a testbench generator (LF: whose purpose is?), and a verifier (LF: used for?).

1) **Verilog to Verilog translator** (LF: this is confusing for someone who check this for the first time)
2) **Verilog to GraphViz translator**
3) **GraphViz to z3py translator**
5) **Testbench generator**
6) **Verify z3py representation**

LF: Add here a better descriptio of each script. Othewise a user would not know what each translator/step does. Images can also help to shwow the difference.
LF: Before the setting up or the how to use, you should also mention the benchmark such that one knows what is doing in the how to use examples.

## Setting up:

clone the repository:

`$ git clone https://github.com/Laura-Pozzi-research-group/translators-morteza.git`

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

TODO
NOTE:
All the results that are present in the report folder obtained using a machine with the following specs: 
ml-edge
CPU: 3.30GHz Intel Core i9
RAM: 256GBs
OS: Linux Ubuntu 20.04LTS



