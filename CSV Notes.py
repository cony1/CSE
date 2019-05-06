import csv

def validate(num: str):
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False

def validate(num: str):
    first_num = int(num[0])
    if first_num % 3 ==0:
        return True
    return False

def divisible_ny_2(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False



def all_16_digits(num: str):
    if not all_16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


# with open("Book1.csv") as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file...   ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = int(row[0])
#             new_number = old_number + 1
#             row[0] = new_number
#             writer.writerow(row)
#             # print(int(old_number) +1)
#             # print(old_number)
# print("Done")





def reverse_(string):
    print(string[::-1])



reverse_it("Hello World")




def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str




with open("Book1.csv") as old_csv:
      with open("MyNewFile.csv", 'w', newline='') as new_csv:
           reader = csv.reader(old_csv)
           writer = csv.writer(new_csv)
           print("Processing...")

         for row in reader:
             # old number = int(row[0]) + 1
             old_number = row[0]
             if validate(old_number):
                 writer.writerow(row)
      print("Done")



def valid_card_number(num: str):


print(valid_card_number("1947333886071750"))



for index in range(len(number)):
    list_num[index] = list_num[index]

