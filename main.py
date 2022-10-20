#print('Welcome to programming 1')

old_books = int(input("Enter the number of old books: "))

fancy_books = int(input("Enter the number of fancy books: "))

yummy_books = int(input("Enter the number of yummy books: "))

#fixed_price = 19.99

#fancy_discount = 0.5*fixed_price
#print(19.99 - fancy_discount)

BOOK_PRICE = 19.99
OLD_BOOKS_DISCOUNT = 0.5
FANCY_BOOKS_DISCOUNT = 0.3
YUMMY_BOOKS_DISCOUNT = 0.2

old_book_subtotal = old_books * BOOK_PRICE - (OLD_BOOKS_DISCOUNT * old_books * BOOK_PRICE)
fancy_book_subtotal = fancy_books * BOOK_PRICE - (FANCY_BOOKS_DISCOUNT * fancy_books * BOOK_PRICE)
yummy_book_subtotal = yummy_books * BOOK_PRICE - (YUMMY_BOOKS_DISCOUNT * yummy_books * BOOK_PRICE)


total = (old_book_subtotal + fancy_book_subtotal + yummy_book_subtotal)
#print(total)

print('{0:.2f}'.format(total))
