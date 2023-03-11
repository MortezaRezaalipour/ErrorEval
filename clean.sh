#!/bin/bash

rm -rf output/z3/*
rm -rf output/aig/*
rm -rf output/report/*
rm -rf output/ver/*
rm -rf output/gv/*

rm -rf test/*
mkdir test/ver
mkdir test/z3

rm yosys_graph.log
rm log.txt
rm lsoracle_log.txt