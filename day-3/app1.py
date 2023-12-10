# with open('ex1.txt') as f:
#     current_row = []
#     previous_row = []
#     total = 0
#     for line in f:
#         print(line)
#         if not current_row:
#             current_row = line
#             for i, c in enumerate(current_row[0:-1]):
#                 print('test')
#                 print(i, c)

import re
def find_part_numbers():
    with open('ex1.txt') as f:
        current_line = []
        previous_line = []
        symbol_line = []
        total = 0
       
        for line in f:
            print(line)
            if not previous_line:
                # print("true!!!")
                pass
            else:
                print("false...")

            num = ""
            for i, c in enumerate(line[0:-1]):
                print(i, c)
                if re.search("[^0-9.]+",c):
                    print("found symbol: ", c)
                    # symbol_line.insert(i, c)
                    symbol_line.append(i)
                    

                if c.isnumeric():
                    num += str(c)
                    # print("the num", num)
                    # print(type(num))
                # print(line[i])
                else:
                    if num:
                        total += int(num)
                        # print(c)
                        # print("c is: ", c)
                    num = ""
            
            previous_line = line
            print(symbol_line)
            
            
        # for x in range(len(symbol_line)):
        #     print(x)
        #     print(symbol_line[x])


    print("the total", total)
    

def main():
    find_part_numbers()



if __name__ == '__main__':
    main()