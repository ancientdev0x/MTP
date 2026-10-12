

# ON THE USE OF SPECTRAL METHODS FOR THE DETERMINATION OF FRACTAL DIMENSION

S. E. Hough

Lamont-Doherty Geological Observatory of Columbia University, Palisades, NY

**Abstract.** This paper discusses the use of fractal theory for quantitative analysis of profiles from two-dimensional surfaces. The theoretical relationship between spectral parameters and fractal dimension is examined, including the conditions under which the derived relationship between spectral parameters and fractal dimension by Voss (1985) is valid, and the limitations in making inferences from spectral parameters. Applications of fractal theory to geophysical data are also discussed. In particular, it is shown that an amplitude spectrum with a decay corresponding to a fractal dimension of 1.5 can result from the concatenation of time series with decays corresponding to different fractal dimensions. It has been shown that the spectral density of a fractal distribution will be characterized by a power-law decay, but this paper illustrates that a power-law decay is not sufficient to identify a fractal distribution. Although this paper discusses applications to the study of Earth topography, the results are applicable to the study of any one-dimensional profile.

## Introduction

Although plate-tectonics provides a comprehensive view of large-scale tectonic processes and geological structures, the formidable complexity of topography has previously hindered efforts to understand the statistical character of Earth topography in any generality. Since Mandelbrot (1967) first introduced the term fractal, many researchers in Earth sciences have looked to fractal theory to provide a framework for quantifying spatial characteristics of topography, faulting, etc. The well-known scale-invariance of many geological and geophysical phenomena suggest that it is appropriate to model observations with a fractal distribution (Turcotte, 1988). The usefulness of interpreting geophysical observations in terms of fractal distribution goes beyond a simple recharacterization of observations because it sets the stage for development of new techniques to understand the statistical nature of topography and other geophysical processes. While details of the geology of individual regions can be understood through conventional geological and geophysical methods, focusing on the spectral and statistical character of topography rather than the spatial details provides a context from which individual pieces can be viewed as part of a larger picture.

As strictly defined, a self-affine fractal distribution describes phenomena which are continuous but not differentiable and correlated over many length scales. A profile is self-similar if its statistical properties are not changed when the profile is decimated or when parts of the profile are enlarged. Mandelbrot (1983) introduced the term self-affine to describe distributions whose statistical properties are unchanged after enlargement only after the  $x$  and  $y$  axes have been rescaled by different proportions.

## Spectral and Fractal Theory

Fractal analysis has been used to look at sea-floor and continental topography (e.g. Sayles and Thomas, 1978;

Berry and Hannay, 1978; Bell, 1975; Fox and Hayes, 1985; Brown and Scholz, 1985; Malinverno, 1988; Gilbert, 1989; Gilbert and Malinverno, 1989; Goff and Jordon, 1989a). A method of relating the fractal dimension,  $D$ , to quantities that can be measured from discrete data is essential to applications of fractal theory. Voss (1985) relates  $D$  to properties of the power spectral density,  $S(f)$ , the 2-point autocorrelation,  $G(\tau)$ , and to the mean square increments,  $V_l(f)$  of a function. These are properties which can be estimated from data, although the strict definition of spectral density must be extended to non-stationary functions (Voss, 1985; Mandelbrot and Van Ness, 1968).

As discussed by Voss (1985), a function  $z(t)$  will have a Fourier transform for  $0 < t < T$  given by

$$Z(f, T) = \frac{1}{T} \int_0^T z(t) e^{-2\pi i f t} dt \quad (1)$$

and a spectral density of

$$S(f) = T |Z(f, T)|^2 \quad T \rightarrow \infty \quad (2)$$

The two-point autocorrelation is given by

$$G(\tau) = \langle z(t) z(t+\tau) \rangle - \langle z(t) \rangle^2 \quad (3)$$

where  $\langle \rangle$  denotes expected value.  $G(\tau)$  is related to the mean-square increments by

$$M_l(\tau) = \langle |z(t+\tau) - z(t)|^2 \rangle = 2[\langle z^2 \rangle - \langle z \rangle^2] - 2G(\tau) \quad (4)$$

In the case of a random, stationary process,  $G(\tau)$  can be related to the spectral density by the Wiener-Khinchine relation,

$$G(\tau) = \int_0^\infty S(f) \cos(2\pi f t) df \quad (5)$$

