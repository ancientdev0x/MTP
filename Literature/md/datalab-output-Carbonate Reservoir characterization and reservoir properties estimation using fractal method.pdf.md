

# Characterization and estimation of reservoir properties in a carbonate reservoir in Southern Iran by fractal methods

Rezvan Rahimi<sup>1</sup> · Mahmoud Bagheri<sup>1</sup> · Mohsen Masihi<sup>2</sup>

Received: 9 September 2016 / Accepted: 14 May 2017 / Published online: 25 May 2017  
© The Author(s) 2017. This article is an open access publication

**Abstract** Reservoir heterogeneity has a major effect on the characterization of reservoir properties and consequently reservoir forecast. In reality, heterogeneity is observed in a wide range of scales from microns to kilometers. A reasonable approach to study this multi-scale variations is through fractals. Fractal statistics provide a simple way of relating variations on larger scales to those on smaller scales and vice versa. Simple statistical fractal models (fBm and fGn) can be useful to understand the model construction and help the reservoir structure characterization. In this paper, the fractal methods (fGn and fBm) have been applied to characterize and to estimate of reservoir properties. Three methods, namely box-counting, variogram, and R/S analysis, were carried out on log and core data for porosity and permeability data to estimate fractal dimension; a high fractal dimension estimated in this study reveals a high heterogeneity in the reservoir. Moreover, sampling from simulated fractal data at non-existing data depths enables us to generate appropriate realizations of reservoir permeability with suitable accuracy at a proper computational time.

**Keywords** Porosity · Permeability · Fractal geometry · fGn · fBm

## Introduction

Reservoir characterization is one of the important tasks in petroleum engineering studies. An accurate characterization of reservoir dynamic behavior can be dependent on the exact characterization of the spatial distribution of reservoir properties throughout the reservoir (Hurtado et al. 2009). The porosity, permeability, and water saturation are key reservoir properties which affect the reservoir flow behavior and fluid recovery (Xiao et al. 2012). Among these, permeability is of prime importance, especially in carbonate reservoirs; the reason is that carbonate reservoirs have a more complex internal structure and more heterogeneous (Gholinejad and Masihi 2012; Al-Khans and Blunt 2007).

Methods for accessing the reservoir properties can be divided into direct and indirect methods. Direct methods include coring, well logging, and well tests; In practice, coring is the most reliable method, but it is expensive and time consuming; Moreover, it may be impossible to take samples in some intervals of a well. Indirect methods are based on estimation and forecast. Geostatistics as a branch of statistical science is one of the tools for indirect methods, which studies spatial structures that vary in pace and/or in time. Geostatistics can also be used for quantity description and local relationship between data within the reservoirs (Deutsch 2002). Methods based on geostatistics, despite their advantages, have drawbacks such as smoothing data; thus, they cannot show details and local heterogeneity (Rasouli and Tokhmechi 2010).

The term “fractal” was coined by Mandelbrot in the 1970s. Fractal geometry can be used to describe irregular and fragmented patterns in nature (Mandelbrot 1983; Aasum et al. 1991). In fact, fractal geometry presents a mathematical model for most of the complex phenomena

✉ Rezvan Rahimi  
Rezvanrahimi39013@gmail.com

<sup>1</sup> Department of Petroleum Engineering, Science and Research Branch, Islamic Azad University, Tehran, Iran

<sup>2</sup> Department of Chemical and Petroleum Engineering, Sharif University of Technology, Tehran, Iran

such as coastline, mountain, cloud, and fracture patterns (Yin 1996; Li et al. 2009; Kim and Schechter 2009).

Recent studies have shown that statistical fractals are useful for modeling natural phenomena (Arizabalo et al. 2006; Vadapalli et al. 2014). Because of the nature of variability in reservoir data, statistical fractals such as fractional Gaussian noise (fGn) and fractional Brownian motion (fBm) are candidate approaches to characterize porosity and permeability and, in general, the hydraulic property variations on the subsurface data (Zeybek and Onur 2003; Lozada-Zumaeta et al. 2012).

The porosity and horizontal component of petrophysical properties such as permeability are usually modeled using kriging-based methods (i.e., Geostatistics). The property values along the well can be used as conditions through these approaches. Although these properties are inferred from well log data, there are some practical cases, where the data are missing in some well intervals. Due to significant variability of petrophysical properties in vertical direction as a result of reservoir layering in reservoirs, fractal models can be used to characterize them and to help model them in these intervals.

The purpose of this paper is to employ the statistical fractals (fBm and fGn) for the characterization and their estimation at non-existing data depths. In this study, three wells in a carbonate reservoir in the southern part of Iran were studied. Once the R/S analysis and spectral density were carried out on log-derived porosity data and core-based porosity, and permeability data, fractal properties were generated based on FFT (fast Fourier transform); next, the fractal structures were investigated. Finally, appropriate realizations of the reservoir permeability were generated.

## The fractal theory

Fractal objects can follow self-similarity described by a fractal dimension. Self-similarity means that fractal objects are made of smaller components, which are similar to the

original shape and have some properties similar to it after a change in scale (Hardy and Beier 1994; Souza and Rostirolla 2011; Molz and Hyden 2006). An example of fractal objects is shown in Fig. 1.

A mathematical definition of a fractal concentrates on the property that fractal objects have a fractional dimension, which is not an integer. The fractal dimension should first be determined (Wang and Li 1997). The larger fractal dimension corresponds to more heterogeneous objects (Cai et al. 2010). One may calculate a fractal dimension by different methods (Li et al. 2009; Souza and Rostirolla 2011). Two methods for the determination of the fractal dimension are presented in Table 1.

### Fractal modeling

