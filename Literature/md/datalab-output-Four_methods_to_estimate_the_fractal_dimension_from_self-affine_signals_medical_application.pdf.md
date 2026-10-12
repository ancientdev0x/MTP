

# Four Methods to Estimate the Fractal Dimension from Self-Affine Signals

Hans E. Schepers  
Max Planck Institute

Johannes H.G.M. van Beek  
Physiology Laboratory  
The Free University, Amsterdam

James B. Bassingthwaite  
Center for Bioengineering  
University of Washington

![A vertical strip on the left side of the page. The upper portion shows a dark, textured, and irregular surface, possibly a medical scan or a natural texture. The lower portion shows a Sierpinski triangle fractal, a well-known example of a self-affine geometric pattern, rendered in white lines on a black background.](5fb340ad68b0c71df0b56698b137e35b_img.jpg)

A vertical strip on the left side of the page. The upper portion shows a dark, textured, and irregular surface, possibly a medical scan or a natural texture. The lower portion shows a Sierpinski triangle fractal, a well-known example of a self-affine geometric pattern, rendered in white lines on a black background.

The analysis of a time series has a deep history. In medicine, waveforms showing repetitive patterns (ECG, EEG, vascular pressure pulses) were analyzed first in terms of the specifics of the pattern and its basis in the underlying physical processes. More general techniques such as Fourier analysis were also applicable and gave measures of the periodicity and of the relative power contributions over a range of frequencies. Such analyses showed that the periodicities were not exact. Exact periodicity of cardiovascular events is an abnormal phenomenon [1], presumably because biological control systems are multidimensional, low-gain, and remarkably redundant. They balance well without any set-points. Nonlinearity in biological control systems is evident and leads, in a natural way, to their examination as low-dimension, chaotic dynamical systems [2], wherein there is a fractal attractor. Such

systems operate within bounds and without apparent predictability.

Demonstrating the fractal or chaotic nature of a signal is valuable, for it provokes the development of new ways for discovering how the system works. It is in this spirit that we undertake to examine time series using one-dimensional approaches. Fractal systems (in time or space) have neighbor-to-neighbor correlation at all levels of scale. In spatial statistics, the variance of a local measure depends on the resolution of the measurement [3]. For instance, the variance of regional blood flow in the heart increases as the resolution of measurement is increased. In an experiment where the heart is divided into many sections for the measurement of the concentration of a flow-proportional marker (e.g., radioactive microspheres) in each of the sections [4], the relation between the resolution mass of observed tissue element,  $m$ , and the variance (Var) of regional blood flows is well described by a power law function:

$$\text{Var}(m) = \text{Var}(m_0) \left( \frac{m}{m_0} \right)^{2H-2} \quad (1)$$

where  $H$  is the Hurst coefficient,  $H = 2-D$ , and  $D$  is the fractal dimension lying between 1.0 and 2.0. The spatial distribution is considered to have fractal properties because it shows statistical

0739-5175/92/\$3.00©1992

June 1992

IEEE ENGINEERING IN MEDICINE AND BIOLOGY

57

self-similarity. Voss [5] showed that in a fractal system all of the moments of the distribution have the same power law slope. In our early analyses [6], we examined the relationship between the measure of variation (the coefficient of variation) and the resolution of the measurement. This was a simple one-dimensional spatial analysis which we label as RD analysis, where RD is the relative dispersion, i.e., the standard deviation divided by the mean.

The dependence of the variance of a variable on the resolution was also found by the same fractal analysis of a time series [6], for example, the velocity of blood cells passing through a small artery as a function of time. If a signal,  $y(t)$ , is divided into intervals of length,  $\Delta t$ , and the mean is calculated for each interval, one can also calculate the variance of these means; there will be a lower variance when the interval length is increased. The relationship between the variance and the sample time may fit a power law, and if so, the fractal dimension of the time series can be calculated by the same RD analysis as was used for a spatial measure.

In this article, we shall examine four methods for analyzing a one-dimensional time signal,  $y(t)$ . The first of these is our RD analysis. The others are correlation analysis, rescaled range analysis, and

## Relative dispersion, correlation, rescaled range, and Fourier analyses all yield the fractal dimension, D

power spectral analysis. All methods yield the fractal dimension, D.

When neighboring elements in a time series or a spatial distribution are positively correlated, the measured variance will drop less rapidly as the resolution is decreased. Based on this phenomenon, Bassingthwaighte and Beyer [7] reinvented the expression for the autocorrelogram (originally provided by Mandelbrot and van Ness [8]) from the relationship for covariances among neighboring units fulfilling Eq. 1. The one parameter of this function is the fractal dimension, and it can be es-

timated directly from an autocorrelogram (correlation analysis).

Another statistical measure from which the fractal dimension can be calculated is Hurst's rescaled range analysis [9, 10] for analyzing flows in rivers. The "range" is of the integral of deviations from the mean over an interval, and it is normalized by dividing by the standard deviation of the differences from the mean. Mandelbrot and Wallis published a series of papers was published on this analysis [11, 12, 13, 14, 15], showing that Hurst's method could be used to estimate the fractal dimension from a fractional Brownian noise. They modified the method by using the differences from a trend line, rather than differences from the mean.

