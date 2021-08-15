def frequency(value, sequence):
    count = 0

    for element in sequence:
        if element == value:
            count += 1

    return (count, count/len(sequence))

if __name__ == "__main__":
    results = frequency(5, [5, 4, 8, 8, 5, 2, 1, 9])
    print ("Frequency: ", results[0])
    print ("Relative Frequency: ", results[1])

