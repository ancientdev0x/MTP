

# Fractal Correction of Well Logging Curves<sup>\*</sup>

Li Qingmou Cheng Qiuming

*Institute of Geology & Geophysics, Chinese Academy of Sciences, Beijing 100101;*

*Department of Earth and Atmospheric Science, York University, Toronto, Ontario, Canada, M3J 1P3*

## ABSTRACT

It is always significant for assessing and evaluation of oil-bearing layers, especially for well logging data processing and interpretation of non-marine oil beds to get more accurate physical properties in thin and inter-thin layers. This paper presents a definition of measures and the measure presents power law relation with the corresponded scale described by fractal theory. Thus, logging curves can be reconstructed according to this power law relation. This method uses the local structure nearby concurrent points to compensate the average effect of logging probes and measurement errors. As an example, deep and medium induced conductivity (IMPH and IDPH) curves in ODP Leg 127 Hole 797C are reconstructed or corrected. Corrected curves are with less adjacent effects through comparison of corrected curves with original one. And also, the power spectra of corrected well logging curve are abounding with more resolution components than the original one. Thus, fractal correction method makes the well logging more resolvable for thin beds.

KEY WORDS fractal, thin bed well logging, singularity of well logging, well logging correction.

## INTRODUCTION

Because well logging measurements give an average results nearby concurrent depth points of the probes as shown in Fig. 1a, well logging curve does not supply the real geophysical properties at concurrent depth but a disturbed result of adjacent layers and borehole environment. How to retrieve real physical value has been a subject for well logging analysts and especially for Chinese well logging analysts who must mainly cope with non-marine sedimentary reservoir. Techniques for well logging data processing and interpretation in thin, inter-thin beds are a Chinese-characterized difficult subjects in oil exploration and development. Intrinsic methods to invest thin beds should work by probes design and calibration, though post-processing method such as deconvolution can also improve the resolution in some extent (Wang et al., 1997).

According to fractal theory, measurement is related with scale by power law (Pape et al., 2000; Cheng, 1999; Dutton, 1998; Van Wagoner, 1990). This is called scale invariant or self-affinity. So, by proper definition of well logging curve measure, power law could be certified and applied.

For an equally sampled well logging series (Fig. 1b), using

an expanding scale window ( $\Delta h, 3\Delta h, 5\Delta h, \dots \Delta h$  is acquisition interval) centered at concurrent points  $K$  (at depth  $K \cdot \Delta h$ ) a series of covers can be built up. With these covers, measure is defined as

$$\mu(K, \epsilon) = \sum_{i=K-\frac{\Delta h}{2}}^{K+\frac{\Delta h}{2}} x(i) \Delta h \quad (1)$$

where  $\mu(K, \epsilon)$  is measure at point  $K$  under cover scale  $\epsilon = M \cdot \Delta h$ ;  $x(i)$  is well logging values at depth  $i \cdot \Delta h$ ;  $\Delta h$  is acquisition interval of well logging curves. According to fractal theory (Renata and Bary, 1999; Donald, 1997), measure  $\mu(K, \epsilon)$  relates scale  $\epsilon = M \cdot \Delta h$  as power law

$$\mu(K, \epsilon) = A \epsilon^{\alpha(K)} \quad (2)$$

where  $A$  is a constant;  $\epsilon = M \cdot \Delta h$  is scale;  $\alpha(K)$  is a point  $K$ -wised constant, also,  $\alpha(K)$  has intrinsic relation with fractal dimension of well logging curves at point  $K$ .  $\alpha(K)$  delineates the sediment stacking pattern at  $K$  point and is called well logging singularity at points  $K$ . Assume  $M=1$  in formula (1), so  $\mu(K, \Delta h) = x(i) \cdot \Delta h$ , and use it to replace  $\mu$  in formula (2)

$$x(k) \cdot \Delta h = A \cdot (\Delta h)^{\alpha(K)} \quad (3)$$

$$(3)/(2) \quad \frac{x(k) \cdot \Delta h}{\mu(k, \epsilon)} = \left(\frac{\Delta h}{M \Delta h}\right)^{\alpha(K)}$$

Then