The signals analyzed here are examples

of fractional Brownian noises; they are characterized by a specific power spectrum of the form  $S(f) = f^{-D}$ , where  $f$  is frequency. Thus Fourier analysis [5, 16] is the fourth procedure used to estimate the fractal dimension. The  $1/f$  noise, as it is frequently called, is common in nature, although the physical reason is not well understood. Recently, Bak et al. [18] proposed a general model for systems with a very high number of degrees of freedom, called "self-organized criticality," which accounts for both the occurrence of  $1/f$  noise and fractals. Fractional Brownian noises and spatial fractals are, respectively, the temporal and the spatial fingerprints of a system that has evolved towards a critical state.

Do these four procedures to estimate the fractal dimension provide the same answer? Are they equally accurate? To find out, we generated signals with a known fractal dimension ( $D = 1.1 - 1.9$ ), then used the four methods to estimate its value. The first problem is how to distinguish between the effects from the different signal generating algorithms, and the estimation methods. However, the estimation methods also perform better on long signals. The production of a truly fractal signal is itself a non-trivial exercise and may be as difficult as producing real random noise. So we must worry about the adequacy of the generating algorithms as well as the analysis algorithms. Some estimation procedures may require a very long signal, whereas others provide good results at shorter signal length. These four methods, however, are not exhaustive. The article by Fortin et al. in this issue [17] describes the use of a maximum likelihood estimator, another useful method.

The significance of D is that it describes, very compactly, the relation between the variance of the signal, and the time scale. No assumptions on the underlying system from which the signal was observed are made, and it is therefore a purely statistical tool. The fractal dimension estimated by these techniques from a time series is between one and two, i.e., for a one dimension function  $y(t)$ , the fractal D lies between the Euclidean dimension E (= 1) and E + 1. (This is not at all the same fractal dimension that one attempts to derive from an embedding or correlation analysis [2], where one seeks a measure related to the order of the set of underlying differential equations.) For our analysis,  $1 < D < 2$ ; values of D near 1 indicate high correlation or "memory" over time. (This can be seen, for example, in the nearest neighbor correlation coefficient  $r_1 = 2^{3-D} - 1$ .) For random signals,  $D = 1.5$  (Table 1).

We will test methods for estimating the fractal dimension of self-affine and self

Table 1  
D and H for Fractal Times Series

| Correlation | D             | H = 2 - D     |
|-------------|---------------|---------------|
| Positive    | $1 < D < 1.5$ | $1 > H > 0.5$ |
| Random      | 1.5           | 0.5           |
| Negative    | $1.5 < D < 2$ | $0.5 > H > 0$ |

similar curves. Self-affine curves repeat themselves only when the different axes are magnified by different factors, whereas self-similar curves use the same factor for each axis. Both a time series and a spatial distribution of local blood flows are classed as self affine, because the variable has units different from that of the axes [5]. Therefore, the standard methods of calculating the fractal dimension for spatial, self-similar fractal patterns (box-, divider- and similarity dimension) [19], require modification for the analysis of self-affine signals. The four methods described below can be used on either self-similar or self-affine signals.

## Generating a Fractal Signal

To generate a signal with a known fractal dimension, two algorithms were used which generate a fractional Brownian motion, fBm, with a parameter,  $H$ , that defines the fractal dimension of the signal. The well known ordinary Brownian motion, such as a random walk of diffusing particles, is a fractional Brownian motion with  $H = 0.5$ . The successive differences between points of an fBm are called a fractional Brownian noise, fBn. Because determining  $H$  or  $D$  from fBm is difficult [8, 16], the fBn is needed to estimate fractal dimension. White noise is the uncorrelated form of fBn, being the increments or successive steps from the normal Brownian motion. Fractional Brownian noise signals with positive autocorrelation have  $H > 0.5$ , whereas fBn signals with negative correlations have  $H < 0.5$ . The fBn is always a stationary signal, and while fBm is stationary over long times, its short term behavior appears non-stationary. Since "short" and "long" are relative, and the signal has statistically self-similar behavior, the overall stationarity may not be demonstrable. Mandelbrot and Wallis [11-15] presented a simple definition of the fBn's with spectral theory: white noise and all its repeated integrals and derivatives have a spectral density of the form  $1/f^{2\beta}$ , where  $f$  is the frequency, and  $\beta$  is an integer. Fractional Brownian noises are defined as having a spectral density of the same form, with  $\beta$  a non-integer fraction, hence the name fractional (Brownian) noise,  $\beta = 2H - 1$ . The fractal dimension relates to  $H$  as  $D = E + 1 - H$ , where  $E$  is the Euclidian dimension [5].

The spectral synthesis method (SSM) generates the signal by computing the backtransform of a Fourier spectrum of known form: the squared amplitude must be a power law function of the frequency. The method is described in some detail by Voss [5]. Saupe [20], in the same volume, gives a pseudocode outline of the program, which requires only a few lines. The phases are usually randomly drawn from

