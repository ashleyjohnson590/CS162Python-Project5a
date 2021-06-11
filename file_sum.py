#Author: Ashley Johnson
#Date: 4/22/2021
#Description: Program sums the values in num_list.txt and writes the sum of the numbers to
# sum.txt

def file_sum(num_list):
    """function opens the num_list.txt file, reads and sums each number, and writes the sum
    to sum.txt"""
    total_sum = 0
    try:
        with open(num_list,'r')as infile:
            for line in infile:
                total_sum += float(line)
    except FileNotFoundError:
        print("the file was not found")

    try:
        with open('sum.txt', 'w') as outfile:
            outfile.write(str(total_sum))
    except FileNotFoundError:
        print("the file was not found")


def main():
    file_sum('num_list.txt')

if __name__ == "__main__": main()