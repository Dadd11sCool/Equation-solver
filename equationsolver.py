import math

print(''' ____  __.__           .__  .__.__   \n 
|    |/ _|  |__ _____  |  | |__|  |   \n
|      < |  |  \\__  \ |  | |  |  |   \n
|    |  \|   Y  \/ __ \|  |_|  |  |__ \n
|____|__ \___|  (____  /____/__|____/ \n
                       
        Welcome to the equation solver made by KHALIL

        ''')


a = int(input('Enter the a : '))
b = int(input('Enter the b : '))
c = int(input('Enter the c : '))
sqrt = math.sqrt((b*b)-(4*a*c))


print('The delta = ',(b*b)-(4*a*c))

if (b*b)-(4*a*c) < 0 :
	print('The equation has nos solutions')
elif (b*b)-(4*a*c) == 0 :
	print('The equation has one solution')
	print('The only solution is : ', (-b/2*a))
elif (b*b)-(4*a*c) > 0 :
	print('The equation has two solutions')
	print('The first solution is : ', (-b-int(sqrt))/2*a)
	print('The second solution is : ', (-b+int(sqrt))/2*a)