![Figure 1: Three plots related to fractional Brownian motion. (a) Top plot: fBm vs. numbered time (0 to 8192). The signal fluctuates around zero. (b) Bottom-left plot: fBm vs. time (0 to 256), a magnification of the first part of (a). (c) Bottom-right plot: fBn vs. time (0 to 256), showing the fractional Brownian noise signal.](a854aa286b14d26d27047ee5893ffaa7_img.jpg)

Figure 1: Three plots related to fractional Brownian motion. (a) Top plot: fBm vs. numbered time (0 to 8192). The signal fluctuates around zero. (b) Bottom-left plot: fBm vs. time (0 to 256), a magnification of the first part of (a). (c) Bottom-right plot: fBn vs. time (0 to 256), showing the fractional Brownian noise signal.

1. Fractional Brownian motion of  $H = 0.75$ ,  $N = 8192$ , created by the Spectral Synthesis method (a). Magnification of the first part of (a),  $N = 256$  (b). The corresponding fractional Brownian noise (c).

![Figure 2: Three log-log plots showing relative dispersion as a function of the number of data points averaged. The x-axis is log2(n) and the y-axis is log2(σ²). Three data series are shown for N = 512 (left), 8192 (middle), and 32768 (right). All three show a linear downward trend, indicating a power-law relationship.](9455ca65b9fc488df790769b0122628e_img.jpg)

Figure 2: Three log-log plots showing relative dispersion as a function of the number of data points averaged. The x-axis is log2(n) and the y-axis is log2(σ²). Three data series are shown for N = 512 (left), 8192 (middle), and 32768 (right). All three show a linear downward trend, indicating a power-law relationship.

2. Relative dispersion as a function of the number of data points averaged. The signals analyzed are fractional Brownian noises with  $H = 0.75$ , consisting of 512 (left), 8192 (middle) and 32768 (right) points (SSM algorithm). Estimated  $H = 0.726$ ,  $0.726$ , and  $0.733$ , respectively.

![Figure 3: Three plots showing the estimation of H using autocorrelation analysis. The x-axis is Number of units distance and the y-axis is Correlation Coefficient. Three data series are shown for N = 512 (left), 8192 (middle), and 32768 (right). All three show a decreasing correlation coefficient as distance increases, fitted with a power law.](e3921a931e5c1e184cf30effc70ded74_img.jpg)

Figure 3: Three plots showing the estimation of H using autocorrelation analysis. The x-axis is Number of units distance and the y-axis is Correlation Coefficient. Three data series are shown for N = 512 (left), 8192 (middle), and 32768 (right). All three show a decreasing correlation coefficient as distance increases, fitted with a power law.

3. Estimation of  $H$  in Eq. 6 (autocorrelation analysis). The signals analyzed are the same as in Fig. 2 using the SSM algorithm,  $N = 512$  (left), 8192 (middle) and 32768 (right). Estimated  $H$ :  $0.716$ ,  $0.743$ , and  $0.717$ , respectively.

a uniform distribution. An alternative method is presented by Osbourne and Provenzano [21]. The derivative of a fractal signal has the exponent of the power law function of the Fourier spectrum reduced by two, as compared to the

original signal. Thus, an fBn can also be directly computed from the power spectrum. Fractional Brownian noises with  $H$  near 1.0 are smooth, while those with  $H$  near 0.5 are rough. For other examples see Fortin, et al. [17]. Figure 1

shows an example of both an fBm and its derivative, fBm, with  $H = 0.75$ .

The successive random addition (SRA) algorithm of Saupe [20] generates an fBm as follows: a random displacement is added to the middle and to the ends of a straight line. Each half of the line is replaced by the connecting line between the new points. Each of the daughter line segments is then treated as in the first step, but with random displacements of lower variance, depending on the parameter  $H$ :

$$\text{Var}_i = \sigma_0^2 \frac{1-2^{2H-2}}{2^{2H}} \quad (2)$$

where  $\sigma_0^2$  is the variance in the first step, and the index,  $i$ , denotes the number of steps. In order to get the fractional Brownian noise that is required for all the estimation procedures, the differences of successive points in the fBm are taken.

## The Estimation Procedures Relative Dispersion Analysis

In spatial statistics, the relative dispersion (RD) analysis compares the variance of a variable as the measurement resolution increases [22]. The RD equals the standard deviation divided by the mean.

#### Relative dispersion analysis is well suited for long signals

In time series analysis, one starts by measuring, at the highest level of resolution, the variance of the signal over its whole time course. The next step is to average the signal over pairs of consecutive values, find the variance, and repeat for longer strings of values of  $y(t_i)$ . String length increasing geometrically, grouping by 2, 4, 8, etc., is efficient because pairs of averages are combined for a next iteration. When the signal is uncorrelated (white noise), with  $H = 0.5$ , one expects that the standard deviation, when

two consecutive values are averaged, is reduced by a factor of  $1/2^{0.5}$ , or when  $n$  consecutive values are averaged, by  $1/n^{0.5}$ . The mean remains the same. Now one will find that with a correlated fBm, and  $H$  not equal to 0.5, the SD will be proportional to  $n^{H-1}$ ,  $n$  being the bin size or the time resolution interval. By calculating the RD ( $\text{RD} = \text{SD}/\text{mean}$ ) for different bin sizes,  $n$ , and fitting the exponent of the power law function:

