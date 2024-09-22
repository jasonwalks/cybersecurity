def main():
    maskNum = int(input("What's the subnet mask number? "))
    availNum = pow(2, 32-maskNum)
    print(availNum)
    
main()
