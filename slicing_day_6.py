if __name__ == '__main__':
    t = int(input().strip())
    
    for _ in range(t):
        s = input().strip()
        
        even_chars = s[0::2]
        odd_chars = s[1::2]
        
        print(f"{even_chars} {odd_chars}")