Because the mean-square increments of a fractal distribution can be related to the fractal dimension (Voss, 1985), equations (1)-(5) have been used to relate spectral parameters to fractal parameters. The Wiener-Khinchine relation must be extended to non-stationary signals (Voss, 1985; Mandelbrot and Van Ness, 1968). It will be argued later that this extension is not, in fact, valid. If one assumes a power spectrum with power-law form,  $S(f) \propto f^{-\beta}$ , then

$$D = \frac{5 - \beta}{2} \quad (6)$$

for a two-dimensional profile (Berry and Lewis, 1980). As defined, estimates of  $D$  from equation (6) are not necessarily consistent with the fractal (Hausdorff) dimension. Because  $D$  for a profile must lie between 1 (completely differentiable) to 2 (so rough as to fill up all of 2-dimensional space),  $\beta$  is apparently constrained to be between 1 and 3. Although equation (6) has been applied with success to real data, the derivation of (6) given by Voss (1985) is incomplete. Most fundamentally, once the complex Fourier transform is reduced to the spectral density in equation (2), then all phase information is lost. Any results from subsequent derivations will be valid if and only if an independent verification of random phase is demonstrated. Even given random phase, the derivation is further flawed when the Wiener-Khinchine relationship is extended to apply to non-random processes. This paper will discuss the validity of equation (6) in light of these concerns, as well as the "paradox" of  $\beta > 3$ .

Copyright 1989 by the American Geophysical Union.

Paper number 89GL00805.  
0094-8276/89/89GL-00805\$03.00

### Spectral Density and Autocorrelation

Voss (1985) states that that equation (5) can be used to obtain  $G(\tau) \propto \tau^{\beta-1}$ . However, this direct calculation is only valid for  $0 < \beta < 1$ . In fact, equation (5) becomes infinite when  $\beta$  is larger than one because the singularity at the origin becomes stronger than a simple pole (e.g. Marsden, 1973). But any real data set is integrated from a discrete minimum frequency,  $f_{min}$ . Replacing the lower limit of integration and letting  $x = 2\pi f\tau$ , equation (5) becomes

$$G(\tau) = (2\pi\tau^{\beta-1}) \int_{x_{min}}^{\infty} \frac{1}{x\beta} \cos x dx = (2\pi\tau^{\beta-1}) I(x) \quad (7)$$

Thus  $G(\tau)$  will be proportional to  $\tau^{\beta-1}$  as long as  $I(x)$  is finite and not dependent on  $\tau$ .  $I(x)$  can be integrated by parts  $n$  times to give equations of the following form

$$I(x) = \frac{1}{1-\beta} \left[ \frac{\cos(x)}{x^{\beta-1}} + \frac{1}{2-\beta} \left[ \frac{\sin x}{x^{\beta-2}} - \frac{1}{3-\beta} \left[ \frac{\cos(x)}{x^{\beta-3}} - \dots - \int_{x_{min}}^{\infty} \frac{\sin(x)}{x^{\beta-3}} \right] \right] \right] \quad (8)$$

until  $\beta-n$  lies between 0 and 1. The integrated terms in equation (8) are evaluated from  $x_{min}$  to  $\infty$ . Clearly, these terms are zero at the upper limit. At the lower limit,  $x_{min} = 2\pi\tau_{min}f_{min}$ . If  $z(t)$  is sampled at  $\delta t$ ,  $f_{min}$  will be given by  $1/(\delta t * n)$ , where  $n$  is the number of points in the time series. Since  $\tau_{min}$  is just given by  $\delta t$ , we have

$$x_{min} = 2\pi \left( \frac{1}{(n\delta t)} \right) (\delta t) = \frac{2\pi}{n} \quad (9)$$

Thus the largest of the integrated terms goes as  $n^{\beta-1}$ , which is finite and independent of  $\tau$ . The remaining integral in equation (8) will either be given by

$$\int_{x_{min}}^{\infty} \frac{\cos(x)}{x^{\beta-n}} dx \quad 0 < \beta-n < 1 \quad (10)$$

or by the same equation with  $\sin(x)$  replacing  $\cos(x)$ . Because  $x_{min}$  is independent of  $\tau$  and because

$$\int_{x_{min}}^{\infty} \frac{\cos(x)}{x^{\beta-n}} dx < \int_0^{\infty} \frac{\cos(x)}{x^{\beta-n}} dx = \Gamma(j) \cos \left[ \frac{(j)\pi}{2} \right] \quad (11)$$