$$\text{RD} = \text{RD}_0 \left( \frac{n}{n_0} \right)^{H-1} \quad (3)$$

where  $\text{RD}_0$  is the RD for some reference bin size  $n_0$ , the fractal dimension (via  $H$ ) is easily computed. The whole of the data

set is used for each calculation of  $\text{RD}(n)$  at each level of resolution or number of pieces,  $n$ .

The exponent can best be estimated after a log-log transformation (Fig. 2):

$$\log(\text{RD}) = \log(\text{RD}_0) + (H-1)\log(n/n_0) \quad (4)$$

As can be seen from Fig. 2, the fit is a little improved when a longer signal is used. The RD analysis yields essentially the same results when only the first three or four points in the graph (i.e., the smallest bin sizes, 2, 4, 8 and 16) are used. With very large bin sizes, the number of bins is of course small and the measure of variance is less accurate. This relationship is an important advantage of the RD analysis, because especially in spatial statistics, signals may not be very long due to limited resolution and domain size.

### Correlation Analysis

Van Beek et al. [23] derived an equation for the correlation between measurements in adjacent units from the assumption that RD diminishes by a factor of  $2^{H-1}$  when two pieces (values in the time series) are lumped together, or are averaged (the bin size is doubled):

$$r_1 = 2^{2H-1} - 1 \quad (5)$$

The correlations between neighboring pieces are independent of the piece size, which is the reciprocal (approximately) of the number of units into which a domain has been divided. Bassingthwaite and Beyer [7] extended the formula to the autocorrelation coefficients between pieces which are separated by  $n-1$  intervening pieces:

$$r_n = \frac{(n+1)^{2H}}{2} - \frac{n+1}{2} - \sum_{i=1}^{n-1} (n-i+1)r_i \quad (6)$$

From this, they derived an expression  $r_n$ , that is not recursive, for all  $n > 0$ , integer or non-integer:

$$r_n = \frac{1}{2} / \ln-11^{2H} - 2\ln 2^{2H} + \ln + 11^{2H} / \quad (7)$$

In doing so, they rediscovered the relationship described by Mandelbrot and van Ness [8], and Mandelbrot [24], and used by others since. For example, Burrough [25, 26] used it for soil characterization, and Lundahl et al. [16] show its meaning and merit with respect to fractional Brownian motion. The relationship for  $H > 0.5$  for large  $n$  goes asymptotically to a power law relationship [27]:

![Figure 4: Three scatter plots showing the power in fBm as a function of frequency. The x-axis is log2 f (ranging from 0 to 15) and the y-axis is log2 |A|^2 (ranging from -20 to 10). The left plot (N=512) shows a steep negative slope. The middle plot (N=8192) shows a less steep negative slope. The right plot (N=32768) shows a very shallow negative slope, almost horizontal. All plots show a dense cloud of points with a clear downward trend that flattens out as frequency increases.](c7df38125cb41e915adc1787b6c3390a_img.jpg)

Figure 4: Three scatter plots showing the power in fBm as a function of frequency. The x-axis is log2 f (ranging from 0 to 15) and the y-axis is log2 |A|^2 (ranging from -20 to 10). The left plot (N=512) shows a steep negative slope. The middle plot (N=8192) shows a less steep negative slope. The right plot (N=32768) shows a very shallow negative slope, almost horizontal. All plots show a dense cloud of points with a clear downward trend that flattens out as frequency increases.

4. Power in fBm as a function of frequency. Estimation of  $H$  in Eq. 9  $|A|^2 \propto f^{-H}$  using spectral analysis. The signals are the same as those analyzed for Fig. 2 using SSM algorithm,  $N = 512$  (left), 8192 (middle) and 32768 (right). True  $H = 0.75$ . Estimated  $H = 0.802, 0.741$ , and  $0.756$  respectively.

$$\frac{r_n}{r_{n-1}} = \left( \frac{n}{n-1} \right)^{2H-2} \quad (8)$$

The slope is the same as that of Eq. 1, and the meanings now coalesce: when the variances are fractal, there is a defined degree of correlation and an extended correlation. This simple expression is quite good for  $n \geq 3$ , and  $H$  can be simply determined from the plot of  $\log r_n$  versus  $\log n$ .

We obtained a nonlinear fit of Eq. 7 to the data with the procedure GGOPT [28] from the National Simulation Resource, Center for Bioengineering, University of Washington, Seattle. The correlograms for the longer signals are much smoother than for the shorter ones. This can be seen in Fig. 3, where three plots are compared. With  $N = 512$  (left panel), the correlation curve is noisy, whereas for  $N = 8192$ , the noise is smaller, but the distant correlations are erroneously low. The error has almost disappeared with  $N = 32768$ .

The long time span over which correlation persists is very remarkable. The autocorrelogram tends very slowly to zero. For high  $H$  ( $= 0.5$  to  $1$ ), the correlations are positive and extend longer. Mandelbrot and Wallis [11 - 15] called this a long-term persistence. When the signal is a straight line, there is no decrease in the correlogram and  $H = 1$ . For  $H < 0.5$  the correlations are negative, which is termed anti-persistence. Examples of correlation versus separation are shown by Fortin, et al. [17].

