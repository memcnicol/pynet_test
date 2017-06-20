ip1 = "10.0.0.1"
ip2 = "69.69.0.1"
ip3 = "192,168.1.1"

print("{:^90}".format("having fun!"))
print("{:^30}{:^30}{:^30}".format("test 1", "test 2", "test3"))
print("{:^30}{:^30}{:^30}".format(ip1, ip2, ip3))

while(True):
    ip4 = input("Please input another IP address: ")
    ip4 = ip4.split(".")
    if(len(ip4) != 4):
        print("IP format invalid. ")
    elif(len(ip4) == 4):
        check = True
        print("{:^30}{:^30}{:^30}{:^30}".format("octet 1", "octet 2", "octet 3", "octet 4"))
        print("{:^30}{:^30}{:^30}{:^30}".format(*ip4))
        break