Fractal modeling is an important class of simulations. One of the advantages of fractals is that the fractal dimension can be kept constant during the simulation and this resolves the smoothing shortcoming associated with kriging, as in fact the fractal dimension carries the data variation property. However, in fractal simulation, the minimized estimation variance is not guaranteed and more importantly, fractal-based approaches are actually simulators and not estimators; thus, with rerunning the fractal simulation, different realizations can be obtained in general (Rasouli and Tokhmechi 2010; Yu and Cheng 2002). The other advantage of fractals is that fractals are independent of scale, which allows one to utilize any data regardless of the measurement scale (Kim and Schechter 2009).

In petroleum engineering, especially where risks and cost are high, fractal models will take their place along with existing models as a powerful tool for the reservoir engineering because of old customary models and assuming that homogenous reservoirs cannot be exact. As an alternative method, a heterogeneous reservoir with a fractal structure can have a better accommodation for reservoir data.

**Fig. 1** Koch snowflake curve as one of the exact fractals

![Figure 1: Two plots illustrating fractal properties. Plot (a) shows the fGn value (y-axis, ranging from -0.1 to 0.6) versus Depth (m) (x-axis, ranging from 0 to 3000). The data is a dense, noisy signal fluctuating around zero. Plot (b) shows the fBm value (y-axis, ranging from -0.8 to 0.8) versus Depth (m) (x-axis, ranging from 0 to 3000). The data is a dense, noisy signal with a clear upward trend, fluctuating between approximately -0.6 and 0.4.](ff574e13f425f22e763f210fa455aca6_img.jpg)

Figure 1: Two plots illustrating fractal properties. Plot (a) shows the fGn value (y-axis, ranging from -0.1 to 0.6) versus Depth (m) (x-axis, ranging from 0 to 3000). The data is a dense, noisy signal fluctuating around zero. Plot (b) shows the fBm value (y-axis, ranging from -0.8 to 0.8) versus Depth (m) (x-axis, ranging from 0 to 3000). The data is a dense, noisy signal with a clear upward trend, fluctuating between approximately -0.6 and 0.4.

![Springer logo](bfa6833c5be8f619218c51763f16602d_img.jpg)

Springer logo

**Table 1** Methods of determination of fractal dimensions

| Method       | Summary method of fractal dimension (D)                                                                                                                                                                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Box-counting | $D = \lim_{r \rightarrow 0} \frac{\log N(r)}{\log(\frac{1}{r})}$ <p>N(r): number of boxes required to completely cover original shape<br/>r: reverse of mesh size for grid that is covering of shape</p> |
| Variogram    | $m = 4 - 2D$ <p>m: slope of Logarithmic graph of variogram versus distances of separation</p>                                                                                                            |

The discovery that well logs often have a fractal character was made by Hewett (Hardy and Beier 1994). It is surprising that the logs analyzed by many authors in many different formations show similar to fGn; for example, Carne and Tubman analyzed three horizontal wells and four vertical wells in a carbonate formation. They found that all the logs behave as fGn (Crane and Tubman 1990). Moreover, Hardy found similar results by analyzing some wells in sandstone formations (Hardy 1993). The analysis of porosity logs of several Iranian reservoirs, which are also mostly carbonate formations, revealed that most of the logs can reasonably well be described by either fGn or fBm models (Sahimi 2000).

One should consider that not all logs are adapted to the fGn models, but one may apply fractal modeling like the fGn and fBm to evaluations of reservoirs properties (Hardy and Beier 1994). It should be noted the details of the application of fractal distributions can vary from one reservoir to another.

### Fractal Brownian motion(fBm)

Brown motion is a random motion of a particle in an interval or distance in a random direction with a step length determined by a Gaussian (normal) probability distribution function (Yin 1996). Mandelbrot and Van Ness applied the term fractional Brownian motion (fBm) in 1968. fBm comprises a family of random functions described by an index  $H$  ( $0 < H < 1$ ) (Mandelbrot and Van Ness 1968; Luo et al. 2005; Dieker 2004; Sheng et al. 2012).

Consider a Gaussian random process  $B_H(r)$  and  $r = (x, y, z)$  and  $r_0 = (x_0, y_0, z_0)$  are two arbitrary points in space and  $H$  is called the **Hurst exponent**.

This process  $B_H(r)$  is a fractional Brownian motion if

1. The mean value is zero:

$$\langle B_H(r) - B_H(r_0) \rangle = 0 \tag{1}$$

2. The variance value is:

$$\text{var}(r - r_0) = \langle (B_H(r) - B_H(r_0))^2 \rangle \cong (r - r_0)^{2H} \tag{2}$$

3. The correlation function will be:

$$C(r) = \frac{\langle -B_H(-r) \times B_H(r) \rangle}{\langle B_H(r)^2 \rangle} \cong 2^{2H-1} \tag{3}$$

fBm, based on the above definition, can be divided into three categories:

- $H = 0.5$  corresponding to an uncorrected trend and model in this condition is completely random (Dashtian et al. 2011; Ostvand 2014; Jafari et al. 2011).
- $H > 0.5$  is characterized by persistence, i.e., the process shows a clear trend; in other words, a trend at  $x$  is likely to be followed by a similar trend at  $x + \Delta x$  (Fonseca-Pinto et al. 2009; Gaci and Zaourar 2011).
- $H < 0.5$  means that it shows an anti-persistent behavior (Fonseca-Pinto et al.2009; Delignieres 2015)

As can be seen in Fig. 2, with an increase in  $H$  value, the sequence of fBm will be smoother.

### Fractal Gaussian noise(fGn)

Another process is called fGn which can be introduced as a range of fBm processes with a time delay  $\delta > 0$ . In other words, the fGn function is the derivative of the fBm function (Sheng et al. 2011). It is emphasized that the fGn is more varied than the fBm (Zeybek and Onur 2003). As can be seen in Fig. 3, with an increase in the exponent  $H$ , the sequence of FGN would be more regular.

