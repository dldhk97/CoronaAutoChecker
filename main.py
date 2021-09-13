import os
from dotenv import load_dotenv
from autochecker import checker, scheduler

def main():
    load_dotenv()

    if os.environ.get('RUN_EVERY_DAY') == 'True':
        scheduler.reserve()
    else:
        checker.parse()

if __name__ == '__main__':
    main()
