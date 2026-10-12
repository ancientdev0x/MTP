

![Elsevier logo featuring a tree and the text 'NON SOLUS' and 'ALTERA'.](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

Elsevier logo featuring a tree and the text 'NON SOLUS' and 'ALTERA'.

![Cover image of the journal Physica A: Theoretical and Computational Physics.](390120de4fe440c42fea8154fcaad334_img.jpg)

Cover image of the journal Physica A: Theoretical and Computational Physics.

# Wavelet Leaders: A new method to estimate the multifractal singularity spectra

E. Serrano<sup>a</sup>, A. Figliola<sup>b,\*</sup>

<sup>a</sup> Centro de Matemática Aplicada, ECyT, Universidad Nacional de San Martín, Irigoyen 3100, San Martín, Pcia. de Buenos Aires, Argentina

<sup>b</sup> Instituto del Desarrollo Humano, Universidad Nacional de General Sarmiento, Juan María Gutiérrez 1150, Los Polvorines, Pcia. de Buenos Aires, Argentina

## ARTICLE INFO

### Article history:

Received 28 July 2008

Received in revised form 15 March 2009

Available online 5 April 2009

### PACS:

64.60.al

43.60.Hj

98.75.-k

### Keywords:

Wavelet Leaders

Multifractal formalism

Hölder regularity

Scalar invariance

Multifractal Detrended Fluctuation Analysis

## ABSTRACT

*Wavelet Leaders* is a novel alternative based on wavelet analysis for estimating the Multifractal Spectrum. It was proposed by Jaffard and co-workers improving the usual wavelet methods. In this work, we analyze and compare it with the well known *Multifractal Detrended Fluctuation Analysis*. The latter is a comprehensible and well adapted method for natural and weakly stationary signals. Alternatively, Wavelet Leaders exploits the wavelet self-similarity structures combined with the Multiresolution Analysis scheme. We give a brief introduction on the multifractal formalism and the particular implementation of the above methods and we compare their effectiveness. We expose several cases: Cantor measures, Binomial Multiplicative Cascades and also natural series from a tonic–clonic epileptic seizure. We analyze the results and extract the conclusions.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Frequently, complex natural systems present characteristics of *scalar invariance*, behavior that has been verified experimentally during the past years. Concerning this, there exists a very rich bibliography that was reported from very diverse fields as those belonging to physics, ecology, biology or economy [1–6].

The *Multifractal Formalism* is based on the calculation of two sets of coefficients associated to the signals: the *Hölder exponents* (HE), that quantify the local regularity of a signal or function  $f$  and the *multifractal spectrum* (MS) that quantifies the multifractality of  $f$ . The MS associates each group of data with the same regularity at a given point with the Hausdorff dimension of this set of points. In this way, it defines a function between the HE and the Hausdorff dimension that is also known as *spectrum of singularities* [7,8].

Stanley and Ostrowsky (1985) and Pietronero and Tosatti (1986) have been pioneers in the development of this research line [9,10]. The MS is intimately related with the dimension widespread fractal based on which Grassberger and Procaccia have published studies widely, in the eighties [11–13]. In 1988, Chhabra and collaborators demonstrated that the MS corresponds to the entropy density of the system, while the set of HE is related with its free energy, [14,15]. Some years later, Arneodo, Bacry and Macy developed a statistical method for the estimation of the MS based on the study of the maxima of the continuous wavelet transform of the signal. This method is known as the *Wavelet Transform Modulo Maxima Method* (WTMM) [16–18]. In 1995, Peng and co-workers presented the *Detrended Fluctuation Analysis* (DFA) [19], formulated to

\* Corresponding author. Tel.: +54 11 44697708.

E-mail address: [alejandra.figliola@gmail.com](mailto:alejandra.figliola@gmail.com) (A. Figliola).

evaluate the scaling properties of a given signal. The DFA was successful in applications to different fields, such as the study of sequences of DNA and signals associated to physiological or economical processes. [20–23]. A generalization of the DFA is the *Multifractal Fluctuation Detrended Analysis* (MFDFA), introduced by the early work of Castro e Silva and Moreira and, in recent years, reformulated and improved by Kantelhardt and Stanley. The new development extends the application field for temporary series with multifractal behavior, [24,25].

WTMM and MFDFA methods are highly effective to characterize real systems from statistical data, such as heart rhythms, seismic patterns or economical dynamic. [3,4,25]. However, the extension of these methods to more general cases is nowadays an open problem. It has also been shown that for short series and negative moments, the significance of the results for MFDFA is better than for WTMM method, [25,26]. They are well proven for the case of non-negative and singular Borel measures  $\mu$  supported on bounded closed sets, including the case of Cantor's ones. In these cases, depending on the method, it is possible to define a *partition function* and to build a corresponding multifractal formalism allowing to analyze **Hölder regularity of the distribution functions for these measures**.

In the past years, Jaffard with Lashermes and Abry [27–31] have proposed another methodology for the characterization of Hölder exponents and their relationship between **Hölder regularity** and local oscillations. They named this method *Wavelet Leaders* (WL). This is a new formulation in terms of the local suprema of the wavelet coefficients or *Leaders* of the signal.

Starting from the existent literature we can conclude that, in general, to characterize fractal properties is a hard problem, mainly in natural phenomena. Moreover, some authors consider that it is almost impossible a faithful numerical analysis from a finite data set, with sampled values of an irregular signal [27]. Anyway, under appropriate assumptions, some calculations are possible, even from experimental data. The more frequently considered hypothesis is the fact that relevant structures, present in the signal, are reflected in the available data. The other main conjecture is the self-similarity of the signal, that is, the general hypothesis of the scalar invariance. Then, in theory, we can extract significant multifractal information from the data using appropriate numerical methods.

The aim of this work is to compare the efficiency between WL and MFDFA methods. For this purpose, we will used consider two numerical data sets coming from well known measures: Cantor and Binomial Multiplicative Cascades. Besides, we will study a natural series from the experimental electroencephalogram (EEG) of a tonic–clonic epileptic seizure.

This paper is organized in the following way: Section 2 is devoted to theoretical mathematical background. **In Sections 3, 4, 5 we present MFDFA and WL methods**. We show an illustrative example in Section 6. In Section 7 we present the multifractal spectrum estimation of the Binomial Multiplicative Cascades using both methods. In Section 8, we present the applications and finally, in Section 9, the conclusions.

## 2. Theoretical background

### 2.1. Pointwise Hölder regularity

**Hölder regularity** is the most widely used notion of pointwise regularity [27,32]. We give a review of the definition: Let  $\alpha \geq 0$  and  $x_0 \in R$  and a locally bounded function  $f : R^d \rightarrow R$ . We say that  $f \in C^\alpha(x_0)$  if there exists a constant  $C > 0$  and a polynomial  $P$  with degree  $\deg(P) < \alpha$  such as:

$$|f(x) - P(x - x_0)| \leq C|x - x_0|^\alpha$$

in the neighbourhood of the point  $x_0$ .

The *pointwise Hölder exponent* of  $f$  in  $x_0$  is:

$$H_f(x_0) = \sup\{\alpha : f \in C^\alpha(x_0)\}.$$

These exponents describe local regularity of  $f$  at  $x_0$ . If  $H_f(x_0) < 1$  the function is not differentiable in  $x_0$ , and  $P(x - x_0) = f(x_0)$ . In this case, the exponent describes the smoothness or the ruggedness of the function in the point and it expresses how spiky the graph is. We recall that usually this is the case in signal processing applications.

On the other hand, if  $H_f(x_0) > 1$  the function is differentiable in  $x_0$ . Moreover, if the Taylor polynomial of degree  $n$  exists at the point, then  $f \in C^n(x_0)$ . In the special case where  $H_f(x_0) = 1$ , we say that  $f$  belongs to the *Zigmund* or *affine* class and when  $\alpha = 0$ , we see that  $|f(x)| \leq C$ . Then, for convenience, the degree of the null polynomial is  $-\infty$ .

We are interested in signals whose HE change from point to point. Then, the problem is to characterize the set of points having the same pointwise regularity, as we well discuss in next section. At last we recall that Hölder pointwise exponents are the usual and most preferable ones but not the unique option to describe regularity. Other exponents and parameters can be used, and we refer to [27,32] for specific details.

### 2.2. Multifractal spectrum of singularities

As we mentioned in the introduction, natural phenomena usually present multifractal characteristics, that is to say, they are suitable represented by signals whose regularity fluctuates showing evidence of fractal properties. For simplicity we will consider only one dimensional real signals. Multifractal analysis is relevant when the set of points having the same HE is

dense in the signal's domain. But if this is the case, it is impossible to estimate them in any point and only a global description of their distribution can be given. Following these purposes, we will denote:

$$E_f(H) = \{x \in \text{dom}(f) : H_f(x) = H\}$$

the set of points having the same regularity. The *spectrum of singularities* or *multifractal spectrum*, denoted by  $d_f(H)$  is the Hausdorff dimension of the set  $E_f(H)$ , [7,27,32].

If  $E_f(H) \neq \emptyset$ , we have  $0 \leq d_f(H) \leq 1$ .

The spectrum is fractal if  $0 < d_f(H) < 1$  for some  $H$  and is multifractal if the same holds for different values  $H$ .

For special functions the singular points are Cantor sets and the spectrum  $d_f(H)$  appears as a smooth concave function of  $H$ , for some interval  $H_1 < H < H_2$ . Beyond these cases, we can expect that the smooth and concave model for  $d_f(H)$  is a reasonable hypothesis for a broad class of fractal signals.

In this way, the spectrum will give us a clear characterization of the global distribution of the HE, the fractal properties of the signal and the underlying phenomena, [7,11–13].

### 2.3. Multifractal formalism

From singular probability measures supported on Cantor sets it is possible a formal and rigorous development of a concise method to obtain the MS, [7]. This scheme was presented as *multifractal formalism* and it can be appropriately modified and extended for a more general class of signals. In fact, the main purpose of this article is the comparison among two different alternatives.

Following the development given in Ref. [28], we introduce a prototype scheme for an unidimensional locally bounded function. First, we define a numerable set of intervals:

$$I_{jk} = [r_j k, r_j(k + 1))$$

where  $r_j$  is a decreasing sequence and  $\lim_{j \rightarrow +\infty} r_j = 0$ . Note that  $|I_{jk}| = r_j$ . We will denote  $I_j(x_0)$  the unique interval of size  $r_j$  such that  $x_0 \in I_{jk}$ . We also denote  $MI_j(x_0)$  a  $M$ -dilation of the interval  $I_j(x_0)$ . Next, we suppose that there exists a non-negative functional defined on a set of intervals:

$$\mu : \{I\} \rightarrow \mathbb{R}_{\geq 0}$$

related with the HE in this way:

$$\mu(MI_j(x_0)) \sim r_j^{H_f(x_0)} \tag{1}$$

for some dilation  $M$ . Or, even, in a strong way:

$$H_f(x_0) = \liminf_{r_j \rightarrow 0} \frac{\log(\mu(MI_j(x_0)))}{\log(r_j)} \tag{2}$$

If this is the case, we define a *scaling function*:

$$S(q, j) = r_j \sum_{k \in K_j} \mu(MI_{jk})^q \tag{3}$$

where  $K_j$  is the index set such that  $\mu(MI_{jk}) > 0$ .

The above hypothesis let us in Eq. (1) or (2) assert that the contribution to  $S(q, j)$  of the intervals  $I_j(x_0)$ ,  $(x_0 \in E_f(H))$  is given by  $\mu(MI_{jk}) = r_j^H$ . Since we need  $\sim r_j^{-d_f(H)}$  intervals to cover  $E_f(H)$ , according Hausdorff's definition, we can deduce that the contribution is:

$$S(q, j)(H) \sim r_j^{(1-d_f(H)+Hq)} \tag{4}$$

and considering that when  $r_j \rightarrow 0$  the principal contribution becomes from the smallest exponents, we can define the function:

$$\eta(q) = \inf_H (1 - d_f(H) + Hq) \tag{5}$$

At last, if the function  $\eta$  is concave and assuming that the spectrum  $d_f$  is concave indeed, the duality relation for concave functions gives us the formula:

$$d_f(H) = \inf_q (1 - \eta(q) + Hq) \tag{6}$$

and the formalism scheme is complete. We emphasize that this scheme has not an empty domain. The distribution functions associated with probability measures supported on Cantor sets verify the multifractal formalism. Because of  $d_f$  concavity

property, the HE and the parameters  $q$  are related by the *Legendre Transform* of the function  $\eta(q)$ . More precisely, the exponent  $H(q)$  is the unique value satisfying the equation:

$$H(q) = \frac{d\eta}{dq}(q), \quad q \in \mathbb{R}. \tag{7}$$

If  $\mu$  is an increasing non-negative function formula, then  $d_f(H)$  at Eq. (6) holds for dyadic intervals. Moreover, if  $\mu$  is a Borel measure then  $\eta(q)$  is a concave function.

However, although we can choose the covering  $\{I_{jk}\}$  and the function  $\mu$  we cannot ensure that  $d_f(H)$  is a concave function and this is independent of our scheme design. Then, the multifractal formalism becomes a suitable designed tool to estimate the fractal properties of the signal. See Ref. [27] for comments about this matter. Moreover, in many cases the signal is given only by samples and the formalism must be discretized in some way. Now, the problem is open to many choices, alternatives and variants.

In next section we revise an alternative method scheme developed by Kantelhardt et al. [25], the MFDDA.

## **3. Multifractal Detrended Fluctuation Analysis**

The MFDDA method was presented as a generalization of the DFA method and it proves its advantage compared with other methods [25,26]. The estimation of the MS of a one dimensional series  $\{x(i), i = 1, \dots, N\}$ , is based on the construction and the analysis of the *fluctuation function*, that is defined as:

$$F_r^2(\nu) = \frac{1}{r} \sum_{i=1}^r \{Y_r[(\nu - 1)r + i]\}^2. \tag{8}$$

To obtain Eq. (8), first we calculate the *profile* of the series integrating:  $Y(k) = \sum_{i=1}^k [x(i) - \langle x \rangle]$ , where  $\langle x \rangle$  represents the mean value of the series  $\{x(i)\}$ . The profile is cut into  $N_r = N/r$  non-overlapping segments of equal length  $r$ . The detrended time series for segment  $r$ , denoted by  $Y_r(i)$ , is calculated as the difference between the original time series and  $p_\nu(i)$ , where  $p_\nu(i)$  is the fitting polynomial in the  $\nu$ th segment:

$$Y_r(i) = Y(i) - p_\nu(i).$$

Since we use a polynomial fit of order  $m$ , the algorithm is denoted as MFDDA- $m$  and when  $m = 1$ , as MFDDA. Due to the detrending of the time series is done by subtraction of the polynomial fits from the profile, these methods differ in their capability of eliminating trends in the data. For each of the  $N_r$  segments, the variance of the detrended time series  $Y_r(i)$  is evaluated averaging over all data point  $i$  in the  $\nu$ th segment. Then, averaging over all segments, we obtain the  $q$ th fluctuation function:

$$F_q(r) = \left\{ \frac{1}{2N_r} \sum_{\nu=1}^{2N_r} [F_r^2(\nu)]^{q/2} \right\}^{1/q}, \tag{9}$$

where, in general, the index  $q$  can be any real value. For  $q = 2$ , the standard DFA procedure is retrieved, and  $h(q = 2)$  is the *Hurst exponent*. The scaling behavior of the fluctuation function is determined by analyzing log-log plots  $F_q(r)$  versus  $r$  for each value of  $q$ . If the series  $x(i)$  is a long-range power-law correlated,  $F_q(r)$  increases, for large values of  $r$ , as a power law, [19,25]:

$$F_q(r) \sim r^{h(q)}. \tag{10}$$

For monofractal time series with compact support,  $h(q)$  is independent of  $q$ , since the scaling behavior of the variance  $F_r^2(\nu)$  is identical for all segments  $\nu$  and the averaging procedure in Eq. (9) will give just this identical scaling behavior for all values of  $q$ . Only if small and large fluctuations scale differently, there will be a significant dependence of  $h(q)$  on  $q$ . If we consider positive values of  $q$ , the segments  $\nu$  with large variance  $F_r^2(\nu)$  will dominate the average  $F_q(r)$ . Thus, for positive values of  $q$ ,  $h(q)$  describes the scaling behavior of the segments with large fluctuations. On the contrary, for negative values of  $q$ , the segments  $\nu$  with small variance  $F_r^2(\nu)$  will dominate the average  $F_q(r)$ . Hence, for negative values of  $q$ ,  $h(q)$  describes the scaling behavior of the segments with small fluctuations.

Following from Eq. (9) and assuming that the length  $N$  of the series is an integer multiple of the scale  $r$ ,

$$\sum_{\nu=1}^{N/r} |Y(\nu r) - Y((\nu - 1)r)|^q \sim r^{qh(q)-1}. \tag{11}$$

Kantelhardt and co-workers showed that this multifractal formalism corresponds to standard box counting theory and they related both formalisms. It is obvious that the term  $|Y(\nu r) - Y((\nu - 1)r)|$  is identical to the sum of the numbers  $x(i)$  within each segment  $\nu$  of length  $r$ . This sum is the box probability  $p_\nu(\nu)$  in the standard formalism for normalized series  $x(i)$ .

The scaling exponent  $\eta(q)$  is usually defined via the *partition function*  $Z_q(r)$ ,

$$Z_q(r) \equiv \sum_{v=1}^{N/r} |p_r(v)|^q \sim r^{\eta(q)} \tag{12}$$

where  $q$  is a real parameter.

Now, we can identify the structure function  $Z_q(r)$  with the scaling function  $S(q, j)$  defined at Eq. (4) take the scale  $r$  as the  $j$ -intervals  $r_j$ . So, from Eqs. (4) and (12), we can conclude that they are identical and we obtain the relation between the two sets of multifractal scaling exponents:

$$\eta(q) = qh(q) - 1 \tag{13}$$

$H$  and  $d_f(H)$  are related with  $\eta(q)$  via a Legendre transformation:

$$H(q) = \eta'(q) \tag{14}$$

and

$$d_f(H) = qH - \eta(q). \tag{15}$$

And using Eq. (10), we can conclude that,

$$(F_q)^q(r) \sim r^{qh(q)}. \tag{16}$$

If we identify

$$F_q^q(r) \sim S(q, j) \sim r_j^{1-d_f(H)+Hq}$$

it is possible to suppose that

$$qh(q) = \inf_H [1 - d_f(H) + Hq] \tag{17}$$

and

$$d_f(H) = \inf_q [1 - qh(q) + Hq]. \tag{18}$$

Then, the MFDFA can be framed into the multifractal formalism.

## 4. Wavelet methods

The above described multifractal formalism MFDFA can be viewed as improvement of the original one proposed by Frisch and Parisi, [33] based on the structure function:

$$S_{fp}(q, j) = 2^{-j} \sum_k \left| f\left(\frac{k+1}{2^j}\right) - f\left(\frac{k}{2^j}\right) \right|^q.$$

Here, the associated measure function

$$\mu_{fp}(I_{jk}) = \left| f\left(\frac{k+1}{2^j}\right) - f\left(\frac{k}{2^j}\right) \right|$$

is defined for the dyadic intervals  $I_{jk} = \left[ \frac{k}{2^j}, \frac{k+1}{2^j} \right)$  for all integers  $j > 0$  and  $k$ . It is a first-order scheme of discrete differences. We emphasize that this is not an increasing function.

On the other hand, it suggests wavelet alternatives. For example, we can replace the above measure by:

$$\mu'(I_{jk}) = 2^j \left| \int_{k/2^j}^{(1/2+k)/2^j} f(x) - f(x+1) dx \right|$$

or, more generally, by the *wavelet coefficients* of the signal  $f$ .

Wavelets are natural tools in multifractal analysis because the concept of self-similarity is implicit in wavelet analysis. Then, wavelet coefficients provide a time-scale decomposition of the signal  $f$  reflecting the scaling properties. Moreover, wavelet methods can be used in signals with non-compact support, as it occurs frequently in monofractal series, where others methods, like MFDFA, cannot work.

Now, we can define the multifractal formalism based on the wavelet coefficients  $c_{jk}$ : the *Wavelet Continuous Multifractal Formalism* (WMCF), from the structure function:

$$S_{wc}(q, j) = 2^{-j} \sum_{k \in K_j} |c_{jk}|^q \tag{19}$$

where  $K_j$  is the index set such that  $|c_{jk}| > 0$ . Here  $\mu_{wc}(I_{jk}) = |c_{jk}|$  is a non-negative function, but we stress that it may be non-increasing. We will return to this point later.

On the other hand, there is a direct correlation between wavelet coefficients and pointwise Hölder regularity, [27].

If  $f \in C^\alpha(x_0)$  then, for all  $j > 0$ ,

$$|c_{jk}| \leq C 2^{-j\alpha} (1 + |2^j x_0 - k|)^\alpha$$

for some constant  $C > 0$ . When  $f$  has a non-oscillating singularity in  $x_0$ , like a *cusp point*, the significance coefficients lie near this point:

$$|c_{jk}| \sim C 2^{-j\alpha} \tag{20}$$

and the local measure is increases around this point. But this is not the case when the function has oscillating singularities, like a *chirp*. Then, the maxima coefficients may be placed far from the singular point and the last property fails. These circumstances are obstacles for the multifractal formalism. Particularly, the structure function becomes unstable for negative values of the parameter  $q$ , (see Ref. [27] for more details).

As we mentioned in the Introduction, the other principal wavelet alternative for estimating the MS was the WTMM, [16–18,27]. It is based on the Continuous Wavelet Transform and gives us a suitable performance. Self-similarity structures can ensure that associated Multifractal Formalism gives the correct spectrum. Nevertheless the mentioned method is not free of criticisms. First, like WCMF, WTMM presents difficulties when the signal has oscillating singularities. Second, the continuous transform implies more computational complexity. This disadvantage increases going up for images and higher dimension signals. More details can be found in Refs. [26,27].

Stéphane Jaffard and co-worker developed a new wavelet method for the characterization of the pointwise Hölder exponent HE and the relationship between Hölder regularity and local oscillation [27,28,31]. They give the formulation of the criterion in terms of local suprema of wavelet coefficients, called *Wavelet Leaders*. This alternative paves the way for a new multifractal formalism combining the advantages of WCMF and WTMM, as we will describe in the section.

## **5. Wavelet Leaders multifractal formalism**

Let  $\psi$  be an orthonormal wavelet, smooth, having fast decay and several null moments. It is centered in  $x_c = 1/2$  and it is essentially localized on the interval  $[0, 1]$ . We can suppose that each wavelet coefficient  $c_{jk}$  – corresponding to the wavelet transform of the signal  $f$  or of the series  $\{x(i)\}$  – is localized on the dyadic interval [32,34]  $I_{jk} = \left[ \frac{k}{2^j}, \frac{k+1}{2^j} \right)$ . We will denote  $3I_{jk} = \left[ \frac{k-1}{2^j}, \frac{k+2}{2^j} \right)$  the dilated intervals, recalling that we can choose other scaling factor  $M \geq 3$ .

The *Wavelet Leaders*  $d_{jk}$  are defined as follow:

$$d_{jk} = \sup\{|c_{lh}| : I_{lh} \subset 3I_{jk}\}. \tag{21}$$

The last definition indicates that to compute  $d_{jk}$  we consider the indexes  $2^{l-j}(k - 1) \leq h \leq 2^{l-j}(k + 2)$ , for each  $l \geq j - 1$ .

The set function:

$$\mu_{wl}(3I_{jk}) = d_{jk}, \tag{22}$$

is an increasing non-negative function, that is, if  $3I_{j'k'} \subset 3I_{jk}$  then  $d_{j'k'} \leq d_{jk}$  and it follows that  $\mu_{wl}(3I_{j'k'}) \leq \mu_{wl}(3I_{jk})$ .

Moreover, it is proved in Refs. [27,28,30], the suitable correlation between the Wavelet Leaders and the pointwise Hölder regularity:

Let  $I_j(x_0)$  the unique dyadic interval containing the point  $x_0$  and  $d_j(x_0)$  the corresponding *Wavelet Leaders*. If  $f \in C^\alpha(x_0)$  then, for all  $j > 0$ ,

$$|d_j(x_0)| \leq C 2^{-j\alpha} \tag{23}$$

for some constant  $C > 0$ .

If we compare the last relation with Eq. (12), it is possible to consider that the Wavelet Leaders lead us to compute a suitable structure formula for the full parameter range and that this fact do not ceases when the method is applied to signal embodying oscillating singularities, [27,28].

Then, it defines the scaling function:

$$S_{wl}(q, j) = 2^{-j} \sum_{k \in K_j} d_{jk}^q \tag{24}$$

where  $K_j$  is the index set such that  $|c_{jk}| > 0$  at last for some  $I_{lh} \in I_{jk}$ , [27].

So, following the development given in Eqs. (2) and (3) and Eqs. (15) and (16), it is possible to deduce:

$$\eta_{wl}(q) = \liminf_{j \rightarrow +\infty} \frac{\log(S_{wl}(q, j))}{\log(2^j)} \tag{25}$$

Since the above referred properties of  $\mu_{wl}$  the function  $\eta$  is concave. Supposing that the spectrum  $d_f$  is also concave, we can complete the multifractal formalism, in the following way:

$$d_f(H) = \inf_q (1 - \eta_{wl}(q) + Hq) \tag{26}$$

and both methods (MFDA and WL) are framed into the Multifractal formalism.

Let us analyze the number of operations needed for each method.

For the MFDA the critical steps occur when the local trends are calculated. The other steps only requires:  $O(N)$  sums for obtaining the profile, no more than  $O(N^2)$  indexing operations (the time for this is despicable respect the products) and  $O(N)$  products for taking log-log slopes and for performing the Legendre Transform in order to finally compute the spectrum. But the  $m - MFDA$  requires for each window length  $s$  under consideration at least  $(m + 2)^2 \cdot s \cdot 2N_s + (s + 1) \cdot 2N_s + 2N_s + 2s \approx 2(m + 2)^2 N$  products to compute the least square fitting functions to obtain the variances and the fluctuation functions. On the other hand, for the WL the most lengthy stage is the proper computing of the wavelet coefficients which is of order  $O(N \log N)$  (due to preserving the Mallat's algorithm scheme) with a constant proportional to the quantify of nodes necessary to represent the orthonormal wavelet required, that it is related with the number of null moments needed to cancel the polynomials with degree up to the integer part of the maximal Hölder regularity of the signals. Then, the computational complexity of the WL algorithm is meaningful lower than the MFDA one.

## **6. An illustrative example: Cantor measures and Haar wavelets**

We consider a singular Borel measure  $\mu$  on the interval  $I = [0, 1)$ . Let  $a > 1$  an integer and for each integer  $j \geq 0$ , the intervals  $I_{jk} = [k, k + 1)/a^j$  for  $0 \leq k < a^j$ . These disjoint intervals cover  $I$  and  $|I_{jk}| = a^{-j}$ . Denoting by  $\mu_{jk} = \mu(I_{jk})$ ,  $K_j$  the index set corresponding to intervals with positive measure and  $m_j$  and  $M_j$  the respective minimum and maximum in  $K_j$ :

$$0 < m_j \leq \mu_{jk} \leq M_j \leq 1.$$

Observe that both  $m_j$  and  $M_j$  are decreasing in  $j$  and converge to 0.

Let the scaling function:

$$S(q, j) = a^{-j} \sum_{k \in K_j} \mu_{jk}^q$$

for real parameters  $q \neq 0$ . We can write:

$$S(q, j) = \begin{cases} a^{-j} m_j^q \sum_{k \in K_j} \left( \frac{\mu_{jk}}{m_j} \right)^q & \text{if } q < 0 \\ a^{-j} M_j^q \sum_{k \in K_j} \left( \frac{\mu_{jk}}{M_j} \right)^q & \text{if } q > 0. \end{cases}$$

Since  $card(K_j) \leq a^j$  we deduce:

$$1 \leq \sum_{k \in K_j} \left( \frac{\mu_{jk}}{m_j} \right)^q \leq a^j \quad \text{and} \quad 1 \leq \sum_{k \in K_j} \left( \frac{\mu_{jk}}{M_j} \right)^q \leq a^j$$

and, therefore,

$$a^{-j} m_j^q \leq S(q, j) \leq m_j^q \quad \text{and} \quad a^{-j} M_j^q \leq S(q, j) \leq M_j^q$$

or, equivalently:

$$\begin{aligned} -q \frac{\log_a m_j}{j} &\leq -\frac{\log_a S(q, j)}{j} \leq 1 - q \frac{\log_a m_j}{j} \\ -q \frac{\log_a M_j}{j} &\leq -\frac{\log_a S(q, j)}{j} \leq 1 - q \frac{\log_a M_j}{j} \end{aligned}$$

for  $q < 0$  and  $q > 0$ , respectively. Then we conclude that the function

$$\eta(q) = \liminf_{j \rightarrow +\infty} -\frac{\log_a S(q, j)}{j}$$

exists if  $(\log_a m_j)/j$  is bounded. Moreover, in this case,  $-\lim_{j \rightarrow +\infty} (\log_a m_j)/j$  and  $-\lim_{j \rightarrow +\infty} (\log_a M_j)/j$  are the slopes of the asymptotes of the curve  $\eta(q)$ .

Therefore the computation of the scaling function  $S_{j,q}$  and the estimation of  $\eta_q$  may be numerically unstable. Particularly, perturbed measures  $\tilde{\mu}_{jk} = \mu_{jk} + \epsilon_{jk}$  can incorporate arbitrary small non-zero values. Then, the re-definition of the admissible sets  $K_j$  become crucial to preserve the above exposed limits.

We give a brief illustration. Let  $1/2 < p_1 < 1$  and  $p_2 = 1 - p_1$  and the triadic intervals  $I_{jk} = [k, k + 1)/3^j$  for  $0 \leq k < 3^j$ . Let  $\mu([0, 1)) = 1$ . Then, a singular Cantor measure  $\mu$  is defined from the recursive scheme:

$$\begin{aligned} \mu(I_{j+1,3k}) &= p_1 \mu(I_{j,k}) \\ \mu(I_{j+1,3k+1}) &= 0 \\ \mu(I_{j+1,3k+2}) &= p_2 \mu(I_{j,k}). \end{aligned}$$

Denote  $\mu_{jk}$  these measures. For each  $j > 0$  we have  $2^j$  positive measures and we easily deduce:

$$S(q, j) = 3^{-j} \sum_{k \in K_j} \mu_{jk}^q = 3^{-j} (p_1^q + p_2^q)^j \tag{27}$$

and the bounds are  $m_{jk} = p_1^j$  and  $M_{jk} = p_1^j$ . Moreover:

$$\eta(q) = 1 - \log_3 (p_1^q + p_2^q). \tag{28}$$

The distribution function  $F(x)$  of the Cantor measure is a continuous function and we can compute the values  $F(3^{-j}(k))$ , on the triadic points.

Next, to illustrate how the wavelet methods work, we choose the Haar basis. The wavelet coefficients of  $F$  are:

$$d_{jk} = 2^j \left( \int_{2^{-jk}}^{2^{-j}(k+1/2)} F(x) \, dx - \int_{2^{-j}(k+1/2)}^{2^{-j}(k+1)} F(x) \, dx \right)$$

and the associated scaling function:

$$S_w(q, j) = 2^{-j} \sum_{k \in K_j^*} |d_{jk}|^q \tag{29}$$

where  $K_j^*$  is the index set of positive values  $|d_{jk}|$ . Observe that, since  $F(x)$  is continuous, we can approximate the Haar coefficients as:

$$|d_{jk}| \cong 2^{-2} (F(2^{-j}(k + 1)) - F(2^{-j}k)). \tag{30}$$

We can estimate these values from:

$$F(2^{-j}k) \cong F(3^{-h}n) \tag{31}$$

where  $h = h(j)$  is the integer nearest to  $j \log 2 / \log 3$  and  $3^{-h}n$  is the nearest point to  $2^{-j}k$ .

Then

$$|d_{jk}| \cong 2^{-2} (F(3^{-h}(n + 1)) - F(3^{-h}n)) = 2^{-2} \mu_{h,n}. \tag{32}$$

The particular structure of the Cantor measure let us to prove that there is an unambiguous correspondence between positive values  $|d_{jk}|$  and positive measures  $\mu_{h,n}$ , then:

$$S_w(q, j) \cong 2^{-j-2} (p_1^q + p_2^q)^{\lfloor j \log 2 / \log 3 \rfloor} \tag{33}$$

and it follows the nice estimation of the function  $\eta(q)$  and the spectrum  $d_f(H)$ . We emphasize that the interpolation method leads us to a well conditioned estimation. On the other hand, bad alternatives will give distorted approximations for the function  $S_w(q, j)$ . This result can be extended in an analogous way to any wavelet coefficients or Wavelet Leaders methods.

## **7. Binomial multiplicative cascades**

Following, we consider a second process class which is inherently multifractal indeed, the binomial multiplicative cascades. It seems analogous to Cantor measures.

For this, consider for each integer  $j \geq 0$ , the dyadic intervals  $I_{jk} = [k, k + 1)/2^j$  for  $0 \leq k < 2^j$ . They are disjoint intervals covering  $I = [0, 1)$  and  $|I_{jk}| = 2^{-j}$ .

Let us consider again  $\mu([0, 1)) = 1$  and  $1/2 < p_1 < 1$  and  $p_2 = 1 - p_1$ . Then, a binomial cascade measure  $\mu$  is defined from the recursive scheme:

$$\begin{aligned} \mu(I_{j+1,2k}) &= p_1 \mu(I_{j,k}) \\ \mu(I_{j+1,2k+1}) &= p_2 \mu(I_{j,k}). \end{aligned} \tag{34}$$

Observe that for each step  $j$  the binomial cascades can be represented on dyadic points  $x_{jk} = k2^{-j}$ , by a finite series of length  $2^j$ :

$$y_{jk} = p_1^{(j-d(k))} p_2^{d(k)} \tag{35}$$

![A line graph showing the multifractal spectrum η versus H. The x-axis (H) ranges from 0.45 to 0.85, and the y-axis (η) ranges from 0 to 0.7. A solid blue curve represents the theoretical spectrum, peaking at approximately η = 0.65 when H = 0.65. A dotted blue curve represents the numerical series, which follows the theoretical curve closely. A series of green dots represents the spectrum estimated by the Wavelet Leaders method, also closely following the theoretical curve. The plot includes a grid with dotted lines.](91be14371a97fb5ce9eeb29ae18d07c3_img.jpg)

A line graph showing the multifractal spectrum η versus H. The x-axis (H) ranges from 0.45 to 0.85, and the y-axis (η) ranges from 0 to 0.7. A solid blue curve represents the theoretical spectrum, peaking at approximately η = 0.65 when H = 0.65. A dotted blue curve represents the numerical series, which follows the theoretical curve closely. A series of green dots represents the spectrum estimated by the Wavelet Leaders method, also closely following the theoretical curve. The plot includes a grid with dotted lines.

**Fig. 1.** Multifractal spectrum of the numerical series from the Cantor set with different weights,  $p_1 = 0.6$  and  $p_1 = 0.4$ . The little dots correspond to the analytical spectrum and the hole dots correspond to the spectrum estimated by the Wavelet Leaders method.

where  $d(k)$  is the numbers of digits,  $k_i = 1$ , of the dyadic expansion:

$$k = \sum_{i=1}^j k_i 2^i; \quad k_i \in \{0, 1\}. \tag{36}$$

For each  $j > 0$  we formulate:

$$S(q, j) = 2^{-j} \sum_{0 \leq k \leq 2^j} y_{jk}^q = 2^{-j} (p_1^q + p_2^q)^j \tag{37}$$

and

$$\eta(q) = 1 - \log_2 (p_1^q + p_2^q). \tag{38}$$

Moreover, the analytic expression of the HE and the MS can both be derived straightforwardly:

$$H(q) = \frac{d\eta(q)}{dq} = - \frac{p_1^q \log_2(p_1) + p_2^q \log_2(p_2)}{(p_1^q + p_2^q)} \tag{39}$$

and:

$$d_f(H) = \log_2 (p_1^q + p_2^q) - q \frac{p_1^q \log_2(p_1) + p_2^q \log_2(p_2)}{(p_1^q + p_2^q)}. \tag{40}$$

In analogous way as above was exposed, we can see that wavelet methods work as well as in Cantor measures processes.

## 8. Applications

### 8.1. Numerical series

We applied WL and MFDFA methods to the series generated from the Cantor Set and from the binomial multiplicative cascade. The Cantor measure was generated with weights  $p_1 = 0.60$  and  $p_2 = 0.40$  and for the binomial cascade we use the series generated with probabilities  $p_1 = 0.25$  and  $p_2 = 0.75$ . In both cases, we obtain a series with 4096 data points.

In Section 6, we demonstrate that the estimation to the MS using Haar wavelets has great precision (see Eq. (27)). We want to remark that this result is a particular one, because it uses the typical form of the Haar basis. As the aim of this work is to demonstrate the efficiency of the WL method, we use the Spline Wavelet Discrete Transform to build the MS of singularities.

Fig. 1 shows the theoretical MS and the one estimated with the WL method. The theoretical spectrum was calculated from Eqs. (39) and (40). Note that the high exactness of the WL estimation. On the other hand, Fig. 2 is the same spectrum but estimated with the MFDFA algorithm. The estimation is reasonable for the right side of the graphic but at the left side the estimation is not good. The left line of the singularities spectrum corresponds to the values  $q < 0$ , and the fluctuation function given by Eq. (8) is close to zero ( $F_q(s) \approx 0$ ) and the numerical estimations to calculate the Eq. (9) are very difficult. Then, the MFDFA results unstable for this kind of signals. On the other hand, the principal difficult to apply the WL method

![Fig. 2. Multifractal Spectrum of the numerical series from the Cantor set with different weights, p1 = 0.6 and p2 = 0.4. The plot shows the spectrum function \bar{\mu} on the y-axis (ranging from 0 to 0.7) against the singularity index H on the x-axis (ranging from 0.4 to 1.2). A solid blue curve represents the analytical spectrum, peaking at approximately H = 0.65 and \bar{\mu} = 0.65. Green dots represent the spectrum estimated by the Multifractal Detrended Fluctuation Analysis (MFDFA) method, which closely follow the analytical curve. Small open circles represent the analytical spectrum for different weights, showing a broader distribution.](7801d00a216dc4dc8a7d210dcb5fe3c5_img.jpg)

Fig. 2. Multifractal Spectrum of the numerical series from the Cantor set with different weights, p1 = 0.6 and p2 = 0.4. The plot shows the spectrum function \bar{\mu} on the y-axis (ranging from 0 to 0.7) against the singularity index H on the x-axis (ranging from 0.4 to 1.2). A solid blue curve represents the analytical spectrum, peaking at approximately H = 0.65 and \bar{\mu} = 0.65. Green dots represent the spectrum estimated by the Multifractal Detrended Fluctuation Analysis (MFDFA) method, which closely follow the analytical curve. Small open circles represent the analytical spectrum for different weights, showing a broader distribution.

Fig. 2. Multifractal Spectrum of the numerical series from the Cantor set with different weights,  $p_1 = 0.6$  and  $p_2 = 0.4$ . The little dots correspond to the analytical spectrum and the hole dots correspond to the spectrum estimated by the Multifractal Detrended Fluctuation Analysis method.

![Fig. 3. Multifractal spectrum for the binomial multiplicative cascade with p1 = 0.25 and p2 = 0.75. The plot shows the spectrum function \bar{\mu} on the y-axis (ranging from 0 to 1) against the singularity index H on the x-axis (ranging from 0.4 to 2). A solid blue curve represents the analytical spectrum, peaking at approximately H = 1.1 and \bar{\mu} = 1.0. Green dots represent the spectrum estimated by the Wavelet Leaders (WL) method, which follow the analytical curve very closely. Small open circles represent the analytical spectrum for different weights, showing a broader distribution.](6b32b7b928d34eeccb15c29cdf9d2cb3_img.jpg)

Fig. 3. Multifractal spectrum for the binomial multiplicative cascade with p1 = 0.25 and p2 = 0.75. The plot shows the spectrum function \bar{\mu} on the y-axis (ranging from 0 to 1) against the singularity index H on the x-axis (ranging from 0.4 to 2). A solid blue curve represents the analytical spectrum, peaking at approximately H = 1.1 and \bar{\mu} = 1.0. Green dots represent the spectrum estimated by the Wavelet Leaders (WL) method, which follow the analytical curve very closely. Small open circles represent the analytical spectrum for different weights, showing a broader distribution.

Fig. 3. Multifractal spectrum for the binomial multiplicative cascade with  $p_1 = 0.25$  and  $p_2 = 0.75$ . The little dots correspond to the analytical spectrum and the hole dots correspond to the spectrum estimated by the Wavelet Leaders method.

is to discriminate the leader between the values very close to zero. Anyway, the performance of WL is much better than MFDFA method for this kind of signals.

Following, we have also considered a sampled binomial multiplicative cascade. We estimate the MS with WL and MFDFA methods and compare it with the analytic expressions of the theoretical spectrum given by Eqs. (39) and (40). Figs. 3 and 4 show the theoretical and the respectively estimation spectra. We have found better accuracy in the estimation made with WL that with the estimate made with MFDFA. We have proven with other couples of values  $p_1$  and  $p_2$  and the improvement in the estimate of the WL method it has stayed.

### 8.2. Natural data: EEG from an epileptic seizure

Also, we compare both estimators with a natural series corresponding to a EEG from an epileptic seizure, applying both methods to three natural series corresponding to an EEG from an epileptic seizure for the same subject. For all cases, we use the first period of the seizure corresponding to the tonic stages. The data are from a secondary generalized *tonic-clonic epilepsy seizure* from a female epileptic patient. The patient has diagnosis of pharmac-resistant epilepsy and no other accompanying disorders. Scalp electrodes with bimastoideal reference were applied following the 10–20 international system. Each signal was digitized at 409.6 Hz through a 12 bit A/D converter and filtered with an “anti-aliasing” 8 pole low pass Bessel filter, with a cutoff frequency of 50 Hz. Then, the signal was digitally filtered with a 1–50 Hz bandpass filter (physician frequency range of interest for diagnosis). The series were analyzed at the right central region, C4 derivation.

We had many evidences of the multifractal behavior of the EEG signals from an epileptic seizure and also in EEG from NO REM sleep [5,35,36]. For this work, we confirm this experimental evidence by using three different series corresponding to the tonic stages. We choose four parameters to characterize the spectrum. They are:  $H_{\min}$  and  $H_{\max}$  that correspond to the

![Figure 4: Multifractal spectrum for the binomial multiplicative cascade with p1 = 0.25 and p2 = 0.75. The plot shows the multifractal spectrum E(H) on the y-axis (ranging from 0 to 1) versus the Hölder exponent H on the x-axis (ranging from 0.4 to 2). The plot features a dense cluster of green dots representing the analytical spectrum, which forms a curve peaking at H=1.0 with E(H)=1.0. There are also several blue dots representing the spectrum estimated by the Multifractal Detrended Fluctuation Analysis (MFDA) method, which are scattered around the analytical curve, generally following its shape but with some deviations.](10c82dcc5f2c237961329dd29d65859c_img.jpg)

Figure 4: Multifractal spectrum for the binomial multiplicative cascade with p1 = 0.25 and p2 = 0.75. The plot shows the multifractal spectrum E(H) on the y-axis (ranging from 0 to 1) versus the Hölder exponent H on the x-axis (ranging from 0.4 to 2). The plot features a dense cluster of green dots representing the analytical spectrum, which forms a curve peaking at H=1.0 with E(H)=1.0. There are also several blue dots representing the spectrum estimated by the Multifractal Detrended Fluctuation Analysis (MFDA) method, which are scattered around the analytical curve, generally following its shape but with some deviations.

**Fig. 4.** Multifractal spectrum for the binomial multiplicative cascade with  $p_1 = 0.25$  and  $p_2 = 0.75$ . The dots correspond to the analytical spectrum and the hole dots correspond to the spectrum estimated by the *Multifractal Detrended Fluctuation Analysis* method.

**Table 1**

Comparison of WL and MFDA methods applied to three EEG series from an epileptic seizure (with numbers 1, 2 and 3). The parameters are:  $H_{\min}$ : minimum value of the Hölder exponents;  $H_{\max}$ : maximum value of the Hölder exponents;  $\Delta H$ : range of the Hölder exponents;  $H^*$ : the Hölder exponent corresponding to the maximum Hausdorff dimension.

|            | WL <sub>1</sub> | MFDA <sub>1</sub> | WL <sub>2</sub> | MFDA <sub>2</sub> | WL <sub>3</sub> | MFDA <sub>3</sub> |
|------------|-----------------|-------------------|-----------------|-------------------|-----------------|-------------------|
| $H_{\min}$ | 0.010           | 0.096             | 0.010           | 0.076             | 0.010           | 0.083             |
| $H_{\max}$ | 0.778           | 0.600             | 0.791           | 0.668             | 0.837           | 0.672             |
| $\Delta H$ | 0.768           | 0.505             | 0.781           | 0.591             | 0.827           | 0.590             |
| $H^*$      | 0.272           | 0.341             | 0.280           | 0.304             | 0.301           | 0.304             |

minimum and maximum of the Hölder set:  $H$ ; the range  $\Delta H = H_{\max} - H_{\min}$  and the  $H^*$  that corresponds to the Hölder of the maximum Hausdorff dimension (i.e.  $d_f(H^*) = \max(d_f)$ ).

Fig. 5 (a), (b) and (c) display the spectra estimated by WL and MFDA method for the three EEG series. In all cases, the length of the natural series is 4096 data points.

Table 1 synthesizes the results obtained through both methods for the three natural series. The range of Hölder exponents ( $\Delta H$ ) estimated by WL method is larger than the one estimated by MFDA method. However, the value of the Hölder exponent corresponding to the maximum  $H^*$  of each spectrum is coincident.

We conclude that for natural series, the efficiency of the both estimators is similar. Anyway, the algorithm of WL is notably faster than MFDA, according to the discussion of the Section 5.

## 9. Conclusions

In this work we studied the numerical estimation of multifractal spectrum for sampled or experimental data. In fact, we analyzed and compared Multifractal Detrended Fluctuation Analysis with the Wavelet Leaders method.

In our analysis we supposed that the data becomes from complex behaviors described by irregular continuous signals having multifractal structures, that is, pointwise Hölder exponents vary in a continuous range and the same irregular points are embedded in dense sets. We also supposed that the signals have self-similar structures or statistic self-similarity properties, to base the multifractal formalism scheme. We supposed that these properties allow us to detect and to characterize the fractal structures from a discrete and finite data set. We briefly described the multifractal formalism scheme to make understandable the above cited methods and their peculiarities. We had emphasized that the scaling function must be computed from positive measures of intervals covering the measure support. The efficiency of consecutive estimation using the Legendre Transform strongly depends on the stability of the scaling function calculation. In our opinion, these circumstances will make the main difference between the compared methods.

According with the literature, MFDA is suitable tool for natural series. It is based on a fixed covering of the domain and it can work with relative short series. It performs better than previous wavelet methods, as the wavelet modulus maxima (WTMM) [26].

On the other hand, WL is a novel and suitable improvement from the discrete wavelet transform well disposed towards singular measures or irregular continuous signals. Wavelets are naturally adapted to detect self-similarity phenomena because of their intrinsic time-scale structure. At the beginning the wavelet continuous transform was used for these purposes. Jaffard introduced the novel use of the Wavelet Leaders coefficients in the multiresolution scheme to aim the same objectives.

![Figure 5: Multifractal spectrum estimated from Multifractal Detrended Fluctuation Analysis (MFDA) and Wavelet Leaders (WL) methods. The figure consists of three subplots (a, b, c) showing the multifractal spectrum dH versus H. Each plot compares the MFDA method (fine solid line with asterisks) and the WL method (thick solid line). Subplot (a) is for series number 1, (b) for series number 2, and (c) for series number 3. The x-axis (H) ranges from 0 to 0.9, and the y-axis (dH) ranges from 0 to 1.0. The curves are symmetric and peak at dH = 1.0 for H ≈ 0.35.](f176174c2978785e86a8352bd45e322e_img.jpg)

Figure 5: Multifractal spectrum estimated from Multifractal Detrended Fluctuation Analysis (MFDA) and Wavelet Leaders (WL) methods. The figure consists of three subplots (a, b, c) showing the multifractal spectrum dH versus H. Each plot compares the MFDA method (fine solid line with asterisks) and the WL method (thick solid line). Subplot (a) is for series number 1, (b) for series number 2, and (c) for series number 3. The x-axis (H) ranges from 0 to 0.9, and the y-axis (dH) ranges from 0 to 1.0. The curves are symmetric and peak at dH = 1.0 for H ≈ 0.35.

**Fig. 5.** Multifractal spectrum estimated from *Multifractal Detrended Fluctuation Analysis* method (fine solid line with asterisks) and from *Wavelet Leaders* method (thick solid line) for the EEG tonic–clonic epileptic seizure series. (a) corresponds to the series number 1, (b) to the series number 2 and (c) to the series number 3.

Carrying on, we observed that MFDA method becomes unstable when the signal do not has compact support. Then, due the sparsely distribution of the positive values, the algorithm presents severe difficulty to compute the scaling function for negative values  $q < 0$ .

This is a frequent case for monofractal series [25] or some multifractal ones, as the **Cantor's measures**.

Opposed to that method, WL is stable even for sparse positive measures. However, we must apply a tight criterion to select the significant leader coefficients during the calculation. The criterion depends on the used wavelet and this task implies a more sophisticated algorithm. At this point we remark that, although Jaffard affirms that WL method does not depend on the type of wavelet bases used, in practice this is not fully true.

We also observed that WL estimation becomes efficient with a reasonable great number of scales. For this reason it requires a relative large number of samples.

Comparing the computational complexity, we deduce that WL algorithm seems better than the **MFDA one**. The first is based on Mallat's scheme and it has complexity  $O(N \log N)$  for  $N$  entries. On the other hand, an upper bound for the MFDA complexity can be estimated in  $O(N^2)$ . Here, the critical steps occur when the local trends are calculated and strongly depend on the windows length  $s$ .

Following, we exposed several applications. For WL method we choose orthogonal spline wavelets. For the natural series, we provide empirical evidence of the multifractality in the data of EEG from an epileptic seizure at the tonic stage. In these cases we can conclude that both methods seem to be efficient estimators. Here we can conjecture that accordance is due to the weakly stationarity behavior of the signal and it is not sparse. We also observed that **the fractal spectrum** given by the WL is wider than the MFDA one. The main differences appear when we analyzed the Cantor measures or the binomial cascades. In this case, the measures have sparse supports and MFDA collapses, while WL gives us nice estimations. These special cases give us the chance to adjust the WL method to a toy model based on the canonical example given by the Haar functions in item 6. In fact, we also obtained and showed nice results using orthogonal cubic splines wavelets, an usual and efficient alternative.

In summary we conclude that **WL performs better than MFDDA**. However, for natural or stationary and short series the latter is a suitable and comprehensible tool. Both methods are open for future improvements and more refined strategies form an interesting research line.

## Acknowledgments

We wish to thank Universidad de San Martín and Universidad Nacional de General Sarmiento for support. This work was partially supported by Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET) and by Agencia para la Promoción Científica y Técnica, Argentina, Grant PICT2004 N<sup>o</sup> 20648.

## References

- [1] B.B. Mandelbrot, A multifractal walk down wall street, *Sci. Am.* 280 (1999) 70–73.
- [2] H.E. Stanley, L.A. Amaral, P. Gopikrishnan, P.Ch. Ivanov, T.H. Keitt, V. Plerou, Scale invariance and universality: Organizing principles in complex systems, *Physica A* 281 (2000) 60–68.
- [3] Y. Ashkenazy, P.Ch. Ivanov, S. Havlin, Ch.-K. Peng, A.L. Goldberger, H.E. Stanley, Magnitude and sign correlations in heartbeat fluctuations, *Phys. Rev. Lett.* 86 (9) (2001) 1900–1909.
- [4] L. Telesca, V. Iapenna, M. Macchiato, Multifractal fluctuations in seismic interspike series, *Physica A* 354 (2005) 629–640.
- [5] A. Figliola, E. Serrano, J.A.P. Rostas, M. Hunter, O.A. Rosso, Study of EEG brain maturation signals with multifractal detrended fluctuation analysis, in: O. Descalzi, O.A. Rosso, H.A. Larrondo (Eds.), *Proceedings of Nonequilibrium Statistical Mechanics and Nonlinear Physics, XV Conference, American Institute of Physics*, 2007, pp. 190–195.
- [6] L. Zunino, B. Tabak, A. Figliola, D.G. Perez, M. Garavaglia, O.A. Rosso, A multifractal approach for the stock market inefficiency, *Physica A* 387 (2008) 26–37.
- [7] K. Falconer, *Techniques in Fractal Geometry*, John Wiley and Sons Ltd, New York, 1997.
- [8] K. Falconer, *Fractal Geometry. Mathematical Foundations and Applications*, John Wiley and Sons Ltd, Chichester, 1990.
- [9] H.E. Stanley, N. Ostrowsky, *On Growth and Form: Fractal and Non-Fractal Patterns in Physics*, Nijhoff, Dordrecht, 1985.
- [10] L. Pietronero, E. Tosatti, *Fractals in Physics*, North-Holland, Amsterdam, 1986.
- [11] P. Grassberger, On the Hausdorff dimension of fractal attractors, *J. Stat. Phys.* 26 (1981) 173–179.
- [12] P. Grassberger, Procaccia measuring the strangeness of strange attractors, *Physica D* 9 (1983) 189–208.
- [13] P. Grassberger, Estimating the fractal dimensions and entropies of strange attractors, *Chaos* 1 (1986) 291–311.
- [14] A. Chhabra, R. Jensen, Direct determination of the  $f(\alpha)$  spectrum, *Phys. Rev. Lett.* 62 12 (1989) 1327–1330.
- [15] A. Chhabra, C. Maineau, R. Jensen, K.R. Sreenivasan, Direct determination of the  $f(\alpha)$  spectrum and its application on fully develop turbulence, *Phys. Rev. A* 40 9 (1989) 5284–5294.
- [16] J.F. Muzy, E. Bacry, A. Arneodo, Wavelets and multifractal formalism for singular signals: Application to turbulence data, *Phys. Rev. Lett.* 67 (1991) 3515–3518.
- [17] E. Bacry, A. Arneodo, J.F. Muzy, Singularity spectrum of fractal signals from wavelet analysis: Exact results, *J. Stat. Phys.* 70 (1993) 635–674.
- [18] A. Arneodo, A. Argoul, J.F. Muzy, M. Tabard, E. Bacry, Beyond classical multifractal analysis using wavelets: Uncovering a multiplicative process hidden in the geometrical complexity of diffusion limited aggregates, *Fractals* 1 (1995) 629–646.
- [19] C.K. Peng, S.V. Buldyrev, A.L. Goldberger, S. Havlin, R.N. Mantegna, M. Simons, H.E. Stanley, Statistical properties of DNA sequences, *Physica A* 221 (1995) 180–192.
- [20] R.B. Govindana, J.D. Wilsona, H. Preil, H. Eswaran, J.Q. Campbell, C.L. Lowery, Detrended fluctuation analysis of short datasets: An application to fetal cardiac data, *Physica D* 226 (2007) 23–31.
- [21] C.-K. Peng, S. Havlin, H.E. Stanley, A.L. Goldberger, Quantification of scaling exponents and crossover phenomena in nonstationary heartbeat time series, *Chaos* 5 (1995) 82–87.
- [22] H.E. Stanley, et al., Anomalous fluctuation in the dynamics of complex systems from DNA and physiology to econophysics, *Physica A* 224 (1996) 545–552.
- [23] C.P. Pan, B. Zheng, Y.Z. Wu, X.W. Tang, Detrended fluctuation analysis of human brain electroencephalogram, *Phys. Lett. A* 329 (2004) 130–135.
- [24] A. Castro e Siva, J.G. Moreira, Roughness exponents to calculate multi/affine fractal exponents, *Physica A* 235 (1997) 327–333.
- [25] J.W. Kantelhardt, S.A. Zschiegner, E. Koscielsny-Bunde, S. Havlin, A. Bunde, H.E. Stanley, Multifractal detrended fluctuation analysis of nonstationary time series, *Physica A* 316 (2002) 87–114.
- [26] P. Oświecińska, J. Kwapiński, S. Drożdż, Wavelet versus detrended fluctuation analysis of multifractal structures, *Phys. Rev. E* 74 (2006) 8–17.
- [27] S. Jaffard, Wavelet techniques in multifractal analysis, fractal geometry and applications: A jubilee of Benoit Mandelbrot, in: M. Lapidus, M. van Franchenhuysen (Eds.), *Proceedings of Symposia in Pure Mathematics Providence, AMS*, 2004, pp. 91–151, 72, part 2.
- [28] B. Lashermes, S. Jaffard, P. Abry, Wavelet Leaders in multifractal analysis, in: *Proceedings of IEEE International Conference on Acoustics, Speech, and Signal, in: IEEE Acoustics, Speech and Signal*, 4, 2005, pp. 161–164.
- [29] S. Jaffard, Some mathematical results about the multifractal formalism for functions, in: C. Chui, L. Montefusco, L. Puccio (Eds.), *Wavelets: Theory, Algorithms, and Applications*, Academic Press, 1994, pp. 325–362.
- [30] S. Jaffard, Multifractal formalism for functions, Parts 1: Results valid for all functions and Part 2: Selfsimilar functions, *SIAM Journal of Mathematical Analysis* 28 (4) (1997) 944–998.
- [31] B. Lashermes, S.C. Roux, P. Abry, S. Jaffard, Comprehensive multifractal analysis of turbulent velocity using Wavelet Leaders, *Eur. Phys. J. Cond. Mat. and Compl. Syst.* 61 (2) (2008) 201–205.
- [32] S. Mallat, *A Wavelet Tour of Signal Processing*, Academic Press, San Diego, 1999.
- [33] U. Frisch, G. Parisi, Fully developed turbulence and intermittency, in: *Proc. Internat. School Phys. Enrico Fermi, North Holland*, 1985, pp. 84–88.
- [34] Y. Meyer, *Ondelettes et Opérateurs*, Hermann, 1990.
- [35] A. Figliola, E. Serrano, O.A. Rosso, Dynamic behavior of tonic-clonic epileptic seizures, *Eur. Phys. J.* 143 (2007) 117–123.
- [36] M. Rosenblatt, A. Figliola, Estudio del Espectro Multifractal de una Señal No Estacionaria con Multifractal Detrended Fluctuation Analysis, in: *AMCA Serie Mecánica Computacional*, XXVI, 2007, pp. 2162–2179.