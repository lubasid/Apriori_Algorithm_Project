# import csv
# def main():
#  with open('order_products__train.csv', 'r') as file:
#      writerFile= open("order_products_train.csv", "w")
#      writer = csv.writer(writerFile,delimiter=',')
#      counter = 0
#      lines = csv.reader(file)
#      dictionary = {"orderId": 0, "productId": 0, "add to cart": 0, "reordered": 0}
#      for eachLine in lines:
#          if counter == 0:
#              writer.writerow(["orderId", "productId","add to cart", "reordered"])
#              counter+=1
#          else:
			 
#              dictionary["orderId"] += eachLine[0] + ","
#              dictionary["productId"]+=eachLine[1]+ ","
#              dictionary["add to cart"]+=eachLine[2]+ ","
#              dictionary["reordered"]+=eachLine[3]+ ","
			 
#              print(eachLine)
			 
#              writer.writerow(eachLine)
			 
#              counter+=1
#              if counter == 20:
#                  writerFile.close()
#                  break
#      # here close the file after deleting the if condition statment == 20            
#      print(dictionary)
# main()


import csv

orders_dict = {}
i = 0
num_orders = 0

with open('order_products_train.csv', 'r') as f:
	for line in f:
		line = line.split(',')

		if line[0] not in orders_dict:
			orders_dict[line[0]] = []
			num_orders += 1

		orders_dict[line[0]].append(line[1])


# with open('order_products_prior.csv', 'r') as f:
# 	for line in f:
# 		line = line.split(',')

# 		if line[0] not in orders_dict:
# 			orders_dict[line[0]] = []
# 			num_orders += 1

# 		orders_dict[line[0]].append(line[1])

with open('new_orders.csv', 'w') as f:
	for order, items in orders_dict.items():
		#f.write(order) we don't need the order id
		for item in items:
			f.write(',')
			f.write(item)

		f.write('\n')


print('Total orders: ' + str(num_orders))
print('orders_dict length: ' + str(len(orders_dict)))


for order, items in orders_dict.items():
	print(str(order) + ': ' + str(items))

	if i == 20:
		break
	
	i += 1