A fGn process has the following main properties:

- A fGn model with  $H$  close to 1 is similar to a fBm model with  $H < 0.4$ .
- The histogram of the fGn model is Gaussian; however, the histogram of the fBm is box-shaped.

![Figure 2: Four stacked time-series plots of Fractional Brownian motion for different Hurst exponents H. The top plot is for H=0.1, showing a highly irregular, noisy signal. The second plot is for H=0.5, showing a moderately irregular signal. The third plot is for H=0.7, showing a smoother signal with a clear upward trend. The bottom plot is for H=0.9, showing a very smooth signal with a clear upward trend. The x-axis represents time or distance, and the y-axis represents the fBm value.](6dbb6274a026cd62e86c023286b13971_img.jpg)

Figure 2: Four stacked time-series plots of Fractional Brownian motion for different Hurst exponents H. The top plot is for H=0.1, showing a highly irregular, noisy signal. The second plot is for H=0.5, showing a moderately irregular signal. The third plot is for H=0.7, showing a smoother signal with a clear upward trend. The bottom plot is for H=0.9, showing a very smooth signal with a clear upward trend. The x-axis represents time or distance, and the y-axis represents the fBm value.

**Fig. 2** Fractional Brownian motion for different values of  $H$

![Figure 3: Fractional Gaussian noise for different values of H. The figure shows four horizontal plots of time series data, each labeled with a different value of H: H=0.1, H=0.5, H=0.7, and H=0.9. The plots show increasing roughness and variability as H increases.](7fb5215fd72210a2e4cce6df55550c89_img.jpg)

Figure 3: Fractional Gaussian noise for different values of H. The figure shows four horizontal plots of time series data, each labeled with a different value of H: H=0.1, H=0.5, H=0.7, and H=0.9. The plots show increasing roughness and variability as H increases.

**Fig. 3** Fractional Gaussian noise for different values of *H*

## Methods of generation of fractal structure

There are different methods for the generation of fractal data based on both fBm and fGn models (Babadagli 2005). In this work, fast Fourier transform (FFT) method was used to generate fractal data. The algorithm based on the FFT has lower computational efforts, less complexity and more suitable performance than other methods.

Equation 4 can be used for the generation of fractal data by the Fourier method:

$$S(\omega) = \frac{1}{\left(\sum_{i=1}^d \omega_i^2\right)^{H+d/2}} \tag{4}$$

where *S* is the spectral density, *d* is the dimension of the system and  $\omega = (\omega_1, \omega_2, \dots, \omega_d)$ .

Based on the Fourier method, one should first generate random data between 0 and 1. The number of random data will be equal to number of the expected simulated data. Once the Fourier transform of random data must be calculated, this Fourier transform is multiplied by root of *S*( $\omega$ ); finally, the data are returned to the original space by using a reverse Fourier transform, and thereby the resulting array containing data with fractal structures having an ideal size.

## Methods of determination of fractal dimension

As summarizes in Table 1, the fractal dimension can be calculated by the following two methods.

### Box-counting

The most popular algorithm for computing the fractal dimension of one-dimensional and two-dimensional data is the box-counting, the method originally developed by Voss (1985). In this method, the fractal surface is covered with a grid of *n*-dimensional boxes or hyper-cubes with side

length  $\delta$ , and counting the number of boxes that contains a part of the fractal object *N*( $\delta$ ). This is repeated by covering the system with boxes of recursively different sizes. An input signal with *N* elements or an image of size *N* \* *N* is used as input where *N* is a power of 2. The slope  $\beta$  is obtained from the logarithmic plot of the number of boxes used to cover the fractal object within the system against the box size, and the fractal dimension *D<sub>F</sub>* is given by (Klinkenberg et al. 1994; Annadhason 2012).

$$D_F = -\beta \tag{5}$$

### Variogram

The variogram is defined as the mean squared increment of points:

$$\gamma(h) = \frac{1}{2n} \sum_{i=1}^n [V(x_i) - V(x_{i+h})]^2 \tag{6}$$

where *h* is lag distance (distance between two successive points),  $\gamma(h)$  is variogram at lag distance *h*, *n* is the number of pairs at a lag distance *h* and *V*(*x<sub>i</sub>*) is the sample of property values at location *x<sub>i</sub>*, fractal distribution is characterized by a variogram power law model:

$$\gamma(h) = \gamma_0 h^\beta \tag{7}$$

where  $\beta$  is the slop of lag distance, *h*, versus variogram  $\gamma(h)$  plot in log–log scale. The fractal dimension *D<sub>F</sub>* is given by (Babadagli and Develi 2001):

$$D_F = 2 - \beta/2 \tag{8}$$

## Analysis methods of fractal data

There are different methods for the analysis of fractal data (Jafari et al. 2011; Kaya 2005). In this paper, both rescaled range (R/S) analysis and spectral density analysis were employed.

### R/S analysis

The rescaled range (R/S) analysis is a measure of how a sequence varies as lag increases. In fact, it is a measure of the cumulative fluctuation of the sequence. The range is rescaled by dividing it by the standard deviation. In the R/S analysis, the rescaled range is plotted versus the lag on a

**Table 2** Range of log data in each of wells (A, B, and C)

| Well | Depth         |
|------|---------------|
| A    | 3927–4173.8   |
| B    | 3943.9–4477.6 |
| C    | 4051.9–4489.9 |

**Table 3** Statistical analysis of log data in each of wells (A, B, and C)

