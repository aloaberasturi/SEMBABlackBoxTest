set term x11 persist           1
plot 'plainWave_Unnamed_point_outRq_Ex_50_50_50.dat' using 1:2 every 1::2 with lines
set term x11 persist           2
plot 'plainWave_Unnamed_point_outRq_Ey_50_50_50.dat' using 1:2 every 1::2 with lines
set term x11 persist           3
plot 'plainWave_Unnamed_point_outRq_Ez_50_50_50.dat' using 1:2 every 1::2 with lines
