all:Results_hw5.pdf
	rm Results_hw5.aux|rm Results_hw5.log
Results_hw5.pdf: Velocidad.pdf 
	pdflatex Results_hw5.tex
Velocidad.pdf: datos.txt
	python Plots.py|rm datos.txt|rm CurvaRotacion.x
datos.txt: CurvaRotacion.x
	./CurvaRotacion.x
CurvaRotacion.x: RadialVelocities.dat
	gcc -o CurvaRotacion.x CurvaRotacion.c -lm



