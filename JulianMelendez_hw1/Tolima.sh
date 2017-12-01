mkdir Tolima
cp ./DatosTolima.dat ./Tolima
cp ./PlotsTolima.py ./Tolima
cd  Tolima
grep -i 'march' DatosTolima.dat >  DatosMarzo1.txt
awk '{print $(NF-2) ',' $NF}' DatosMarzo1.txt > DatosMarzo.txt
awk '{print $(NF-2) ',' $NF}' DatosTolima.dat > GRF_vs_EQ1.txt
sed '1d' GRF_vs_EQ1.txt > GRF_vs_EQ.txt 
rm GRF_vs_EQ1.txt
rm DatosMarzo1.txt
rm DatosTolima.dat
python3 PlotsTolima.py
