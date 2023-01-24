# translators

This project contains three translators, a testbench generator, and a verifier.

1) **Verilog to Verilog translator**
2) **Verilog to GraphViz translator**
3) **GraphViz to z3py translator**
5) **Testbench generator**
6) **Verify z3py representation**



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


