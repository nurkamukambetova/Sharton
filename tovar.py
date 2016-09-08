print "Tovar 100 som"
print "Tovar 200 som"
print "Tovar 300 som"
print "vyberite Tovar"
Tovar = raw_input (">")
if Tovar== "1":
	print "mojete vvesti kolvo Tovara"
	kolvo = int (raw_input (">"))
	summ = int (kolvo) * 100
	print "stoimost tovara %d" % summ 
	if summ > 500:
	    skidka = int (summ) - 50
	    print "U vas skidka, vasha summa sostavlyaet %d som" % skidka
	    print "vvedite oplatu"
	    oplata = raw_input (">")
	    if int(oplata) < int(skidka):
	        print "vy vveli nedostatochno sredstv, poprobuite vvesti snova!"
	        oplata = raw_input (">")
	        print "Blagodarim za pokupku"
if Tovar== "2":
	print "mojete vvesti kolvo Tovara"
	kolvo = int (raw_input (">"))
	summ = int(kolvo) * 200
	print "stoimost tovara %d" % summ 
	if summ > 500:
	    skidka = int(summ) - 75
	    print "U vas skidka, vasha summa sostavlyaet %d som" % skidka
	    print "vvedite oplatu"
	    oplata = raw_input (">")
	    if int(oplata) < int(skidka):
	        print "vy vveli nedostatochno sredstv, poprobuite vvesti snova!"
	        oplata = raw_input (">")
	        print "Blagodarim za pokupku"
if Tovar== "3":
	print "mojete vvesti kolvo Tovara"
	kolvo = int(raw_input (">"))
	summ = int(kolvo) * 300
	print "stoimost tovara %d" % summ 
	if summ > 500:
	    skidka = int(summ) - 100
	    print "U vas skidka, vasha summa sostavlyaet %d som" % skidka
	    print "vvedite oplatu"
	    oplata = raw_input (">")
	    if int(oplata) < int(skidka):
	        print "vy vveli nedostatochno sredstv, poprobuite vvesti snova! "
	        oplata = raw_input (">")
	        print "Blagodarim za pokupku"