(where  $j=1+n-\beta$ ) then equation (10) is also finite and independent of  $\tau_{min}$ . The same argument holds when  $\cos(x)$  is replaced by  $\sin(x)$ . Thus the result  $G(\tau) \propto \tau^{\beta-1}$  can be extended for discrete time series to  $1 < \beta < 3$ . This same result for 1, 2, and 3-dimensional spectra is found by Andrews (1981), although his paper does not examine rigorously the conditions of convergence of equations of the form of equation (7).

### The "Paradox" of $\beta > 3$

If  $G(\tau) \propto \tau^{\beta-1}$ , then the mean square increments of  $z(t)$ , given by equation (4), are also proportional to  $\tau^{\beta-1}$ . If  $\beta > 3$ , the mean-square increments are twice differentiable near the origin and the function,  $z(t)$ , is itself differentiable (Journel and Huijbrechts, 1978). Thus  $\beta > 3$  does not present the mathematical paradox of  $D < 1$  as implied by equation (5). Rather,  $\beta > 3$  implies  $D = 1$ ; that the function is differentiable. Although the large class of continuous, differentiable functions varies considerably in the degree of what is non-rigorously thought of as wiggliness, the fractal dimension, as defined, cannot distinguish between the character of any function in this class.

The breakdown of equation (4) is suggested by numerical results given by Malinverno (1989) and explained by Brown and Scholz (1985) by examining the second moment of the power spectrum. Malinverno (1989) compares the fractal dimension estimated from spectral slope with  $D$  determined from the behavior of the mean-square increments at short range, and finds that the two estimates

![Figure 1a: Three vertically offset time series plots showing amplitude versus time. The x-axis is labeled 'Time' with values from 2 to 1102. The y-axis is labeled 'Amplitude' with values from -1 to 8. The three series show oscillatory behavior with increasing frequency over time.](0d40c16595b159eb7c919bf9a475d4c6_img.jpg)

Figure 1a: Three vertically offset time series plots showing amplitude versus time. The x-axis is labeled 'Time' with values from 2 to 1102. The y-axis is labeled 'Amplitude' with values from -1 to 8. The three series show oscillatory behavior with increasing frequency over time.

Fig. 1a. Time (or space) series generated by scaling sine waves with differing functions of time (or space). Three series are offset vertically for clarity.

are equal only for  $D=1.5$ ; they are slightly different for all other values of  $D$  between 1 and 2. This illustrates the previously-mentioned problem with extensions of the Wiener-Khinchine relation: Given random phase and  $D=1.5$ , the profile is a random walk, and equation (5) is valid. For other values of  $D$ , however, then even with random phase, then a profile or time series is not a random process and there is no justification for the use of equation (5). Numerical results of Malinverno (1989) and Fox (1989) suggest, however, that for  $1 < \beta < 3$ , equation (6) can be a reasonable approximation.

## Application to Analysis of Data

The notion that a function with a specified amplitude spectrum will be critically dependent on its phase spectrum is by no means new, but the extensive utilization of equations (2)-(6) illustrates that this point has not been consistently appreciated. To present a few simple illustrations, one can construct time series with specified amplitude spectra and distinctly non-random phase. Figure 1 shows functions made up of sine waves with increasing period.

![Figure 1b: A log-log plot of amplitude spectrum versus frequency. The x-axis is labeled 'log(frequency)' with values from -2.0 to -1.0. The y-axis is labeled 'log(amplitude spectrum)' with values from -4.9 to 1.1. The plot shows three downward-sloping lines representing the amplitude spectra of the time series in Figure 1a.](e86cabf941a88f29766cc50abf162fc4_img.jpg)

Figure 1b: A log-log plot of amplitude spectrum versus frequency. The x-axis is labeled 'log(frequency)' with values from -2.0 to -1.0. The y-axis is labeled 'log(amplitude spectrum)' with values from -4.9 to 1.1. The plot shows three downward-sloping lines representing the amplitude spectra of the time series in Figure 1a.

Fig. 1b. Amplitude spectra of the time series shown in figure 1a. The spectra are shown for frequencies corresponding to the frequency range of the sine waves in figure 1a, roughly 0.01 Hz to 0.1 Hz

