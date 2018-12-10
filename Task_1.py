import re
def cut_file():
    while True:
        n = input("Nhap ten file: ")
        if n[0]==".":
            print("Nhap lai: ")
        elif n[-1]==".":
            print("Nhap lai: ")
        elif not re.search("[.]",n):
            print("Nhap lai")
        else:
            file = n.split(".")
            print(file[1])
            break

def main():

    cut_file()

if __name__ == '__main__':
    main()





# import re
#
# # def cut_file(n):
# n = input(" Nhap file bat ky: ")
# x= True
# while x:
#         n = input(" Nhap file bat ky: ")
#         if n[0] == ".":
#             print("Nhap lai: ")
#         elif n[-1]== ".":
#             print(" Nhap lai: ")
#         elif not re.search("[.]",n):
#             print("Nhap lai: ")
#         elif re.search("[.]",n):
#             print(n)
#             break
#
#
# # def main():
# #     n= input(" Nhap file bat ky: ")
# #     cut_file(n)
# # if __name__ == '__main__':
# #
# #     main()