For the estimation of  $H$  from the autocorrelogram, it is important that not too many correlation coefficients be used in the estimation procedure. With long separations, even minuscule degrees of random noise or measurement error will cause the estimate to be biased towards  $H = 0.5$  as shown by Lundahl et al. [16].

A further test of the self-affine nature of the signal using the autocorrelation function follows the style of the RD analysis. It is particularly useful for distinguishing a single fractal process from a multifractal. A true fractal will follow Eq. 7 for any chosen sample size. Therefore, the test is to group successive samples, take the mean of the groups, and repeat the calculation of  $r_n$ . Repeat this for groups of a few different sizes, e.g., of two, four, etc. points of the original signal. If different group sizes all give the same estimate of  $H$ , it is strong evidence of a fractal signal that is stationary over long times, given the context that the signal set is a finite sampling of an infinite and stationary signal.

### Fourier analysis

The power spectrum (the square of the amplitude from the Fourier transform) of a pure fractional Brownian motion is

![Figure 5: Estimation of H in Eq. 14 (R/S analysis). Three scatter plots showing log2(r/s) vs log2(N) for N=512, 8192, and 32768. The data points follow a linear trend with a positive slope, indicating a fractal signal.](bc04d002fc79e8a3637b1552ac3361e6_img.jpg)

Figure 5: Estimation of H in Eq. 14 (R/S analysis). Three scatter plots showing log2(r/s) vs log2(N) for N=512, 8192, and 32768. The data points follow a linear trend with a positive slope, indicating a fractal signal.

5. Estimation of  $H$  in Eq. 14 (R/S analysis). The signals analyzed are the same as in Figure 2 using SSM algorithm,  $N = 512$  (left),  $8192$  (middle) and  $32768$  (right). Estimated  $H =$

![Figure 6: Averaged values of estimated H from 10 signals. Six line plots showing estimated H vs synthesis method (SSM or SRA) for N=512, 8192, and 32768. The x-axis categories are RD, Corr, R/S, and Spectrum. A horizontal line at H=0.75 is shown in each panel.](1a6d75c94d3fd49936527eadd25e9278_img.jpg)

Figure 6: Averaged values of estimated H from 10 signals. Six line plots showing estimated H vs synthesis method (SSM or SRA) for N=512, 8192, and 32768. The x-axis categories are RD, Corr, R/S, and Spectrum. A horizontal line at H=0.75 is shown in each panel.

6. Averaged values of estimated  $H$  from 10 signals. Error bars denote  $\pm$  one standard deviation. The preset value of  $H$  is  $0.75$ , indicated by the horizontal line on each panel. The panel headings indicate the synthesis method (SSM or SRA) and the numbers of points,  $N$ . The abbreviations on the abscissa are RD = relative dispersion analysis; Cor = autocorrelation analysis; R/S = rescaled range analysis; Spectrum = Fourier analysis.

known to be described by a power law function [5]:

$$|A|^2 \approx \frac{1}{f^\beta} \quad (9)$$

where  $|A|$  is the magnitude of the spectral density at frequency  $f$ , with an exponent equal to  $\beta = 2H + 1$ . In general, fractal signals always have such a very broad spectrum. When the derivative is taken

from a fractal signal,  $\beta$  is reduced by two. Thus, for fractional Brownian noise,  $\text{fBn}$ ,  $\beta$  is expected to be:

$$\beta = 2H - 1 \quad (10)$$

Here again, a straight line is fitted from a log-log plot, and  $H$  is calculated from the slope  $\beta$ , as in the examples in Fig. 4. The influence for longer signals in the Fourier analysis is not clear from the individual plots, but the estimates are quite accurate even for shorter signals.

### Rescaled Range Analysis

Edwin Hurst [9, 10] a hydrology engineer, had a statistical problem when designing the Aswan dam on the Nile River. He wanted to know how high the dam should be to contain all incoming river water and provide a constant outflow. When the inflow of the dam is a stationary random variable, the water level of the lake is the integral of the differences of the inflow and the constant outflow. He took data on the annual flow in the Nile and other rivers, and computed the range,  $R(u)$ , defined as the maximum value minus the minimum value of the integral of the differences of the annual flow from the mean flow, divided by the standard deviation of the yearly inflow for different time spans ("time lag"  $u$ ), averaged at different starting times,  $t_0$ . He found that a power law relation between the quotient of the range  $R(t_0, u)$  and the standard deviation,  $S(u)$ , of the inflow and the time span  $u$  described the data very well:

$$\frac{R(u)}{S(u)} = u^H \quad (11)$$

where  $R/S$  is called the rescaled range. The longer time a dam should be able to hold all inflow, the higher it must be.

Mandelbrot and Wallis used Hurst's rescaled range analysis as an estimation procedure to estimate the fractal dimension of a signal [8, 11, 12, 13, 14, 15]. The quantity  $R(t_0, u)/S(t_0, u)$  is calculated for subsets of the data over intervals of time lag  $u$ , starting from each of many starting points,  $t_0$  separated by some interval,  $\Delta t > u$ , so that there are no overlapping subsets. The range is:

$$R(t_0, u) = \text{MAX} \{X(t_0, u)\} - \text{MIN} \{X(t_0, u)\} \quad (12)$$