$$x(k) = \frac{1}{\Delta h} \left(\frac{1}{M}\right)^{\alpha(K)} \cdot \mu(k, \epsilon) \quad (4)$$

\* The paper is supported by National Natural Science Foundation of China (No. D49774237).

![Figure 1: Well logging curve measurement definition demonstration. The figure consists of four sub-diagrams labeled (a) through (d). (a) shows a vertical axis with a shaded elliptical region representing a measurement zone. (b) shows a vertical axis with a series of horizontal arrows pointing to the right, representing measurements at different depths. (c) shows a vertical axis with a 'current point' and an 'interpolate point' indicated by arrows. (d) shows a vertical axis with a 'current point' and an 'interpolate point' indicated by arrows, similar to (c) but with a different arrow configuration.](61972112770d9c8fb00883057954f885_img.jpg)

Figure 1: Well logging curve measurement definition demonstration. The figure consists of four sub-diagrams labeled (a) through (d). (a) shows a vertical axis with a shaded elliptical region representing a measurement zone. (b) shows a vertical axis with a series of horizontal arrows pointing to the right, representing measurements at different depths. (c) shows a vertical axis with a 'current point' and an 'interpolate point' indicated by arrows. (d) shows a vertical axis with a 'current point' and an 'interpolate point' indicated by arrows, similar to (c) but with a different arrow configuration.

Figure 1. Well logging curve measurement definition demonstration.

![Figure 2: Measures of well logging curve vs scales show a linear line in dual logarithm coordinate system. The figure contains four subplots for IDPH(345 m), IDPH(360 m), IDPH(380 m), and IDPH(420 m). Each subplot shows log μ on the y-axis (ranging from 0 to 5) versus log ε on the x-axis (ranging from -2 to 4). The data points in all four plots form a clear linear trend.](8d2f4e036a5e0205a1ea3f0b3378f584_img.jpg)

Figure 2: Measures of well logging curve vs scales show a linear line in dual logarithm coordinate system. The figure contains four subplots for IDPH(345 m), IDPH(360 m), IDPH(380 m), and IDPH(420 m). Each subplot shows log μ on the y-axis (ranging from 0 to 5) versus log ε on the x-axis (ranging from -2 to 4). The data points in all four plots form a clear linear trend.

Figure 2. Measures of well logging curve vs scales show a linear line in dual logarithm coordinate system.

$$x(k) = \left(\frac{1}{M-1}\right)^{\alpha(K)} \sum_{i=k-\frac{M}{2}}^{k+\frac{M}{2}, i \neq k} x(i) \quad (5)$$

Solve  $X(K)$ , by formula (5), we get formula (6)

$$x(k) = \left(\frac{1}{M}\right)^{\alpha(K)} \sum_{i=k-\frac{M}{2}}^{k+\frac{M}{2}} x(i) \quad (6)$$

Use formula (5) to recalculate known points for well logging correction, and use formula (6) to interpolate well logging values between two known adjacent points.

## LOCAL SINGULARITY $\alpha(K)$ OF WELL LOGGING

From formula (2),  $\log \mu(K, \epsilon) \cdot \log \epsilon$  should be a linear relation in theory. But, well logging curves are affected by adjacent layers and borehole environment, therefore, the measures and scale maybe don't combine an exact line in dual logarithm coordinate system in real world. A least square error (LS)

method is used to simulate a line passing through these of measures versus scales, and the slope of this simulated line is the best estimation of  $\alpha(K)$  with the least square error significance.

Well logging curves of ODP Leg127, Hole 797C are used as test example. Figure 2 shows the LS linear regression results of curve IDPH at depths 345 m, 365 m, 380 m and 420 m mb-sf (meter below sea floor) with  $M$  from 3, 5, 7, 71 (logging acquisition interval is 0.1 m, so the maximum scale length is 7.1 m) in dual logarithm coordinate system. It shows quite a good linear relation of measures and scale in dual logarithm coordinate system. The regression index and errors are displayed in Fig. 3.

How to choose the length of  $M$  depends on the vertical geometry of logging probes. If  $M$  is less, the corrected result will only reflect nearby concurrent points, and  $M$  should be in

