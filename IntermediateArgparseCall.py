from samwise import pb

import sys
import intermediateArgparse

while True:
    input_args = input("Please input equations values\n(Ex. # + #) to get a result: ")
    input_args_parsed = input_args.split(" ")
    n_1 = input_args_parsed[0]
    s_operator = input_args_parsed[1]
    n_2 = input_args_parsed[2]

    result = f"{n_1} {s_operator} {n_2} is an invalid expression..."
    n_1digit = str(n_1).replace(".", "", 1)
    n_2digit = str(n_2).replace(".", "", 1)
    if str(n_1digit).isdigit() and str(n_2digit).isdigit() and s_operator in ("+", "-", "*", "/"):
        sys.argv = ["intermediateArgparse.py", f"--n_1={n_1}", f"--n_2={n_2}", f"--s_operator={s_operator}"]
        result = intermediateArgparse.main()
    pb(result, "Called From Application")
