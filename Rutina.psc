Algoritmo Rutina
	DEfinir a,b,c Como Real
	definir d, e, f Como real
	definir g ,h , i, j , k,l, m, n , p, q, r, s , t , u , v , w , x ,z como reales 
	Escribir ' Hola, soy tu sistema de rutinas diarias, tus solicitudes son '
	Escribir ' 1. Bañarte'
	escribir '2. Lavar la ropa'
	escribir '3. Lavar al perro'
	escribir ' ordena tu horario a tu manera de manera en al que cada actividad quede representada por su numero en un orden especifico'
	leer a 
	leer b
	leer c
	Si a = 1 y b = 2 y c = 3 Entonces
		escribir '¿Entonces te quieres banar primero, luego lavar la ropa y por ultimo lavar al perro?'
		escribir ' escribe 1 para si y 2 para no '
		leer d 
		Si d = 1   Entonces
			Escribir 'siuuuuuuuuuuuuuuuuuu'
			escribir'ahora te mostrare los pasos a seguir para completar la tarea llamada BAÑARSE'
			escribir 'primero tienes que quitarte la ropa, lo vas a hacer? (1 para si 2 para no ) '
			leer g 
			Si g=1  Entonces
				escribir 'siuuuuuuuuuu'
				escribir 'ahora sigue actrivar o prender la ducha (1 para si 2 para no)'
				leer h
				Si h=1 Entonces
					escribir 'siuuuuu ya vamos 2 de n pasos '
					escribir 'ahora debes aplicarte el shampoo en el pelo y adicionar jabon corporal en el cuerpo (1 para si 2 para no)'
					leer i
					Si i=1 Entonces
						escribir ' excelente trabajo, ya nos falta muy poco, eres un campeon'
						
					SiNo
						acciones_por_falso
					Fin Si
				SiNo
					acciones_por_falso
				Fin Si
			SiNo
				escribir ' vuelve a llenar todo desde el principio'
			Fin Si
		SiNo
			escribir 'chale bro'
		Fin Si
	SiNo
		Si a = 2 y b =  3 y c=1  Entonces
			escribir ' quieres lavar la ropa, lavar al perro y por ultimo bañarte?'
			escribir 'escribe 1 para si y 2 para no'
			leer e
			Si e=1 Entonces
				escribir 'siuuuuu'
			SiNo
				escribir ' reinicia el programa porfi'
				
			Fin Si
		SiNo
			Si a=3 y b=1 y c=2  Entonces
				escribir 'quieres lavar al perro, bañarte y por ultimo lavar la ropa?'
				escribir 'escribe 1 para si y 2 para no '
				leer f
				Si f=1 Entonces
					escribir 'siuuuuuuuuuuuuuuuuuuu'
					
				SiNo
					Escribir 'rellena otra vez el formulario '
				Fin Si
				
			SiNo
				escribir 'uwu'
			Fin Si
		Fin Si
	Fin Si
	
	
FinAlgoritmo