![Figure 3: Deep and middle induced conductivity (IDPH, IMPH) of ODP Leg 127, Hole 797C. The figure consists of five panels (a) through (e) showing data from 340 to 440 depth in meters. Panel (a) shows IDPH (1/Ω·m) with values from 0.4 to 1.4. Panel (b) shows IMPH (1/Ω·m) with values from 0.998 to 1.4. Panel (c) shows the regression index for IMPH with values from 0.85 to 1.15. Panel (d) shows the local singularity of IMPH with values from 0 to 0.05. Panel (e) shows the local standard regression errors of IMPH with values from 0.4 to 1.4. Each panel contains multiple curves: solid lines for IDPH and IMPH, thick solid lines for moving average results with a 7.1 m window length, and dotted lines for the fractal corrected result.](3cab54230d8ae3b786ddda81346602cc_img.jpg)

Figure 3: Deep and middle induced conductivity (IDPH, IMPH) of ODP Leg 127, Hole 797C. The figure consists of five panels (a) through (e) showing data from 340 to 440 depth in meters. Panel (a) shows IDPH (1/Ω·m) with values from 0.4 to 1.4. Panel (b) shows IMPH (1/Ω·m) with values from 0.998 to 1.4. Panel (c) shows the regression index for IMPH with values from 0.85 to 1.15. Panel (d) shows the local singularity of IMPH with values from 0 to 0.05. Panel (e) shows the local standard regression errors of IMPH with values from 0.4 to 1.4. Each panel contains multiple curves: solid lines for IDPH and IMPH, thick solid lines for moving average results with a 7.1 m window length, and dotted lines for the fractal corrected result.

Figure 3. Deep and middle induced conductivity (IDPH, IMPH) of ODP Leg 127, Hole 797C original and corrected curves. (a), (e). Solid line for the IDPH and IMPH; Thick solid lines for the moving average results with 7.1 m window length; Dotted line for the fractal corrected result; (b). regression index for IMPH; (c). local singularity of IMPH; (d). local standard regression errors of IMPH.

creased if long-range effects are considered as experience based on many tests.  $\alpha(K)$  is not sensitive to  $M$  changes in a wide range of  $M$  as in Fig. 2. It will not affect the slope of the line ( $\alpha(K)$ ) if using a little less points in Fig. 2, because the regression line is quite stable and the regression index is exceptional, most of them is greater than 0.998 as shown in Fig. 3.

$\alpha(K)$  is the slope of measures vs scale in dual logarithm from formula (2) and Fig. 2.  $\alpha(K)$  is the measure of concavity or convex in  $\delta$  domain of point  $K$ . The slope should be 1 if the well logging curves keep stable in a series of expanding windows centered at concurrent point, herein the well logging curves need not to be corrected. If the well logging values increased is too fast compared with the scale expanding rate, the slope in Fig. 2 will be greater than 1 ( $\alpha(K) > 1$ ). The curve is with concave property in current point presenting that the stacking pattern around current point is with increasing model and current point is at the center of this expanding (sliding window) and concurrent well logging value is raised by adjacent layers and borehole environment with high values. So the correction is

low down concurrent logging value. For the same reason, if  $\alpha(K) < 1$ , logging curve is convex and the correct process will increase its value. So,  $\alpha(K)$  represents the changing patterns in  $\delta$  domain of current point. This correction method is reflected by the changing patterns in  $\delta$  domain of interested point (Renata and Barry, 1999; Doveton, 1998; Van Wagoner, 1990).

## IDPH, IMPH CORRECTION

The processed IDPH, IMPH results of Hole 797C, ODP Leg 127 are shown in Fig. 3. In Fig. 3a, the thin solid line is the IDPH curve; thick solid line, the moving average result of IDPH with 71 points sliding window length, and the thin dotted line, the fractal corrected result with the same window length of the moving average. The moving average makes maximum peaks a little lower and minimum peaks a little bit higher, this will lose the high frequency information. But, fractal correction method makes not only maximum points upper and minimum points lower in most cases to compensate the adjacent

![Figure 4: Power spectra of IDPH (a) and IMPH (b) against corrected curves (dotted lines).](7fb5215fd72210a2e4cce6df55550c89_img.jpg)

