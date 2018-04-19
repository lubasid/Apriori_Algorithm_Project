import csv
def main():
 with open('order_products__train.csv', 'r') as file:
     writerFile= open("newData.csv", "w")
     writer = csv.writer(writerFile,delimiter=',')
     counter = 0
     lines = csv.reader(file)
     dictionary = {"orderId":"", "productId":"", "add to cart":"", "reordered": ""}
     for eachLine in lines:
         if counter == 0:
             writer.writerow(["orderId", "productId","add to cart", "reordered"])
             counter+=1
         else:
             
             dictionary["orderId"] += eachLine[0] + ","
             dictionary["productId"]+=eachLine[1]+ ","
             dictionary["add to cart"]+=eachLine[2]+ ","
             dictionary["reordered"]+=eachLine[3]+ ","
             
             print(eachLine)
             
             writer.writerow(eachLine)
             
             counter+=1
             if counter == 20:
                 writerFile.close()
                 break
     # here close the file after deleting the if condition statment == 20            
     print(dictionary)
main()
