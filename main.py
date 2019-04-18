import argparse
from ImageAndVideoSeparator import Separator

class Program:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def crateArgs(self):
        self.parser.add_argument("--path", "-p")
        self.parser.add_argument("--output", "-o")

    def parseArgs(self):
        args = self.parser.parse_args()
        if(args.path and args.output):
            return args
    
    def main(self):

        self.crateArgs()
        args = self.parseArgs()
        seperator = Separator(path = args.path, outputPath = args.output)
        seperator.start()

start = Program()
start.main()
