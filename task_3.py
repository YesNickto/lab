# TODO Найдите количество книг, которое можно разместить на дискете

inf_dis = 1.44 * (1024**2)
book = 100
stran = 50
strok = 25
simv = 4

w_book = book*stran*strok*simv



print(w_book)

print("Количество книг, помещающихся на дискету:", inf_dis//w_book)
