import datetime
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=int, default=1970, help='enter birth year')
    parser.add_argument('--month', type=int, default=1, help='enter birth month')
    parser.add_argument('--day', type=int, default=1, help='enter day of birth')

    args = parser.parse_args()
    date = {"year" : args.year, "month" : args.month, "day" : args.day}
    print(days_alive(date))

def days_alive(date):
    current_date = datetime.datetime.now()
    birth_date = datetime.datetime(date["year"], date["month"], date["day"])
    diff = current_date.timestamp() - birth_date.timestamp()

    return diff / 60 / 60 / 24
if __name__ == "__main__":
    main()