Figure 4 consists of two line graphs, (a) and (b), showing power spectra. Both graphs have 'power spectra' on the y-axis and 'wave number' on the x-axis. Graph (a) for IDPH has a y-axis from 0 to 40 and an x-axis from 0 to 1. Graph (b) for IMPH has a y-axis from 0 to 50 and an x-axis from 0 to 1. In both graphs, there are three types of curves: a thin solid line representing the original data, a thick solid line representing a moving average, and a dotted line representing the fractal corrected result. The curves show high-frequency oscillations that dampen as the wave number increases.

Figure 4: Power spectra of IDPH (a) and IMPH (b) against corrected curves (dotted lines).

Figure 4. Power spectra of IDPH (a) and IMPH (b) against corrected curves (dotted lines).

effects, but also will make low points upper and upper points lower in some cases according to the stacking pattern nearby concurrent points.

Figure 3e shows the calculated local singularity  $\alpha(K)$ .  $\alpha(K)$  fluctuates around 1. When  $\alpha(K) > 1$ , fractal correction will low down the corresponded curves; when  $\alpha(K) < 1$ , it will raise corresponded curves; when  $\alpha(K) = 1$ , concurrent curve is not singular, so well logging curve need not to be corrected.

Figure 2b is the regression index in calculating  $\alpha(K)$ . All values are greater than 0.998, most of which is nearby 1. This means the defined measure in this paper is accordance with the fractal measure assumption. Figure 2d is the standard errors in calculation of  $\alpha(K)$ .

Corrected IMPH is shown in Fig. 3e. In it, thin solid line is IMPH curve, solid thick line is moving averaging with sliding window length of 71 points and the dotted line is fractal corrected result. IMPH correction shows the same results with IDPH.

## DISCUSSION

The power spectra of IDPH and IMPH in Fig. 3a and 3e are estimated and plotted in Fig. 4a and 4b to compare the resolution message inside original and corrected curves. The fractal corrected well logging curve not only keep the original curve resolution message both in high and low frequency bands, but also enhance some component spectra value in middle frequency band as shown in Fig. 4. This will benefit in resolution and real data estimation. Herein, fractal correction method can be used in well logging correction.

The geometry characters of logging probe must be considered in well logging fractal correction. By adding weights in formula (5) and selecting  $M$  according to logging geometry, correction method could be improved and this needs future work.

This method could be also used in unevenly distributed situation by using average value in a window for measure calculation as shown in Fig. 1.

This method is programmed in 32 bits windows environment (WIN32) with friendly GUI. Interested reader can relate

with the authors.

## REFERENCES CITED

- Cheng Q. 1999. Multifractal Interpolation. In: Lippard S J, Nass A, Sinding L, eds. 5th Annual Conference [IAMG '99] Proceedings. International Association of Mathematical Geology, 245—250.
- Donald L T. 1997. Fractals and Chaos in Geology and Geophysics. Second Edition. London: Cambridge University Press. 398.
- Doveton J H. 1998. Beyond the Perfect Martini—Teaching the Mathematical Geology of Petrophysical Logs. In: Buccianti A, Nardi G, Potenza R., eds. 4th Annual Conference [IAMG '98] Proceedings. International Association of Mathematical Geology, 71—75.
- Pape H, Clauser G, Iffland J. 2000. Variation of Permeability with Porosity in Sandstone Diagenesis Interpreted with a Fractal Pore Space Model. Pure and Applied Geophysics, 157:603—619.
- Qian Y, Zhong X. 1999. Thin Bed Information Resolution of Well-Logs and Its Applications. Log Analyst, 40(1):31—38.
- Renata D, Barry S. 1999. Long-Range Persistence in Geophysical Time Series. Advances in Geophysics (40). New York: Academic Press.
- Van Wagoner J C. 1990. Siliciclastic Sequence Stratigraphy in Well Logs, Core and Outcrops; Concepts for High Resolution Correlation of Time and Facies. AAPG Methods in Exploration Series, 7:55.
- Wang H, Li Z, Yang S, et al. 1997. Normalized Method for Better Resolution of Natural Gamma Ray Well Logging Data. Acta Geophysica Sinica, 40(6):84.