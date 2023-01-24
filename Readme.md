# translators

This project contains three translators, testbench generator, and a verifier.

1) **Verilog to Verilog:**
2) **Verilog to GraphViz**
3) **GraphViz to z3py**
5) **Verilog to Testbench**
6) **Verify z3py representation**

## Description:

## Setup:

Head to the **main/** directory

create a virtual environment:

`$ make setup`

activate the environment:

`$ source venv/bin/activate`


install requirements:

`$ make requirements`


add he current directory to your `PYTHONPATH`:

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