| Statistical parameter                          |                    | Well A | Well B | Well C |
|------------------------------------------------|--------------------|--------|--------|--------|
| Porosity ( $\frac{v}{V}$ )                     | Mean               | 0.0302 | 0.0521 | 0.0333 |
|                                                | Standard deviation | 0.0425 | 0.0427 | 0.0354 |
| Irreducible water saturation ( $\frac{v}{V}$ ) | Mean               | 0.787  | 0.538  | 0.818  |
|                                                | Standard deviation | 0.289  | 0.310  | 0.227  |
| Rock density ( $\frac{gr}{cm^3}$ )             | Mean               | –      | 2.73   | 2.730  |
|                                                | Standard deviation | –      | 0.0257 | 0.032  |

log–log scale and the slope of the line fitted gives the Hurst exponent ( $H$ ). The R/S algorithm is presented in Appendix (Hardy and Beier 1994; Kirichenko et al. 2011; Li et al. 2011; Arizabal et al. 2004).

The fractal dimension ( $D_F$ ) can then be calculated, by using  $H$  and Euclidean dimension of the system ( $D_E$ ):

$$D_F = D_E + 2H - 1 \quad (9)$$

### Spectral density

The spectral density is a measure based on the Fourier transform of the original data. The analysis of spectral density can provide insights into the ordering of the sequence of data (Harcarik et al. 2012).

Fractal models have spectral densities ( $S$ ), which is related to angular frequency ( $\omega$ ) as reads (Hewett 1986; Serinaldi 2010):

$$S \propto \omega^\beta \quad (10)$$

where, for the fGn,  $\beta$  is related to the slope of the R/S analysis ( $H$ ):

$$\beta = -(2H - 1) \quad (11)$$

For the fBm, the relationship between  $\beta$  and  $H$  is given by:

$$\beta = -(2H + 1) \quad (12)$$

### Field data description

The data have been gathered from a part of three real wells (A, B, and C) in Fahliyan reservoir in the Southern Iran. The log data (porosity, water saturation, and rock density) were available for all the wells (A, B, and C), while the core data, namely porosity, permeability, and rock density, were attainable in 305 points in only well C (Table 2).

### Statistical analysis

The statistical analysis of both log and core data in each well under study was performed, and the results are tabulated in Tables 3 and 4.

**Table 4** Statistical analysis of core data in well C

| Statistical parameter | Porosity ( $\frac{v}{V}$ ) | Permeability (mD) | Rock density ( $\frac{gr}{cm^3}$ ) |
|-----------------------|----------------------------|-------------------|------------------------------------|
| Mean                  | 0.0446                     | 1.764             | 2.720                              |
| Standard deviation    | 0.0028                     | 0.4893            | 0.0007                             |

## Estimation of fractal dimension

The R/S analysis of the porosity data obtained from the log data of the wells A, B, and C was carried out, and the Hurst exponents were calculated. The results are shown in Fig. 4. The Hurst exponents (Table 5) were about 0.5, which showed that the porosity in these wells is distributed approximately in random.

For each well, namely well A, B, and C, the fractal dimension ( $d$ ) was calculated by Eq. 5 as shown in Table 6 with three methods of box-counting, variogram, and R/S analysis. Then, the spectral density exponents ( $\beta$ ) were calculated by using Eqs. 7 and 8 and the Hurst exponents mentioned in Table 7.

For porosity, the permeability distribution based on the core data in well C, Hurst exponent ( $H$ ), spectral density exponents ( $\beta$ ) and fractal dimension were determined, and the results are summarized in Tables 8 and 9.

## Generation of fractal models for distribution of reservoir properties

Fractal data based on fast Fourier transformation (FFT) method were generated by a computer code written in MATLAB. The code can generate both fBm and fGn data according to the spectral density exponent ( $\beta$ ) for every data set with a specific mean and standard deviation. Using the data in Tables 3, 4, 7, and 8, the fractal models were generated for the distribution of reservoir properties as displayed in Figs. 5, 6, and 7.

As can be inferred from Figs. 5, 6, and 7, the fGn structure is more varied than the fBm. Furthermore, the comparison of the porosity structures of these wells shows a more random structure in well C, as indicated

**Fig. 4** Log–log plot of R/S analysis of porosity distribution each of wells (A, B, and C)![Figure 4: Log-log plots of R/S analysis for porosity distribution for three wells: Well A, Well B, and Well C. Each plot shows log R/S on the y-axis (0 to 2) versus log lag on the x-axis (0 to 4). Well A: y = 0.4661x - 0.1738, R² = 0.9913. Well B: y = 0.4671x - 0.2648, R² = 0.9721. Well C: y = 0.4987x - 0.2993, R² = 0.9637. All plots show a strong positive linear correlation with data points clustered around the regression line.](46f43cb4ffd47565e7c0ca306d461435_img.jpg)

Figure 4: Log-log plots of R/S analysis for porosity distribution for three wells: Well A, Well B, and Well C. Each plot shows log R/S on the y-axis (0 to 2) versus log lag on the x-axis (0 to 4). Well A: y = 0.4661x - 0.1738, R² = 0.9913. Well B: y = 0.4671x - 0.2648, R² = 0.9721. Well C: y = 0.4987x - 0.2993, R² = 0.9637. All plots show a strong positive linear correlation with data points clustered around the regression line.

**Table 5** Hurst exponents in each of wells (A, B, and C)

| Well | Hurst exponent(H) |
|------|-------------------|
| A    | 0.4661            |
| B    | 0.4671            |
| C    | 0.4987            |

**Table 6** Determination of fractal dimension in each of wells (A, B, and C) by log data

| Well | Fahliyan thickness in the well (m) | $D_F$ (by box-counting method) | $D_F$ (by variogram method) | $D_F$ (by R/S analysis) |
|------|------------------------------------|--------------------------------|-----------------------------|-------------------------|
| A    | 246.8                              | 1.69                           | 1.829                       | 1.9322                  |
| B    | 530.6                              | 1.753                          | 1.956                       | 1.9342                  |
| C    | 438                                | 1.918                          | 1.904                       | 1.997                   |

