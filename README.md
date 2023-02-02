# translators

This project contains three translators for circuit representation in different formats, a testbench generator for circuits expressed in Verilog, and a verifier for testing.

1. **Verilog to Verilog translator**: 

   Takes in a Verilog in any format (structural, behavioral, etc) and it outputs a Gate-Level limited Verilog (_clean Verilog_) representation which is funcionally equivalent to the input
   
  | ![v2v](https://user-images.githubusercontent.com/71635528/216324115-2f25124e-fa2c-4668-b76a-2a3c45fa6c56.png) |
  |:--:|
  | *An example of Verilog to Verilog translator on an m-bit Absolute Difference circuit* |



2. **Verilog to GraphViz translator**:

Takes in a _clean Verilog_ converts it into a graph representation in GraphViz format

| ![v2gv](https://user-images.githubusercontent.com/71635528/216329239-7c42ba1b-0e33-4821-8ae9-2276777d81f3.png) |
|:--:|
| *An example of Verilog to GraphViz translator on a 2-bit Absolute Difference circuit* |
   
   
   
3. **GraphViz to z3py translator**: 
   
   Takes in a circuit graph in GraphViz format and converts it into its z3py representation that is readable by Z3 SMT-solver
   
   
   
4. **Testbench generator**: 
   
   Takes in a _clean Verilog_ and the number of samples and generates a testbench over the samples
     
   
   
5. **Verify z3py representation**: 

   Takes in a Verilog in any format, generates a z3py and testbench from it, and test whether the functionalities of the two are equivalent
   
   
   
6. **Evaluate Worst-Case-Error(WCE) of an input circuit**:

   
   Takes in an exact and approximate circuit in _clean Verilog_ form and reports its WCE
   
   
   
7. **Labeling all gates of an input circuit**

   Takes in a circuit in _clean Verilog_ form and reports the WCE each gate when pruned. 

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




## How to use:

From the **main/** directory and launch the desired script:

1) **Verilog to Verilog:**

`$ python3 scripts/v2v.py benchmark-name`

2) **Verilog to GraphViz**

`$ python3 scripts/v2gv.py benchmark-name`


3) **GraphViz to z3py**

`$ python3 scripts/gv2z3.py benchmark-name -s num-of-mc-samples`

4) **Verilog to Testbench**

`$ python3 scripts/v2tb.py benchmark-name -s num-of-mc-samples`

5) **Verify z3py representation**

`$ python3 scripts/verify_z3.py benchmark-name`

6) **Evaluate WCE**

`$ python3 scripts/evaluate_wce.py exact-circuit-name -app approximate-circuit-name`

the csv report file is generated in the "output/report/" directory. 

7) **Label gates**

`python3 scripts/label_gates.py benchmark-name`

the csv report files are generated in the "output/report/benchmark-name/" directory.


## NOTE:

All the results that are present in the report folder obtained using a machine with the following specs:

- Machine-name: ml-edge

- CPU: 3.30GHz Intel Core i9

- RAM: 256GBs

- OS: Linux Ubuntu 20.04LTS
