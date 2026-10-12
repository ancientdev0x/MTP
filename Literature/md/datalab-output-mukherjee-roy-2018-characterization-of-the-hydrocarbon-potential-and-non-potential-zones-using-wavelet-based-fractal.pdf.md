

## Articles

# CHARACTERIZATION OF THE HYDROCARBON POTENTIAL AND NON-POTENTIAL ZONES USING WAVELET-BASED FRACTAL ANALYSIS

BAPPA MUKHERJEE\* and P. N. S. ROY\*,†,‡

*\*Department of Applied Geophysics  
 Indian Institute of Technology (ISM)  
 Dhanbad 826004, Jharkhand, India*

*†The Abdus Salam International Centre for  
 Theoretical Physics, Trieste, Italy*

*‡pns\_may1@yahoo.com*

Received March 31, 2017

Accepted November 17, 2017

Published January 2, 2018

## Abstract

The identification of prospective and dry zone is of major importance from well log data. Truthfulness in the identification of potential zone is a very crucial issue in hydrocarbon exploration. In this line, the problem has received considerable attention and many conventional techniques have been proposed. The purpose of this study is to recognize the hydrocarbon and non-hydrocarbon bearing portion within a reservoir by using the non-conventional technique. The wavelet based fractal analysis (WBFA) has been applied on the wire-line log data in order to obtain the pre-defined hydrocarbon (HC) and non-hydrocarbon (NHC) zones by their self-affine signal nature is demonstrated in this paper. The feasibility of the proposed technique is tested with the help of most commonly used logs, like self-potential, gamma ray, resistivity and porosity log responses. These logs are obtained from the industry to make out several HC and NHC zones of all wells in the study region belonging to the upper Assam basin. The results obtained in this study for a particular log response, where in the case of HC bearing zones, it is found that they are mainly situated in a variety of sandstones lithology which leads to the higher Hurst exponent. Further, the NHC zones found to be analogous to lithology with higher

†Corresponding author.

shale content having lower Hurst exponent. The above proposed technique can overcome the chance of miss interpretation in conventional reservoir characterization.

*Keywords:* Well Logging; Wavelet Transform; WBFA; Self-Affine Signal.

## 1. INTRODUCTION

In conventional methods, geophysical well log data is used for finding the lithological boundary, prospective zones and petrophysical properties of the formation through which the borehole is drilled. In general, spontaneous potential (SP), gamma ray (GR), resistivity (latero-log deep (LLD), latero-log shallow (LLS) and micro-spherically focused log (MSFL)), bulk density (RHOB), neutron porosity (NPHI) log response are used for identifying the potential zones as well as the lithological boundaries of the formations. In our study, we have used these entire wire-line log responses mentioned above. Individual log response is a measurement of a specific petrophysical parameter of the formation at a particular sampling interval, so that the well log response can be treated as a time series. In conventional interpretation, the interpreter may use their own experience and knowledge of geological conditions for marking the prospective zones within the formation. However, the possibility of contradiction in outcomes cannot be overruled. The identification of different lithology is of essential prominence from the well log data to obtain a trustworthy reservoir characterization. According to this logic, the identification of rock types and their potentiality is the main motto in oil exploration, for finding out the prospective zones in a reservoir. However, for reliability, we need an accurate analysis of conventional wire-line log as well as the core data simultaneously. Statistical approaches have been used for facies identification and mapping which are usually based on the inspection of core data and well logs.<sup>1</sup> The concept of fractal study and its application on geophysical data has clearly deliberated by Refs. 2 and 3. In our study, we used the conventional well log data to distinguish potential zones from non-potential zones of several wells. A signal can be decomposed into a number of windows that are accompanying with a mother wavelet, (specific scale) at a specific time, widely known as wavelet transform of a signal.<sup>4,5</sup> The combined wavelet and fractal analysis is basically a scaling tool measurement of a non-stationary signal,

hence provides an agenda for analyzing scale properties of the signal (well log data). The application wavelet based fractal analysis (WBFA) has been recently advised for determining the Hurst coefficients.<sup>6-9</sup> applied WBFA for studying two wells in order to identify lithology.

Moreover, the concept of fractals comes due to the failure of the measurement of objects with Euclidian geometry, which fails to precisely explain the actual geometrical shape of the geological distribution. Objects that displayed scale-invariance properties that can vary from point to point can be represented by multifractal. Further, the homogeneous object can be represented by monofractal. Thus, complex mathematical objects that are invariant with respect to dilations, i.e. same properties should hold over all scales, so-called isotropic medium. In that case, self-similarity could be applicable. However, in real world self-similarity may exist in the exceptional case.<sup>10,11</sup>

However, in this study the signals having variability in the vertical direction as well as in horizontal direction, as in this case of well log data corresponding to stratified lithology are called self-affine signals. Earth is an anisotropic medium, thus in nature, the acquired geophysical datasets are in abundance of self-affine signals. Therefore, well log data can be treated as a self-affine signal.<sup>12,13</sup>

In the present paper, we have used WBFA on wire-line log data to recognize the potential zones (mostly found to be in sandstone) from non-potential zones (mostly associated to lithology with higher shale content) of the wells by their fractal nature.

## 2. THEORY

The wavelet transform of a signal provides a partition of the signal into different scale components. i.e. split up the signal into a bunch of signals, each scale component having a particular frequency range.<sup>14</sup> Wavelets are scaled and translated into copies of a finite length waveform which is called

as **mother wavelet  $\psi(t)$** , which is defined by

$$\psi_{\tau,s}(t) = \frac{1}{\sqrt{|s|}}\psi\left(\frac{t-\tau}{s}\right), \quad s, \tau \in R, \quad s \neq 0, \quad (1)$$

where the parameter, scaling ( $s$ ) defines the degree of compression and translation ( $\tau$ ) measuring the time location of the wavelet. The mathematical expression of wavelet coefficient is given by

$$w_{\psi}^{(s,\tau)} = \frac{1}{\sqrt{|s|}} \int_{-\infty}^{\infty} x(t)\psi^*\left(\frac{t-\tau}{s}\right)dt, \quad (2)$$

where  $\psi^*$  represents complex conjugate of  $\psi$ . Results of wavelet transform depends upon variety of mother wavelet ( $\psi$ ) used for the transform procedure.<sup>15</sup> The time series  $x(t)$  can be recovered by using wavelet transform of  $w_{\psi}^{(s,\tau)}$ :