One can obtain power spectral amplitudes with  $S(f) \propto f^{-\beta}$  behavior over the frequency bands corresponding to the periods in the sine waves. Depending on how the amplitudes are scaled,  $\beta$  can take on a range of values. Topographic or bathymetric data sets are unlikely to look anything like the curves in figure 1, but processes such as folding could produce features with non-random phase. The potential danger of computing spectra from non-stationary profiles

was recognized by Fox and Hayes (1985) who showed that, while a spectrum of a long bathymetric profile crossing several "statistically homogeneous provinces" corresponds to  $D = 1.5$ , spectral slopes taken from individual quasi-stationary profiles give a range of spectral slope that generally do not correspond to  $D$  of 1.5 (Figure 2). Numerical studies by Fox (1989) also suggest a general tendency of long non-stationary profiles to tend towards a "self-similar" model. Fox and Hayes (1985) make only passing reference to interpretation in terms of fractal distribution. It is clear from the behavior of the individual profiles that it would be inappropriate to interpret  $D$  from the long profile as implying self-affinity because in that case, any part of the long profile would have the same statistical properties as any other.

The results of Fox and Hayes (1985) and Fox (1989) suggest that a fractal dimension of 1.5 might, in fact, be a limiting value obtained by summing time series with different fractal dimensions. In fact, if the time series shown in figure 1a are concatenated (figure 3a), the amplitude spectrum has a decay very close to  $\beta = 2$ , or  $D = 1.5$  over the frequency range of the sine waves (figure 3b). Sayles and Thomas (1978) argue that a  $1/f^2$  spectrum is the result of a central limit theorem. However, what they show is that this spectrum results from a fractal distribution. A proof that results such as those shown in figure 3b are the result of a limit theorem requires the consideration of a sum of adjacent time series, each of which has an amplitude given by  $1/f^\beta$ , where  $\beta$  ranges between 1 and 3 and in part of a specified distribution. If a time series,  $z(t)$  is created by concatenating  $n$  time series,  $z_i(t)$ , each of which has a spectrum given by  $1/f^\beta$ , then

![Figure 3a: A plot of amplitude versus distance. The x-axis is labeled 'distance' and ranges from 0 to 3000. The y-axis is labeled 'amplitude' and ranges from -4 to 0. The plot shows a series of high-frequency oscillations that decrease in amplitude as distance increases, with a noticeable change in slope around distance 1000.](af191c691aa1282801a350dbb14c7925_img.jpg)

Figure 3a: A plot of amplitude versus distance. The x-axis is labeled 'distance' and ranges from 0 to 3000. The y-axis is labeled 'amplitude' and ranges from -4 to 0. The plot shows a series of high-frequency oscillations that decrease in amplitude as distance increases, with a noticeable change in slope around distance 1000.

Figure 3a. Series generated by the concatenation of the three series' shown in figure 1a.

$$z(t) = \sum_{i=1}^n (H(t-t_i) - H(t-t_{i-1}))z_i(t) \quad (12)$$

and the Fourier transform of  $z(t)$ ,  $S(f)$ , is given by

$$S(f) = \int_{-\infty}^{\infty} \sum_{i=1}^n (H(t-t_i) - H(t-t_{i-1}))z_i(t) e^{2\pi i f t} dt \quad (13)$$

where  $H(t)$  is the heavyside step function. Interchanging the order of integration and summation, and noting that the effect of the boxcar functions is to change the integration limits from  $\pm\infty$  to  $t_{i-1}, t_i$ . Ignoring windowing effects, one obtains,

$$S(f) \rightarrow \sum_{i=1}^n \frac{1}{f^{\beta_i}} \quad (14)$$

If  $\beta_i$  are given by  $m \pm \sigma_i$ , then

$$S(f) = \frac{\sum_{i=1}^n \frac{((n-1)m + \sum_i (1-\delta_i)\sigma_i)}{f^{(nm + \sum_i \sigma_i)}}}{f} \quad (15)$$

![Figure 2: A log-log plot of normalized amplitude versus frequency. The x-axis is labeled 'FREQUENCY (CYCLES/KILOMETER)' and ranges from 10^-2 to 10^1. The y-axis is labeled 'NORMALIZED AMPLITUDE (KILOMETERS)' and ranges from 10^-6 to 10^1. The plot shows a series of data points with several straight lines of different slopes superimposed, representing different spectral slopes.](ed14725db41dc9fb8e9460b1478f8366_img.jpg)