where:

$$X(t_0, u) = \int_{t_0}^{t_0+u} [B(s) - \langle B(s) \rangle] ds \quad (13)$$

and  $\langle B(s) \rangle$  denotes the mean value of the fBn over the interval  $B(t_0, t_0+u)$ . The standard deviation  $S(t_0, u)$  is the standard

deviation of  $B(t)$  over the same interval. For a data set of  $N$  evenly spaced observations, there are  $N/(u/\Delta t)$  estimates of  $R/S$  obtainable from non-overlapping intervals of length  $u$ . We abbreviate  $R(t_0, u)/S(t_0, u)$  to  $R(u)/S(u)$ , which is a function of  $t_0$  and  $u$ , and plot the individual calculations for each interval length,  $u$ , in Fig. 5, giving the "pox plot" [11]. A straight line is fitted in the log-log plot:

$$\log[R(u)/S(u)] = c + H \log(u) \quad (14)$$

The individual points for a given  $u$  in Fig. 5 are calculated independently of each other, since there is no overlap between subsets. Using the GGOPT optimizer or a maximum likelihood estimator as used by Fortin et al. [17] gives a minimally biased estimate of  $H$ , which is better than fitting the means of  $R/S$  at each  $u$ .

The estimations from the  $R/S$  analysis depend on the way the subsets from the signal are taken to calculate the rescaled range. With longer signals, larger lags can be used, along with more points per lag.

#### Correlation and rescaled range analyses yield biased results under many circumstances

Also, the length of the shortest lag can be increased, which improves the fit further, as reported by Mandelbrot and Wallis [11-15].

## Results

In Fig. 6, the results are summarized for estimates obtained with the four methods for ten signals generated by the spectral synthesis method (SSM) and the successive random addition method (SRA) for  $H = 0.75$ . Several conclusions can be drawn from this

Figure. Except from the  $R/S$  analysis and the Fourier analysis, the estimates of  $H$  tend to be too low. Some of the deviation may be blamed on the synthesis algorithm. For instance, deviations from the preset value of  $H = 0.75$  with signals generated by the SSM algorithm are smaller than the deviations with the SRA algorithm (Figs 6a, 6b).

In general, estimates from the Fourier analysis come closest to the correct value of  $H = 0.75$ , and have a small standard deviation. The estimates from the RD and correlation analyses are low. The correlation estimates may be biased towards 0.5 because correlation coefficients over too

**Table 2**  
Estimates of  $H$  from  $y(f)$ , ten trials each; actual  $H = 0.75$

| Synthesis Algorithm | Analysis Method | Estimates of $H$ at different $N$ ( $\pm$ SD) |               |                |
|---------------------|-----------------|-----------------------------------------------|---------------|----------------|
|                     |                 | $N = 512$                                     | $N = 8192$    | $N = 32768$    |
| SSM                 | RD              | 0.652 (0.076)                                 | 0.735 (0.028) | 0.7043 (0.027) |
|                     | Cor             | 0.678 (0.036)                                 | 0.736 (0.018) | 0.724 (0.007)  |
|                     | R/S             | 0.736 (0.169)                                 | 0.778 (0.042) | 0.738 (0.032)  |
|                     | Spectrum        | 0.764 (0.042)                                 | 0.773 (0.013) | 0.770 (0.008)  |
| SRA                 | RD              | 0.639 (0.065)                                 | 0.698 (0.027) | 0.716 (0.033)  |
|                     | Cor             | 0.622 (0.057)                                 | 0.676 (0.023) | 0.696 (0.015)  |
|                     | R/S             | 0.727 (0.054)                                 | 0.740 (0.046) | 0.748 (0.047)  |
|                     | Spectrum        | 0.748 (0.033)                                 | 0.738 (0.018) | 0.742 (0.003)  |

large distances are taken into account. The mean of the estimations from the rescaled range analysis is fairly good, but the standard deviation is very large. The estimates from Fig. 6 are listed in Table 2.

The estimates of  $H$  obtained via these procedures are presented in Fig. 7 for signals with true values of  $H$  from 0.1 to 0.9. The Fourier analysis yields the best results (right lower panel). It is apparent that the correlation analysis yields estimates biased towards  $H = 0.5$ . The correlation estimates for high values of  $H$  are clearly improved when a longer signal is analyzed.

Estimates of the R/S analysis tend to be too high, but with a large standard deviation (Fig. 7, right upper panel). The RD analysis yields excellent results with 8192 points. Even with only 512 points, at  $H = 0.1$  and 0.3, the RD analysis provides almost correct values, underestimating at higher  $H$ .

An important difference between the correlation structure of signals generated by the SRA and SSM algorithm is shown in Fig. 8. The first 25 correlation coefficients of 10 signals for each algorithm are plotted along with Eq. 7 with  $H = 0.75$ . The SRA algorithm appears to produce a more nearly randomly structured signal, as the estimates tend toward 0.5 and therefore fall mostly below the expected correlation for  $H = 0.75$  (Fig. 8a). The values for the correlations are too low, and the scatter is large. The SSM produced signals whose autocorrelations are only a little below the model function equation, Eq. 7 (Fig. 8b).

