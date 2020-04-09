# -*- coding: utf-8 -*-
from math import sqrt
from sys import exit

arr = []

def input_array(n):
	for i in range(n):
		num = input('Введите число: ')
		if num == 'exit':
			print('Программа остановлена.')
			exit(0)
		else:	
			while not num.isdigit():
				num = input('Некорректный ввод. Введите число: ')
				if num == 'exit':
					print('Программа остановлена.')
					exit(0)
			num = int(num)
		arr.append(num)

def sqrt_decomposition():
	while True:
		n = input('Введите размерность массива. Введите \'exit\' для завершения.\n')
		if n == 'exit':
			print('Программа остановлена.')
			exit(0)
		else:	
			while not n.isdigit():
				n = input('Некорректный ввод. Введите размерность массива: ')
				if n == 'exit':
					print('Программа остановлена.')
					exit(0)
			n = int(n)
		m = int(sqrt(n)) + 1
		input_array(n)
		l = input('Введите индекс начального элемента: ')
		if l == 'exit':
			print('Программа остановлена.')
			exit(0)
		else:	
			while not l.isdigit() or int(l) >= n:
				l = input('Некорректный ввод. индекс начального элемента: ')
				if l == 'exit':
					print('Программа остановлена.')
					exit(0)
			l = int(l)
		r = input('Введите индекс конечного элемента: ')
		if r == 'exit':
			print('Программа остановлена.')
			exit(0)
		else:	
			while not r.isdigit() or int(r) < l or int(r) >= n:
				r = input('Некорректный ввод. индекс конечного элемента: ')
				if r == 'exit':
					print('Программа остановлена.')
					exit(0)
			r = int(r)
		i = 0
		sum = [0] * m
		while i < n:
			sum[i // m] += arr[i]
			i += 1 
		l_id = l // m
		r_id = r // m
		result_sum = 0
		if l_id == r_id:
			while l <= r:
				result_sum += arr[l]
				l += 1
		else:
			i = l
			while i < (l_id + 1) * m:
				result_sum += arr[i]
				i += 1
			i = r
			while r_id * m <= i:
				result_sum += arr[i]
				i -= 1	
			i = l_id + 1
			while i < r_id:
				result_sum += sum[i]
				i += 1
		print('Конечная сумма: ',result_sum)

def sqrt_decomposition_from_file():
		file = open(input('Введите имя файла с расширением: '))
		for i in file:
			n = int(i)
			break
		m = int(sqrt(n)) + 1
		i = 0
		while i < n:
			for j in file:
				arr.append(int(j))
				break
			i += 1
		for i in file:
			l = int(i)
			break
		for i in file:
			r = int(i)
			break
		i = 0
		sum = [0] * m
		while i < n:
			sum[i // m] += arr[i]
			i += 1 
		l_id = l // m
		r_id = r // m
		result_sum = 0
		if l_id == r_id:
			while l <= r:
				result_sum += arr[l]
				l += 1
		else:
			i = l
			while i < (l_id + 1) * m:
				result_sum += arr[i]
				i += 1
			i = r
			while r_id * m <= i:
				result_sum += arr[i]
				i -= 1	
			i = l_id + 1
			while i < r_id:
				result_sum += sum[i]
				i += 1
		print('Конечная сумма: ',result_sum)
		file.close()

answer = input('Input \'self\' or \'file\'\n')
if answer == 'self':
	sqrt_decomposition()
elif answer == 'file':
	sqrt_decomposition_from_file()
else:
	print('Invalid input!')