Figure 2: A log-log plot of normalized amplitude versus frequency. The x-axis is labeled 'FREQUENCY (CYCLES/KILOMETER)' and ranges from 10^-2 to 10^1. The y-axis is labeled 'NORMALIZED AMPLITUDE (KILOMETERS)' and ranges from 10^-6 to 10^1. The plot shows a series of data points with several straight lines of different slopes superimposed, representing different spectral slopes.

Fig. 2. Amplitude spectrum of long bathymetric profile extending almost 500 km from the Oregon coast. Superimposed line has slope corresponding to  $D$  of 1.5. Also shown are spectral slopes from individual segments which Fox and Hayes (1985) identify as representing quasi-stationary provinces on the seafloor. Reprinted from Fox and Hayes (1985).

![Figure 3b: A log-log plot of log(amplitude spectrum) versus log(frequency). The x-axis is labeled 'log(frequency)' and ranges from -2.0 to -1.0. The y-axis is labeled 'log(amplitude spectrum)' and ranges from -4.0 to 1.0. The plot shows a series of data points with a straight line of slope -2.0 superimposed, indicating a 1/f^2 fall-off.](de10b5831c09191aadec04dfe0f9e7c3_img.jpg)

Figure 3b: A log-log plot of log(amplitude spectrum) versus log(frequency). The x-axis is labeled 'log(frequency)' and ranges from -2.0 to -1.0. The y-axis is labeled 'log(amplitude spectrum)' and ranges from -4.0 to 1.0. The plot shows a series of data points with a straight line of slope -2.0 superimposed, indicating a 1/f^2 fall-off.

Figure 3b Amplitude spectrum of the concatenated time series shown in figure 3a. Straight line shows a  $1/f^2$  fall-off between 0.01 Hz and 0.1 Hz.

If the sum of  $\sigma_i$  averages to zero, then

$$S(f) \rightarrow \frac{nf^{(n-1)m}}{f^{nm}} = \frac{n}{f^m} \quad (16)$$

Thus a  $1/f^2$  spectrum can result from a simple averaging process. It should be noted that the summed segments here are assumed to have consistent amplitudes. If one scales the amplitude of the individual segments differently, then the largest amplitude segments will dominate the spectrum of the concatenated time series.

A self-affine or self-similar fractal distribution is characterized by three essential characteristics: 1) It must have appropriate correlation over many length scales, 2) It must be continuous but not differentiable, and 3) It must have random phase. Criteria (1) can be tested by examining the behaviour of the amplitude spectrum, although Gilbert (1988) notes that care must be taken in making inferences from topographic data because data processing can affect spectral behaviour. The amplitude spectrum can also be used to determine whether or not a profile is differentiable, since a differentiable profile will have  $\beta > 3$ . Testing for random phase can be accomplished by computing spectral parameters within a moving window within the time series, a "split moving window" method (Malinverno, 1988; Webster, 1973; Fox and Hayes, 1985; Goff and Jordan, 1989b). This type of test identifies boundaries between statistically homogeneous segments by computing spectra from a specified window length which is moved across the profile. Malinverno (1989) shows that statistically distinct segments can be identified by changes in spectrum slope and intercept.

## Conclusions

This paper has discussed the applicability of fractal theory to the analysis of geophysical, generally topographic, data. The theoretical relation between spectral parameters to fractal dimension (Voss, 1985) is discussed. While theoretical limitations are noted, it is argued that the results of Voss (1985) are good approximations under certain circumstances. The usefulness of the concepts of fractal distributions for the analysis of data, beyond recharacterization of observations, has been demonstrated in the analysis of topographic data. Fox and Hayes (1985), Malinverno (1989), and Goff and Jordan (1989b) present ways to identify distinct portions of the seafloor, and Malinverno and Gilbert (1989) interprets observed fractal dimensions in terms of a fractal faulting process. The elegant simplicity of fractal analysis is appealing, as is the recognition that universal physical principles appear to control the complexities of diverse types of physical and biological systems. What is elegant and attractive is not, however, necessarily strictly applicable. Studies of topography done by Brown and Scholz (1985), Gilbert (1989), and Goff and Jordan (1989b) suggest that spectra of topographic profiles do not obey a strict power-law decay. And, as discussed in this paper, the requirement of power-law decay of a spectrum is only a necessary, not a sufficient, condition for identifying a fractal distribution. Several researchers have combined data from different regions to form a composite spectrum with a  $1/f^2$  decay and concluded that this demonstrates self-affinity of Earth topography (Sayles and Thomas, 1978; Turcotte, 1989). Results from this paper demonstrate that conclusions about Earth topography as a whole are premature, and that while statistically homogeneous provinces may be described by self-similar or self-affine distributions, analysis of topographic data will permit inferences about geological processes only if careful studies are made in limited geographical regions.

