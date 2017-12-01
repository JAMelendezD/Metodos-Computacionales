Resultados_hw4.pdf: Onda.pdf Cuerda.pdf Tambor1.pdf Tambor2.pdf Tambor3.pdf Tambor4.pdf
	pdflatex Resultados_hw4.tex
Onda.pdf Cuerda.pdf Tambor1.pdf Tambor2.pdf Tambor3.pdf Tambor4.pdf: Ondas.x
	python3 Plots.py
Ondas.x: cond_ini_cuerda.dat
	gcc -o Ondas.x Ondas.c -lm
