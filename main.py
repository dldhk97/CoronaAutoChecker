from autochecker import checker
from dotenv import load_dotenv

def main():
    load_dotenv()
    checker.parse()

if __name__ == '__main__':
    main()
