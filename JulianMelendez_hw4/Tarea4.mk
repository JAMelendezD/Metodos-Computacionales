Resultados_hw4.pdf: Onda.pdf Cuerda.pdf Tambor1.pdf Tambor2.pdf Tambor3.pdf Tambor4.pdf
	pdflatex Resultados_hw4.tex|rm Tambor1.pdf|rm Tambor2.pdf|rm Tambor3.pdf|rm Tambor4.pdf|rm Ondas.x|rm Resultados_hw4.aux|rm Resultados_hw4.log
Onda.pdf Cuerda.pdf Tambor1.pdf Tambor2.pdf Tambor3.pdf Tambor4.pdf: Ondas.x
	python3 Plots.py
Ondas.x: cond_ini_cuerda.dat
	gcc -o Ondas.x Ondas.c -lm
