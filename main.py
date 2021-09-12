from dotenv import load_dotenv
from autochecker import checker, scheduler

def main():
    load_dotenv()

    if scheduler.is_reservation_arg_exists():
        scheduler.reserve(checker.parse)
    else:
        checker.parse()

if __name__ == '__main__':
    main()