by its Hurst exponent (see Table 5). These statistically generated realizations for the porosity distribution in wells A, B, and C (Figs. 5, 6, and 7) show similar trends in spatial structures as compared to the real porosity distribution shown in Fig. 8. The structures can also be

**Table 7** Estimation of  $\beta$  for fBm, fGn models by log data

| Well | $\beta$ (For fBm model) | $\beta$ (For fGn model) |
|------|-------------------------|-------------------------|
| A    | −1.932                  | 0.0678                  |
| B    | −1.934                  | 0.0658                  |
| C    | −1.997                  | 0.0028                  |

**Table 8** Estimation of H,  $\beta$  for core data

| Distribution      | H     | $\beta$ (For fBm model) | $\beta$ (For fGn model) |
|-------------------|-------|-------------------------|-------------------------|
| Core porosity     | 0.434 | −1.868                  | 0.133                   |
| Core permeability | 0.349 | −1.698                  | 0.302                   |

**Table 9** Determination of fractal dimension ( $D_F$ ) in well C for core data

| Distribution      | $D_F$ (by variogram method) | $D_F$ (by R/S analysis) |
|-------------------|-----------------------------|-------------------------|
| Core porosity     | 1.844                       | 1.868                   |
| Core permeability | 1.851                       | 1.698                   |

**Fig. 5** Two realizations with fractal structure for well log porosity in well A; ( $H = 0.4661$ ). **a** fGn model, **b** fBm model

![Figure 5: Two realizations with fractal structure for well log porosity in well A. (a) fGn model plot showing fGn value vs Depth(m) with a low amplitude signal. (b) fBm model plot showing fBm value vs Depth(m) with a higher amplitude, jagged signal.](a6a8016b231533e7f34b550f4676afc6_img.jpg)

Figure 5: Two realizations with fractal structure for well log porosity in well A. (a) fGn model plot showing fGn value vs Depth(m) with a low amplitude signal. (b) fBm model plot showing fBm value vs Depth(m) with a higher amplitude, jagged signal.

**Fig. 6** Two realizations with fractal structure for well log porosity in well B; ( $H = 0.4671$ ). **a** fGn model, **b** fBm model

![Figure 6: Two realizations with fractal structure for well log porosity in well B. (a) fGn model plot showing fGn model vs Depth(m) with a low amplitude signal. (b) fBm model plot showing fBm model vs Depth(m) with a higher amplitude, jagged signal.](4279c8be6ec4ed56f4b3349be98bb426_img.jpg)

Figure 6: Two realizations with fractal structure for well log porosity in well B. (a) fGn model plot showing fGn model vs Depth(m) with a low amplitude signal. (b) fBm model plot showing fBm model vs Depth(m) with a higher amplitude, jagged signal.

**Fig. 7** Two realizations with fractal structure for well log porosity in well C; ( $H = 0.4987$ )

![Figure 7: Two realizations with fractal structure for well log porosity in well C. (a) fGn model plot showing fGn model vs Depth-feed with a low amplitude signal. (b) fBm model plot showing fBm model vs Depth-feed with a higher amplitude, jagged signal.](84e2ac543ffc4145dc85b05a48ec62e3_img.jpg)

Figure 7: Two realizations with fractal structure for well log porosity in well C. (a) fGn model plot showing fGn model vs Depth-feed with a low amplitude signal. (b) fBm model plot showing fBm model vs Depth-feed with a higher amplitude, jagged signal.

quantitatively compared by looking at the fractal dimensions (see Table 6).

The comparison of porosity and permeability structures in well C confirms that the porosity distribution has a more random structure than the permeability distribution, as indicated by its Hurst exponent (see in Table 8). In addition, the realizations of porosity and permeability in well C (Figs. 9 and 10) show similar spatial structures as compared to the real porosity and permeability distribution shown in Figs. 11 and 12. These can also be quantitatively

compared by looking at the fractal dimensions (see Table 9).

### Pseudo-permeability log of Fahliyan reservoir

In this work, the fractal data generated as mentioned in “Generation of fractal models for distribution of reservoir properties” section were used in calculations where the core data were not available; moreover, the realizations of the permeability distribution in well C based on

