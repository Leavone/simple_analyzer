def read_config():
    with open('config/config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            if key == 'interval' or key == 'sequence_length':
                print(key, value)

def main():
    read_config()

if __name__ == "__main__":
    main()

# minor change