**Acknowledgments** The author acknowledges helpful discussions with Lewis Gilbert, Alberto Malinverno, and Chris Scholz; and thoughtful reviews by Bill Menke, Chris

Fox, and two anonymous reviewers. Work was supported by grants NCEER 87-1302 and 88-1302. Lamont-Doherty Geological Observatory contribution number 4467.

## References

- Andrews, D.J., A stochastic fault model, 2. Time dependent case, *J. Geophys. Res.* **86**, 10821-10834, 1981.
- Bell, T.H., Statistical features of sea-floor topography, *Deep-Sea Res.* **22**, 883-892, 1975.
- Berry, M.V. and J.H. Hannay, Topography of random surfaces, *Nature*, **273**, 573, 1978.
- Berry, M.V. and Z.V. Lewis, On the Wierstrass-Mandelbrot fractal function, *Proc. R. Soc. Lond. A*, **370**, 459-484, 1980.
- Brown, S.R., and C.H. Scholz, Broad bandwidth study of the topography of natural rock surfaces, *J. Geophys. Res.* **90**, 12575-12582, 1985.
- Fox, C.G. and D.E. Hayes, Quantitative methods for analyzing the roughness of the seafloor, *Rev. Geophys. Space Phys.* **23**, 1-48, 1985.
- Fox, C.G., Empirically derived relationships between fractal dimension and power law frequency spectra, *Pure Applied Geophys.* **131**, 1-29, 1989.
- Gilbert, L.E., Are topographic data sets fractal?, *Pure Applied Geophys.*, in press.
- Gilbert, L.E. and A. Malinverno, A characterization of the spectral density of residual ocean floor topography, *Geophys. Res. Lett.* **15**, 1401-1404, 1988.
- Goff, J.A., and T.H. Jordan, Stochastic modeling of seafloor morphology: A parameterized Gaussian model, *Geophys. Res. Lett.* **16**, 45-48, 1989a.
- Goff, and T. Jordan, Stochastic modeling of seafloor morphology: Resolution of topographic parameters by Sea Beam data, submitted to *IEEE J. Oceanic Engineering*, 1989b.
- Journel, A.G. and C.J. Huijbrechts, *Mining Geostatistics*, Academic Press, New York, 1978.
- Malinverno, A. (1989) On the segmentation of topographic profiles of the sea-floor, in prep.
- Malinverno, A. and L.E. Gilbert, A stochastic model for the creation of ocean floor topography at a slow-spreading center, *J. Geophys. Res.*, in press, 1989.
- Mandelbrot, B.B., How long is the coastline of Britain? Statistical self-similarity and fractional dimension, *Science*, **156**, 636-638, 1967.
- Mandelbrot, B.B. and J.W. Van Ness, Fractional Brownian motions, fractional noises, and applications, *SIAM Review*, **10**, 422-437, 1968.
- Mandelbrot, B.B., *The Fractal Geometry of nature*, W.H. Freeman and Company, New York, 1983.
- Marsden, J.D., *Basic Complex Analysis*, W.H. Freeman and Co., San Francisco, 1973.
- Sayles, R.S. and T.R. Thomas, Surface topography as a non stationary random process, *Nature*, **271**, 431-434, 1978.
- Turcotte, D.L., Fractals in geology and geophysics, unpublished manuscript, 1988.
- Voss, R.F., Random fractal forgeries, in *Fundamental Algorithms for Computer Graphics*, NATO ASI Series, vol. F17, edited by R.A. Earnshaw, pp. 805-835, Springer-Verlag, Berlin, 1985.
- Webster, R., Automatic soil-boundary location from transect data, *J. Math. Geology*, **5**, 27-37, 1973.

S.E. Hough, Lamont-Doherty Geological Observatory, Palisades, NY 10964.

(Received March 7, 1989;  
revised April 20, 1989;  
Accepted April 20, 1989)