![Figure 8: Real porosity distribution for well log data in wells (A, B, and C). The figure consists of three vertically stacked scatter plots. The top plot is for Well #A, the middle for Well #B, and the bottom for Well #C. Each plot shows Porosity value (V/V) on the y-axis (ranging from 0 to 0.2) versus Depth (m) on the x-axis. Well #A depth ranges from 3900 to 4200 m. Well #B depth ranges from 3900 to 4500 m. Well #C depth ranges from 4000 to 4500 m. The data points are represented by blue, cyan, and purple diamonds respectively, showing a highly variable and noisy distribution of porosity with depth.](a71911ad87414271aeb190e0eebcb989_img.jpg)

Figure 8: Real porosity distribution for well log data in wells (A, B, and C). The figure consists of three vertically stacked scatter plots. The top plot is for Well #A, the middle for Well #B, and the bottom for Well #C. Each plot shows Porosity value (V/V) on the y-axis (ranging from 0 to 0.2) versus Depth (m) on the x-axis. Well #A depth ranges from 3900 to 4200 m. Well #B depth ranges from 3900 to 4500 m. Well #C depth ranges from 4000 to 4500 m. The data points are represented by blue, cyan, and purple diamonds respectively, showing a highly variable and noisy distribution of porosity with depth.

**Fig. 8** Real porosity distribution for well log data in wells (A, B, and C)

**Fig. 9** Two realizations with fractal structure for core porosity in well C; ( $H = 0.434$ ).  
a fGn model, b fBm model

![Figure 9: Two realizations with fractal structure for core porosity in well C. The figure contains two side-by-side line plots. Plot (a) shows the fGn model, with the y-axis labeled 'fGn model' ranging from -0.1 to 0.6 and the x-axis labeled 'Depth(m)' ranging from 0 to 3000. The data is a dense, noisy line centered around zero. Plot (b) shows the fBm model, with the y-axis labeled 'fBm model' ranging from -0.6 to 0.8 and the x-axis labeled 'Depth(m)' ranging from 0 to 3000. This plot shows a smoother, more structured line with a clear upward trend and oscillations, ranging from approximately -0.4 to 0.4.](7ff005f9556dc6518981bb92091d36ab_img.jpg)

Figure 9: Two realizations with fractal structure for core porosity in well C. The figure contains two side-by-side line plots. Plot (a) shows the fGn model, with the y-axis labeled 'fGn model' ranging from -0.1 to 0.6 and the x-axis labeled 'Depth(m)' ranging from 0 to 3000. The data is a dense, noisy line centered around zero. Plot (b) shows the fBm model, with the y-axis labeled 'fBm model' ranging from -0.6 to 0.8 and the x-axis labeled 'Depth(m)' ranging from 0 to 3000. This plot shows a smoother, more structured line with a clear upward trend and oscillations, ranging from approximately -0.4 to 0.4.

fBm and fGn are presented in Figs. 13 and 14, respectively.

As can be seen in Figs. 13 and 14, the fractal data generated by fGn are noisier than those generated by fBm. The results of the statistical analysis of the data generated by fBm and fGn at non-sampled depths are presented in Table 10. Additionally, the percentage of error in mean was calculated in comparison with the mean of permeability core mentioned in Table 4.

## Conclusions

According to the results obtained, the following conclusions can be drawn:

- Fractal theory, a main branch of mathematics that can consider most of geometrics, can be used as a powerful method in petroleum engineering. The application of fractal modeling, because of the heterogeneous nature of reservoirs, has an appropriate adaption to real reservoirs. In this work, fractal modeling proved efficiently suitable for the characterization of reservoir properties;
- In this study, Hurst exponents were calculated for wells A, B, and C and were about 0.5; thus, the porosity in these wells was approximately randomly distributed;
- The fractal dimension was calculated by using three methods, namely box-counting, variogram, and R/S analysis, and the results confirmed that the determination of the fractal dimension by variogram method, because of doing it by the GS + software package, could have higher accuracy and lower computational time than the other manual methods;
- In the current work, an appropriate model for the distribution of permeability in Fahliyan reservoir was

**Fig. 10** Two realizations with fractal structure for core permeability in well C; ( $H = 0.349$ ). **a** fGn model, **b** fBm model

![Figure 10: Two line plots showing fractal structure for core permeability. Plot (a) is the fGn model, showing a highly oscillatory signal between -0.2 and 0.6 over a depth of 0 to 300 m. Plot (b) is the fBm model, showing a smoother, oscillating signal between -0.4 and 0.8 over the same depth range.](bedcca5cdf168e3508ef511d94ec514c_img.jpg)

Figure 10: Two line plots showing fractal structure for core permeability. Plot (a) is the fGn model, showing a highly oscillatory signal between -0.2 and 0.6 over a depth of 0 to 300 m. Plot (b) is the fBm model, showing a smoother, oscillating signal between -0.4 and 0.8 over the same depth range.

![Figure 11: A scatter plot of Core-Permeability (mD) versus Depth (m) for well C. The x-axis represents depth from 4200 to 4295 m, and the y-axis represents permeability from 0 to 0.25 mD. Data points are clustered at various depths, showing a general increase in permeability towards the bottom of the well.](891ff9b651838b7f59e9a1612a739e15_img.jpg)

Figure 11: A scatter plot of Core-Permeability (mD) versus Depth (m) for well C. The x-axis represents depth from 4200 to 4295 m, and the y-axis represents permeability from 0 to 0.25 mD. Data points are clustered at various depths, showing a general increase in permeability towards the bottom of the well.

**Fig. 11** Porosity distribution for core data in well C

![Figure 12: A scatter plot of Core permeability (mD) versus Depth (m) for well C. The x-axis represents permeability from 0 to 30 mD, and the y-axis represents depth from 4200 to 4295 m. The plot shows a dense vertical column of data points with some horizontal spread, indicating a wide range of permeability values at many depths.](0f3e3ea50bcceb86f6c524ab2b6f3e7a_img.jpg)

Figure 12: A scatter plot of Core permeability (mD) versus Depth (m) for well C. The x-axis represents permeability from 0 to 30 mD, and the y-axis represents depth from 4200 to 4295 m. The plot shows a dense vertical column of data points with some horizontal spread, indicating a wide range of permeability values at many depths.

**Fig. 12** Plot of permeability distribution for core data in well C

presented by using fBm and fGn data in non-sampled intervals. The fractal data used showed a suitable coordination with the core data in well C.

**Open Access** This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (<http://creativecommons.org/licenses/by/4.0/>), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

## Appendix

R/S analysis is called “RESCALED RANGE” ANALYSIS. The range is the difference between the maximum and minimum values of a running sum of the data. The range is rescaled by dividing the range by the standard deviation of the data. A very clear description of the R/S analysis in terms of rainfall is given by Feder (1988). For each starting location,  $j$ , and for a given analysis length,  $\tau$ , the range of a set of data,

$$R_j(\tau) = \max\theta(\lambda, \tau) - \min\theta(\lambda, \tau)$$

where

$$\theta_j(\lambda, \tau) = \sum_{k=j}^{\tau+j} (e_k - \overline{e_j(\tau)})$$

$$\overline{e_j(\tau)} = \frac{1}{\tau + 1} \sum_{m=j}^{j+\tau} e_m$$

The standard deviation is:

$$\sigma_j(\tau) = \frac{1}{\tau + 1} \sum_{k=j}^{j+\tau} (e_k - \overline{e_j(\tau)})^2$$

Finally, the rescaled range is

![Figure 13: Realizations-based fBm for permeability distribution of Fahliyan reservoir. The figure consists of four plots. The first plot shows 'core data' as a blue line with horizontal bars, representing permeability (mD) on the x-axis (0 to 30) versus depth (m) on the y-axis (4200 to 4295). A red circle highlights a section around 4215-4225 m. The second plot shows five colored lines (1-5) representing individual realizations of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The third plot shows the 'Mean' permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The fourth plot shows the 'Standard deviation' of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230).](7801d00a216dc4dc8a7d210dcb5fe3c5_img.jpg)

Figure 13: Realizations-based fBm for permeability distribution of Fahliyan reservoir. The figure consists of four plots. The first plot shows 'core data' as a blue line with horizontal bars, representing permeability (mD) on the x-axis (0 to 30) versus depth (m) on the y-axis (4200 to 4295). A red circle highlights a section around 4215-4225 m. The second plot shows five colored lines (1-5) representing individual realizations of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The third plot shows the 'Mean' permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The fourth plot shows the 'Standard deviation' of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230).

