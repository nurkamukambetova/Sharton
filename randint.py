# -*- coding: utf-8-*-
from random import randint
chislo = randint (1,10)
play = True;
print u"Компьютер загадал число, отгадайте его!" 
while play:
    
    answer = raw_input (">")
    if int(answer) == chislo:
	    print u"Правильно!!! Вы угадали!"
	    play  = False  
    else:
        print u"Вы не угадали!Попробуй еще раз" 
        if int(answer) < chislo:
        	print u"ваше число меньше того что загадал компьютер"
        else:
        	print u"Ваше число больше того что загадал компьютер"
        
	       	
