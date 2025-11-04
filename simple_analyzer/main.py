import time
import random
from analyzer import Analyzer

def read_config():
    config = {}
    with open('config/config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            config[key] = int(value)
    return config.get('interval'), config.get('sequence_length')

def main():
    interval, sequence_length = read_config()
    analyzer = Analyzer()
    while True:
        num = random.randint(1, 100)
        analyzer.add_number(num)
        if len(analyzer.numbers) > sequence_length:
            analyzer.numbers.pop(0)
        print("Even:", analyzer.even_count())
        print("Odd:", analyzer.odd_count())
        print("Highest:", analyzer.highest_number())
        print("Increasing pairs:", analyzer.increasing_pairs())
        time.sleep(interval)
        if len(analyzer.numbers) == sequence_length and time.localtime().tm_sec == 0:
            break

if __name__ == "__main__":
    main()