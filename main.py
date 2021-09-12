import os
from dotenv import load_dotenv
from autochecker import checker, scheduler

def main():
    load_dotenv()

    run_every_day = os.environ.get('RUN_EVERY_DAY')
    if run_every_day == 'True':
        scheduler.reserve(checker.parse)
    else:
        checker.parse()

if __name__ == '__main__':
    main()
