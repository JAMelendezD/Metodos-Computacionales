#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define N 300

float similitud(float *observado, float *modelo, int len)
{
	float chi;
	float suma;
	int i;
	for(i=0;i<len;i++)
	{
		suma = suma + ((observado[i]-modelo[i])*(observado[i]-modelo[i]));
	}
	chi = suma/2.0;
	return exp(-chi);
}


float * modelo(float *r, float Mb, float Md, float Mh,int len)
{
	float bb = 0.2497;
	float bd = 5.16;
	float ad = 0.3105;
	float ah = 64.3;
	int i;
	float *array = malloc(N*sizeof(float));
	for(i=0;i<len;i++)
	{
		array[i] = sqrt(Mb)*r[i]/pow(r[i]*r[i]+bb*bb, 0.75) + sqrt(Md)*r[i]/pow(r[i]*r[i]+pow(bd+ad,2.0), 0.75) + sqrt(Mh)*r[i]/pow(r[i]*r[i]+ah*ah, 0.25);
	}
	return array;
}


void copy(float *inicio, float *fin, int len)
{
  	int i;
  	for(i=0;i<len;i++)
	{
    		fin[i] = inicio[i];
	}
}

	
int main()
{
	FILE *in;
	int i;
	float *v = malloc(N*sizeof(float)); 
	float *vi = malloc(N*sizeof(float)); 
	float *r = malloc(N*sizeof(float)); 
	float *MbW = malloc(N*sizeof(float)); 
	float *MdW = malloc(N*sizeof(float)); 
	float *MhW = malloc(N*sizeof(float)); 
	float L; 


	
	in = fopen("RadialVelocities.dat", "r");
	for(i = 0; i< N; i++)
	{
		fscanf(in,"%f %f" , &r[i] , &v[i]);
	}
	fclose(in);
	
	for(i = 0; i< N; i++)
	{
		MbW[i] = 0;
		MdW[i] = 0;
		MhW[i] = 0;
	}
	

	MbW[0] = drand48();
	MdW[0] = drand48();
	MhW[0] = drand48();
	
	vi = modelo(r, MbW[0],MdW[0],MhW[0],N);
	L = similitud(v,vi,N);
		



	in = fopen("datos.txt", "w");
	for(i = 0; i< N; i++)
	{
		fprintf(in, "%f, %f,%f,%f,%f,%f\n", r[i],v[i],MbW[i],MdW[i],MhW[i],L);
	}
	fclose(in);

	free(r);
	free(v);
	free(vi);
	free(MbW);
	free(MdW);
	free(MhW);

 	return 0;

}