## Discussion

A major problem of the work described above involves the question: "What is being tested, the estimation procedures by the signal generating algorithm, or the signal generating algorithm by the estimation procedures?" When a signal generating algorithm produces a signal with a different fractal dimension from the dimension corresponding to the parameter  $H$ , it cannot be expected that the estimation procedures will be unbiased with respect to the preset parameter value. But because the estimations were done on the same signals, it is still possible to determine which of the methods comes closest to the preset value, and the variances of the estimation procedures can be compared.

The variance of estimates from the R/S analysis is much larger than those of the other estimation procedures. This occurs because in the R/S analysis, the signal must be divided into several subintervals, which can be done in many ways. The results for the R/S analysis clearly depend on the number of subintervals (the number of points in Fig. 5 at each lag), the mini-

![Figure 7: Comparison of estimates of H from short (N = 512, dotted lines) and long (N = 8192, solid lines) signals from the different estimation procedures. The figure consists of four subplots: (a) Correlation, (b) R/S, (c) R/D, and (d) Spectrum. Each subplot shows 'estimated H' on the y-axis versus 'H signal' on the x-axis, both ranging from 0 to 1. In (a), the correlation analysis shows a bias towards 0.5, especially for short signals. In (b), the R/S analysis shows high estimates with large error bars. In (c), the R/D analysis shows estimates very close to the diagonal line. In (d), the spectral analysis shows the best results, with estimates very close to the diagonal line for both short and long signals.](84e2ac543ffc4145dc85b05a48ec62e3_img.jpg)

Figure 7: Comparison of estimates of H from short (N = 512, dotted lines) and long (N = 8192, solid lines) signals from the different estimation procedures. The figure consists of four subplots: (a) Correlation, (b) R/S, (c) R/D, and (d) Spectrum. Each subplot shows 'estimated H' on the y-axis versus 'H signal' on the x-axis, both ranging from 0 to 1. In (a), the correlation analysis shows a bias towards 0.5, especially for short signals. In (b), the R/S analysis shows high estimates with large error bars. In (c), the R/D analysis shows estimates very close to the diagonal line. In (d), the spectral analysis shows the best results, with estimates very close to the diagonal line for both short and long signals.

7. Comparison of estimates of  $H$  from short ( $N = 512$ , dotted lines) and long ( $N = 8192$ , solid lines) signals from the different estimation procedures. The error bars denote standard deviations of estimates of  $H$  from ten signals at each  $H$ . Signals were generated by the SSM algorithm. Correlation analysis (a); R/S analysis (b); RD analysis (c); spectral analysis (d).

![Figure 8: Autocorrelations r_n versus n calculated for each of ten signals for the SRA (left) and the SSM (right) algorithms, both for N = 8192, H = 0.75. The figure consists of two subplots: (a) SRA and (b) SSM. Each subplot shows 'Correlation coefficient' on the y-axis versus 'Number of units distance' on the x-axis, both ranging from 0 to 25. In (a), the SRA algorithm shows correlation coefficients that are mostly below zero and scatter widely. In (b), the SSM algorithm shows correlation coefficients that are mostly above zero and follow a smooth curve that decreases towards zero.](797231cfee084ca299de599340240401_img.jpg)

Figure 8: Autocorrelations r\_n versus n calculated for each of ten signals for the SRA (left) and the SSM (right) algorithms, both for N = 8192, H = 0.75. The figure consists of two subplots: (a) SRA and (b) SSM. Each subplot shows 'Correlation coefficient' on the y-axis versus 'Number of units distance' on the x-axis, both ranging from 0 to 25. In (a), the SRA algorithm shows correlation coefficients that are mostly below zero and scatter widely. In (b), the SSM algorithm shows correlation coefficients that are mostly above zero and follow a smooth curve that decreases towards zero.

8. Autocorrelations  $r_n$  versus  $n$  calculated for each of ten signals for the SRA (left) and the SSM (right) algorithms, both for  $N = 8192$ ,  $H = 0.75$ . The lines represent the expected correlation function with  $H = 0.75$ .

mum and maximum lags. It is not clear how important the number of subintervals is. Mandelbrot and Wallis noted that the smallest lags (under 30) can't be expected to be on the line, and should not be included in the procedure. In this article, we chose not to use overlapping subintervals, so that no extra dependence between these subintervals occurs. Hurst reported that the estimates from the R/S analysis might

be biased towards 0.72, in agreement with our finding at short signal lengths. However, at long signal lengths the bias seemed to be toward  $H = 0.8$ . It is not clear why this would occur. Further work needs to be done, especially on the influence of picking the particular subintervals from the main signal. As can be seen with the correlation analysis for signals of length 512, 8192 and 32768, in Fig. 3, the SSM

algorithm produces a better correlation structure for longer signals. From Fig. 6, it can be seen that the same applies to the SRA algorithm, because the estimations also become progressively better; compare Figs. 6b, 6d, and 6f.

