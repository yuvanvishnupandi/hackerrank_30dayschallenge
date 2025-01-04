if __name__ == '__main__':
    n = int(input().strip()) 
    binary_rep = bin(n)[2:] 
    max_consecutive_ones = max(len(group) for group in binary_rep.split('0'))  
    print(max_consecutive_ones) 
5