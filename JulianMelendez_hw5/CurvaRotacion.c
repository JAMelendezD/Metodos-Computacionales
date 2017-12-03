#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define N 300

long double similitud(float *observado, float *modelo, int len)
{
	float chi;
	float suma;
	int i;
	for(i=0;i<len;i++)
	{
		suma = suma + pow((observado[i]-modelo[i]),2);
	}
	return exp(-chi/2.0);
}


float * modelo(float *r, float Mb, float Md, float Mh,int len)
{
	float bb = 0.2497;
	float bd = 5.16;
	float ad = 0.3105;
	float ah = 64.3;
	float sum = bd+ad;
	int i;
	float *array = malloc(N*sizeof(float));
	for(i=0;i<len;i++)
	{
		array[i] = sqrt(Mb)*r[i]/pow(r[i]*r[i]+bb*bb, 0.75) + sqrt(Md)*r[i]/pow(r[i]*r[i]+sum*sum, 0.75) + sqrt(Mh)*r[i]/pow(r[i]*r[i]+ah*ah, 0.25);
	}
	return array;
}

double normal(double m, double d)
{
  	double distribucionNormal = sqrt(-2.0*log(drand48())*cos(2*(3.1415)*drand48());
	return ((d*distribucionNormal) + m);
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
	float *vnueva = malloc(N*sizeof(float)); 
	float *l = malloc(N*sizeof(float)); 


	
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
	l[0] = similitud(v,vi,N);
		
	int j;
	int n;
	for(j=0; j<n; j++)
	{
	
    		vi = modelo(r, MbW[j],MdW[j],MhW[j],N);

    		double MbN = normal(MbW[j], 100.0);
    		double MdN = normal(MdW[j], 100.0);
    		double MhN = normal(MhW[j], 100.0);
		vnueva = modelo(r, MbN, MdN, MhN);
		long double lvieja = repositorio(v,vi);
    		long double lnueva = repositorio(v,vnueva);
		double alpha = lnueva/lvieja;

  

    		if(alpha >= 1.0)
		{
      		MbW[j+1] = MbN;
      		MdW[j+1] =MdN;
      		MhW[j+1] = MhN;
      		l[j+1] = lnueva;
    		}
		else 
		{
      		double beta = drand48();
      		if(beta <= alpha)
      		{
      		MbW[j+1] = MbN;
      		MdW[j+1] =MdN;
      		MhW[j+1] = MhN;
      		l[j+1] = lnueva;
      		} 
      		else 
      		{
      		MbW[j+1] = MbN;
      		MdW[j+1] =MdN;
      		MhW[j+1] = MhN;
      		l[j+1] = l[j];
      		}
    	}      
  

	in = fopen("datos.txt", "w");
	for(i = 0; i< N; i++)
	{
		fprintf(in, "%f, %f,%f,%f,%f,%f\n", r[i],v[i],MbW[i],MdW[i],MhW[i],l[i]);
	}
	fclose(in);

	free(r);
	free(v);
	free(vi);
	free(MbW);
	free(MdW);
	free(MhW);
	free(l);
	free(vnueva);

 	return 0;

}