$$x(t) = \frac{1}{K_{\psi}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \frac{1}{\sqrt{s}} \psi\left(\frac{t-\tau}{s}\right) w_{\psi}^{(s,\tau)} \frac{ds d\tau}{s^2}. \quad (3)$$

The admissibility constant  $K_{\psi}$  has to satisfy the admissibility condition,  $0 < K_{\psi} < +\infty$  and is given by

$$K_{\psi} = 2\pi \int_0^{\infty} \frac{|\hat{\psi}(\omega)|^2}{|\omega|} d\omega, \quad (4)$$

where  $\hat{\psi}(\omega)$  is the Fourier transform of  $\psi(t)$ . **WBFA is used to obtain the Hurst exponent from a non-stationary signal.** In this process, initially the wavelet coefficient is obtained for each and every level of decomposition. The slope ( $m$ ) or power law exponent can be estimated from the straight line fitted to the plot of log of variance of the wavelet

coefficients ( $\sigma$ ) versus the log of scale ( $S$ ). Linear portion of this plot is tally to power-law process over a specific frequency. The above approach was applied in order to obtain the fractal dimension of the echo-cardiac signals.<sup>8</sup> It has been recommended that average wavelet coefficient method affords realistically better results.<sup>6</sup>

In WBFA, **the relation between the slope** (power law exponent) of the straight line and **Hurst exponent** (parameter properly represents the statistical self-affine property) are related as<sup>6,16</sup>

$$H = (m - 1)/2, \quad (5)$$

where for  $1 - D$  dataset  $0 < H < 1$ . **The Hurst exponent ( $H$ ) obtained according to this method will truthfully characterize the self-affine signal like a well-line log or a seismic data**, that might be associated with different sedimentary environments and formations behaving like self-affine signal. Also, time series associated with different geological complexity (lithology) can be interpreted from this dimension.

## 3. WELL LOG ANALYSIS

In this paper, studied wells are selected from **Bhogpara oil field of Assam-Arakan Basin**, which is situated in the north-eastern part of India, categorized as category-I basin on the basis of production, the basin covers an area of 116,000 sq. km, details of the geographic situation for this area and well location are shown in Fig. 1.

As per conventional logging for an ideal HC zone, the log response according to resistivity logging

![Figure 1: Geographic situation of the study area and well location. The figure consists of two parts. The left part is a map of the study area showing the Assam Basin, Bengal Basin, and surrounding regions like Himalaya, NE India, and Mikir Hills. It labels major geological features like the Main Central Thrust (MCT), Main Boundary Thrust (MBT), Dauki Fault (DF), and Indo Burma Fault (IBFT). The city of Bhogpara is marked. The right part is a scatter plot titled 'Well location' showing the coordinates of five wells: Well-3, Well-4, Well-13, Well-7, and Well-14. The x-axis is Longitude (94.975 to 94.995) and the y-axis is Latitude (27.425 to 27.445).](8ae925c5e796101b53aba9fb3f36dfc9_img.jpg)

| Well    | Longitude | Latitude |
|---------|-----------|----------|
| Well-3  | 94.985    | 27.442   |
| Well-4  | 94.992    | 27.440   |
| Well-13 | 94.980    | 27.435   |
| Well-7  | 94.990    | 27.438   |
| Well-14 | 94.992    | 27.435   |

MCT - Main Central Thrust  
 MBT - Main Boundary Thrust  
 DF - Dauki Fault  
 IBFT - Indo Burma Fault

Figure 1: Geographic situation of the study area and well location. The figure consists of two parts. The left part is a map of the study area showing the Assam Basin, Bengal Basin, and surrounding regions like Himalaya, NE India, and Mikir Hills. It labels major geological features like the Main Central Thrust (MCT), Main Boundary Thrust (MBT), Dauki Fault (DF), and Indo Burma Fault (IBFT). The city of Bhogpara is marked. The right part is a scatter plot titled 'Well location' showing the coordinates of five wells: Well-3, Well-4, Well-13, Well-7, and Well-14. The x-axis is Longitude (94.975 to 94.995) and the y-axis is Latitude (27.425 to 27.445).

Fig. 1 Geographic situation of the study area and well location specified by their latitude and longitude (after Ref. 20).

![Well log plot for well-3 showing depth (m) from 3825 to 3925. The plot includes three main columns: (MSFL), (NPHI), and (RHOB). Each column has a header table with parameters like (GR), (SP), (LLS), (LLD), and (G/C3). The plot shows various curves representing different logging parameters, with horizontal bands indicating different hydrocarbon (HC) and non-hydrocarbon (NHC) zones labeled on the right.](e94f3bbb6f7501b9a1344dd0210e5dd8_img.jpg)

The figure displays a well log for well-3. The vertical axis represents depth in meters, ranging from 3825 m to 3925 m. The horizontal axis is divided into three main sections: (MSFL), (NPHI), and (RHOB). Each section has a header table with specific parameters and values. The (MSFL) section includes (GR) with values 0, GAPI 150, and (SP) with values 50, MV 90. The (NPHI) section includes (LLS) with values 0.2, OHMM 2000, and (G/C3) with values 0.45, V/V -0.15. The (RHOB) section includes (LLD) with values 0.2, OHMM 2000, and (G/C3) with values 1.95, G/C3 2.95. The plot shows several curves representing different logging parameters, with horizontal bands indicating different hydrocarbon (HC) and non-hydrocarbon (NHC) zones labeled on the right: NHC-1, HC-1, NHC-2, HC-2, NHC-3, HC-3, NHC-4, HC-4, NHC-5, HC-5, and NHC-6.

Well log plot for well-3 showing depth (m) from 3825 to 3925. The plot includes three main columns: (MSFL), (NPHI), and (RHOB). Each column has a header table with parameters like (GR), (SP), (LLS), (LLD), and (G/C3). The plot shows various curves representing different logging parameters, with horizontal bands indicating different hydrocarbon (HC) and non-hydrocarbon (NHC) zones labeled on the right.

Fig. 2 The original well log data of well-3 for all conventional logging are displayed, where different HC and NHC zones are labeled properly on the basis of quick look interpretation.

![Well log plot for well-4 showing depth (m) from 3825 to 3925. The plot includes three main columns: (MSFL), (NPHI), and (RHOB). Each column has a header table with parameters like (SP), (GR), (LLS), (LLD), and (G/C3). The plot shows various curves representing different logging parameters, with horizontal bands indicating different hydrocarbon (HC) and non-hydrocarbon (NHC) zones labeled on the right.](f961cbef0f8217e216b553bed270315b_img.jpg)

The figure displays a well log for well-4. The vertical axis represents depth in meters, ranging from 3825 m to 3925 m. The horizontal axis is divided into three main sections: (MSFL), (NPHI), and (RHOB). Each section has a header table with specific parameters and values. The (MSFL) section includes (SP) with values -40, MV 60, and (GR) with values 0, GAPI 150. The (NPHI) section includes (LLS) with values 0.2, OHMM 2000, and (G/C3) with values 0.45, V/V -0.15. The (RHOB) section includes (LLD) with values 0.2, OHMM 2000, and (G/C3) with values 1.95, G/C3 2.95. The plot shows several curves representing different logging parameters, with horizontal bands indicating different hydrocarbon (HC) and non-hydrocarbon (NHC) zones labeled on the right: NHC-1, Not Identified, HC-1, NHC-2, HC-2, NHC-3, Not Identified, NHC-4, and HC-3.

Well log plot for well-4 showing depth (m) from 3825 to 3925. The plot includes three main columns: (MSFL), (NPHI), and (RHOB). Each column has a header table with parameters like (SP), (GR), (LLS), (LLD), and (G/C3). The plot shows various curves representing different logging parameters, with horizontal bands indicating different hydrocarbon (HC) and non-hydrocarbon (NHC) zones labeled on the right.

Fig. 3 The original well log data of well-4 for all conventional logging are displayed, where different HC and NHC zones are labeled properly on the basis of quick look interpretation.

![Well log plot for well-7 showing depth (m) from 3825 to 3925. The plot includes tracks for (SP), (GR), (MSFL), (LLS), (LLD), (NPHI), and (RHOB). zones are labeled on the right: NHC-1, Not Identified, HC-1, NHC-2, Not Identified, HC-2, NHC-3, HC-3, NHC-4, HC-4.](e0d425c8e4eef259e4c52d81426d93fa_img.jpg)

Well log plot for well-7. The vertical axis represents depth in meters, ranging from 3825 m to 3925 m. The horizontal axis represents various logging parameters. The plot is divided into several sections: (SP) with values -40, MV, 60; (GR) with values 0, GAPI, 150; (MSFL) with values 0.2, OHMM, 2000; (LLS) with values 0.2, OHMM, 2000; (LLD) with values 0.2, OHMM, 2000; (NPHI) with values 0.45, V/V, -0.15; and (RHOB) with values 1.95, G/C3, 2.95. The right side of the plot shows zone labels: NHC-1, Not Identified, HC-1, NHC-2, Not Identified, HC-2, NHC-3, HC-3, NHC-4, and HC-4.

Well log plot for well-7 showing depth (m) from 3825 to 3925. The plot includes tracks for (SP), (GR), (MSFL), (LLS), (LLD), (NPHI), and (RHOB). zones are labeled on the right: NHC-1, Not Identified, HC-1, NHC-2, Not Identified, HC-2, NHC-3, HC-3, NHC-4, HC-4.

Fig. 4 The original well log data of well-7 for all conventional logging are displayed, where different HC and NHC zones are labeled properly on the basis of quick look interpretation.

![Well log plot for well-13 showing depth (m) from 3825 to 3925. The plot includes tracks for (SP), (GR), (MSFL), (LLS), (LLD), (NPHI), and (RHOB). zones are labeled on the right: NHC-1, Not Identified, HC-1, NHC-2, Not Identified, HC-2, NHC-3, HC-3, NHC-4, HC-4.](6de7dcb072cef2388026fb0f504084b2_img.jpg)

Well log plot for well-13. The vertical axis represents depth in meters, ranging from 3825 m to 3925 m. The horizontal axis represents various logging parameters. The plot is divided into several sections: (SP) with values -40, MV, 60; (GR) with values 0, GAPI, 150; (MSFL) with values 0.2, OHMM, 2000; (LLS) with values 0.2, OHMM, 2000; (LLD) with values 0.2, OHMM, 2000; (NPHI) with values 0.45, V/V, -0.15; and (RHOB) with values 1.95, G/C3, 2.95. The right side of the plot shows zone labels: NHC-1, Not Identified, HC-1, NHC-2, Not Identified, HC-2, NHC-3, HC-3, NHC-4, and HC-4.

Well log plot for well-13 showing depth (m) from 3825 to 3925. The plot includes tracks for (SP), (GR), (MSFL), (LLS), (LLD), (NPHI), and (RHOB). zones are labeled on the right: NHC-1, Not Identified, HC-1, NHC-2, Not Identified, HC-2, NHC-3, HC-3, NHC-4, HC-4.

Fig. 5 The original well log data of well-13 for all conventional logging are displayed, where different HC and NHC zones are labeled properly on the basis of quick look interpretation.

Table 1. Represents the Details About Every Conventionally Defined HC and NHC Zones, Which are Selected from Several Wells Belonging to Our Study Area.

| Well-3                   |                    |                       |                          | Well-4             |                       |                          |                    | Well-7                |                          |                    |                       | Well-13                  |                    |                       |  |
|--------------------------|--------------------|-----------------------|--------------------------|--------------------|-----------------------|--------------------------|--------------------|-----------------------|--------------------------|--------------------|-----------------------|--------------------------|--------------------|-----------------------|--|
| Defined HC/<br>NHC Zones | Depth<br>Range (m) | No. of<br>Data Points | Defined HC/<br>NHC Zones | Depth<br>Range (m) | No. of<br>Data Points | Defined HC/<br>NHC Zones | Depth<br>Range (m) | No. of<br>Data Points | Defined HC/<br>NHC Zones | Depth<br>Range (m) | No. of<br>Data Points | Defined HC/<br>NHC Zones | Depth<br>Range (m) | No. of<br>Data Points |  |
| NHC-1                    | 3825–3829.9        | 50                    | NHC-1                    | 3825–3859.9        | 350                   | NHC-1                    | 3815–3825          | 101                   | NHC-1                    | 3825–3840          | 151                   |                          |                    |                       |  |
| HC-1                     | 3830–3833.2        | 33                    | HC-1                     | 3860–3864.6        | 47                    | HC-1                     | 3842.4–3846.4      | 41                    | HC-1                     | 3850–3864          | 141                   |                          |                    |                       |  |
| NHC-2                    | 3833.3–3862.4      | 292                   | NHC-2                    | 3864.7–3887        | 224                   | NHC-2                    | 3846.5–3855.6      | 92                    | NHC-2                    | 3864.1–3878.1      | 141                   |                          |                    |                       |  |
| HC-2                     | 3862.5–3866.9      | 45                    | HC-2                     | 3887.1–3889        | 20                    | HC-2                     | 3855.7–3860.6      | 50                    | HC-2                     | 3901.1–3908.9      | 78                    |                          |                    |                       |  |
| NHC-3                    | 3867–3873.9        | 70                    | NHC-3                    | 3889.1–3892.4      | 34                    | NHC-3                    | 3860.7–3881.8      | 212                   | NHC-3                    | 3909–3917.1        | 82                    |                          |                    |                       |  |
| HC-3                     | 3874–3877.3        | 34                    | HC-3                     | 3892.5–3896.5      | 41                    | HC-3                     | 3904.4–3913.8      | 114                   | HC-3                     | 3917.2–3918.9      | 18                    |                          |                    |                       |  |
| NHC-4                    | 3877.4–3890.1      | 128                   | NHC-4                    | 3896.6–3903.5      | 70                    | NHC-4                    | 3913.9–3925        | 92                    | NHC-4                    | 3919–3921.9        | 30                    |                          |                    |                       |  |
| HC-4                     | 3890.2–3893.3      | 32                    | HC-4                     | 3903.6–3915        | 115                   | HC-3                     |                    |                       |                          |                    |                       |                          |                    |                       |  |
| NHC-5                    | 3893.4–3903.1      | 198                   | NHC-5                    | 3915.1–3925        | 100                   |                          |                    |                       |                          |                    |                       |                          |                    |                       |  |
| HC-5                     | 3903.2–3914.9      | 98                    |                          |                    |                       |                          |                    |                       |                          |                    |                       |                          |                    |                       |  |
| NHC-6                    | 3915–3925          | 101                   |                          |                    |                       |                          |                    |                       |                          |                    |                       |                          |                    |                       |  |

should be like LLD>LLS>MSFL, according to porosity tool there must be a crossover in between neutron (NPHI) and density (RHOB) log response. Further, this zone should be within the clean sand zone for which SP response shows negative or positive deflection with respect to shale base line depending upon the salinities of the formation water and mud filtrate, with low GR response. In real

field, this thumb rule is not always applicable for finding a hydrocarbon zone.<sup>17,18</sup> intensely deliberated the details of different kind of borehole data and their interpretation techniques. However, in our study, we treated only those zones as a potential zone where all the thumb rules are obeyed.

All possible HC and NHC zones within the depth range 3825–3925 m are identified by quick-look

Table 2 Results of WBFA Analysis of Available Log Response Associated with the Selected HC and NHC Zones from Well-3 of Assam Basin with User-Defined Values of Slope (*m*) and Fractal Dimension (*D*) and Corresponding Intercept (*b*).

| Zone  | Log Response | <i>m</i>    | <i>H</i>    | <i>b</i> | Zone | Log Response | <i>m</i>    | <i>H</i>    | <i>b</i> |
|-------|--------------|-------------|-------------|----------|------|--------------|-------------|-------------|----------|
| NHC-1 | GR           | 1.80 ± 0.02 | 0.40 ± 0.02 | 0.89     | HC-1 | GR           | 2.66 ± 0.03 | 0.83 ± 0.03 | 0.31     |
|       | SP           | 1.94 ± 0.07 | 0.47 ± 0.07 | 0.77     |      | SP           | 2.54 ± 0.02 | 0.77 ± 0.02 | 0.79     |
|       | LLD          | 3.03 ± 0.12 | Error       | 0.37     |      | LLD          | 2.18 ± 0.11 | 0.59 ± 0.11 | 0.81     |
|       | LLS          | 3.08 ± 0.09 | Error       | 0.43     |      | LLS          | 2.11 ± 0.13 | 0.55 ± 0.13 | 0.94     |
|       | MSFL         | 2.14 ± 0.07 | 0.57 ± 0.07 | 1.43     |      | MSFL         | 2.17 ± 0.11 | 0.58 ± 0.11 | 1.18     |
|       | NPHI         | 1.77 ± 0.02 | 0.38 ± 0.02 | −4.19    |      | NPHI         | 2.80 ± 0.11 | 0.90 ± 0.11 | −4.86    |
|       | RHOB         | 1.94 ± 0.03 | 0.47 ± 0.03 | −2.17    |      | RHOB         | 2.28 ± 0.02 | 0.64 ± 0.02 | −2.02    |
| NHC-2 | GR           | 1.95 ± 0.02 | 0.47 ± 0.02 | 0.04     | HC-2 | GR           | 2.75 ± 0.03 | 0.87 ± 0.03 | 0.78     |
|       | SP           | 2.04 ± 0.03 | 0.52 ± 0.03 | −0.05    |      | SP           | 2.42 ± 0.02 | 0.71 ± 0.02 | 0.69     |
|       | LLD          | 3.38 ± 0.11 | Error       | 0.32     |      | LLD          | 3.82 ± 0.09 | Error       | −0.12    |
|       | LLS          | 3.68 ± 0.13 | Error       | −0.04    |      | LLS          | 3.28 ± 0.08 | Error       | 0.02     |
|       | MSFL         | 1.64 ± 0.12 | 0.32 ± 0.12 | 2.09     |      | MSFL         | 2.14 ± 0.08 | 0.57 ± 0.08 | 0.47     |
|       | NPHI         | 2.03 ± 0.02 | 0.51 ± 0.02 | −4.77    |      | NPHI         | 2.78 ± 0.02 | 0.89 ± 0.02 | −4.61    |
|       | RHOB         | 2.03 ± 0.02 | 0.51 ± 0.02 | −2.95    |      | RHOB         | 2.37 ± 0.03 | 0.68 ± 0.03 | −2.15    |
| NHC-3 | GR           | 1.69 ± 0.03 | 0.34 ± 0.03 | 0.62     | HC-3 | GR           | 2.84 ± 0.02 | 0.92 ± 0.02 | 0.38     |
|       | SP           | 1.96 ± 0.01 | 0.48 ± 0.01 | 0.50     |      | SP           | 2.50 ± 0.03 | 0.75 ± 0.03 | 0.76     |
|       | LLD          | 2.00 ± 0.09 | 0.50 ± 0.09 | 0.77     |      | LLD          | 3.37 ± 0.09 | Error       | 0.37     |
|       | LLS          | 2.06 ± 0.07 | 0.53 ± 0.07 | 0.60     |      | LLS          | 3.14 ± 0.11 | Error       | 0.30     |
|       | MSFL         | 2.14 ± 0.04 | 0.57 ± 0.04 | 0.24     |      | MSFL         | 3.00 ± 0.13 | Error       | 0.37     |
|       | NPHI         | 2.14 ± 0.06 | 0.57 ± 0.06 | −4.82    |      | NPHI         | 2.83 ± 0.02 | 0.91 ± 0.02 | −3.91    |
|       | RHOB         | 1.95 ± 0.03 | 0.47 ± 0.03 | −2.34    |      | RHOB         | 2.35 ± 0.04 | 0.67 ± 0.04 | −2.05    |
| NHC-4 | GR           | 2.12 ± 0.02 | 0.56 ± 0.02 | 0.27     | HC-4 | GR           | 2.93 ± 0.02 | 0.96 ± 0.02 | 1.05     |
|       | SP           | 1.99 ± 0.03 | 0.49 ± 0.03 | 0.25     |      | SP           | 2.85 ± 0.07 | 0.92 ± 0.07 | 0.95     |
|       | LLD          | 2.38 ± 0.07 | 0.69 ± 0.07 | −0.49    |      | LLD          | 2.75 ± 0.11 | 0.87 ± 0.11 | −0.47    |
|       | LLS          | 2.41 ± 0.09 | 0.70 ± 0.09 | −0.57    |      | LLS          | 2.63 ± 0.11 | 0.81 ± 0.11 | −0.55    |
|       | MSFL         | 1.94 ± 0.03 | 0.47 ± 0.03 | 0.16     |      | MSFL         | 2.61 ± 0.13 | 0.80 ± 0.13 | −0.45    |
|       | NPHI         | 1.87 ± 0.01 | 0.43 ± 0.01 | −4.57    |      | NPHI         | 2.91 ± 0.04 | 0.95 ± 0.04 | −4.08    |
|       | RHOB         | 2.03 ± 0.05 | 0.51 ± 0.05 | −2.57    |      | RHOB         | 2.38 ± 0.02 | 0.69 ± 0.02 | −2.10    |
| NHC-5 | GR           | 2.38 ± 0.02 | 0.69 ± 0.02 | 0.88     | HC-5 | GR           | 2.93 ± 0.02 | 0.96 ± 0.02 | 0.51     |
|       | SP           | 2.01 ± 0.06 | 0.50 ± 0.06 | 0.44     |      | SP           | 2.48 ± 0.03 | 0.74 ± 0.03 | 0.32     |
|       | LLD          | 2.49 ± 0.11 | 0.74 ± 0.11 | 2.76     |      | LLD          | 2.45 ± 0.09 | 0.72 ± 0.09 | −0.58    |
|       | LLS          | 2.39 ± 0.18 | 0.69 ± 0.18 | 3.28     |      | LLS          | 2.60 ± 0.09 | 0.80 ± 0.09 | −0.86    |
|       | MSFL         | 1.27 ± 0.15 | 0.13 ± 0.15 | 2.45     |      | MSFL         | 2.68 ± 0.13 | 0.84 ± 0.13 | −1.19    |
|       | NPHI         | 2.12 ± 0.02 | 0.56 ± 0.02 | −4.31    |      | NPHI         | 2.85 ± 0.04 | 0.92 ± 0.04 | −4.66    |
|       | RHOB         | 1.99 ± 0.02 | 0.49 ± 0.02 | −2.63    |      | RHOB         | 2.32 ± 0.07 | 0.66 ± 0.07 | −2.49    |
| NHC-6 | GR           | 2.32 ± 0.03 | 0.66 ± 0.03 | 0.53     |      |              |             |             |          |
|       | SP           | 2.01 ± 0.03 | 0.50 ± 0.03 | 0.33     |      |              |             |             |          |
|       | LLD          | 2.25 ± 0.09 | 0.62 ± 0.09 | −0.70    |      |              |             |             |          |
|       | LLS          | 2.37 ± 0.07 | 0.68 ± 0.07 | −0.95    |      |              |             |             |          |
|       | MSFL         | 2.39 ± 0.11 | 0.69 ± 0.11 | −0.26    |      |              |             |             |          |
|       | NPHI         | 2.14 ± 0.04 | 0.57 ± 0.04 | −4.41    |      |              |             |             |          |
|       | RHOB         | 1.98 ± 0.03 | 0.49 ± 0.03 | −2.46    |      |              |             |             |          |

Table 3 Results of WBFA Analysis of Available Log Response Associated with the Selected HC and NHC Zones from Well-4 of Assam Basin with User-Defined Values of Slope (*m*) and Fractal Dimension (*D*) and Corresponding Intercept (*b*).

| Zone  | Log Response | <i>m</i>    | <i>H</i>    | <i>b</i> | Zone | Log Response | <i>m</i>    | <i>H</i>    | <i>b</i> |
|-------|--------------|-------------|-------------|----------|------|--------------|-------------|-------------|----------|
| NHC-1 | GR           | 2.32 ± 0.03 | 0.66 ± 0.03 | 0.07     | HC-1 | GR           | 2.85 ± 0.02 | 0.92 ± 0.02 | 0.19     |
|       | SP           | -NIL-       | -NIL-       | -0.07    |      | SP           | -NIL-       | -NIL-       | -NIL-    |
|       | LLD          | 3.43 ± 0.11 | Error       | -0.73    |      | LLD          | 2.97 ± 0.07 | 0.98 ± 0.07 | 0.93     |
|       | LLS          | 3.29 ± 0.13 | Error       | -1.00    |      | LLS          | 3.10 ± 0.07 | Error       | 0.29     |
|       | MSFL         | 1.39 ± 0.15 | 0.19 ± 0.15 | 1.86     |      | MSFL         | 1.49 ± 0.13 | 0.24 ± 0.13 | 0.79     |
|       | NPHI         | 1.83 ± 0.02 | 0.41 ± 0.02 | -2.07    |      | NPHI         | 2.63 ± 0.02 | 0.81 ± 0.02 | -4.59    |
| NHC-2 | RHOB         | 2.02 ± 0.02 | 0.51 ± 0.02 | -3.05    | HC-2 | RHOB         | 2.52 ± 0.04 | 0.76 ± 0.04 | -2.27    |
|       | GR           | 2.26 ± 0.07 | 0.63 ± 0.07 | 0.05     |      | GR           | 2.95 ± 0.02 | 0.97 ± 0.02 | 1.26     |
|       | SP           | -NIL-       | -NIL-       | -0.05    |      | SP           | -NIL-       | -NIL-       | -NIL-    |
|       | LLD          | 2.66 ± 0.13 | 0.83 ± 0.13 | -0.22    |      | LLD          | 1.89 ± 0.11 | 0.44 ± 0.11 | 0.58     |
|       | LLS          | 2.73 ± 0.11 | 0.86 ± 0.11 | -0.41    |      | LLS          | 1.87 ± 0.13 | 0.43 ± 0.13 | 0.36     |
|       | MSFL         | 1.92 ± 0.15 | 0.46 ± 0.15 | 0.58     |      | MSFL         | 1.67 ± 0.11 | 0.33 ± 0.11 | 0.01     |
| NHC-3 | NPHI         | 2.18 ± 0.02 | 0.59 ± 0.02 | -4.88    | HC-3 | NPHI         | 2.81 ± 0.02 | 0.90 ± 0.02 | -3.90    |
|       | RHOB         | 2.06 ± 0.04 | 0.53 ± 0.04 | -2.82    |      | RHOB         | 2.72 ± 0.04 | 0.86 ± 0.04 | -1.79    |
|       | GR           | 1.95 ± 0.02 | 0.47 ± 0.02 | 1.40     |      | GR           | 2.85 ± 0.03 | 0.92 ± 0.03 | 1.03     |
|       | SP           | -NIL-       | -NIL-       | -1.40    |      | SP           | -NIL-       | -NIL-       | -NIL-    |
|       | LLD          | 2.24 ± 0.07 | 0.62 ± 0.07 | 0.79     |      | LLD          | 3.33 ± 0.11 | Error       | 1.93     |
|       | LLS          | 2.76 ± 0.09 | 0.88 ± 0.09 | 0.61     |      | LLS          | 3.37 ± 0.15 | Error       | 2.66     |
| NHC-4 | MSFL         | 1.32 ± 0.11 | 0.16 ± 0.11 | 1.92     | HC-4 | MSFL         | 2.23 ± 0.13 | 0.61 ± 0.13 | 2.51     |
|       | NPHI         | 2.22 ± 0.13 | 0.61 ± 0.13 | -4.00    |      | NPHI         | 2.57 ± 0.04 | 0.78 ± 0.04 | -3.67    |
|       | RHOB         | 2.12 ± 0.15 | 0.56 ± 0.15 | -2.19    |      | RHOB         | 2.87 ± 0.07 | 0.93 ± 0.07 | -2.51    |
|       | GR           | 2.18 ± 0.02 | 0.59 ± 0.02 | 0.79     |      | GR           | 2.65 ± 0.02 | 0.82 ± 0.02 | 0.66     |
|       | SP           | -NIL-       | -NIL-       | -0.79    |      | SP           | -NIL-       | -NIL-       | -NIL-    |
|       | LLD          | 1.68 ± 0.09 | 0.34 ± 0.09 | 1.74     |      | LLD          | 3.27 ± 0.09 | Error       | -0.27    |
| NHC-5 | LLS          | 1.67 ± 0.13 | 0.33 ± 0.13 | 2.25     |      | LLS          | 1.88 ± 0.11 | 0.44 ± 0.11 | 0.17     |
|       | MSFL         | 1.20 ± 0.11 | 0.10 ± 0.11 | 2.73     |      | MSFL         | 1.91 ± 0.13 | 0.45 ± 0.13 | 0.19     |
|       | NPHI         | 2.14 ± 0.02 | 0.57 ± 0.02 | -3.59    |      | NPHI         | 2.44 ± 0.02 | 0.72 ± 0.02 | -4.54    |
|       | RHOB         | 2.06 ± 0.03 | 0.53 ± 0.03 | -2.74    |      | RHOB         | 2.42 ± 0.05 | 0.71 ± 0.05 | -2.63    |
|       | GR           | 2.34 ± 0.02 | 0.67 ± 0.02 | 0.71     |      |              |             |             |          |
|       | SP           | -NIL-       | -NIL-       | -0.71    |      |              |             |             |          |
|       | LLD          | 2.37 ± 0.11 | 0.68 ± 0.11 | 0.66     |      |              |             |             |          |
|       | LLS          | 2.33 ± 0.15 | 0.66 ± 0.15 | 0.45     |      |              |             |             |          |
|       | MSFL         | 1.17 ± 0.07 | 0.08 ± 0.07 | 0.99     |      |              |             |             |          |
|       | NPHI         | 2.27 ± 0.03 | 0.63 ± 0.03 | 0.97     |      |              |             |             |          |
|       | RHOB         | 2.15 ± 0.02 | 0.57 ± 0.02 | -2.56    |      |              |             |             |          |
|       |              |             |             |          |      |              |             |             |          |

Table 4 Results of WBFA Analysis of Available Log Response Associated with the Selected HC and NHC Zones from Well-7 of Assam Basin with User-Defined Values of Slope ( $m$ ) and Fractal Dimension ( $D$ ) and Corresponding Intercept ( $b$ ).

| Zone  | Log Response | $m$             | $H$             | $b$   | Zone | Log Response | $m$             | $H$             | $b$   |
|-------|--------------|-----------------|-----------------|-------|------|--------------|-----------------|-----------------|-------|
| NHC-1 | GR           | $1.87 \pm 0.02$ | $0.43 \pm 0.02$ | 0.18  | HC-1 | GR           | $2.64 \pm 0.04$ | $0.82 \pm 0.04$ | 0.85  |
|       | SP           | $1.98 \pm 0.02$ | $0.49 \pm 0.02$ | 0.78  |      | SP           | $2.40 \pm 0.07$ | $0.70 \pm 0.07$ | 1.07  |
|       | LLD          | $3.07 \pm 0.11$ | Error           | -0.04 |      | LLD          | $2.80 \pm 0.09$ | $0.90 \pm 0.09$ | 0.68  |
|       | LLS          | $3.10 \pm 0.09$ | Error           | -0.10 |      | LLS          | $2.72 \pm 0.07$ | $0.86 \pm 0.07$ | -0.50 |
|       | MSFL         | $1.09 \pm 0.15$ | $0.04 \pm 0.15$ | 4.86  |      | MSFL         | $1.01 \pm 0.18$ | $0.00 \pm 0.18$ | 2.19  |
|       | NPHI         | $2.30 \pm 0.05$ | $0.65 \pm 0.05$ | -4.79 |      | NPHI         | $2.79 \pm 0.03$ | $0.89 \pm 0.03$ | -4.40 |
|       | RHOB         | $1.99 \pm 0.02$ | $0.49 \pm 0.02$ | -2.47 |      | RHOB         | $2.37 \pm 0.09$ | $0.68 \pm 0.09$ | -2.15 |
| NHC-2 | GR           | $2.02 \pm 0.02$ | $0.51 \pm 0.02$ | 0.28  | HC-2 | GR           | $2.64 \pm 0.03$ | $0.82 \pm 0.03$ | 0.23  |
|       | SP           | $1.96 \pm 0.02$ | $0.48 \pm 0.02$ | 0.72  |      | SP           | $2.42 \pm 0.02$ | $0.71 \pm 0.02$ | 0.93  |
|       | LLD          | $1.87 \pm 0.09$ | $0.43 \pm 0.09$ | 0.68  |      | LLD          | $3.32 \pm 0.09$ | Error           | 0.98  |
|       | LLS          | $1.91 \pm 0.11$ | $0.45 \pm 0.11$ | 0.52  |      | LLS          | $3.26 \pm 0.11$ | Error           | 0.65  |
|       | MSFL         | $1.52 \pm 0.14$ | $0.26 \pm 0.14$ | 0.70  |      | MSFL         | $1.75 \pm 0.14$ | $0.37 \pm 0.14$ | 1.13  |
|       | NPHI         | $2.32 \pm 0.02$ | $0.66 \pm 0.02$ | -4.36 |      | NPHI         | $2.88 \pm 0.05$ | $0.94 \pm 0.05$ | -4.51 |
|       | RHOB         | $1.98 \pm 0.04$ | $0.49 \pm 0.04$ | -2.48 |      | RHOB         | $2.36 \pm 0.07$ | $0.68 \pm 0.07$ | -2.23 |
| NHC-3 | GR           | $2.09 \pm 0.02$ | $0.54 \pm 0.02$ | -0.08 | HC-3 | GR           | $2.95 \pm 0.02$ | $0.97 \pm 0.02$ | -0.05 |
|       | SP           | $1.94 \pm 0.04$ | $0.47 \pm 0.04$ | 0.35  |      | SP           | $2.50 \pm 0.02$ | $0.75 \pm 0.02$ | 0.55  |
|       | LLD          | $2.31 \pm 0.11$ | $0.65 \pm 0.11$ | -0.69 |      | LLD          | $2.83 \pm 0.09$ | $0.91 \pm 0.09$ | -0.92 |
|       | LLS          | $2.29 \pm 0.15$ | $0.64 \pm 0.15$ | -0.68 |      | LLS          | $2.85 \pm 0.11$ | $0.92 \pm 0.11$ | -1.11 |
|       | MSFL         | $1.08 \pm 0.09$ | $0.04 \pm 0.09$ | 2.33  |      | MSFL         | $1.99 \pm 0.11$ | $0.49 \pm 0.11$ | -0.30 |
|       | NPHI         | $2.15 \pm 0.07$ | $0.57 \pm 0.07$ | -5.06 |      | NPHI         | $2.85 \pm 0.07$ | $0.92 \pm 0.07$ | -5.24 |
|       | RHOB         | $1.99 \pm 0.02$ | $0.49 \pm 0.02$ | -2.83 |      | RHOB         | $2.38 \pm 0.03$ | $0.69 \pm 0.03$ | -2.48 |
| NHC-4 | GR           | $2.09 \pm 0.04$ | $0.54 \pm 0.04$ | 0.67  |      |              |                 |                 |       |
|       | SP           | $1.98 \pm 0.05$ | $0.49 \pm 0.05$ | 0.67  |      |              |                 |                 |       |
|       | LLD          | $1.98 \pm 0.09$ | $0.49 \pm 0.09$ | -0.34 |      |              |                 |                 |       |
|       | LLS          | $2.03 \pm 0.15$ | $0.51 \pm 0.15$ | -0.51 |      |              |                 |                 |       |
|       | MSFL         | $1.07 \pm 0.09$ | $0.53 \pm 0.09$ | 2.53  |      |              |                 |                 |       |
|       | NPHI         | $2.16 \pm 0.02$ | $0.58 \pm 0.02$ | -4.83 |      |              |                 |                 |       |
|       | RHOB         | $2.01 \pm 0.05$ | $0.50 \pm 0.05$ | -2.53 |      |              |                 |                 |       |

interpretation technique from each of these four wells (well-3, well-4, well-7, and well-13). Selected HC and NHC zones from four wells, i.e. zones obtained with the help of quick-look interpretation from well-3, well-4, well-7, and well-13 are shown in Figs. 2–5. In accordance with the geology of the Bhogpara area, the hydrocarbon is mostly entrapped in multitasked reservoirs within the Lakadong and Therria formation which lies over the Langpar formation. The details about the conventionally defined HC and NHC zones are given in Table 1.

## 4. WBFA ANALYSIS ON LOG DATA

The results are shown in Tables 2–5, respectively for the WBFA. These results are based on selected conventional wire-line log response associated with HC and NHC zones from well-3, well-4, well-7,

well-13. Typical graphical representation of WBFA for GR log response belonging to the first-NHC zone of well-3 and well-4 are explained in Figs. 6a and 6b, respectively. Further, WBFA of GR log response belonging to the first-HC zone of well-7 and well-13 are explained in Figs. 7a and 7b, respectively.

In order to obtain the fractal behavior, the Hurst exponent ( $H$ ) values were calculated for available log response corresponding to the pre-defined HC and NHC portions, which are sensibly selected from different wells.

The results of WBFA analysis clearly depicts that,  $H$  values obtained in the case of different kinds of resistivity log responses associated with several HC and NHC zones are found to be erroneous. On the other hand, in NHC zones the  $H$  values corresponding to GR log response varies from 0.34 to 0.69, while for the same log response  $H$  values for HC zones varies from 0.75 to 0.99. Similarly,

Table 5 Results of WBFA Analysis of Available Log Response Associated with the Selected HC and NHC Zones from Well-13 of Assam Basin with User-Defined Values of Slope (*m*) and Fractal Dimension (*D*) and Corresponding Intercept (*b*).

| Zone  | Log Response | <i>m</i>    | <i>H</i>    | <i>b</i> | Zone | Log Response | <i>m</i>    | <i>H</i>    | <i>b</i> |
|-------|--------------|-------------|-------------|----------|------|--------------|-------------|-------------|----------|
| NHC-1 | GR           | 2.37 ± 0.07 | 0.68 ± 0.07 | −0.34    | HC-1 | GR           | 2.50 ± 0.04 | 0.75 ± 0.04 | 0.41     |
|       | SP           | 2.07 ± 0.02 | 0.53 ± 0.02 | −0.24    |      | SP           | 2.86 ± 0.07 | 0.93 ± 0.07 | −0.58    |
|       | LLD          | 3.30 ± 0.11 | Error       | 0.19     |      | LLD          | 3.58 ± 0.13 | Error       | 0.31     |
|       | LLS          | 3.89 ± 0.13 | Error       | −0.33    |      | LLS          | 3.42 ± 0.18 | Error       | −0.46    |
|       | MSFL         | 2.89 ± 0.13 | 0.94 ± 0.13 | −0.06    |      | MSFL         | 3.19 ± 0.11 | Error       | −0.87    |
|       | NPHI         | 2.14 ± 0.04 | 0.57 ± 0.04 | −4.15    |      | NPHI         | 3.11 ± 0.09 | Error       | −4.80    |
|       | RHOB         | 2.03 ± 0.02 | 0.51 ± 0.02 | −2.73    |      | RHOB         | 2.63 ± 0.02 | 0.81 ± 0.02 | −2.81    |
| NHC-2 | GR           | 2.24 ± 0.05 | 0.62 ± 0.05 | 0.11     | HC-2 | GR           | 2.99 ± 0.04 | 0.99 ± 0.04 | 0.34     |
|       | SP           | 2.04 ± 0.02 | 0.52 ± 0.02 | −0.49    |      | SP           | 2.93 ± 0.04 | 0.96 ± 0.04 | −0.38    |
|       | LLD          | 2.08 ± 0.11 | 0.54 ± 0.11 | −0.12    |      | LLD          | 2.85 ± 0.18 | 0.92 ± 0.18 | −0.32    |
|       | LLS          | 2.13 ± 0.15 | 0.56 ± 0.15 | −0.27    |      | LLS          | 2.91 ± 0.12 | 0.95 ± 0.12 | −0.46    |
|       | MSFL         | 2.59 ± 0.18 | 0.79 ± 0.18 | −0.66    |      | MSFL         | 2.69 ± 0.14 | 0.84 ± 0.14 | −0.92    |
|       | NPHI         | 2.21 ± 0.09 | 0.60 ± 0.09 | −4.78    |      | NPHI         | 3.15 ± 0.18 | Error       | −4.39    |
|       | RHOB         | 2.00 ± 0.07 | 0.50 ± 0.07 | −2.00    |      | RHOB         | 2.66 ± 0.05 | 0.83 ± 0.05 | −2.47    |
| NHC-3 | GR           | 2.26 ± 0.02 | 0.63 ± 0.02 | −0.08    | HC-3 | GR           | 3.01 ± 0.09 | Error       | 0.28     |
|       | SP           | 1.85 ± 0.07 | 0.42 ± 0.07 | −0.35    |      | SP           | 2.93 ± 0.07 | 0.96 ± 0.07 | 0.11     |
|       | LLD          | 1.90 ± 0.09 | 0.45 ± 0.09 | −0.58    |      | LLD          | 2.96 ± 0.03 | 0.98 ± 0.03 | −0.32    |
|       | LLS          | 1.91 ± 0.11 | 0.45 ± 0.11 | −0.78    |      | LLS          | 3.02 ± 0.07 | Error       | −1.03    |
|       | MSFL         | 2.79 ± 0.18 | 0.89 ± 0.18 | −1.02    |      | MSFL         | 2.97 ± 0.11 | 0.98 ± 0.11 | −2.05    |
|       | NPHI         | 2.12 ± 0.02 | 0.56 ± 0.02 | −4.79    |      | NPHI         | 2.98 ± 0.04 | 0.99 ± 0.04 | −4.61    |
|       | RHOB         | 1.98 ± 0.07 | 0.49 ± 0.07 | −2.46    |      | RHOB         | 2.87 ± 0.03 | 0.93 ± 0.03 | −2.68    |
| NHC-4 | GR           | 2.23 ± 0.04 | 0.61 ± 0.04 | 0.89     | HC-4 | GR           | 2.89 ± 0.04 | 0.94 ± 0.04 | 0.74     |
|       | SP           | 1.86 ± 0.04 | 0.43 ± 0.04 | 0.18     |      | SP           | 2.87 ± 0.07 | 0.93 ± 0.07 | 0.11     |
|       | LLD          | 2.17 ± 0.03 | 0.58 ± 0.03 | 0.05     |      | LLD          | 2.89 ± 0.09 | 0.94 ± 0.09 | −1.07    |
|       | LLS          | 2.14 ± 0.13 | 0.57 ± 0.13 | −0.15    |      | LLS          | 2.99 ± 0.15 | 0.99 ± 0.15 | −0.97    |
|       | MSFL         | 1.93 ± 0.09 | 0.46 ± 0.09 | −0.25    |      | MSFL         | 2.99 ± 0.07 | 0.99 ± 0.07 | −1.44    |
|       | NPHI         | 2.06 ± 0.02 | 0.53 ± 0.02 | −4.44    |      | NPHI         | 2.99 ± 0.09 | 0.99 ± 0.09 | −4.89    |
|       | RHOB         | 1.86 ± 0.04 | 0.43 ± 0.04 | −1.96    |      | RHOB         | 2.74 ± 0.02 | 0.87 ± 0.02 | −2.87    |

![Figure 6: (a) Plot of log(σ) vs log(Scale) for GR log data from first-NHC zone (Well-3). The regression line is y = 1.8*x + 0.89 with R² = 0.99. (b) Plot of log(σ) vs log(Scale) for GR log data from first-NHC zone (Well-4). The regression line is y = 2.32*x + 0.07 with R² = 0.98. Both plots show a strong positive linear correlation between log(σ) and log(Scale).](f519a5be118c846f631c992412353fb9_img.jpg)

Figure 6: (a) Plot of log(σ) vs log(Scale) for GR log data from first-NHC zone (Well-3). The regression line is y = 1.8\*x + 0.89 with R² = 0.99. (b) Plot of log(σ) vs log(Scale) for GR log data from first-NHC zone (Well-4). The regression line is y = 2.32\*x + 0.07 with R² = 0.98. Both plots show a strong positive linear correlation between log(σ) and log(Scale).

Fig. 6 (a) Representation of WBFA for GR log data corresponding to first-NHC zone defined from well-3. Hence the slope is obtained from the log ( $\sigma$ ) versus scale ( $S$ ) plot. and (b) Representation of WBFA for GR log data corresponding to first-NHC zone defined from well-4. Hence the slope is obtained from the log ( $\sigma$ ) versus scale ( $S$ ) plot.

for SP log response  $H$  values associated with NHC zones varies from 0.42 to 0.53, whereas,  $H$  values associated with HC zones varies from 0.70 to 0.96. Again, for NPHI log response  $H$  values analogs to

NHC zones varies from 0.38 to 0.66; however,  $H$  values analogs to HC zones varies from 0.72 to 0.99. Lastly, for RHOB log response  $H$  values associated with NHC zones varies from 0.43 to 0.57, while  $H$

![Figure 7: (a) Representation of WBFA for GR log data corresponding to first-HC zone defined from well-7. (b) Representation of WBFA for GR log data corresponding to first-HC zone defined from well-13.](32cbf74724dd69f0603b24cf051810a9_img.jpg)

Figure 7 consists of two scatter plots, (a) and (b), showing the relationship between  $\log(\sigma)$  and  $\log(\text{Scale})$ . Both plots show a strong positive linear correlation with  $R^2 = 0.98$ .

(a)  $y = 2.64 * x + 0.85$ ,  $R^2 = 0.98$ . The x-axis is  $\log(\text{Scale})$  ranging from 0 to 0.7, and the y-axis is  $\log(\sigma)$  ranging from 0.5 to 3.

(b)  $y = 2.50 * x + 0.41$ ,  $R^2 = 0.98$ . The x-axis is  $\log(\text{Scale})$  ranging from 0 to 0.8, and the y-axis is  $\log(\sigma)$  ranging from 0 to 2.5.

Figure 7: (a) Representation of WBFA for GR log data corresponding to first-HC zone defined from well-7. (b) Representation of WBFA for GR log data corresponding to first-HC zone defined from well-13.

**Fig. 7** (a) Representation of WBFA for GR log data corresponding to first-HC zone defined from well-7. Hence the slope is obtained from the  $\log(\sigma)$  versus scale ( $S$ ) plot. (b) Representation of WBFA for GR log data corresponding to first-HC zone defined from well-13. Hence the slope is obtained from the  $\log(\sigma)$  versus scale ( $S$ ) plot.

![Figure 8: The range of D_WBFA values of conventional log responses are shown for HC and NHC zones.](ff2492be4fa814905acbad18f261b8a5_img.jpg)

Figure 8 is a horizontal bar chart showing the range of  $H$  variation for different log responses in HC and NHC zones. The x-axis represents  $H$  Variation, ranging from 0.4 to 1.0.

| Log Response      | Zone      | Approximate $H$ Variation Range |
|-------------------|-----------|---------------------------------|
| RHOB log response | HC zones  | 0.64 - 0.85                     |
| RHOB log response | NHC zones | 0.45 - 0.55                     |
| NPHI log response | HC zones  | 0.65 - 0.85                     |
| NPHI log response | NHC zones | 0.45 - 0.65                     |
| SP log response   | HC zones  | 0.65 - 0.85                     |
| SP log response   | NHC zones | 0.45 - 0.55                     |
| GR log response   | HC zones  | 0.65 - 0.85                     |
| GR log response   | NHC zones | 0.45 - 0.65                     |

Figure 8: The range of D\_WBFA values of conventional log responses are shown for HC and NHC zones.

**Fig. 8** The range of  $D_{WBFA}$  values of conventional log responses are shown for HC and NHC zones.

values associated with HC zones varies from 0.64 to 0.93.

The graphical representation of  $H$  value variation in HC and NHC zones corresponding to several log responses is shown in Fig. 8, where we are able to clearly demarcate the selected HC and NHC portions of the reservoir.

Therefore, from the above results, it can be clearly seen that the  $H$  values from HC zone for a particular log response (other than resistivity log) are higher in magnitude as compared to  $H$  value obtained from the same log response associated

with NHC zones. Thus, after application of WBFA on log data, Hurst exponent is found to be an important distinguishable parameter.

## 5. DISCUSSION AND CONCLUSIONS

In this study, WBFA method was applied in order to identify the hydrocarbon potential zone and lithology characterization at the Bhogpara oil field. The power law relationship between variance and scale was obtained to analyze the conventional wire-line log responses, which are associated with several potential and non-potential zones. Among them, only analyses for GR, SP, NPHI and RHOB logs are found to provide fruitful results.

Reference 19 reported that, zones with fractal dimension values lower than 0.9 correspond to sandstone channels, whereas values between 0.9 and 1.2 coincide with the inter-distributary deltaic shelf and value greater than 1.2 might be associated with zones of greater shale content.

In this paper, most of the potential zones are found to be having sandstone formation, whereas dry zones correspond to shale formations. In this paper, **Hurst exponent values higher than 0.75 are obtained for the potential zones in the case of GR log response**, whereas, **Hurst exponent values lower than 0.69 are obtained for the non-potential zone**. Similarly,  $H$  values higher than 0.70 obtained for the potential zones in the case of **SP log** response, whereas,  $H$  values lower than 0.53 for the non-potential zone. However,  $H$  values higher than 0.72 are obtained for the potential zones in the case of **NPHI log** response, whereas,  $H$  values lower than

0.66 for the non-potential zone. Lastly,  $H$  values higher than 0.64 are obtained for the potential zones in the case of RHOB log response, whereas  $H$  values lower than 0.57 for the non-potential zone. Thus, the obtained results are found to be consistent with the previous work of Ref. 19, i.e. WBFA analyses of a particular log response (GR, SP, NPHI, and RHOB) reflects, HC zones having lower  $H$  values as compared to NHC zones.

Here, in this study region most of the potential zones are situated in sandstone lithology, which are characterized with lower fractal dimension of self-affine nature. On the other hand, the non-potential zones are found to be in shale lithology, which leads to the higher fractal dimension of self-affine nature.

These results suggest that the fractal dimension obtained using WBFA can be used as derived attributes for the detection of the potential and non-potential zone as well as lithology characterization of the reservoir.

## ACKNOWLEDGMENTS

We are grateful to the Oil India Limited (OIL), Duliajan, Assam and GM, G&R of this corporation, who kindly allowed us to use their well-log data and special gratitude to Mr. S. Rath, former Director (Exploration) for his kind initiative to support the research with data of OIL. We would acknowledge anonymous reviewers and Prof. S. S. Manna, managing editor for their valuable constructive review, which has improved the manuscript substantially. The authors also gratefully acknowledge Ministry of Earth Science, Government of India for partly sponsoring this work (Project Number: MOES/P.O. (Seismo)/1(148)/2012).

## REFERENCES

1. A. John, L. W. Lake, C. Torres-Verdin and S. Srinivasan, Seismic facies identification and classification using simple statistic, in *Proceedings of SPE Annual Technical Conference and Exhibition*, SPE 96577, Dallas, Texas, 2005, pp. 984–990.
2. B. B. Mandelbrot, *Fractals* (W. H. Freeman, San Francisco, 1977).
3. M. V. Berry, Diffractals, *J. Phys. A: Math. Gen.* **2**(6) (1979) 781–797.
4. P. Kumar and E. Fufoula-Georgiou, *Wavelet Analysis in Geophysics*, eds. E. Fufoula-Georgiou and P. Kumar, Vol. 4 (Academic Press, 1994), pp. 1–43.
5. O. Rioul and M. Vetterli, Wavelets and signal processing, *IEEE Sig. Proc. Mag.* **8**(4) (1991) 14–38.
6. I. Simonsen, A. Hanesn and O. M. Nes, Determination of the Hurst exponent by use of wavelet transform, *Phys. Rev. E* **58** (1998) 2779–2787.
7. A. Arneodo, E. Bacry and J. F. Muzy, The thermodynamics of fractals revisited with wavelets, *Physica A* **213** (1995) 232–275.
8. M. Akay, Wavelets in biomedical engineering, *Ann. Biomed. Eng.* **23**(5) (1995) 531–542.
9. J. R. Jimenez, A. Peinado and R. J. Michelena, Facies recognition using wavelet-based fractal analysis on compressed seismic data, in *Proceedings of the 69th Annual International Meeting*, Society of Exploration Geophysicists, Houston, Texas, 1999, pp. 1922–1925.
10. D. L. Turcotte, *Fractals and Chaos in Geology and Geophysics*, 2nd edn. (Cambridge University Press, New York, 2007), p. 398.
11. L. Aliouane, S. A. Ouadfeul and A. Boudella, Fractal analysis based on the continuous wavelet transform and lithofacies classification from well-logs data using the self-organizing map neural network, *Arab J. Geosci.* **6** (2013) 1681–1691.
12. F. J. Herrmann, A scaling medium representation, a discussion on well-logs, fractals and waves, Ph.D. thesis, Delft University of Technology, Delft, The Netherlands (1997), p. 315.
13. R. D. Arizabal, K. Oleschko, G. Ronquillo and E. Cedillo-Pardo, Fractal and cumulative trace analysis of wire line logs from a well in a naturally fractured limestone of wire-line logs from a well in a naturally fractured limestone reservoir in the Gulf of Mexico, *Geofisica Int.* **43**(3) (2004) 467–476.
14. R. Polikar, The story of wavelets, in *Physics and Modern Topics in Mechanical and Electrical Engineering*, ed. N. Mastorakis (World Scientific and Engineering Society Press, Greece, 1999), pp. 192–197.
15. M. Misiti, Y. Misiti, G. Oppenheim and J. M. Poggi, *Wavelet Toolbox for Use with MATLAB User's Guide* (The Math Works, Natick, MA, USA, 2000), p. 572.
16. M. Sekine, T. Tamura, M. Akay, T. Fujimoto, T. Togawa and Y. Fukui, Discrimination of walking patterns using wavelet-based fractal analysis, *IEEE Trans. Neural Syst. Rehabil. Eng.* **10**(3) (2002) 188–196.
17. O. Serra, *Fundamentals of Well-Log Interpretation-1. Acquisition of Logging Data* (Elsevier, Amsterdam, 1984).

18. Schlumberger, *Log Interpretation Principles/Applications* (Schlumberger Educational Services, Houston, 1989).
19. M. L'opez and M. Aldana, Facies recognition using wavelet based fractal analysis and waveform classifier at the Oritupano-A Filed, Venezuela, *Nonlinear Process. Geophys.* **14** (2007) 325–335.
20. B. Mukherjee, V. Srivhardhan and P. N. S. Roy, Identification of formation interfaces by using wavelet and Fourier transforms, *J. Appl. Geophys.* **128** (2016) 140–149.