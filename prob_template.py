"""
file: prob_template.py
language: python3.x
author: Alex Wall
description: creates a standard python template file to write algorithms to solve Project Euler Problems
"""
import sys


def _write_time_sol(f):
    """
    Writes the timing the computation function
    :param f: the file
    """
    f.write("def time_sol(func):\n\n")
    f.write("\tstart = time.time()\n")
    f.write("\tres = func()\n")
    f.write("\tfinish = time.time()\n")
    f.write("\tprint(\"%s:\ttime: %f, result: %s\" % (func.__name__, finish - start, res))\n")


def _write_imports(f):
    """
    writes the import modules into the python file
    :param f: the file
    """
    lib = ["math", "sympy", "itertools", "time"]
    for l in lib:
        f.write("import %s\n" % l)


def _write_stubs(f, s, t):
    """
    writes the stubbed functions to solve problems s to t
    :param f: file
    :param s: starting number
    :param t: end number
    """
    for i in range(s, t + 1):
        f.write("def prob%d():\n" % i)
        f.write("\t\"\"\"\n\n\t\"\"\"\n\n")


def _write_main(f, s, t):
    """
    writes the name-main condition along with time_sol calls
    :param f: the file
    """
    f.write("if __name__ == \"__main__\":\n")
    for i in range(s, t + 1):
        if i == s:
            f.write("\ttime_sol(prob%d)\n" % i)
        else:
            f.write("\t#time_sol(prob%d)\n" % i)


def _write_newlines(f):
    """
    just writes empty newlines to the python file
    :param f: the file
    """
    f.write("\n\n")


def write_template(s, t):
    """
    combines everything together in this function to build the ultimatum
    :param s: the starting number
    :param t: the ending number
    """
    if s > t:
        raise Exception("Starting number is greater than ending number (%d > %d)" % (s, t))

    f = open("prob%d_%d.py" % (s, t), "w")

    _write_imports(f)
    _write_newlines(f)
    _write_time_sol(f)
    _write_newlines(f)
    _write_stubs(f, s, t)
    _write_newlines(f)
    _write_main(f, s, t)


if __name__ == '__main__':

    if len(sys.argv) != 3:
        raise Exception("Usage: python3 prob_template.py num1 num2")

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    write_template(num1, num2)
