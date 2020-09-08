# from samwise import pb
import argparse
import sys

# from IntermediateArgparseCall import s_operator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_1", type=float, default=1.0,
                        help="What is the first number?")
    parser.add_argument("--n_2", type=float, default=1.0,
                        help="What is the second number?")
    parser.add_argument("--s_operator", type=str, default="+",
                        help="What operation? (+, -, *, /)")
    args = parser.parse_args()
    n_val = calc(args)
    if __name__ == '__main__':
        sys.stdout.write(str(n_val))
    return n_val


def calc(args):
    n_val = "?"
    if args.s_operator in ("add", "+"):
        n_val = args.n_1 + args.n_2

    elif args.s_operator in ("sub", "-"):
        n_val = args.n_1 - args.n_2

    elif args.s_operator in ("mul", "*"):
        n_val = args.n_1 * args.n_2

    elif args.s_operator in ("div", "/"):
        n_val = args.n_1 / args.n_2
    return n_val


def calc_old(n_1, n_2, s_operator):
    n_val = f"{n_1} {s_operator} {n_2} is an invalid expression..."
    n_1digit = str(n_1).replace(".", "", 1)
    n_2digit = str(n_2).replace(".", "", 1)
    if str(n_1digit).isdigit() and str(n_2digit).isdigit():
        n_1 = float(n_1)
        n_2 = float(n_2)
        if s_operator in ("add", "+"):
            n_val = n_1 + n_2
        elif s_operator in ("sub", "-"):
            n_val = n_1 - n_2
        elif s_operator in ("mul", "*"):
            n_val = n_1 * n_2
        elif s_operator in ("div", "/"):
            n_val = n_1 / n_2
    return n_val

if __name__ == '__main__':
    main()


# user_input_parsed = [7, 3, "div"]
# val = calc(user_input_parsed[0], user_input_parsed[1], user_input_parsed[2])
# print(val)
