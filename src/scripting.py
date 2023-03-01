import argparse # Package for parsing command line arguments.

def input_parse(): # Function to parse command line arguments.
    # initialize the parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--name", help="name of the person", type=str, default="someone")
    parser.add_argument("--age", help="age of the person", type=int, required=True)
    # parse the arguments from the command line
    args = parser.parse_args()
    # get the name
    return args

def hello(name, age):
    print("Hello, " + name + ". Remember that this too shall pass.")
    print("I am told that you're " + str(age) + " years of age. Time is running, eh?")

# Define main function

def main():
    args = input_parse()
    # pass name to hello function
    hello(args.name, args.age)

main()