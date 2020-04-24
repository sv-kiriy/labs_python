# -*- coding: utf-8 -*-
import random
import sys
import argparse

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(iteration)
    filledLength = int(length * iteration // total)
    bar = '|' + fill * filledLength + '-' * (length - filledLength) + '|'
    print(prefix, bar, percent,'%', suffix, end = printEnd)
    if iteration == total: 
        print()

"""
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
"""

def generate():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n',type = str, default = 'file',help = "This is name of file (default = 'file')")
	parser.add_argument('-s',type = int, default = 1,help = "This is size of file (default = 1)")
	parser.add_argument('-la',type = int,default = 3,help = "This is 'a' for length of words (default = 3)")
	parser.add_argument('-lb',type = int,default = 10,help = "This is 'b' for length of words (default = 10)")
	parser.add_argument('-wa',type = int,default = 10,help = "This is 'a' for quantity of words (default = 10)")
	parser.add_argument('-wb',type = int,default = 100,help = "This is 'b' for quantity of words (default = 100)")
	
	args = parser.parse_args()
	name = args.n
	size = args.s
	length_a = args.la
	length_b = args.lb
	if length_a > length_b or length_a < 1 or length_b < 1:
		print('Invalid input')
		sys.exit(0)
	words_a = args.wa
	words_b = args.wb
	if words_a > words_b or words_a < 1 or words_b < 1:
		print('Invalid input')
		sys.exit(0)

	file = open(name + '.txt', 'tw', encoding='utf-8')
	size = size_max = size*1048576	

	progress = 0

	while size:
		words_rand = random.randint(words_a,words_b)
		for i in range(words_rand):
			length_rand = random.randint(length_a,length_b)
			for j in range(length_rand):
				if random.randint(0,1):
					file.write(chr(random.randint(65,90)))
				else:
					file.write(chr(random.randint(97,122)))	
				if int((1 - size/size_max)*100) == progress:
					printProgressBar(progress + random.random(), 100, prefix = 'Progress:')
					progress += 1
				size -= 1
				if not size:
					file.close()
					printProgressBar(progress, 100, prefix = 'Progress:', suffix = 'Complete')
					sys.exit(0)
			if i < words_rand - 1:
				file.write(' ')
				if int((1 - size/size_max)*100) == progress:
						printProgressBar(progress + random.random(), 100, prefix = 'Progress:')
						progress += 1
				size -= 1
			if not size:
				file.close()
				printProgressBar(progress, 100, prefix = 'Progress:', suffix = 'Complete')
				sys.exit(0)
		file.write('\n')
		if int((1 - size/size_max)*100) == progress:
					printProgressBar(progress + random.random(), 100, prefix = 'Progress:')
					progress += 1
		size -= 2
		if not size:
			file.close()
			printProgressBar(progress, 100, prefix = 'Progress:', suffix = 'Complete')
			sys.exit(0)

if __name__ == '__main__':
	generate()