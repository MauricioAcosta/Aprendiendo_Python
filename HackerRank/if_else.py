if __name__ == '__main__':
    n = int(input())
    if 1<= n <= 1000:
        if n%2!=0 or 6<=n<=20:
            print("Weird")
        else:
            print("Not Weird")