**Fig. 13** Realizations-based fBm for permeability distribution of Fahliyan reservoir

![Figure 14: Realizations-based fGn for permeability distribution of Fahliyan reservoir. The figure consists of four plots. The first plot shows 'core data' as a blue line with horizontal bars, representing permeability (mD) on the x-axis (0 to 30) versus depth (m) on the y-axis (4200 to 4295). A red circle highlights a section around 4215-4225 m. The second plot shows five colored lines (1-5) representing individual realizations of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The third plot shows the 'Mean' permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The fourth plot shows the 'Standard deviation' of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230).](6b32b7b928d34eeccb15c29cdf9d2cb3_img.jpg)

Figure 14: Realizations-based fGn for permeability distribution of Fahliyan reservoir. The figure consists of four plots. The first plot shows 'core data' as a blue line with horizontal bars, representing permeability (mD) on the x-axis (0 to 30) versus depth (m) on the y-axis (4200 to 4295). A red circle highlights a section around 4215-4225 m. The second plot shows five colored lines (1-5) representing individual realizations of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The third plot shows the 'Mean' permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230). The fourth plot shows the 'Standard deviation' of permeability (mD) on the x-axis (0 to 4) versus depth (m) on the y-axis (4212 to 4230).

**Fig. 14** Realizations-based fGn for permeability distribution of Fahliyan reservoir

**Table 10** Statistical analysis of simulated permeability distribution in well C

| Method        | Mean   | Standard deviation | Error of mean |
|---------------|--------|--------------------|---------------|
| Fractal (fBm) | 1.7645 | 0.4893             | 0.0025        |
| Fractal (fGn) | 1.7506 | 0.4894             | 0.0075        |

$$\overline{RS}(\tau) = \frac{1}{N-1} \sum_{j=1}^{N-1} RS_j(\tau)$$

It is very slow to calculate this sum over all stating values and all legs. A subset is usually chosen (Hardy and Beier 1994).

$$RS_j(\tau) = \frac{R_j(\tau)}{\sigma_j(\tau)}$$

This function depends on the analysis length,  $\tau$ , and the starting location,  $j$ , over which  $R/S$  is calculated. Generally, the average of  $R/S$  over a number of starting location,  $\overline{RS}(\tau)$ , is plotted, the analysis length or lag,  $\tau$ . That is,

## References

- Aasum Y, Kelkar M, Gupta S (1991) An application of geostatistics and fractal geometry for reservoir characterization. SPE-20257-PA 11–19
- Al-Khans i AS, Blunt MJ (2007) Network extraction from sandstone and carbonate pore space images. Pet Sci Eng 56:219–231

