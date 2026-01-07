import csv
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        str_names = reader.fieldnames[1:]
        database = list(reader)

    with open(sys.argv[2]) as txtfile:
        sequence = txtfile.read()

    str_counts = {}
    for str_seq in str_names:
        str_counts[str_seq] = longest_match(sequence, str_seq)

    for person in database:
        match = True
        for str_seq in str_names:
            if int(person[str_seq]) != str_counts[str_seq]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")

def longest_match(sequence, subsequence):
    longest_run = 0
    subseq_length = len(subsequence)
    seq_length = len(sequence)

    for i in range(seq_length):
        count = 0
        while True:
            start = i + count * subseq_length
            end = start + subseq_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run

if __name__ == "__main__":
    main()