In the estimation of  $H$  from the correlogram, the estimates of  $r$  are biased towards zero when  $n$  is large. Figure 9 shows the estimations of  $H$  as a function of lags included in the correlogram for the fit of the correlation function, Eq. 6. The signal was generated with the SSM algorithm with an  $H = 0.9$ . The bias towards 0.5 becomes progressively more apparent when more distant correlation coefficients are included. With  $n$  large, the calculation of  $r_n$  is also rendered less accurate, simply because there are fewer pairs of values to correlate at large distances. These difficulties are exacerbated when  $H$  is closer to 0.5, and lessened when  $H$  is  $> 0.8$ .

In the range of  $H$  between 0 and 0.5, all estimations except for the Fourier analysis and RD analysis with long signals are not

### Spectral analysis yields the least biased results, and the lowest variance in estimates of $D$

very good. The reason is that the data points from which the Fourier analysis estimates the fractal dimension are independent of each other. With the correlogram this is not the case. The correlations are negative for the first few lags, but very quickly become scattered around zero. When too many correlation coefficients are included in the estimation procedure, a biased estimate towards  $H = 0.5$  is obtained. The estimation from only the first autocorrelation coefficient is not good, either. The first autocorrelation coefficient as a

function of  $H$  is described by Eq. 5 [23]. Why a first autocorrelation coefficient of less than  $-0.5$  is not possible for a fractal signal is not well understood.

Of all the methods discussed, the Fourier method is generally best. However, the variance (or SD) of the estimate is still larger than that given by the maximum likelihood methods (MLE) in Lundahl et al. [16] and Fortin et al. [17]. For example, with the Fourier method and  $N = 512$  points, the SD is 0.033. Use of the MLE yields an SD =

0.01. The major liability of the MLE is its extensive computation time.

The procedure to calculate the fractal dimension of the strange attractor of the underlying dynamical system [2] is not discussed here. The fractal dimension of the strange attractor is conceptually different: it gives a measure of the minimal order of a system, the order  $N$  of  $N$ -dimensional phase space in which the time signal and its derivatives (or the order of the set of differential equations defining the system) can be mapped, plus the degree to which the signal fills the space. Although one would think that a little noise would encourage overestimating the dimension, in the situation where the system is relatively stable, the noise actually has the effect of revealing the dimensionality of the attractor more fully [29]. A main drawback of the analysis in [2] is that it requires a very large (long) time series in order to converge on the estimate of the dimension.

## Conclusion

The fractal dimension provides a measure of the heterogeneity of the system and takes the correlation structure into account:  $D \neq 1.5$  implies that we are not dealing with a random distribution, but that there is correlation between adjacent regions. We compared four numerical methods to estimate the fractal dimension. Correlation analysis and rescaled range analysis yield seriously biased results under many circumstances. Relative dispersion analysis is well suited for long signals. Spectral analysis gives the least biased results, and also has lowest variance in the estimates of the fractal dimension. The same methods can be used for the one-dimensional analysis of spatial signals, as Hurst et al. [10] did for the analysis of thicknesses of tree growth rings, and mud layers. For the analysis of two- and three-dimensional signals, the methods can be extended to account for anisotropy, making the analysis more complicated but adhering to the same basic theory.

*James Bassingthwaite*, born 1929, MD (Toronto), Ph.D. (Minnesota) is Professor of Bioengineering at the University of Washington, Seattle. His research is centered on cardiac blood flow and metabolism and the kinetics of exchange of substrates and ions. Address for correspondence: Center for Bioengineering WD 12, Seattle, WA 98195

*Johannes H.G.M. van Beek*, born 1952, B.S. (University of Utrecht, The Netherlands), Ph.D. (University of Leiden), is Assistant Professor at the Laboratory for

![Figure 9: A line graph showing the effect of the number of correlation coefficients used for estimation on the estimated value of H. The x-axis is 'Number of correlation coefficients used for estimation' ranging from 0 to 200. The y-axis is 'Estimated H' ranging from 0.75 to 0.9. The data points show a decreasing trend from approximately 0.82 at 0 coefficients to 0.76 at 200 coefficients. A legend in the top right corner indicates 'Actual H = 0.9', 'SSM', and 'N = 8192'.](fd40c60cfaff879ea9bec71d4f72a8ec_img.jpg)

| Number of correlation coefficients | Estimated H |
|------------------------------------|-------------|
| 0                                  | 0.82        |
| 20                                 | 0.81        |
| 40                                 | 0.80        |
| 60                                 | 0.79        |
| 80                                 | 0.785       |
| 100                                | 0.78        |
| 120                                | 0.775       |
| 140                                | 0.77        |
| 160                                | 0.765       |
| 180                                | 0.762       |
| 200                                | 0.76        |

Figure 9: A line graph showing the effect of the number of correlation coefficients used for estimation on the estimated value of H. The x-axis is 'Number of correlation coefficients used for estimation' ranging from 0 to 200. The y-axis is 'Estimated H' ranging from 0.75 to 0.9. The data points show a decreasing trend from approximately 0.82 at 0 coefficients to 0.76 at 200 coefficients. A legend in the top right corner indicates 'Actual H = 0.9', 'SSM', and 'N = 8192'.

9. The effect of the number of correlation coefficients that are included in the estimation for  $H$  from a signal generated by the SSM algorithm, with  $N = 8192$  and  $H = 0.9$ .

(continued on page 71)