- Annadhason A (2012) Computer science and information technology and security. 2, ISSN: 2249-955
- Arizabaló R, Oleschko K, Korvin G, Ronquillo G, Cedillo-Pardo E (2004) Fractal and cumulative trace analysis of wire-line logs from a well in naturally fractured limestone reservoir in the Gulf of Mexico. *J Geofis Int* 43:467–476
- Arizabaló R, Oleschko K, Korvin G, Lozada M, Castejón R, Ronquillo G (2006) Lacunarity of geophysical well logs in the Cantarell oil field in Gulf of Mexico. *J Geofis Int* 45:99–113
- Babadagli T (2005) Effect of fractal permeability correlations on water flooding performance in carbonate reservoirs. *J Pet Sci Eng* 23:223–228
- Babadagli T, Develi K (2001) Fractal fracture surfaces and fluid displacement process in fractured rocks. In: 10th International conference on fracture, Honolulu, December 02–06, 2001
- Cai J, Yu B, Zou M, Luo L (2010) Fractal characterization of spontaneous co-current imbibition in porous media. *J Energy Fuels* 24(3):1860–1867
- Crane SD, Tubman KM (1990) Reservoir variability and modeling with fractures. SPE 20606, doi:10.2118/20606-MS
- Dashtian H, Jafari GR, Masihi M, Sahimi M (2011) Scaling, multifractality and large-range correlations in well log data of large-scale porous media. *J Phys A* 390:2096–2111
- Delignieres D (2015) Correlation Properties of (discrete) fractional Gaussian noise and fractional Brownian motion. *J Math Probl Eng*, Hindawi Publishing Corporation, Article ID: 485623
- Deutsch CV (2002) Geostatistical reservoir modeling. Oxford University Press, Oxford
- Dieker T (2004) Simulation of fractional Brownian motion. MSc thesis, University of Twente, Department of Mathematical Sciences
- Feder J (1988) Fractals. Plenum Press, New York
- Fonseca-Pinto R, Ducla JL, Araujo F, Aguiar A (2009) On the influence of time-series length in EMD to extract frequency content: simulations and models in biomedical signals. *J Med Eng Phys* 31:713–719
- Gaci S, Zaourar N (2011) A new approach for the investigation of the multifractality of borehole wire-line logs. *J Earth Sci* 3:63–70
- Gholinejad S, Masihi M (2012) A physical-based model of permeability/porosity relationship for the rock data of Iran southern carbonate reservoirs. *Iran J Oil Gas Sci Technol* 1:25–36
- Harcarik T, Bocko J, Maslavkova K (2012) Frequency analysis of acoustic signal using the fast Fourier transformation in MATLAB. *J Procedia Eng* 48:199–204
- Hardy H (1993) In: Linville B (ed) Reservoir characterization III. Penn well, Tulsa, pp 787–797
- Hardy HH, Beier R (1994) Fractals in reservoir engineering. World Scientific Singapore, Singapore. ISBN 978-981-02-2069-3
- Hewett TA (1986) Fractal distribution of reservoir heterogeneity and their influence on fluid transport. In: SPE15386, pp 1–16
- Hurtado N, Aldana M, Torres J (2009) Comparison between neuro-fuzzy and fractal model for permeability prediction. *J Comput Geosci* 13:181–186
- Jafari R, Sahimi M, Rasaei R, Rahimi Tabar R (2011) Analysis of porosity distribution of Large-Scale porous media and their reconstruction by Lanqevain equation. *J Phys Res* 83:026309
- Kaya A (2005) An investigation with fractal geometry analysis of time series. MSc thesis, Izmir institute of technology
- Kim T, Schechter D (2009) Estimation of fracture porosity of naturally fractured reservoirs with no matrix porosity using fractal discrete fracture networks. *J Reserv Eng* 12:232–242
- Kirichenko L, Radivilova T, Deineko Zh (2011) Comparative analysis for estimating of the Hurst exponent for stationary and non-stationary time series. *J Inf Technol Knowl* 5:371–388
- Klinkenberg C et al (1994) Modeling of the anisotropy of Young's modulus in polycrystals. *J Mater Technol* 65:291–297
- Li J, Du Q, Sun C (2009) An improved box counting method for image fractal dimension estimation. *J. Pattern Recognit* 42:2460–2469
- Li W, Yu C, Carriquis A, Kliemann W (2011) The asymptotic behavior of the R/S statistic for fractional Brownian motion. *J Stat Prob Lett* 81:83–91
- Lozada-Zumaeta M et al (2012) Distribution of petrophysical properties for sandy-clays reservoirs by fractal interpolation. *J Nonlinear-Process Geophys* 19:239–250
- Luo Ch, Lee W, Lai Y, Wen C, Liaw J (2005) Measuring the fractal dimension of diesel soot agglomerates by fractional Brownian motion processor. *J Atmos Environ* 39:3565–3572
- Mandelbrot B (1983) The fractal geometry of nature, 3rd edn. Freeman, San Francisco. ISBN 13: 9780716711865
- Mandelbrot BB, Van Ness JW (1968) Fractional Brownian motion, fractional Gaussian noise and their application. *SIAM Rev* 4:422–437
- Molz F, Hyden P (2006) A new type of stochastic fractal for application in subsurface hydrology. *J Geoderma* 134:274–283
- Ostlund L (2014) Long range memory in time series of Earth surface temperature. A dissertation for the degree of Philosophiae doctor, Faculty of Science and Technology, The Arctic university of Norway
- Rasouli V, Tokhmechi B (2010) Difficulties in using geostatistical models in reservoir simulation. In: SPE North Africa technical conference and exhibition, energy management in a challenging economy. Egypt, pp 103–114
- Sahimi M (2000) Fractal—wavelet neural network approach to characterization and up scaling of fractured reservoirs. *J Comput Geosci* 26:877–905
- Sernaldini F (2010) Use and misuse of some Hurst parameter estimators applied to stationary and non-stationary financial time series. *J Phys. A* 389:2770–2781
- Sheng H, Sun H, Chen Y, Qiu T (2011) Synthesis of multifractional Gaussian noises based on variable-order fractional operators. *J Signal Process* 91:1645–1650
- Sheng H, Chen H, Qiu Y (2012) Fractional processes and fractional-order signal processing, signal and communication technology. Springer, London. ISSN 1860-4862
- Souza J, Rostirolla S (2011) A fast matlab program to estimate the multifractal spectrum of multidimensional data: application to fractures. *J Comput Geosci* 37:241–249
- Vadapalli U, Srivastava RP, Vedanti N, Dimri VP (2014) Estimation of permeability of a sandstone reservoir by a fractal and Monte Carlo simulation approach. *J Non-linear Process Geophys* 21:9–18
- Voss RF (1985) Random fractal forgeries. In: Earnshaw RA (ed) Fundamental Algorithms for computer graphics. NATO ASI Series. Springer-Verlag, Berlin, pp. 805–835
- Wang F, Li S (1997) Determination of the surface fractal dimension for porous media by capillary condensation. *J Ind Eng Chem Res* 36:1598–1602
- Xiao B, Fan J, Ding F (2012) Prediction of relative permeability of unsaturated porous media based on fractal theory and monte carlo simulation. *J Energy Fuels* 26:6971–6978
- Yin ZM (1996) New methods for simulation of fractional Brownian motion. *J Comput Phys* 127:66–72
- Yu B, Cheng P (2002) A fractal permeability model for bi-dispersed porous media. *J Heat Mass Transf* 45:2983–2993
- Zeybek A, Onur M (2003) Conditioning fractal (fBm, fGn) porosity and permeability field to multiwell pressure data. *J Math Geol* 35:577–612