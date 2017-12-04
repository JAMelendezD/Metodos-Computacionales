#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#define N 300

long double similitud(double *observado, double *modelo, int len)
{
	double suma;
	int i;
	for(i=0;i<len;i++)
	{
			
		suma = suma + pow((observado[i]-modelo[i])/100.0,2);
	}
	return exp(-suma/2.0);
}


double * modelo(double*r, double Mb, double Md, double Mh,int len)
{
	float bb = 0.2497;
	float bd = 5.16;
	float ad = 0.3105;
	float ah = 64.3;
	float sum = bd+ad;
	int i;
	double *array = malloc(N*sizeof(double));
	for(i=0;i<len;i++)
	{
		array[i] = sqrt(Mb)*r[i]/pow(r[i]*r[i]+bb*bb, 0.75) + sqrt(Md)*r[i]/pow(r[i]*r[i]+sum*sum, 0.75) + sqrt(Mh)/pow(r[i]*r[i]+ah*ah, 0.25);
	}
	return array;
}


double normal(double m, double d)
{
	double al1 = drand48();
	double al2 = drand48();
	double normal = sqrt(-2.0*log(al1)*cos(2*(3.1415))*al2);
	return (d*normal+m);
}




	
int main(void)
{
	FILE *in;
	int i,j;
	int n = 50000;
	double *v = malloc(N*sizeof(double)); 
	double *vi = malloc(N*sizeof(double)); 
	double *r = malloc(N*sizeof(double)); 
	double *MbW = malloc(n*sizeof(double)); 
	double *MdW = malloc(n*sizeof(double)); 
	double *MhW = malloc(n*sizeof(double)); 
	double *vnueva = malloc(N*sizeof(double)); 
	double *l = malloc(n*sizeof(double)); 


	
	in = fopen("RadialVelocities.dat", "r");
	fscanf(in, "%*[^\n]"); 
	
	for(i = 0; i< N; i++)
	{
		fscanf(in,"%lf %lf" , &r[i] , &v[i]);
	}

	fclose(in);
	
	for(i = 0; i< N; i++)
	{
		MbW[i] = 0;
		MdW[i] = 0;
		MhW[i] = 0;
	}
	

	MbW[0] = 5000*drand48();
	MdW[0] = 5000*drand48();
	MhW[0] = 5000*drand48();
	
	vi = modelo(r, MbW[0],MdW[0],MhW[0],N);
	l[0] = similitud(v,vi,N);
		

	for(i=0; i<n; i++)
	{
	
    		vi = modelo(r, MbW[i],MdW[i],MhW[i],N);

    		double MbN = normal(MbW[i], 100.0);
    		double MdN = normal(MdW[i], 100.0);
    		double MhN = normal(MhW[i], 100.0);
		vnueva = modelo(r, MbN, MdN, MhN,N);
		long double lvieja = similitud(v,vi,N);
    		long double lnueva = similitud(v,vnueva,N);
		double alpha = lnueva/lvieja;

  

    		if(alpha >= 1.0)
		{
      		MbW[i+1] = MbN;
      		MdW[i+1] =MdN;
      		MhW[i+1] = MhN;
      		l[i+1] = lnueva;
    		}
		else 
		{
      			double beta = drand48();
      			if(beta <= alpha)
      			{
      				MbW[i+1] = MbN;
      				MdW[i+1] =MdN;
      				MhW[i+1] = MhN;
      				l[i+1] = lnueva;
      			} 
      			else 
      			{
      			MbW[i+1] = MbN;
      			MdW[i+1] =MdN;
      			MhW[i+1] = MhN;
      			l[i+1] = l[j];
      			}
		}
    	}      
  
  	double max = l[0];
  	for(i=1; i<n; i++)
   	{
    		if(l[i] >= max)
    		{
     			max = l[i];
      			j = i;
    		}
 	}

	printf("Las masas son respectivamente: %lf,%lf,%lf\n", MbW[j],MdW[j],MhW[j]);
	
	in = fopen("datos.txt", "w");
	fprintf(in, "%f,%f,%f", MbW[j], MdW[j], MhW[j]);
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


