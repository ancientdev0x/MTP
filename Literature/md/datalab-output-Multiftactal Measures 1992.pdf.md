

# MULTIFRACTAL MEASURES

CARL J. G. EVERTSZ<sup>†</sup> AND BENOIT B. MANDELBROT<sup>‡</sup>

Appeared in *Chaos and Fractals* by Heinz-Otto Peitgen, Hartmut Jürgens, Dietmar Saupe, Springer-Verlag, New York, Appendix B, 849–881 (1992)

Before we generalize [fractal sets to measures], it may be recalled that, among our uses of fractal sets [to describe nature], several involve an approximation. While discussing clustered errors, we repressed our conviction that, between the errors, the underlying noise weakens, but does not stop. While discussing the distribution of stars, we repressed our knowledge of the existence of interstellar matter, which is also likely to have a very irregular distribution. While discussing turbulence, we approximated it as having [nonfractal] laminar inserts. In addition, no new concept would have been needed to deal with the distribution of minerals. Between the regions where the abundance of a metal like copper justifies commercial mining, the density of this metal is low, even very low, but one does not expect any region of the world to be totally without copper. All these voids [within fractals sets] must now be filled – without, it is hoped, inordinately modifying the mental pictures we have achieved thus far. This Chapter will outline a way of reaching this goal, by assuming that various parts of the whole share the same nature.

Benoit B. Mandelbrot<sup>1</sup>

## 1 Introduction

The bulk of this book [1] is devoted to *fractal sets*. A set's visual expression is a region drawn in black ink against white paper (or in white chalk against a blackboard). A set's defining relation is an *indicator function*  $I(P)$ , which can only take two values:  $I(P) = 1$ , or  $I(P)$ ="true" if the point  $P$  belongs to the set  $S$ ; and  $I(P) = 0$ , or  $I(P)$ ="false," if  $P$  does not belong to  $S$ .

---

<sup>†</sup>Center for Complex Systems and Visualization, University of Bremen, Postfach 330 440, D-2800 Bremen 33, Germany

<sup>‡</sup>Mathematics Department, Yale University, Box 2155 Yale Station, New Haven, CT 06520, USA and Physics Department, IBM T. J. Watson Research Center, Yorktown Heights, NY 10598, USA

<sup>1</sup>Introduction to Chapter IX of *Les objets fractals: forme, hasard et dimension*, 1975. A related text appears in B. B. Mandelbrot, *The Fractal Geometry of Nature*, 1982.

However, as stated in the 1975 quote which opens this treatise, most facts about nature cannot be expressed in terms of the contrast between “black and white,” “true and false” or “1 and 0”. Therefore, those aspects cannot be illustrated by sets; they demand more general mathematical objects that succeed to embody the idea of “shades of grey.” Those more general objects are called *measures*.

It is most fortunate that the idea of self-similarity is readily extended from sets to measures. The goal of this treatise is to sketch the theory of self-similar measures, which are usually called *multifractals*. We shall include various heuristic arguments that are often used in this context and then (Section 4) describe the proper probabilistic background behind the concept of multifractals.<sup>2</sup> Against this background, the nature of the usual heuristic steps becomes clear, their limitations and proneness to error become obvious and the unavoidable generalizations demanded by both logic and the data become easy. However, these generalizations are beyond the scope of this treatise.

### 1.1 Simple Examples of Multifractals

Consider a geographical map of a continent or an island. An example of a measure  $\mu$  on such a map is “the quantity of groundwater.” To each subset  $\mathcal{S}$  of the map, the measure attributes a quantity  $\mu(\mathcal{S})$ , which is the amount of ground water below  $\mathcal{S}$  down to some prescribed level. Now divide the map into two equally-sized pieces  $\mathcal{S}_1$  and  $\mathcal{S}_2$ . It will not come as a surprise if their respective groundwater contents  $\mu(\mathcal{S}_1)$  and  $\mu(\mathcal{S}_2)$  are unequal. If  $\mathcal{S}_1$  is subdivided further into two equally sized pieces  $\mathcal{S}_{11}$  and  $\mathcal{S}_{12}$ , their groundwater contents would again differ. This subdivision could be extended until the pieces are the size of pores in rocks, where some pores are found filled with water and others are found empty. This is a familiar story: some countries have more groundwater than others; parts of a country contain more groundwater than others; you may drill a well and find flowing water, while your neighbor finds none; and so forth. Many other quantities exhibit the same behavior, that is, the quantity

$$\mu = \text{the amount of ground water below } \mathcal{S}$$

is an example of a measure which is irregular at all scales.

When the irregularity is *the same* at all scales, or at least statistically the same, one says that the measure is *self-similar*, or that it is a *multifractal*. A Sierpiński gasket is a self-similar *set* in the sense that each piece (however small) is identical to the whole after some rescaling and translation; something similar holds for multifractal measures.

---

<sup>2</sup>The probabilistic approach to multifractals was first described in two papers by B.B. Mandelbrot:

Mandelbrot, B.B., *Intermittent turbulence in self-similar cascades: divergence of high moments and dimension of the carrier* J. Fluid Mech. **62** (1974) 331.

Mandelbrot, B.B., *Multiplications aléatoires itérées et distributions invariantes par moyenne pondérée aléatoire*, I & II, Comptes Rendus (Paris): 278A (1974) 289-292 & 355-358.

These papers, together with related ones, will soon be reissued in Mandelbrot, B.B., *Selecta Volume N, Multifractals & 1/f Noise: 1963-76*, Springer, New York.

#### The Chaos Game and the Pascal Triangle

Examples of multifractal measures have already entered in previous chapters of this book. One example is the *chaos game* that corresponds to an iterated function system (IFS) that is run with unequal probabilities  $p_1 = 0.5, p_2 = 0.3$  and  $p_3 = 0.2$  for the various reducing similarities in Section 6.3 of Reference [1], and the other example is the Pascal triangle mentioned in Chapter 8 of Reference [1], and further discussed in Section 2.2. Let us explore the Sierpiński IFS more closely.

We saw that playing the chaos game long enough produces a Sierpiński gasket with fractal dimension  $D = \log 3 / \log 2$ . We also found that the subtriangles making up the Sierpiński gasket were visited with different probabilities, which are summarized in Figures 6.22 and 6.23 in Reference [1] for the first two levels. These Figure have been reproduced in Figure 1.

![Figure 1: Multiplicatively generated probabilities at the levels 1 and 2 of the Sierpiński gasket. The figure consists of four triangular diagrams arranged in a 2x2 grid. The top row shows level 1: the left triangle is labeled 'addresses' with vertices 1, 2, and 3; the right triangle is labeled 'probabilities' with vertices 0.5, 0.3, and 0.2. The bottom row shows level 2: the left triangle is labeled 'addresses' with vertices 11, 12, 13, 21, 22, 23, 31, and 33; the right triangle is labeled 'probabilities' with vertices 0.25, 0.15, 0.10, 0.06, 0.06, 0.15, 0.10, and 0.04.](e863446d7d263c68be9402afd63668ac_img.jpg)

Figure 1: Multiplicatively generated probabilities at the levels 1 and 2 of the Sierpiński gasket. The figure consists of four triangular diagrams arranged in a 2x2 grid. The top row shows level 1: the left triangle is labeled 'addresses' with vertices 1, 2, and 3; the right triangle is labeled 'probabilities' with vertices 0.5, 0.3, and 0.2. The bottom row shows level 2: the left triangle is labeled 'addresses' with vertices 11, 12, 13, 21, 22, 23, 31, and 33; the right triangle is labeled 'probabilities' with vertices 0.25, 0.15, 0.10, 0.06, 0.06, 0.15, 0.10, and 0.04.

Figure 1: Multiplicatively generated probabilities at the levels 1 and 2 of the Sierpiński gasket. The 3-dimensional rendering of the coarse measure at the 8<sup>th</sup> stage of a trinomial multiplicative cascade is shown in Figure 2. This illustration is a reproduction from Reference [1].

A very rough examination of the first figure indicates that the subset with address 3 seems to include a smooth distribution of hitting probabilities. But closer examination reveals an irregular distribution among its subsets with addresses 31, 32 and 33. The same holds for the parts 1, 2 and, as a closer examination reveals, a part such as 32. We also see that if part  $3 = \{31, 32, 33\}$  is blown up by a factor 2,

while its component probabilities are multiplied by a factor 5, we achieve not only a geometric fit but also a fit of the probabilities to those at level 1 in Figure 1. Again, the same holds for parts 1 and 2 with factors 2 and  $3\frac{1}{3}$ , respectively. Hence, up to a numerical factor, the distribution of the hitting probabilities is the same in each of the subsets 1, 2 and 3. If such an exact invariance holds for all scales, the overall distribution is said to be *linearly self-similar*. For the random IFS this invariance is exactly the invariance under the Markov operator defined on page 331 in Reference [1] and discussed later. The multifractal measure produced by the random IFS is simply the probability of hitting a subset of the triangle. The distribution of these probabilities is shown in Figure 2. The Sierpiński IFS can be interpreted as

![A 3D visualization of the self-similar density of hitting probabilities for a Sierpiński gasket at stage 8. The plot shows a complex, fractal-like structure with many sharp, vertical spikes of varying heights, representing the density of hits. The base of the structure is a triangular shape, and the overall pattern is highly symmetric and self-similar.](e94f3bbb6f7501b9a1344dd0210e5dd8_img.jpg)

A 3D visualization of the self-similar density of hitting probabilities for a Sierpiński gasket at stage 8. The plot shows a complex, fractal-like structure with many sharp, vertical spikes of varying heights, representing the density of hits. The base of the structure is a triangular shape, and the overall pattern is highly symmetric and self-similar.

Figure 2: The self-similar density of hitting probabilities of the IFS on stage 8 of the Sierpiński gasket. This is a 3-dimensional rendering of Fig. 6.22. The height of the function above each sub-triangle is proportional to the number of hits in the limit of infinite game points. In order to draw this illustration we did not play the game infinitely long, but instead we used the fact that this distribution is the 8<sup>th</sup> stage of a trinomial multiplicative cascade with  $m_0 = p_1, m_1 = p_2$  and  $m_2 = p_3$ , where the  $p_i$  are the probabilities for the different contractions in the random IFS discussed on page 346, i.e.  $p_1 = 0.5, p_2 = 0.3$  and  $p_3 = 0.2$ .

a caricature model for the above groundwater example by taking the total quantity of groundwater as unity and by identifying the quantity of groundwater with the hitting probability.

#### A Measure-generating Multiplicative Cascade

Another way to look at the Sierpiński IFS measure is suggested by Figures 6.22 and 6.23 (reproduced in Figure 1) and Equation 6.3 in Reference [1]. We note that, while each triangle is further fragmented into 3 subtriangles, the measure  $\mu$  (or hitting probability) is also fragmented by factors  $p_1 = 0.5$ ,  $p_2 = 0.3$  and  $p_3 = 0.2$ . Denote the measure of the set with address 3 by  $\mu_3$ . Its 3 sub-parts with addresses 31, 32 and 33 carry the measures  $\mu_{31} = p_1\mu_3$ ,  $\mu_{32} = p_2\mu_3$  and  $\mu_{33} = p_3\mu_3$ . A single process fragments a *set* into smaller and smaller components according to a fixed rule and at the same time fragments the *measure* of the components by another rule. Such a process is called a multiplicative process or cascade.

Multiplicative processes are a very important paradigm in the theory of multifractals and play a central role in this treatise. In the language of multiplicative processes, the fragmentation ratios  $p_i$  are usually called *multipliers* and are denoted by  $m$  with various indices. In the Sierpiński IFS, the fragmentation of the set yields a fractal. This feature is a complication and is not essential. To avoid it, most of this Appendix uses multiplicative rules that operate over an ordinary Euclidean set, usually the unit interval, but are such that the measure is fragmented non-trivially.

### 1.2 Characterization of Multifractals

Let us step back and apply the idea of a box-counting dimension to the set  $\mathcal{S}$  supporting a measure (in the IFS example  $\mathcal{S}$  was the Sierpiński gasket). One covers  $\mathcal{S}$  with a collection of boxes of size  $\epsilon$ . One evaluates the number  $N(\epsilon)$  of boxes needed to cover the object, and one finds the dimension  $D$  through the scaling relation  $N(\epsilon) \sim \epsilon^{-D}$ . However, simply counting the boxes is like counting coins without caring about the denomination. When the set supporting the measure is Euclidean – as it will be in this treatise – the value of its fractal dimension only confirms that there is nothing fractal about this support. Thus, knowledge of  $D$  is not sufficient to give a quantitative description of the self-similar measure supported by this set. Instead, the measure contained in each box must somehow be given a weight.

A priori, the obvious weight would be the average density of probability in each box. In a Euclidean space of dimension  $E$  (or, more generally, in a space of embedding dimension  $E$ ), the density is simply defined as  $\mu(\mathcal{S})/\epsilon^E$ . When this density varies slowly, it can be mapped in the form of a relief or in the form of lines of constant height. As  $\epsilon \rightarrow 0$ , one expects this relief to tend to a limit. Furthermore, to characterize the irregularity of the spatial distribution of a measure, the first step – but not the last! – is to draw the familiar frequency distribution of its density. If the measure is random, one draws either the frequency distribution of the density in a sample or its probability distribution.

However, in the case of self-similar measures, this familiar process loses all meaning simply because, as we shall see, the density itself loses all meaning. Instead, the loose notion that ordinarily leads to a density becomes embodied in a very different and more complicated quantity,

$$\alpha = \frac{\log \mu(\text{box})}{\log \epsilon},$$

called the *coarse Hölder exponent*. This quantity  $\alpha$  is the logarithm of the measure of the box divided by the logarithm of the size of the box. For a large class of self-similar measures,  $\alpha$  is restricted to an interval  $[\alpha_{\min}, \alpha_{\max}]$ , where  $0 < \alpha_{\min} < \alpha_{\max} < \infty$ . But the study of some of the most interesting multifractal phenomena (such as turbulence or aggregation of particles into clusters) often demands  $\alpha_{\min} = 0$  and/or  $\alpha_{\max} = \infty$ .

Once  $\alpha$  has been defined, the first step – but not the last! – is just as above: to draw the frequency distribution of  $\alpha$ , as follows. For each value  $\alpha$ , one evaluates the number  $N_\epsilon(\alpha)$  of boxes of size  $\epsilon$  having a coarse Hölder exponent equal to  $\alpha$ . Now suppose that a box of side  $\epsilon$  has been selected at random among boxes whose total number is proportional to  $\epsilon^E$ . The probability of hitting the value  $\alpha$  of the coarse Hölder exponent is  $p_\epsilon(\alpha) = N_\epsilon(\alpha)\epsilon^{-E}$ . Again, the first impulse would be to draw the distribution of this probability, but this drawing would not be useful. In the case of interest to us, this distribution no longer tends to a limit as  $\epsilon \rightarrow 0$  hence, an intrinsic characteristic is to be found elsewhere.

The considerations to be explored in detail in this paper will show that it is necessary, instead, to take weighted logarithms and to consider either of the functions

$$f_\epsilon(\alpha) = \frac{\log N_\epsilon(\alpha)}{\log \epsilon} \quad \text{or} \quad (1)$$

$$C_\epsilon(\alpha) = \frac{-\log p_\epsilon(\alpha)}{\log \epsilon}. \quad (2)$$

As  $\epsilon \rightarrow 0$ , both  $f_\epsilon(\alpha)$  and  $C_\epsilon(\alpha)$  tend to well-defined limits  $f(\alpha)$  and  $C(\alpha)$ . The function  $C(\alpha)$  is more widely applicable, but the function  $f(\alpha)$  is more widely known. When  $f(\alpha)$  exists one has

$$C(\alpha) = f(\alpha) - E. \quad (3)$$

The definition of  $f(\alpha)$  means that, for each  $\alpha$ , the number of boxes increases for decreasing  $\epsilon$  as  $N_\epsilon(\alpha) \sim \epsilon^{-f(\alpha)}$ . The exponent  $f(\alpha)$  is a continuous function of  $\alpha$ . In the simplest cases, the graph of  $f(\alpha)$  ( often called  $f(\alpha)$  curve ) is shaped like the mathematical symbol  $\cap$ , usually leaning to one side. The values of  $f(\alpha)$  could be interpreted loosely as a fractal dimension of the subsets of boxes of size  $\epsilon$  having coarse Hölder exponent  $\alpha$  in the limit as  $\epsilon \rightarrow 0$ . As  $\epsilon \rightarrow 0$ , there is an increasing multitude – increasing to infinity – of subsets, each characterized by its own  $\alpha$  and a fractal dimension  $f(\alpha)$ . This is one of several reasons for the term *multifractal* [2].

### 1.3 Summary

This Appendix restricts itself to the simplest multiplicatively generated multifractal measures. For the more delicate examples of multifractal measures, it refers the reader to the literature. We have already seen a close connection between the IFS and multiplicative processes. Section 2.2 will digress to discuss the multiplicative process that lurks behind the Pascal triangle in Figures 8.14 and 8.32 in Reference [1]. There is evidence that multiplicative processes can account for many multifractal measures such as those related to the electrostatic charge distribution (the harmonic measure) on fractal boundaries [3], wavefunctions [4] and random resistor networks [5]. But this evidence does not mean that every self-similar measure is

multiplicatively generated. For example, many models for the multifractality of the dissipation field in turbulence are based on multiplicative processes, but a physical counterpart remains elusive.

The very simplest multiplicatively generated self-similar measure is the binomial measure. For it,  $f(\alpha)$  will be evaluated in three ways: the histogram method [6, 7], the method of moments [2, 8] and large deviation theory [6, 7]. The method of moments<sup>3</sup> is easy to use mechanically, and therefore it has been applied very widely. In our first three sections, the only prerequisite for the reader is elementary analysis. Section 4 goes further and casts self-similar measures in their proper probabilistic setting. It shows that multiplicatively generated multifractal measures are intimately related to a standard topic in probability theory, namely, the behavior of sums of random variables. The method of moments and the histogram method are consequences of the theory of large deviations in such sums. While it is more technical, Section 4 requires no prior knowledge of sums of random variables nor of large deviation theory. The conceptual superiority of the probabilistic approach has immediate practical consequences: it is more general. It explains the nature of various mechanical manipulations and provides tools to handle and to understand self-similar measures to which the method of moments fails to apply. Hence, Section 4 of this treatise is an introduction to more advanced literature.

The reader may want to consult other books, reviews or articles about multifractals. For examples see References [9, 10, 11, 12, 6, 7].

## 2 The Binomial and Multinomial Measures

The Introduction discussed the central role that multiplicative processes play in the theory of multifractal measures. This section concerns the very simplest multiplicative process, one that generates the binomial measures. A binomial measure appears naturally in the Pascal triangle of Figures 8.14 and 8.32 in Reference [1], and, with a little modification ( the replacement of the binomial by the trinomial), it links to the IFS discussed in the Introduction.

### 2.1 A Measure-generating Multiplicative Cascade

Exact (or linear) self-similarity of measures is best illustrated with the binomial measures (also called the Bernoulli or Besicovitch measures) [6]. In the spirit of the construction of the exactly self-similar Sierpiński gasket through a geometric cascade, these measures  $\mu$  are recursively generated with the *multiplicative cascade* that is depicted schematically in Figure 3. This cascade starts ( $k = 0$ ) with a uniformly distributed unit of mass on the unit interval  $I = I_0 = [0, 1]$ . The next stage ( $k = 1$ ) fragments this mass by distributing a fraction  $m_0$  uniformly on the left half  $I_{0,0} = [0, \frac{1}{2}]$  of the unit interval and the remaining fraction  $m_1 = 1 - m_0$

---

<sup>3</sup>The earliest reference and the reference that is best known are, respectively,

Frisch, U., Parisi, G. *Fully developed turbulence and intermittency in Turbulence and Predictability of Geophysical Flows and Climate Dynamics*, edited by Ghil, M., Benzi, R. and Parisi, G., North-Holland, New York, p. 84 (1985)

Halsey, T.C., Jensen, M.H., Kadanoff, L.P., Procaccia, I. and Shraiman, B.I.: *Fractal measures and their singularities: The characterization of strange sets*. Phys. Rev. A **33** 1141 (1986)

![Figure 3: A diagram illustrating the multiplicative cascade generating a binomial measure. The left side shows a tree structure of dyadic intervals. The root interval [0, 1] is split into [0, 1/2] and [1/2, 1] with masses m_0 and m_1. These are further split into [0, 1/4], [1/4, 1/2], [1/2, 3/4], and [3/4, 1] with masses m_0, m_1, m_0, m_1. The intervals are labeled 00, 01, 10, 11. The right side shows the corresponding density functions at each stage, which become increasingly complex and oscillatory as the cascade progresses.](c3c305cefbac2e7b13be34ab87054d1e_img.jpg)

Figure 3: A diagram illustrating the multiplicative cascade generating a binomial measure. The left side shows a tree structure of dyadic intervals. The root interval [0, 1] is split into [0, 1/2] and [1/2, 1] with masses m\_0 and m\_1. These are further split into [0, 1/4], [1/4, 1/2], [1/2, 3/4], and [3/4, 1] with masses m\_0, m\_1, m\_0, m\_1. The intervals are labeled 00, 01, 10, 11. The right side shows the corresponding density functions at each stage, which become increasingly complex and oscillatory as the cascade progresses.

Figure 3: The multiplicative cascade generating a binomial measure. At each stage the mass of each of the previous dyadic intervals is redistributed as follows: A fraction  $m_0$  goes to the left half, and  $m_1 = 1 - m_0$  goes to the right half. Here we took  $m_0 = \frac{2}{3}$  and  $m_1 = \frac{1}{3}$ . The density of the measure is shown for the first eight stages. The scales on the coordinate axes have been kept the same throughout the figure. The actual measure of a dyadic interval is the integral of this density. For example, the measures of the four intervals of size  $\frac{1}{4}$  at stage 2 are  $m_0 m_0, m_0 m_1, m_1 m_0$  and  $m_1 m_1$ .

uniformly on the right half  $I_{0,1} = [\frac{1}{2}, 1]$ . At this stage, the left half carries the measure  $\mu(I_{0,0}) = m_0$  and the right half carries the measure  $\mu(I_{0,1}) = m_1$ . In this process, because  $\mu(I_0) = \mu(I_{0,0}) + \mu(I_{0,1}) = m_0 + m_1 = 1$ , the original measure of the unit interval is conserved. The  $\mu$ 's appear like probabilities, and one says that  $\mu$  is a probability measure.

At the next stage ( $k = 2$ ) of the cascade, the subintervals  $I_{0,0}$  and  $I_{0,1}$  receive the same treatment as the original unit interval. That is,  $I_{0,0}$  is split into the intervals  $I_{0,00} = [0, \frac{1}{4}]$  and  $I_{0,01} = [\frac{1}{4}, \frac{1}{2}]$  of size  $2^{-k}$ , and the mass is fragmented further. Similarly,  $I_{0,1}$  is split into a left half  $I_{0,10}$  and a right half  $I_{0,11}$ . Writing  $\mu(I_{0,00}) = \mu_{0,00}$  for the measure of interval  $I_{0,00}$ , and similarly for the other intervals, this second stage of the cascade yields

$$\mu_{0,00} = m_0 m_0 \ ; \ \mu_{0,01} = m_0 m_1 \ ; \ \mu_{0,10} = m_1 m_0 \ ; \ \mu_{0,11} = m_1 m_1 .$$

The condition  $m_0 + m_1 = 1$  continues to insure that the original unit of mass is conserved.

At the  $k^{\text{th}}$  stage of the cascade, the mass is fragmented over the *dyadic intervals*  $[i2^{-k}, (i+1)2^{-k})$ , where  $i = 0, \dots, 2^k - 1$ . Recall that a point  $x \in [0, 1]$  is said to have the binary expansion  $0.\beta_1\beta_2\dots\beta_k$  when  $x = \beta_1 2^{-1} + \beta_2 2^{-2} + \dots + \beta_k 2^{-k}$  with  $\beta_i \in \{0, 1\}$ . For dyadic points, like  $x = \frac{3}{4}$ , this expansion is ambiguous and may end with either an infinity of zeroes or an infinity of ones; in the present application, one must choose the former expansion. An arbitrary dyadic interval  $I^k = I_{0,\beta_1\beta_2\dots\beta_k}$  of size  $2^{-k}$  consists of all points  $x \in [0, 1]$  whose binary expansion starts with  $0.\beta_1\beta_2\dots\beta_k$ . For example,  $\beta_1 = 0$  if our interval  $I^k$  is in the left half  $I_0$  of the unit interval, and  $\beta_1 = 1$  if  $I^k$  lies in the right half  $I_1$ . Similarly,  $\beta_2 = 0$  if  $I^k$  lies in the left half of  $I_{\beta_1}$ , and so forth. Clearly, the measure of the dyadic interval  $I_{0,\beta_1\beta_2\dots\beta_k}$  equals

$$\mu_{0,\beta_1\beta_2\beta_3\dots\beta_k} = \prod_{i=1}^k m_{\beta_i} = m_0^{n_0} m_1^{n_1}, \quad (4)$$

where  $n_0$  is the number of digits 0 in the address  $0.\beta_1\beta_2\beta_3\dots\beta_k$  of the left end of the interval and  $n_1 = k - n_0$  is the number of digits 1. Since the binomial measure of each dyadic interval of size  $2^{-k}$  is the product of  $k$  multipliers  $m_\beta$ , it is called a measure generated by a multiplicative process.

The binomial multifractal measure is the measure  $\mu^B$  which attributes masses according to Equation 4 to the dyadic subintervals of the unit interval (*Note for the mathematically minded*: the measures  $\mu_{0,\beta_1\beta_2\beta_3\dots\beta_k}$  of all dyadic subintervals of the unit interval can be extended to a Borel field of subsets of  $[0, 1]$ ). The multiplicative cascade is a mechanism for producing this measure. In the case  $m_0 = m_1 = \frac{1}{2}$  this measure reduces to the uniform (Lebesgue) measure.

### 2.2 The Pascal Triangle and the Binomial Measure

This section is a digression that can be skipped with no loss of continuity. When viewed in a mirror, the distribution in Figure 8.32 in Reference [1] resembles closely the density of the binomial measure, as shown in Figure 3. This is not a coincidence. Remember that the height of the  $r^{\text{th}}$  column in Figure 8.32 in Reference [1] equals the number  $h(r)$  of black squares in the  $r^{\text{th}}$  row of the Pascal triangle (mod.2) in Figure 8.14 in Reference [1]. Turning the page  $90^\circ$  counterclockwise (so that the columns point upwards) and looking only at the black geometry of the triangle, one sees that the total number of black squares in the rows  $[4, 7]$  is twice the number in the rows  $[0, 3]$ , i.e.,  $\sum_{r=4}^7 h(r) = 2 \sum_{r=0}^3 h(r)$ . This factor of 2 turns out to be ubiquitous in this application. Every time one considers a block of rows  $[0, 2^k - 1]$ , its right half  $[2^{k-1}, 2^k - 1]$  contains twice as many black squares as its left half  $[0, 2^{k-1} - 1]$ . If this left half, in turn, splits into two halves of size  $2^{k-2}$ , one again finds the ratio 1 : 2 between the left and right, and so forth. To conclude: up to an overall factor, the numbers of black triangles in the columns of Figure 8.14 in Reference [1] have the same structure as those of the mirrored binomial multifractal in the  $k = 4$  stage of the multiplicative cascade shown in Figure 3. In general, one finds that  $3^{-k}h(r)$  is the binomial measure of the dyadic interval  $[r \cdot 2^{-k}, (r+1) \cdot 2^{-k}]$  for  $r = 0, \dots, 2^k - 1$ . This highly visual analogy establishes a relationship between the distribution  $h(r)$  of the Pascal triangle and the binomial measure  $\mu$  with multipliers  $m_0 = \frac{1}{3}$  and  $m_1 = \frac{2}{3}$ .

The formal connection between the triangle and the binomial multiplicative process follows from an earlier result (Section 8.5 in Reference [1]). There, Equation 8.18 states that for  $r = \beta_0 + \beta_1 2 + \beta_2 2^2 + \dots \beta_k 2^k$  with  $\beta_i \in \{0, 1\}$  (that is, if  $\beta_0 \beta_1 \dots \beta_k$  is the binary expansion of  $r$ ), one has

$$h(r) = h_2(r) = \prod_{i=0}^k (\beta_i + 1) = 1^{n_0} 2^{n_1} = 3^k \left(\frac{1}{3}\right)^{n_0} \left(\frac{2}{3}\right)^{n_1},$$

where  $n_0$  is the number of digits 0 in the expansion of  $r$  and  $n_1$  is the number of digits 1. Comparing this expression with Equation 4, one finds  $h(r) = 3^k \mu_{0, \beta_1 \beta_2 \dots \beta_k}$ , where  $\mu$  is the binomial measure with  $m_0 = \frac{1}{3}$  and  $m_1 = \frac{2}{3}$ . Note that we replaced the digit “ $\beta_0$ ” by “0.” to emphasize that  $0. \beta_1 \beta_2 \dots \beta_k$  stands for the dyadic subinterval of the unit interval as discussed in the previous section.

#### The Markov Operator $M(\nu)$ , the Binomial Measure and the Sierpiński IFS

It is important to mention in passing that both the binomial measure and the hitting probability of the IFS on the Sierpiński gasket are invariant measures of the Markov operator  $M(\nu)$  discussed on page 331 in Reference [1].

The binomial measure  $\mu^B$  with multipliers  $m_0$  and  $m_1$  is the invariant measure of the Markov operator  $M(\nu) = m_0 \nu w_1^{-1} + m_1 \nu w_2^{-1}$ , with

$$\begin{aligned} w_1(x) &= \frac{1}{2}x \\ w_2(x) &= \frac{1}{2}x + \frac{1}{2}. \end{aligned}$$

that is,  $M(\mu^B) = \mu^B$ .

The trinomial measure in Figure 2, which is associated with the random Sierpiński IFS in Section 6.3, is the invariant measure of  $M(\nu) = 0.5 \nu w_1^{-1} + 0.3 \nu w_2^{-1} + 0.2 \nu w_3^{-1}$ , with

$$\begin{aligned} w_1(x, y) &= \left(\frac{1}{2}x, \frac{1}{2}y\right) \\ w_2(x, y) &= \left(\frac{1}{2}x + 1, \frac{1}{2}y\right) \\ w_3(x, y) &= \left(\frac{1}{2}x + \frac{1}{2}, \frac{1}{2}y + \frac{1}{2}\sqrt{3}\right). \end{aligned}$$

### 2.3 Self-similarity and Singularities

#### Self-similarity

The Introduction briefly discussed the notion of self-similarity in the case of an IFS. We now discuss this notion in the case of the binomial measure. The measure of the arbitrarily selected interval  $I_{0, \beta_1 \beta_2 \dots \beta_k}$  is  $\mu_{0, \beta_1 \beta_2 \beta_3 \dots \beta_k}$  times smaller than that of the original unit interval, which had mass 1. Apart from this overall difference,

the mass in both these intervals is fragmented in exactly the same way. That is, consider the mass distribution on the interval  $I_{0,\beta_1\beta_2\beta_3\dots\beta_k}$  of the stage  $k + k'$  of the multiplicative cascade; then by spatially rescaling this subinterval by a factor  $2^k$ , and renormalizing its mass by a factor  $(\mu_{0,\beta_1\beta_2\beta_3\dots\beta_k})^{-1}$ , one recovers the mass distribution on the whole interval at the stage  $k'$  of the cascade. It is in this sense that the mass distribution (or the measure) is said to be self-similar. We now show that such self-similar measures are very singular, and discuss in more detail the notions of Hölder exponents  $\alpha$  mentioned in the Introduction.

#### The Coarse and the Local Forms of the Hölder Exponent

For the uniform measure (the Lebesgue measure), the density is 1 everywhere in  $[0, 1]$ ; i.e., the Lebesgue measure of an interval of size  $\epsilon$  is  $\epsilon$ . For the binomial measures, the situation is altogether different. Near  $\alpha = 0$ , Equation 4 shows that  $\mu([0, 2^{-k}]) = m_0^k = (2^{-k})^{v_0}$  with  $v_0 = -\log_2 m_0$ . That is, the measure in the neighborhood of 0 scales as

$$\mu([0, \epsilon]) \sim \epsilon^\alpha, \quad \text{with } \alpha = v_0.$$

The density  $\mu/\epsilon$  scales like  $\epsilon^{\alpha-1}$ , and if  $\alpha \neq 1$  the limit of the density as  $\epsilon \rightarrow 0$  is degenerate, equal to either 0 or  $\infty$ .

When the measure in the  $\epsilon$ -neighborhood of a point scales as a power law in the limit  $\epsilon \rightarrow 0$ , the exponent  $\alpha$  of this law is called the local *Hölder exponent* (Alternative terms, such as *singularity index* or *singularity strength* [8] are also encountered in the physics literature). That is, given a point  $x$  in the support of the measure, the local Hölder exponent is defined as

$$\alpha(x) = \lim_{\epsilon \rightarrow 0} \frac{\log \mu(B_x(\epsilon))}{\log \epsilon}, \quad (5)$$

where  $B_x(\epsilon)$  is a ball of size  $\epsilon$  around  $x$ . When the limit fails to exist, we shall say that the local Hölder exponent is undefined. (The mathematician's more elaborate local definition replaces lim by a limsup. This replacement broadens the cases where the Hölder exponent is defined locally; but this detail cannot be discussed here).

In most practical applications, the limit  $\epsilon \rightarrow 0$ , which enters in the definition of the local Hölder exponent, cannot be taken. One must, instead, work with the concept of *coarse* (or *coarse-grained*) *Hölder exponent*. This is a number attributed to each finite interval. For any box  $B(\epsilon)$  of size  $\epsilon$ , the coarse-grained Hölder exponent is defined as

$$\alpha = \frac{\log \mu(B(\epsilon))}{\log \epsilon}. \quad (6)$$

Thus, the concept of Hölder exponent has a local and a coarse version. Both enter into the theory of multifractals, but the coarse Hölder exponent plays an especially central role. As mentioned in the introduction,  $\alpha$  serves to label the boxes covering the set supporting a measure, thereby allowing a separate counting for each value of  $\alpha$ . For dyadic intervals  $I^k$  of size  $2^{-k}$ , equations 4 and 6 yield

$$\alpha(0, \beta_1 \beta_2 \dots \beta_k) = \frac{\log \mu_{0, \beta_1 \beta_2 \dots \beta_k}}{\log 2^{-k}} = \frac{\log m_0^{n_0} m_1^{n_1}}{-k \log 2} = \frac{n_0}{k} v_0 + \frac{k - n_0}{k} v_1, \quad (7)$$

where

$$v_1 = -\log_2 m_1 \quad \text{and} \quad v_0 = -\log_2 m_0. \quad (8)$$

Let  $\varphi_0 = \varphi_0(I^k)$  be the fraction  $n_0/k$  of 0's in the address  $0.\beta_1\beta_2\dots\beta_k$  of interval  $I^k$ . Equation 7 becomes

$$\alpha = \varphi_0 v_0 + (1 - \varphi_0) v_1 = \varphi_0 \alpha_{\min} + (1 - \varphi_0) \alpha_{\max}. \quad (9)$$

The notation  $\alpha_{\min}$  and  $\alpha_{\max}$  is explained shortly. It follows that the coarse Hölder exponent  $\alpha$  of an interval  $I^k$  only depends on the fraction  $\varphi_0$  of digits 0 in its address  $0.\beta_1\beta_2\dots\beta_k$ . Note that we use the same symbol  $\alpha$  for both the local Hölder exponent (equation 5) and the coarse Hölder exponent (equation 6). When present, the argument of the former is a point on the support of the measure, and that of the latter the address of a dyadic interval. In both cases  $\varphi_0$  in Equation 9 is the fraction of zeroes in their binary address.

Without loss of generality, we can take  $m_1 \leq m_0$ , so that  $v_0 \leq v_1$  and Equation 7 yields  $v_0 < \alpha < v_1$ . (The same restriction also applies to the local Hölder exponent). The extreme values of  $\alpha$  are usually denoted by  $\alpha_{\min}$  and  $\alpha_{\max}$ , i.e.,

$$\alpha_{\min} = v_0 \quad \text{and} \quad \alpha_{\max} = v_1.$$

This restriction on the values of the coarse Hölder exponent is independent of the size  $2^{-k}$  of the dyadic intervals; hence, it is independent of the scale on which the fractal measure is probed. This makes  $\alpha$  an ideal index with which to mark the boxes of any size covering the set supporting the measure. (Equation 19 will provide an alternative way of rewriting Equation 5, and emphasizing the role of the coarse Hölder exponent in transforming a multiplicative process into an additive process).

Keep the fraction  $\varphi_0 = n_0/k$  of 0's in Equation 9 constant, and let  $k \rightarrow \infty$  thereby squeezing  $I^k$  to a point. By permuting the order of appearance of the digits 0 and 1, increasingly many points  $x \in [0, 1]$  are found with fixed Hölder exponent  $\alpha(x) = \varphi_0 \alpha_{\min} + (1 - \varphi_0) \alpha_{\max}$ . In the case of the binomial, the extreme values  $\alpha_{\min} = v_0$  and  $\alpha_{\max} = v_1$  continue to be attained (respectively) in the left – and the right – most dyadic subinterval of the unit interval. But this is a peculiarity of the binomial measure; in general the minimal and maximum coarse and local Hölder exponents can lie anywhere in the support of the measure.

#### Singular Distributions

A measure  $\mu$  on  $[0, 1]$  has a density  $\rho(x)$  in a point  $x$  if  $\lim_{\epsilon \rightarrow 0} \mu(B_x(\epsilon))/\epsilon = \rho(x)$  exists and satisfies  $0 \leq \rho(x) < \infty$ . If  $\alpha(x)$  is the local Hölder exponent in  $x \in [0, 1]$ , then  $\rho(x) \sim \lim_{\epsilon \rightarrow 0} \epsilon^{\alpha(x)-1}$ . In points  $x$  where  $\alpha(x) \neq 1$  the density of the binomial measure is singular. Section 4.2 will show that, with probability 1, the local Hölder exponent of a randomly picked point in the support  $[0, 1]$  of the binomial measures is

$$\tilde{\alpha} = (v_0 + v_1)/2 = -\frac{1}{2} \log_2(m_0 m_1).$$

A measure for which  $\tilde{\alpha} \equiv 1$  occurs when, and only when,  $m_0 = m_1 = \frac{1}{2}$ , in which case the binomial measure reduces to the uniform (Lebesgue) measure. In the interesting

cases,  $m_0 \neq \frac{1}{2}$ , and the density is almost everywhere either 0 or  $\infty$ , hence it is called singular. For reasons which will become apparent later on,  $\hat{\alpha}$  is usually denoted by  $\alpha_0$  or  $\alpha(0)$ .

When the local density is singular, it continues to be possible to define a  $\epsilon$ -coarse-grained density, by covering the set supporting the measure with boxes  $B(\epsilon)$  of size  $\epsilon$  and attributing the coarse density  $\mu(B)/\epsilon^E$  to each box ( $E$  is the dimension of the box). Figure 3 shows an examples of a sequence of coarse-grained densities for the binomial measure.

### 2.4 The $f(\alpha)$ Curve of the Binomial Measure

The  $f(\alpha)$  curve describes the distribution of the coarse-grained Hölders exponents. To introduce this function, we first compute the number  $N_k(\alpha)$  of intervals  $I^k$  of size  $2^{-k}$  with coarse Hölder exponent  $\alpha$ . Equation 9 shows that the value of  $\alpha$  is determined by the frequency  $\varphi_0$  of zeroes in the expansion of the interval, and conversely, that to each  $\alpha$  corresponds a unique  $\varphi_0(\alpha)$ . Thus, the number of intervals with coarse Hölder exponent  $\alpha$  is given by the number of ways one can distribute  $n_0 = \varphi_0(\alpha)k$  zeros among  $k$  positions. This is the binomial coefficient

$$N_k(\alpha) = \binom{k}{\varphi_0(\alpha)k}.$$

This fact explains why the term *binomial* is applied to the binomial distribution and measure. To simplify, write  $z$  instead of  $\varphi_0$ , and apply Stirling's approximation  $k! \approx \sqrt{2\pi k} (k/e)^k$ . It yields

$$\binom{k}{zk} = \frac{k!}{(zk)!(k-zk)!} \sim \frac{\sqrt{k} k^k}{\sqrt{zk} (zk)^{zk} \sqrt{k-zk} (k-zk)^{k-zk}}.$$

Many terms cancel out, leaving

$$\binom{k}{zk} \sim \frac{(z^z (1-z)^{1-z})^{-k}}{\sqrt{z(1-z)}} \sim (2^{-k})^{-g(z)},$$

with  $g(z) = -\log_2(z^z (1-z)^{1-z})$ . Using Equation 9 to eliminate  $\varphi_0 = z$  in favour of the variable  $\alpha$ , we find

$$N_k(\alpha) \sim (2^{-k})^{-f(\alpha)}, \quad (10)$$

with

$$f(\alpha) = -\frac{\alpha_{\max} - \alpha}{\alpha_{\max} - \alpha_{\min}} \log_2 \left( \frac{\alpha_{\max} - \alpha}{\alpha_{\max} - \alpha_{\min}} \right) - \frac{\alpha - \alpha_{\min}}{\alpha_{\max} - \alpha_{\min}} \log_2 \left( \frac{\alpha - \alpha_{\min}}{\alpha_{\max} - \alpha_{\min}} \right).$$

The graph of  $f(\alpha)$  is shown in Figure 4. Expanding  $f(\alpha)$  around  $\alpha = \alpha_0 = (\alpha_{\min} + \alpha_{\max})/2$  using the approximation  $\ln x = x - x^2/2$ , yields for  $\alpha - \alpha_0 \ll 1$ ,

$$f(\alpha) = 1 - \frac{2}{\ln 2} \left( \frac{\alpha - \alpha_0}{\alpha_{\max} - \alpha_{\min}} \right)^2. \quad (11)$$

![Figure 4: A graph of the function f(alpha) versus alpha. The curve is a symmetric, inverted U-shape (parabola-like) starting at alpha_min, peaking at alpha(0), and ending at alpha_max. The y-axis is labeled f(alpha) with a tick mark at 1. The x-axis is labeled alpha with tick marks at alpha_min, alpha(0), and alpha_max. A straight line from the origin is tangent to the curve at its peak, labeled q=1. Another line from the origin is tangent to the curve at its base, labeled q=infinity.](7c1f9e78e0f033d391b687f1652f6e47_img.jpg)

Figure 4: A graph of the function f(alpha) versus alpha. The curve is a symmetric, inverted U-shape (parabola-like) starting at alpha\_min, peaking at alpha(0), and ending at alpha\_max. The y-axis is labeled f(alpha) with a tick mark at 1. The x-axis is labeled alpha with tick marks at alpha\_min, alpha(0), and alpha\_max. A straight line from the origin is tangent to the curve at its peak, labeled q=1. Another line from the origin is tangent to the curve at its base, labeled q=infinity.

Figure 4: The  $f(\alpha)$  curve for the binomial measure with  $m_0 = \frac{2}{3}$  and  $m_1 = \frac{1}{3}$ . At each level of coarse graining of the measure, one can distinguish intervals with different coarse Hölder exponents  $\alpha$ . As the coarse graining box-sizes become smaller, the number  $N_\epsilon(\alpha)$  of boxes with certain  $\alpha$  increases as  $N_\epsilon(\alpha) \sim \epsilon^{-f(\alpha)}$ .

The  $f(\alpha)$  curve has the following noticeable properties.

- (a) It is defined for  $0 < \alpha_{\min} < \alpha < \alpha_{\max} < \infty$  and  $f(\alpha) \geq 0$ .
- (b) The maximum of  $f(\alpha)$  is attained in one value of  $\alpha$ , called “ $\alpha_0$ ”.
- (c) The curve is symmetric around this maximum.
- (d) The local behavior of  $f(\alpha)$  near the maximum is quadratic.
- (e) The curve lies under the bisector defined by  $f(\alpha) = \alpha$ , with contact at  $\alpha = \alpha_1$ .

One may wonder whether these features are typical for self-similar measures. The answer is no. Upcoming sections touch upon these properties.

For finite  $k$ , the above equations only holds when  $k\varphi_0$  is an integer  $h$  between  $0 \leq h \leq k$ . Let  $\varphi_0'' = (h-1)/k$  and  $\varphi_0' = (h+1)/k$ . For fixed  $k$  there is no  $\alpha$  between  $\alpha(\varphi_0') < \alpha < \alpha(\varphi_0'')$ . From Equation 9 it follows that  $\alpha(\varphi_0'') - \alpha(\varphi_0') = 2(v_1 - v_0)/k = \Delta_k$  is independent of  $h$ . Equation 10 should therefore read that the number  $N_k(\alpha)\Delta_k$  of intervals  $I^k$  with a coarse Hölder exponent between  $\alpha$  and  $\alpha + \Delta_k$  scales like  $(2^{-k})^{-f(\alpha)}$ . Asymptotically  $N_k(\alpha)d\alpha$  is the number of intervals with a coarse Hölder exponent between  $\alpha$  and  $\alpha + d\alpha$ .

The role of  $f(\alpha)$  as scaling exponent (equation 10) suggests that the  $f(\alpha)$  is a kind of box-counting dimension. (The fact that there are a multitude of different values of  $\alpha$ , each with different  $f(\alpha)$ , is one reason for the term *multifractals*). However, a closer look shows  $f(\alpha)$  is not really a box-counting dimension. The box-counting dimension is related to the covering of a *fixed* set, by boxes of increasingly small boxes nested within each other. This is not the case for boxes with a given coarse Hölder exponent: indeed, a box of size  $2^{-k}$  with coarse Hölder exponent  $\alpha$ , contains sub-boxes of size  $2^{-k}$  with different values of  $\alpha$ .

#### Hausdorff Dimension versus Box-Counting Dimension

Another way of visualizing *multifractality* is to consider all the points  $x$  in the support of the measure for which the local Hölder exponent is  $\alpha$  (Equation 5). For each value of  $\alpha$  this defines a set  $A^\alpha \subset [0, 1]$ . It is not difficult to show that the box-counting dimension of each of the sets  $A^\alpha$  of the binomial measure is 1. (See the *Proof* at the end of this paragraph). Hence, instead of the box-counting dimension, we need the concept of Hausdorff dimension. It is beyond the scope of this Appendix to go beyond simply stating that for a class of multifractal measures (including the above binomial measure) it has been rigorously shown [14] that the Hausdorff dimension of  $A^\alpha$  is  $f(\alpha)$  (Ref. [15] includes a proof in the case of the binomial measure). *Proof that the box-counting dimension of  $A^\alpha$  is 1* . It suffices to show that each dyadic subinterval  $I^k$  of the unit interval contains points with any coarse Hölder exponent between  $\alpha_{\min}$  and  $\alpha_{\max}$ . Take any value  $\alpha' \in [\alpha_{\min}, \alpha_{\max}]$ . Let the binary expansion of  $I^k$  be  $0.\beta_1\beta_2\dots\beta_k$ . Remember that all  $x \in [0, 1]$  whose binary expansion starts with digits  $0.\beta_1\beta_2\dots\beta_k$  lie in  $I^k$ . So any choice of an infinite sequence of digits  $\beta_{k+1}\beta_{k+2}\dots$  such that its fraction  $\varphi_0$  of 0's satisfies Equation 9 for  $\alpha = \alpha'$ , yields a point  $x \in I^k$  with binary expansion  $\beta_1\beta_2\dots\beta_k\beta_{k+1}\beta_{k+2}\dots$  having  $\alpha(x) = \alpha'$ .

### 2.5 Multinomial Measures and the Legendre Transforms

In a multinomial cascade [6, 7, 16], the base  $b$  satisfies  $b > 2$  rather than  $b = 2$ . Each stage of the construction redistributes mass or measure over  $b$  equally sized intervals, following the fragmentation ratios  $m_0, m_1, \dots, m_{b-1}$  with  $\sum_{i=0}^{b-1} m_i = 1$ . We already encountered a *trinomial* multifractal ( $b = 3$ ) in the Introduction, namely, an IFS-generated trinomial measure on the Sierpiński gasket with multipliers  $m_0 = p_1$ ,  $m_1 = p_2$  and  $m_2 = p_3$ . Here we restrict ourselves to multinomial measures supported by  $[0, 1]$ .

To show how the notion of  $f(\alpha)$  generalizes to these measures, let  $I_b^k \subset [0, 1]$  be an arbitrary  $b$ -adic interval of size  $b^{-k}$ , and let its base- $b$  address be  $0.\beta_1\beta_2\dots\beta_k$  with  $\beta_i \in \{0, 1, \dots, b-1\}$ . Denote by  $\varphi$  the point in  $E = b$  dimensional Euclidean space whose coordinates are the frequencies  $\varphi_i$  of the digits  $i$  in this address. The combinatorics of the binomial measure and the use of the Stirling approximation can be generalized to every interval  $I_b^k$  characterized by  $\varphi$ . For the measure of such  $I_b^k$  and its coarse Hölder exponent, one obtains

$$\mu(I_b^k) = \prod m_i^{k\varphi_i} \text{ and } \alpha = -\sum \varphi_i \log_b m_i.$$

For the number of such intervals one finds  $N_k(\varphi) \sim (b^{-k})^{-\delta}$  with

$$\delta = -\sum \varphi_i \log_b \varphi_i.$$

In the binomial case, a single  $\delta = f(\alpha)$  could be deduced from the value of  $\alpha$ , but this possibility is not available here. A given  $\alpha$ , indeed, allows several possible sets of values of  $\varphi_i$  that are constrained by  $\sum \varphi_i = 1$  and  $\alpha = -\sum \varphi_i \log_b m_i$ . After

![Figure 5: A graph in the (alpha, delta) plane. The horizontal axis is alpha and the vertical axis is delta. A straight line delta = alpha starts from the origin. A shaded region is bounded by the alpha-axis, the line delta = alpha, and a concave-down curve that starts at alpha_max on the alpha-axis, reaches a peak at delta=1, and ends at alpha_min on the alpha-axis. The region inside the curve and below the line delta = alpha is shaded black.](ad29805cd4f64ad2828e14feb66de664_img.jpg)

Figure 5: A graph in the (alpha, delta) plane. The horizontal axis is alpha and the vertical axis is delta. A straight line delta = alpha starts from the origin. A shaded region is bounded by the alpha-axis, the line delta = alpha, and a concave-down curve that starts at alpha\_max on the alpha-axis, reaches a peak at delta=1, and ends at alpha\_min on the alpha-axis. The region inside the curve and below the line delta = alpha is shaded black.

Figure 5: Rough idea of the domain of  $(\alpha, \delta)$  for a multinomial multifractal with  $b = 4$ . The domain's upper boundary defines the function  $f(\alpha)$ . Here, all the  $m_i$  are different,  $\alpha_{\min} = \min_i(v_0, \dots, v_{b-1}) > 0$  and  $\alpha_{\max} = \max_i(v_0, \dots, v_{b-1}) < \infty$ .

the points  $(\alpha, \delta)$  corresponding to all the values of  $\alpha$  have been combined, the result is a domain of the plane [16], as shown in black in Figure 5.

There is a powerful heuristic way of replacing this domain by its upper bound. This heuristic method also provides the shortest path towards the Legendre transforms, which are essential in the study of multifractals. (A full mathematical justification will be given in Section 4.4.) The key step is to argue that, given a value of  $\alpha$ , the  $\delta$ 's are dominated by the largest  $\delta$  which we denote by  $f(\alpha)$ . This requires solving for the point  $\varphi$  that maximizes  $-\sum \varphi_i \log_b \varphi_i$ , given  $-\sum \varphi_i \log_b m_i = \alpha$  and  $\sum \varphi_i = 1$ . The classical method then uses Lagrange multipliers [17] to solve this problem. It introduces a multiplier  $q$ , with  $-\infty < q < \infty$ , and yields

$$\varphi_i = \frac{b^q \log_b m_i}{\sum_j b^q \log_b m_j} = \frac{m_i^q}{\sum_j m_j^q},$$

and thus

$$\alpha(q) = -\sum_i \left( \frac{m_i^q}{\sum_j m_j^q} \right) \log_b m_i \quad \text{and} \quad f(\alpha) = -\sum_i \left( \frac{m_i^q}{\sum_j m_j^q} \right) \log_b \left( \frac{m_i^q}{\sum_l m_l^q} \right)$$

Here, the quantities  $\sum_j m_j^q$  and  $\tau(q) = -\log_b \sum_j m_j^q$  play the roles that the “partition function” and the “free energy” are known to play in thermodynamics.

In terms of  $\tau(q)$ , the Lagrange multipliers yield

$$\alpha = \frac{\partial \tau(q)}{\partial q} \quad \text{and} \quad f(\alpha) = \frac{q \partial \tau}{\partial q} - \tau = q\alpha - \tau.$$

As previously stated, these steps replace the domain indicated in black in Figure 5 [16] by its upper boundary, which is the graph of a function  $f(\alpha)$ . This function  $f(\alpha)$  has all the properties that apply in the binomial case, except for symmetry.

Knowing  $\tau(q)$  for all values of  $q$ , one can trace all the straight lines of equation  $\delta_q(\alpha) = q\alpha - \tau$ . These straight lines define  $f(\alpha)$  as their envelope, namely

$$f(\alpha) = \min_q(q\alpha - \tau).$$

This transformation is called a Legendre transform, and we shall encounter it repeatedly in later contexts.

In many cases, a graphical approach is illuminating. If the lines represented by  $\delta_q(\alpha)$  are traced in green, they merge into a green domain in the  $(\alpha, \delta)$  plane, which “surrounds” the black domain that we have considered previously.

#### Beyond the Multinomial Measures

One way to expand the notion of the multiplicative process is to allow  $b = \infty$ . Examples can be found in Ref. [18, 19, 20]; one example is shown in Figure 6. It

![Figure 6: A plot of an exactly self-similar multiplicatively generated measure. The x-axis ranges from 0 to 1.0, and the y-axis ranges from 0 to 0.004. The plot shows a highly oscillatory, fractal-like curve with many sharp peaks, characteristic of a self-similar measure.](62ad98a4bc47922b5cf47de04571dae8_img.jpg)

Figure 6: A plot of an exactly self-similar multiplicatively generated measure. The x-axis ranges from 0 to 1.0, and the y-axis ranges from 0 to 0.004. The plot shows a highly oscillatory, fractal-like curve with many sharp peaks, characteristic of a self-similar measure.

Figure 6: An example of an exactly self-similar multiplicatively generated measure for which  $\alpha(0) = \infty$  and hence, a fortiori,  $\alpha_{max} = \infty$ . It follows that  $f(\alpha)$  is defined for  $\alpha_{min} < \alpha$ . Such measures are called left-sided. The corresponding function  $\tau(q)$  is not defined for  $q < 0$ , and the method of moments does not adequately describe the whole measure.

is interesting to note that although the measures are exactly self-similar (a piece, if expanded, looks exactly the same as the whole), the  $f(\alpha)$  curve is very different from the symbol  $\cap$  encountered for the binomial. One can construct examples for which a)  $\alpha_{min} = 0$  and  $\alpha_{max} = \infty$ , b) the maximum is not quadratic and c) the maximum is not attained for *one* value of  $\alpha$  but over a halfline of  $\alpha$  values. We will briefly comment on these examples in Section 5.

### 2.6 Random Multiplicative Cascades

A second way to expand the notion of the multiplicative process is to use random multipliers. When  $b = 2$ , the process proceeds in the same way as the binomial

measure, except that each multiplier is now the outcome of some probabilistic process such as throwing dice. Just as most fractal sets in nature are random fractal sets, the random multiplicative processes are very useful for modelling real multifractal measures like those in turbulence [21, 22, 9, 23] or diffusion limited aggregation [24, 25, 3]. For such measures, all properties of the  $f(\alpha)$  mentioned in the last section may be violated, although its graph still always lies under the bisector  $f(\alpha) = \alpha$ . Such measures are described in great detail in Ref. [6, 7]. We will postpone a brief discussion of them to Section 5.

## 3 Methods for Estimating the Function $f(\alpha)$ from Data

It is nice to say that a measure is multifractal if it is self-similar, in the sense described for the binomial measure. In our study of the binomial, the cascade was a given, and the quantity  $N_k(\alpha)d\alpha$  could be evaluated for all  $k$  and interpreted as the number of intervals of size  $2^{-k}$  in the  $k^{\text{th}}$  stage of the cascade having a coarse Hölder exponent between  $\alpha$  and  $\alpha + d\alpha$ . But it is important to keep in mind that behind most measures there is no obvious multiplicative cascade! When one may exist, like perhaps in turbulence or the distribution of mass in the universe, this cascade is history; only the measure that it has created exists in the present. How does one find out whether a given measure is multifractal?

This can still be accomplished when only one stage  $k$  of a measure is given, since one can reconstruct any previous stage  $h < k$  by coarse-graining with intervals of size  $2^{-h}$ . We shall examine two methods for obtaining an empirical estimate of  $f(\alpha)$  for an arbitrary measure.

### 3.1 The Histogram Method

Given a measure  $\mu$ , the histogram method involves the following steps:

- (a) Coarse-grain the measure with boxes of size  $\epsilon$ . This yields a collection of boxes  $\{B_i(\epsilon)\}_{i=1}^{N(\epsilon)}$ , where  $N(\epsilon)$  is the total number of boxes needed to cover the set supporting the measure.
- (b) Compute the coarse Hölder exponent  $\alpha_i = \log \mu_i / \log \epsilon$ , where  $\mu(B_i)$  is the measure of box  $i$ .
- (c) Make a histogram. That is, subdivide the variable  $\alpha$  into bins of suitably small size  $\Delta\alpha$  and estimate the number density  $N_\epsilon(\alpha)$  by recording the number of times  $N_\epsilon(\alpha)\Delta\alpha$  that a specific value of the falls between  $\alpha$  and  $\alpha + \Delta\alpha$ .
- (d) Repeat step (c) for different values of coarse-graining size  $\epsilon$ .
- (e) Since we expect

$$N_\epsilon(\alpha) \sim \epsilon^{-f(\alpha)}, \quad (12)$$

plot  $-\log N_\epsilon(\alpha) / \log \epsilon$  versus  $\alpha$  for different values of  $\epsilon$ .

This method suggests that a measure be called multifractal when the resulting plots collapse onto a curve  $f(\alpha)$  if  $\epsilon$  is small enough. We must state that self-similar measures exist [18, 19, 20] for which the collapse to a function  $f(\alpha)$  is extraordinarily

slow and largely irrelevant for any physically meaningful  $\epsilon$ . A test of these steps in the case of the binomial measure and methods to accelerate the convergence are discussed in Ref. [26].

### 3.2 The Method of Moments

The method of moments [8] is based on a quantity called the *partition function* (because of analogies with the partition function in the theory of equilibrium thermodynamics). It is defined as

$$\chi_q(\epsilon) = \sum_{i=1}^{N(\epsilon)} \mu_i^q, \quad q \in \mathcal{R}. \quad (13)$$

For example, take the binomial measure and denote by  $\chi_q(\epsilon_k)$  the partition function at coarse-graining box-size  $\epsilon_k = 2^{-k}$ . An inspection of Figure 3 immediately yields  $\chi_q(\epsilon_0) = 1^q$ ,  $\chi_q(\epsilon_1) = m_0^q + m_1^q$  and  $\chi_q(\epsilon_2) = (m_0^q + m_1^q)^2$ . More generally the partition function is written as

$$\chi_q(\epsilon_k) = (m_0^q + m_1^q)^k.$$

Returning to Equation 13 in the general case, let us rewrite the measures  $\mu_i$  of the boxes as  $\mu_i = \epsilon^{\alpha_i}$ , yielding  $\chi_q(\epsilon) = \sum_{i=1}^{N(\epsilon)} (\epsilon^{\alpha_i})^q$ . Motivated by the results for the binomial measure, denote by  $N_\epsilon(\alpha)d\alpha$  the number of boxes out of the total  $N(\epsilon)$  for which the coarse Hölder exponent satisfies the inequality  $\alpha < \alpha_i < \alpha + d\alpha$ . Assume, in addition, that  $N_\epsilon(\alpha)$  is continuous and that there exist constants  $\alpha_{\min}$  and  $\alpha_{\max}$  such that  $0 < \alpha_{\min} < \alpha < \alpha_{\max} < \infty$ . Then the contribution to  $\chi_q(\epsilon)$  of the subset of boxes with  $\alpha_i$  between  $\alpha$  and  $\alpha + d\alpha$  is  $N_\epsilon(\alpha)(\epsilon^\alpha)^q d\alpha$ . Instead of adding the contribution of each box  $i$  separately, integrate over  $d\alpha$  to add the contributions of the subsets with their exponents between  $\alpha$  and  $\alpha + d\alpha$ . Thus,

$$\chi_q(\epsilon) = \int N_\epsilon(\alpha)(\epsilon^\alpha)^q d\alpha.$$

If  $N_\epsilon(\alpha) \sim \epsilon^{-f(\alpha)}$ , it follows that

$$\chi_q(\epsilon) = \int \epsilon^{q\alpha - f(\alpha)} d\alpha. \quad (14)$$

In the limit as  $\epsilon \rightarrow 0$ , the dominant contribution to the integral comes from the values of  $\alpha$  near the  $\alpha$  value that minimizes the exponent  $q\alpha - f(\alpha)$ . If  $f(\alpha)$  is differentiable, the necessary condition for the existence of an extremum is

$$\frac{\partial}{\partial \alpha} \{q\alpha - f(\alpha)\} = 0.$$

For a given value of  $q$ , the extremum occurs for the value  $\alpha = \alpha(q)$  that satisfies

$$\left. \frac{\partial}{\partial \alpha} f(\alpha) \right|_{\alpha=\alpha(q)} = q, \quad (15)$$

and this extremum is a minimum provided that

$$\left. \frac{\partial^2}{\partial \alpha^2} f(\alpha) \right|_{\alpha=\alpha(q)} < 0.$$

Thus, the function  $f(\alpha)$  should be cap convex as in Figure 4, and for the  $\alpha = \alpha(q)$  where the minimum is attained the slope of  $f(\alpha)$  is  $q$ .

Note: by now we have encountered three different arguments for  $\alpha$ : i)  $x \in [0, 1]$ ,

ii) the dyadic expansion  $0.\beta_1\beta_2\dots\beta_k$  of an interval  $I^k$  and iii) the variable  $q$ .

Only the latter two, which are easily distinguished, will be used in the future.

Keeping only the dominant contribution in Equation 14 and introducing

$$\tau(q) = q\alpha(q) - f(\alpha(q)),$$

we find that

$$\chi_q(\epsilon) \sim \epsilon^{\tau(q)}. \quad (16)$$

For the binomial measures,

$$\tau(q) = \lim_{k \rightarrow \infty} \frac{\log(m_0^q + m_1^q)^k}{\log 2^{-k}} = -\log_2(m_0^q + m_1^q), \quad (17)$$

and for the multinomial measures

$$\tau(q) = -\log_b \sum_{i=0}^{b-1} m_i^q. \quad (18)$$

Returning to the general case, it is not difficult to show that

$$\frac{\partial}{\partial q} \tau(q) = \alpha(q). \quad (19)$$

This shows that  $f(\alpha)$  can be computed from  $\tau(q)$ , and vice versa, by the identity

$$f(\alpha(q)) = q \alpha(q) - \tau(q). \quad (20)$$

This relation between  $\tau(q)$  and  $f(\alpha)$  has already been encountered in Section 2.5; it is called a *Legendre transform*. As an example, the Legendre transform of Equation 17 yields the  $f(\alpha)$  of the binomial measure in Equation 10.

Note that Equation 15 and the strict cap convexity of  $f(\alpha)$  imply that  $\alpha(q)$  is a decreasing function of  $q$ , so  $\alpha_{\min} = \alpha(\infty)$  and  $\alpha_{\max} = \alpha(-\infty)$ ; thus  $\tau(q)$  should also be strictly cap convex. The function  $\tau(q)$  is sometimes written as  $\tau(q) = (q-1)D_q$ , where the exponents  $D_q$  [27], are called generalized dimensions. (See also the discussion in Section 12.6 of Reference [1]).

#### The Method of Moments in practice

In practice, computing  $f(\alpha)$  through the partition function requires the following steps:

- (a) Coarse-grain the measure with a covering  $\{B_i(\epsilon)\}_{i=1}^{N(\epsilon)}$  of boxes of size  $\epsilon$  and determine the corresponding box-measures  $\mu_i = \mu(B_i(\epsilon))$ .
- (b) Compute the partition function in Equation 13 for various values of  $\epsilon$ .

(c) Check whether the plots of  $\log \chi_q(\epsilon)$  versus  $\log \epsilon$  are straight lines. If they are straight,  $\tau(q)$  is the slope of the line corresponding to the exponent  $q$  (see Equation 16).

(d) Form  $f(\alpha)$  by the Legendre transformation of  $\tau(q)$  (Equation 20).

In actual applications, the above steps must be carried out numerically. The usual reason is that it is not possible to obtain analytic expressions due to a lack of theoretical knowledge about the phenomena. But even when an analytic expression for the partition function is available, it may yet be too difficult to find an analytic expression for  $\tau(q)$  or  $f(\alpha)$ .

When the check described under (c) gives a straight line, the method of moments is justified, and it yields the same  $f(\alpha)$  as the histogram method. Moreover, given that moments tend to smooth the data, while the histogram method handles raw data, the method of moments converges much faster.

#### Pitfalls

At this point, we must voice a serious warning. The fact that this work must proceed numerically creates a strong temptation to proceed blindly by resorting to ready-made computer programs. Unfortunately, some programs fail to include a sufficiently demanding test for the linearity required in (c). Instead, they automatically fit a straight line “mechanically,” using a method such as least squares fitting. While statistically objective in all cases, those  $\tau(q)$  values obtained from the fitted lines have no physical meaning unless the points plotted in (c) are straight. As a matter of fact, the literature is cluttered with thoroughly bizarre  $f(\alpha)$  curves that were obtained objectively but mean nothing.

Equation 16 shows that under the assumptions mentioned under Equation 13, the partition function scales as a function of the box-size  $\epsilon$  for all  $q \in \mathcal{R}$ . It is then said that “the  $q^{\text{th}}$  moment” of the measure exists for all  $q$ . For example, all moments exist for the binomial and multinomial multifractals. The method of moments suggests that a measure is multifractal if, and only if, the function  $\tau(q)$  exists for all  $q \in \mathcal{R}$ . But this definition of multifractals is not satisfactory. Self-similar measures exist [18, 19] for which  $\tau(q)$  fails to be defined for, say,  $q < 0$ . Self-similar measures for which all moments exist should be called *restricted* multifractals to indicate the existence of a broader class of multifractals.

### 3.3 Properties of $f(\alpha)$

Let us briefly review some of the characteristics of  $f(\alpha)$  for restricted multifractal measures, i.e., measures for which the method of moments is applicable and for which the histogram method converges reasonably fast.

Let  $A^\alpha(\epsilon)$  be the subset of boxes covering the support of the measure having a coarse Hölder exponent between  $\alpha$  and  $\alpha + d\alpha$ . The total measure carried by such a subset is  $\mu(A^\alpha(\epsilon)) = N_\epsilon(\alpha)\epsilon^\alpha d\alpha \sim \epsilon^{-f(\alpha)+\alpha} d\alpha$ . Now, the total measure in all boxes is 1. This implies that  $f(\alpha) \leq \alpha$ ; the reason is that the contrary would be absurd: if

there existed a value of  $\alpha$  such that  $f(\alpha) > \alpha$ , it would follow that  $\mu(A^\alpha(\epsilon)) \rightarrow \infty$  for  $\epsilon \rightarrow 0$ . So, the  $f(\alpha)$  always lies under the bisector. Second, consider the value of  $\alpha$  that maximizes  $\mu(A^\alpha(\epsilon))$ . If it were true for all  $\alpha$  that  $f(\alpha) < \alpha$ , it would follow for all  $\alpha$  that  $\mu(A^\alpha(\epsilon)) \rightarrow 0$  as  $\epsilon \rightarrow 0$ . This result would contradict the fact that the total measure is 1. So the  $f(\alpha)$  curve should have at least one point in common with the bisector. Because  $f(\alpha)$  is concave, this point of intersection is unique and occurs where  $f'(\alpha) = 1$ . This corresponds to the  $q = 1$  case in the method of moments (see Equation 15), and this value of  $\alpha$  is denoted by  $\alpha(1)$  or  $\alpha_1$ . The subset of boxes  $A^{\alpha_1}(\epsilon)$  carries all the measure in the limit as  $\epsilon \rightarrow 0$ , i.e.,  $\mu(A^{\alpha_1}(\epsilon)) \rightarrow 1$  for  $\epsilon \rightarrow 0$ .

Restating Equation 16 as  $\tau(q) = \lim_{\epsilon \rightarrow 0} (\log \sum_{i=1}^{N(\epsilon)} \mu_i^q) / \log \epsilon$  and using Equation 19, one finds that

$$\alpha(q) = \lim_{\epsilon \rightarrow 0} \frac{\sum_{i=1}^{N(\epsilon)} (\mu_i^q / \sum_j \mu_j^q) \log \mu_i}{\log \epsilon}. \quad (21)$$

An equation similar to Equation 21 can be derived for  $f(\alpha(q))$  and can be used to find  $f(\alpha)$  directly [28]. In particular

$$\alpha(1) = f(\alpha(1)) = \lim_{\epsilon \rightarrow \infty} \frac{\sum_{i=1}^{N(\epsilon)} \mu_i \log \mu_i}{\log \epsilon}.$$

The quantity  $-\sum_{i=1}^{N(\epsilon)} \mu_i \log \mu_i$  is related to entropy and information. Correspondingly, the quantity  $f(\alpha(1)) = \alpha(1)$  is called the *information dimension* of the measure [10, 29, 27, 30].

$f(\alpha(1))$  is also the dimension of the set carrying “all” the measure. (This set is called the measure theoretic support of the measure.) To illustrate this, let us consider the IFS discussed in the Introduction. We know that the visiting process is probabilistically ruled by a trinomial multifractal measure. Let  $n$  be the number of times the IFS is played. From the above discussion we conclude that it is possible to find a subset of  $(3^k)^{f(1)}$  boxes of size  $3^{-k}$  whose total number of visits  $n_1(n)$  satisfies  $n_1(n)/n \rightarrow 1$  for  $n \rightarrow \infty$  and  $k \rightarrow \infty$ . The set  $A^{\alpha(1)}$  carries all the measure.

The number of elements in the sets  $A^\alpha(\epsilon)$  is  $N_\epsilon(\alpha) \sim \epsilon^{-f(\alpha)}$ . The set  $\alpha$  with the maximum number of elements contains that value of  $\alpha$  at which  $f(\alpha)$  attains its maximum. From Equation 15 it follows that the maximum of  $f(\alpha)$  should occur for  $\alpha = \alpha(0)$ . At the maximum, Equation 20 yields  $f(\alpha(0)) = -\tau(0)$  and Equation 13 gives  $\chi_q(\epsilon) = N(\epsilon) \sim \epsilon^{-D}$ . Combining this with Equation 16 yields  $f(\alpha(0)) = -\tau(0) = D_0$ . Clearly, the maximum value of the  $f(\alpha)$  curve is the box-counting dimension of the geometric support of the measure. Since the number of boxes with coarse Hölder exponent  $\alpha(0)$  is infinitely larger than those with other values of the coarse Hölder exponent in the limit as  $\epsilon \rightarrow 0$ , one expects a randomly picked box of size  $\epsilon$  to be of type  $\alpha(0)$  (see also Section 4.2). For the binomial measure, Equation 17 gives  $D_0 = -\tau(0) = 1$ , which is the dimension of the set  $[0, 1]$  supporting the measure. From the symmetry of its  $f(\alpha)$  curve (Equation 10), it immediately follows that  $\alpha(0) = (\alpha_{\min} + \alpha_{\max})/2$ .

## 4 Probabilistic Roots of Multifractals. Role of $f(\alpha)$ in Large Deviation Theory

At this point, many questions remain to be raised and to be answered. Why should an  $f(\alpha)$  curve exist for a self-similar measure? Its existence for the binomial measure does not guarantee its existence in general. Indeed, self-similar measures exist for which  $f(\alpha)$  exists, but  $f(\alpha)$  is attained very slowly and is not of direct interest. If a useful  $f(\alpha)$  does not always exist for self-similar measures, then what about alternative quantitative descriptions of the measure? To a large extent, these questions can be answered when the self-similar measures are generated by, or can be mapped onto, multiplicative cascades. The understanding of such measures is based largely on the following basic fact about fractals. Even when a fractal is nonrandom, like the Cantor set, it becomes a random set if its origin is chosen randomly. As an example, consider the binomial measure in an interval that was chosen at random. This measure is then a random variable! Therefore, as we shall see, the Hölder exponent can be expressed as a sum of random variables [31, 6, 7]. This fact, again, is true both of random and nonrandom multifractals. This randomness points to the probabilistic roots of the concept of  $f(\alpha)$ , and in addition – this is perhaps even more important – it allows one to know the limitations of  $f(\alpha)$ , while providing new tools to handle more complicated self-similar measures.

The properties of sums of random variables are a central topic in probability theory. The next section discusses the relevance to multifractals of three theorems dealing with such sums: i) the law of large numbers, ii) the Gaussian central limit theorem and iii) the large deviations theorem. No familiarity with these subjects is assumed, and the section should serve as an introduction to literature applying more advanced results from probability theory to self-similar measures.

### 4.1 Transformation of a Multiplicative Cascade into an Additive Cascade

Suppose that the dyadic interval  $I^k = I_{0.\beta_1\beta_2\dots\beta_k}$  has been picked randomly. This is essentially the same as picking a random sequence of digits  $\beta_1\beta_2\dots\beta_k$  where each  $\beta_i$  is either 0 or 1 with probability  $\frac{1}{2}$ . Indeed, suppose that  $I^k$  has equal probability to lie in the left or right half of the unit interval. For the first digit, this means that  $\Pr\{\beta_1 = 0\} = \frac{1}{2}$  and similarly for the second digit,  $\Pr\{\beta_1 = 1\} = \frac{1}{2}$ . Furthermore, irrespective of whether the chosen dyadic interval  $I^k$  actually lies in  $I_{0,0}$  or in  $I_{0,1}$ , it will again have equal probability to lie in the left or right half subinterval, that is,  $\Pr\{\beta_2 = 0\} = \Pr\{\beta_2 = 1\} = \frac{1}{2}$ .

Equation 4 has shown that the measure of the randomly picked dyadic interval  $I^k$  is  $\mu_{0.\beta_1\beta_2\dots\beta_k} = \prod_{i=1}^k m_{\beta_i}$ . Because the  $\beta_i$  are random, either 0 or 1, the variables  $m_{\beta_i}$  are also random, either  $m_0$  or  $m_1$ . This means that this measure  $\mu$  is the product of  $k$  statistically independent values of a *random variable*  $\mathbf{M}$ , which can be either  $m_0$  or  $m_1$  with probability  $\frac{1}{2}$ .

#### Random Variables

A random variable can be thought of as a “mathematical coin or die.” It has prescribed probabilities for yielding certain results when “thrown.” Our convention denotes random variables by boldface capital letters. The *sample value* that is the outcome of a throw is denoted by a corresponding lower case letter. For example, the random variable  $\mathbf{D}$  meant to represent a real die with six faces would have a probability distribution  $\Pr\{\mathbf{D} = d\} = \frac{1}{6}$  for  $d = 1, 2, 3, 4, 5, 6$ .

So the measure  $\mu$  of a randomly picked  $I^k$  is a sample value of the random variable  $\prod_{i=1}^k \mathbf{M}$ , where the random multiplier  $\mathbf{M}$  has the distribution

$$\Pr\{\mathbf{M} = m_0\} = \Pr\{\mathbf{M} = m_1\} = \frac{1}{2}. \quad (22)$$

Equation 6 yields the coarse Hölder exponent  $\alpha_k$  of such an interval  $I^k$  in the following form, which restates Equation 4,

$$\alpha_k(0, \beta_1 \beta_2 \dots \beta_k) = \frac{\log \prod_{i=1}^k m_{\beta_i}}{\log 2^{-k}} = -\frac{1}{k} \sum_{i=1}^k \log_2 m_{\beta_i} = \frac{1}{k} \sum_{i=1}^k v_{\beta_i}. \quad (23)$$

Here we use the variables  $v_\beta$  introduced in Section 2.3 ( $v_\beta = -\log_2 m_\beta$ ,  $\beta = 0, 1$ ). Thus, the coarse Hölder exponent of a random  $I^k$  is the random variable

$$\mathbf{H}_k = \frac{1}{k} \sum_{h=1}^k \mathbf{V}_h. \quad (24)$$

This is the average of  $k$  independently chosen sample values  $v$  of a random variable  $\mathbf{V}$  with distribution

$$\Pr\{\mathbf{V} = v_0\} = \Pr\{\mathbf{V} = v_1\} = \frac{1}{2}. \quad (25)$$

Let us rephrase the above discussion in terms of a well-balanced coin, that is, one with equal probabilities for heads and tails. A collection of  $k$  identical coins ( $\mathbf{V}_1, \mathbf{V}_2, \dots, \mathbf{V}_k$ ), each with one face marked  $v_0$  and the other  $v_1$ , are tossed, and the sample average  $\frac{1}{k} \sum_{h=1}^k \mathbf{V}_h$  is computed. These averages have the same distribution as the values of the coarse Hölder exponent of randomly picked dyadic intervals of size  $2^{-k}$  in the support  $[0, 1]$  of the binomial measure.

The distribution  $\Pr\{\mathbf{H}_k \geq \alpha\}$  is closely linked to the distribution  $p_\epsilon(\alpha)d\alpha$  discussed in the introduction (Equation 2) and eventually will link us back to the method of moments and the histogram method. The following two paths are open

1) One can count the number of coarse Hölder exponents at the  $k^{\text{th}}$  stage of the multiplicative cascade which are larger than  $\alpha$ , and then divide this number by the total number  $2^k$  of boxes needed to cover the unit interval, or

2) One can make  $n$  series of  $k$  coin tosses, and for each series compute the average. Then count the number of times this average is larger than  $\alpha$ , and divide this number by  $n$ , considering the result in the limit  $n \rightarrow \infty$ .

The first path is essentially the histogram method and will not be discussed further. We now follow the second path using the fact that the distribution of the

coarse Hölder exponent at the  $k^{\text{th}}$  level of the multiplicative cascade is the same as the distribution of the random variable  $\mathbf{H}_k$  defined in Equation 24. This reformulation in terms of sums of independent identically distributed random variables (Equation 24) allows the use of many techniques of probability theory.

### 4.2 The Law of Large Numbers and the Role of $\alpha_0$ as the Most Probable Hölder Exponent

Tossing the coin marked with  $v_0$  and  $v_1$   $k$ -times yields, say,  $n_0$  times the value  $v_0$  and  $n_1 = k - n_0$  times the value  $v_1$ . Since the probabilities for heads and tails are equal, one expects for  $k \rightarrow \infty$  that  $n_0/k \rightarrow \frac{1}{2}$  as does  $n_1/k$ . This would mean that the sample average  $\frac{1}{k}(n_0 v_0 + n_1 v_1)$  converges as  $k \rightarrow \infty$  to the expectation

$$\mathbf{EV} = \frac{1}{2}v_0 + \frac{1}{2}v_1.$$

Different forms of convergence yield different forms of the law of large numbers. The *weak* law of large numbers guarantees such convergence when the expectation  $\mathbf{EV}$  of  $\mathbf{V}$  exists. The *strong* law of large numbers is more interesting for the theory of multifractals. It states that, almost surely (with probability 1) the sample average will converge for  $k \rightarrow \infty$  to the expectation, that is,

$$\Pr\left\{\lim_{k \rightarrow \infty} \frac{1}{k} \sum_{h=1}^k \mathbf{V}_h = \mathbf{EV}\right\} = 1.$$

Using the equivalence established in the previous section between the binomial measure and coin tossing, this equation shows that, with probability 1, the local Hölder exponent at a randomly picked point in the support of the binomial measure equals  $\mathbf{EV}$ , that is

$$\Pr\left\{\lim_{k \rightarrow \infty} \mathbf{H}_k = \mathbf{EV}\right\} = 1. \quad (26)$$

Another way of obtaining this result uses the fact that the strong law of large numbers implies that the binary expansion of a randomly picked point  $0.\beta_1\beta_2\beta_3\dots$  almost surely has the same frequencies of zeroes and ones, that is,  $\varphi_0 = 1/2$  almost surely. Inserting this into Equation 9 yields  $\alpha = \mathbf{EV}$ , and Equation 26 is recovered.

If the law of large numbers had meant that the random choice of  $x$  should yield one particular value of  $\alpha$  with probability 1, then it should yield the value that occurs most often. Going back to the  $f(\alpha)$  curve, this particular value of  $\alpha$  is the one that maximizes  $f(\alpha)$ . Previously in Section 3.3, this special value of the coarse Hölder exponent was denoted by  $\alpha(0)$  or  $\alpha_0$  because it is the value of  $\alpha$  that corresponds to  $q = 0$  in the method of moments. Indeed, for the binomial measure we found  $\alpha(0) = (v_0 + v_1)/2$  in agreement with Equation 26. This establishes a link between  $f(\alpha)$  and the theory of sums of random variables.

The results related to the laws of large numbers only hold pointwise, that is, in the limit of infinitesimal box-sizes ( $k \rightarrow 0$ ). In most physical systems, such limits cannot be attained; therefore, their properties are not especially interesting. It is clear that random selection of a large number of boxes of finite size  $2^{-k}$  will *not* always yield coarse Hölder exponents equal to the expected value  $\mathbf{EV} = \frac{1}{2}(\alpha_{\min} + \alpha_{\max})$ . Instead, for large enough number boxes, one finds all values of the Hölder

exponent  $\alpha$  between  $\alpha_{\min}$  and  $\alpha_{\max}$ . In other words, the deviations from the expected value become important for finite  $k$ , and their probability of occurrence must be known. The relevant information is given by central limit theorems and, far more importantly, by large deviation theory.

### 4.3 Gaussian Central Limit Theorem and the Shape of $f(\alpha)$ near $\alpha_0$

The Gaussian central limit theorem does go beyond the law of large numbers. Unfortunately, it mainly explains merely why the maximum of the  $f(\alpha)$  is often quadratic.

Actually, the term *Gaussian central limit theorem* covers a variety of distinct results that all conclude that deviations from the expected value have a Gaussian distribution. The specific form of interest here relates the sums of independent and identically distributed random variables, such as the sum  $\sum_{h=1}^k \mathbf{V}_h$  that enters in Equation 24. The basic assumption is that the random addend  $\mathbf{V}$  is a random variable with a finite expectation  $\mathbf{EV}$  and a finite second moment  $\mathbf{EV}^2$ . (The binomial measure is the standard example, since both  $\mathbf{EV} = \frac{1}{2}(v_0 + v_1)$  and  $\mathbf{EV}^2 = \frac{1}{2}(v_0^2 + v_1^2)$  are finite.) The theorem states that, in the limit as  $k \rightarrow \infty$ , the distribution of the rescaled random variable  $\mathbf{Y}_k = (\sum_{h=1}^k \mathbf{V}_h - k\mathbf{EV})/(\sigma\sqrt{k})$  converges to the Gaussian distribution with zero mean and variance  $\sigma^2 = \mathbf{EV}^2 - (\mathbf{EV})^2$ . That is,

$$\lim_{k \rightarrow \infty} \Pr \left\{ \frac{\sum_{h=1}^k \mathbf{V}_h - k\mathbf{EV}}{\sigma\sqrt{k}} \leq y \right\} = \int_{-\infty}^y G(x) dx, \quad (27)$$

where the integrand

$$G(x) = \frac{1}{\sqrt{2\pi}} \exp \left\{ -\frac{1}{2}x^2 \right\}$$

is the reduced Gaussian density. (A graph of this density is found on the German bill for 10 Deutschmarks together with a portrait of Carl Friedrich Gauss.)

In the coin-tossing experiment that yields either  $v_0$  or  $v_1$ , the law of large numbers makes us “ideally” expect an equal number of  $v_0$  and  $v_1$  from  $k$  tosses, that is, when adding  $k$  sample values of  $\mathbf{V}$  one expects to get the value  $\frac{k}{2}v_0 + \frac{k}{2}v_1 = k\mathbf{EV}$ , so that  $\sum_{h=1}^k \mathbf{V}_h - k\mathbf{EV} = 0$ . However, Equation 27 shows that  $\sum_{h=1}^k \mathbf{V}_h - k\mathbf{EV}$  deviates from the “ideal” value 0 by an amount that scales like  $\sqrt{k}$ .

Let us now return to the probability density  $p_k(\alpha)$  of the coarse Hölder exponent  $\mathbf{H}_k = \frac{1}{k} \sum_{h=1}^k \mathbf{V}_h$ . Writing  $\mathbf{H}_k = \mathbf{Y}_k/\sqrt{k} + \mathbf{EV} = \mathbf{Y}_k/\sqrt{k} + \alpha_0$ , we see that  $\mathbf{H}_k$  has the variance  $\sigma^2/\sqrt{k}$  and scales like  $1/\sqrt{k}$ . Keeping  $k$  finite, the limit in Equation 27 yields the approximation

$$p_k^G(\alpha) d\alpha = \frac{1}{(\sigma/\sqrt{k})\sqrt{2\pi}} \exp \left\{ -\frac{1}{2} \left( \frac{\alpha - \alpha_0}{\sigma/\sqrt{k}} \right)^2 \right\} d\alpha.$$

Here, the superscript  $G$  is meant to remind us that  $p_k^G(\alpha)$  is not the actual probability density  $p_k(\alpha)$  of the coarse Hölder exponent of the binomial measure, but instead it is a Gaussian approximation that applies only for  $\alpha$  near  $\alpha_0$ . Very near to the most probable value  $\alpha_0$ , Equations 2 and 3 yield the approximation

$$f(\alpha) \approx f^G(\alpha) = 1 + \frac{1}{k} \log_2 p_k^G(\alpha) = 1 - \frac{2}{\ln 2} \left( \frac{\alpha - \alpha_0}{\alpha_{\max} - \alpha_{\min}} \right)^2.$$

This approximation agrees with the expansion, Equation 11, around the maximum of the exact result. But as  $\alpha$  moves away from  $\alpha_0$ ,  $f^G(\alpha)$  becomes increasingly larger than the exact  $f(\alpha)$ . Outside  $[\alpha_{\min}, \alpha_{\max}]$ , the approximate  $f^G(\alpha)$  is grossly inadequate: the exact  $f(\alpha)$  is not defined there, but  $f^G(\alpha)$  is. Further away from  $\alpha_0$ ,  $f^G(\alpha) < 0$ , which is meaningless for the binomial measure.

In summary, the Gaussian central limit theorem shows that the appearance of a quadratic maximum in the  $f(\alpha)$  of the binomial measure is not a coincidence. In general, it shows that a quadratic maximum contains no information other than the finiteness of the first and second moment of the logarithm of the multiplier.

### 4.4 Cramèr's Large Deviations Theory and $f(\alpha)$

#### The Significance of $f(\alpha)$ in the Discrete Finite Cases

Take a random variable with  $E\mathbf{X} < \infty$  and satisfying  $\Pr\{\mathbf{X} > E\mathbf{X}\} > 0$ . Large deviation theory is concerned with very large fluctuations around the expected value, namely with the behavior of

$$\Pr\left\{\frac{1}{k} \sum_{h=1}^k \mathbf{X}_h - E\mathbf{X} \geq \delta\right\}$$

as a function of  $\delta$  and  $k$ . The law of large numbers tells us that, in the limit as  $k \rightarrow \infty$ ,  $\Pr\{\frac{1}{k} \sum_{h=1}^k \mathbf{X}_h - E\mathbf{X} = 0\} = 1$ . So for  $\delta = 0$ , one expects the above quantity to vanish with speed 0. For all other  $\delta$ , one expects  $\Pr\{\frac{1}{k} \sum_{h=1}^k \mathbf{X}_h - E\mathbf{X} \geq \delta\}$  to vanish for  $k \rightarrow \infty$ . The question is, “How fast does it vanish”.

The answer was provided by Harald Cramèr in 1938 under special conditions that gradually were weakened by many authors. A survey (with history) is found in the entry on large deviations in Reference [32]. Cramèr made rigorous use of saddle point approximations that are expressed in heuristic form in the widely used justifications of the method of moments.

We shall proceed to answer the questions in two steps: a detailed study of discrete and finite addends, made possible by a theorem in Chernoff 1948, and then a quick sketch of the general case.

#### Chernoff's Theorem on Large Deviations

Chernoff's theorem applies (among other cases) when the random variable  $\mathbf{X}$  is discrete and finite, meaning that it can only take a finite number  $b$  of values  $x_1, x_2, \dots, x_b$ . Thus, its distribution can be written as  $\Pr\{\mathbf{X} = x_i\} = p_i$ ,  $i = 1, \dots, b$ , with  $\sum_1^b p_i = 1$ . The simplest example of a discrete and finite random variable is when  $p_i = 1/b$  for all  $i$ . This case corresponds to the multinomial measures discussed in Section 2.5. Hence, Chernoff's theorem provides a rigorous justification of the heuristic “Lagrange multipliers” path described in that section.

$\mathbf{X}$  being a discrete and finite random variable with  $E\mathbf{X} < 0$ , one can write [33]

$$\lim_{k \rightarrow \infty} \frac{1}{k} \log \Pr \left\{ \sum_{h=1}^k \mathbf{X}_h \geq 0 \right\} = \log \left\{ \inf_q \Phi(q) \right\},$$

where  $\Phi(q)$  is the moment generating function defined (for our purposes) by

$$\Phi(q) = E(e^{-q \ln b} \mathbf{X}).$$

The factor  $\ln b$  has been inserted for later convenience, when  $b$  will be the base of an arbitrary multinomial measure.

#### The Tail Distributions of the Coarse Hölder Exponent

Chernoff's theorem can be used to compute the tail distribution of the coarse Hölder exponent, that is, the probability

$$\Pr\{\mathbf{H}_k \geq \alpha\} = \Pr\left\{\frac{1}{k} \sum_{h=1}^k \mathbf{V}_h \geq \alpha\right\}$$

that the coarse Hölder exponent of a randomly picked interval of the binomial measure is larger than  $\alpha$  for  $\alpha > \alpha_0$ . Note that this is the probability of finding a deviation larger than  $\alpha - \alpha_0$  to the right of the most probable value  $\alpha_0$ .

We can rewrite  $\Pr\{\mathbf{H}_k \geq \alpha\} = \Pr\{\sum_{h=1}^k (\mathbf{V}_h - \alpha) \geq 0\}$  and can introduce the shifted random variable  $\mathbf{X} = \mathbf{V} - \alpha$ , so that  $\Pr\{\mathbf{H}_k \geq \alpha\} = \Pr\{\sum_{h=1}^k \mathbf{X}_h \geq 0\}$ . This  $\mathbf{X}$  satisfies  $E\mathbf{X} = E\mathbf{V} - \alpha = \alpha_0 - \alpha < 0$ . Since for the binomial measure  $\mathbf{V}$  is a discrete random variable with  $b = 2$ , the same is true of  $\mathbf{X}$ , with  $\Pr\{\mathbf{X} = v_i - \alpha_0\} = \frac{1}{2}$ . Chernoff's theorem applies and yields

$$\lim_{k \rightarrow \infty} \log_b \Pr\{\mathbf{H}_k \geq 0\} = \log_b \left\{ \inf_q \Phi(q) \right\} = \Gamma^R(\alpha). \quad (28)$$

For later convenience, we divided both sides of this main equation in Chernoff's theorem by  $\log b$ . The superscript  $R$  in this equation refers to deviations to the *right* of the most probable value  $\alpha_0$ , that is, to  $\alpha_0 < \alpha$ . Note that the above also holds for multinomial, measures and that Equation 28 only makes sense for  $\alpha \leq v_{\max} = \max\{v_0, v_1, \dots, v_{b-1}\}$ .

For the  $b$ -nomial measures  $p_i = 1/b$ ,  $i = 1, \dots, b$  and the generating function becomes

$$\Phi(q) = \frac{1}{b} \sum_{i=1}^b e^{-qx_i \ln b} = \frac{1}{b} \sum_{i=1}^b e^{-q(v_i - \alpha) \ln b} = e^{q\alpha \ln b} \frac{1}{b} \sum_{i=1}^b e^{-qv_i \ln b}.$$

From  $v_i = -\log_b m_i$ , it follows that  $e^{-qv_i \ln b} = m_i^q$ . Hence,

$$\Phi(q) = e^{q\alpha \ln b} \frac{1}{b} \sum_{i=1}^b m_i^q = e^{q\alpha \ln b} E(\mathbf{M}^q),$$

where  $\mathbf{M}$  is the random multiplier of Equation 22. By simple algebra,

$$\Gamma^R(\alpha) = \inf_q \{\log_b \Phi(q)\} = \inf_q \{q\alpha + \log_b E(\mathbf{M}^q)\}.$$

Recall now the multinomial case discussed in Section 2.5 and in Equation 18. In that case  $p_i = \frac{1}{b}$  for all  $i$ 's, hence

$$-\log_b E(\mathbf{M}^q) = -\log_b \left[ \frac{1}{b} \sum_{i=0}^{b-1} m_i^q \right] = 1 + \tau(q).$$

Therefore, it is legitimate to generalize the definition of  $\tau(q)$  to read

$$\tau(q) = -\log_b E(\mathbf{M}^q) - 1. \quad (29)$$

We see that  $\Gamma^R(\alpha)$  is the Legendre transform of  $\tau(q) + 1$  and that

$$\Gamma^R(\alpha) = \inf_q \{q\alpha - \tau(q)\} - 1.$$

Chernoff's large deviation theorem reads

$$\lim_{k \rightarrow \infty} \frac{1}{k} \log_b \Pr\{\mathbf{H}_k \geq \alpha\} = \Gamma^R(\alpha) = \inf_q \{q\alpha - \tau(q)\} - 1, \quad \alpha > \alpha_0. \quad (30)$$

For  $\alpha < \alpha_0$ , all previous steps can be redone using the shifted variable  $\mathbf{X} = \alpha - \mathbf{V}$ , and one finds

$$\lim_{k \rightarrow \infty} \frac{1}{k} \log_b \Pr\{\mathbf{H}_k \leq \alpha\} = \Gamma^L(\alpha) = \inf_q \{q\alpha - \tau(q)\} - 1, \quad \alpha < \alpha_0. \quad (31)$$

The superscripts  $L$  and  $R$  in Equations 30 and 31 cease to serve a purpose and will be dropped.

The existence of the infimum of  $\{q\alpha - \tau(q)\}$  is guaranteed [33], and one can show that  $\Gamma(\alpha)$  is smooth and concave. This infimum occurs for  $q$  such that  $\tau'(q) = \alpha = \alpha(q)$ , so that  $\Gamma(\alpha(q)) + 1 = q\alpha(q) - \tau(q) = q\tau'(q) - \tau(q)$ . It follows that  $(d/d\alpha)\Gamma(\alpha) = q$ , meaning that the slope of  $\Gamma(\alpha)$  equals  $q$ .

The quantity  $E(\mathbf{M}^q)$  is the  $q^{\text{th}}$  moment of the random variable  $\mathbf{M}$ . One can easily show that these moments exist for all  $q \in \mathcal{R}$  when  $\mathbf{M}$  is a discrete finite random variable. In particular, the multinomial measure of base  $b$  yields  $E(\mathbf{M}^q) = \frac{1}{b} \sum_{i=0}^{b-1} m_i^q < \infty$  for all  $q \in \mathcal{R}$ . However, when  $\mathbf{M}$  is not discrete and finite, the moments may diverge, i.e.,  $E(\mathbf{M}^q) = \infty$  for certain values of  $q$ . This happens for example in the  $b = \infty$  measure shown in Figure 6.

#### Identity between $\Gamma(\alpha)$ and $C(\alpha)$

The above properties of  $\Gamma(\alpha)$  are very similar to those properties that Section 3.2 has described for  $f(\alpha)$  and, hence,  $C(\alpha)$ . The only difference is that  $f(\alpha)$  and  $C(\alpha)$  were defined in Equations 1 and 2 in terms of a *number density*  $N_e$  and a *probability density*  $p_e$ , respectively, while  $\Gamma(\alpha)$  is defined through a theorem concerning *tail probabilities*. However, in the case of our large deviation probabilities, the densities and tail probabilities happen to have exactly the same behavior – except for corrections that vanish for large  $k$  if one takes a logarithm and divides by  $k$ . Indeed, observe that, using Equation 30, the existence of  $\Gamma(\alpha)$  implies that

$$\Pr\{\mathbf{H}_k \geq \alpha\} \sim (b^{-k})^{-\Gamma(\alpha)} \text{ for } \alpha > \alpha_0 \text{ and } k \rightarrow \infty.$$

The coarse Hölder exponent falls between the values  $\alpha$  and  $\alpha + d\alpha$  with the probabilities

$$\begin{aligned} p_k(\alpha)d\alpha &= \Pr\{\mathbf{H}_k \geq \alpha\} - \Pr\{\mathbf{H}_k \geq \alpha + d\alpha\} \\ &\sim (b^{-k})^{-\Gamma(\alpha)} - (b^{-k})^{-\Gamma(\alpha+d\alpha)} \\ &\sim (b^{-k})^{-\Gamma(\alpha)} [1 - (b^{-k})^{-\Gamma(\alpha+d\alpha)+\Gamma(\alpha)}]. \end{aligned}$$

$\Gamma(\alpha)$  is concave ( $\cap$ ) and  $\alpha > \alpha(0)$  is right of the maximum; hence,  $\Gamma(\alpha) > \Gamma(\alpha + d\alpha)$ , and the second term in the square bracket vanishes for large  $k$ . Thus,

$$p_k(\alpha)d\alpha \sim (b^{-k})^{-\Gamma(\alpha)}. \quad (32)$$

This same result is found for  $\alpha < \alpha_0$  if one starts with  $\Pr\{\mathbf{H}_k \leq \alpha\}$  and Equation 31. Comparing Equation 32 with Equation 2 yields  $C(\alpha) = \Gamma(\alpha)$ .

For a measure supported by a set of box-counting dimension  $D$ , the number  $N_\epsilon(\alpha)$  of boxes with a coarse Hölder exponent between  $\alpha$  and  $\alpha + d\alpha$  is the fraction  $p_\epsilon(\alpha)$  of the total number  $\epsilon^{-D}$  of boxes, i.e.,  $N_k(\alpha) = \epsilon^{-D} p_\epsilon(\alpha)$ . Using Equations 1 and 2 yields  $f(\alpha) = C(\alpha) + D$ . For a measure supported by a Euclidean set of dimension  $E$  one finds the result in Equation 3.

To summarize, we have shown that

$$C(\alpha) = \Gamma(\alpha) \text{ and } f(\alpha) = C(\alpha) + 1.$$

This generalizes in a rigorous fashion the results that Section 2.5 has obtained for the multinomial by using Lagrange multipliers and provides the probabilistic roots of the notions discussed in the Introduction in Equations 1 and 2.

#### The Continuous and/or Unbounded Cases

Cramèr's large deviation theory in the continuous and/or unbounded cases is very important and justifies a special section. But we can only state that more general Cramèr type theorems exist and that they provide a full justification of the so-called thermodynamic formalism of multifractals based on the Legendre transforms.

## 5 Some Applications and Advanced Multifractals

### Applications

Self-similar measures appear in a variety of natural phenomena. In fully developed turbulence, there is strong evidence that the rate of dissipation of kinetic energy is multifractal [21, 22, 9, 23, 41]. Multifractal measures also play an important role in the formation of fractal patterns such as lightning, aggregates, snowflakes (dendritic solidification) and fractal viscous fingering [10, 42, 43]. Related to these latter examples is the self-similarity of the electrostatic charge on fractal boundaries like the Koch tree [3] or Julia sets [34, 35, 44]. The self-similarity of these measures is

due to the interaction of the Laplace equation with a fractal boundary [3, 47]. Other occurrences of multifractals, not all of them self-similar, concern the eigenfunctions of the Schrödinger equation in disordered systems [4], the current distributions in random resistor networks [5, 45] and their hydrodynamic analogues, the distribution of mass in the universe [46], the invariant measures on strange attractors [29, 8, 9, 11, 13] and the distribution of states in the evolution pattern of a class of cellular automata. An example of the latter is the Pascal triangle discussed in Section 2.2.

In some cases, the function  $\tau(q)$  is defined for all  $q$ 's and one has  $f(\alpha) > 0$  for all  $\alpha$ . In these cases, the method of moments is sufficient. But there is increasing evidence that many applications demand more advanced multifractals. Let us mention some of the most frequently encountered cases.

### **$C(\alpha)$ and Negative $f(\alpha)$**

When  $\mu$  is a nonrandom measure handled by probabilistic methods, one always finds that  $C(\alpha) > -E$ , hence  $f(\alpha) = C(\alpha) + E > 0$ . But when  $\mu$  is properly random, there are values of  $\alpha$  for which  $f(\alpha) < 0$ . This very important possibility has recently become the subject of a significant literature [36, 37, 38, 39, 6, 7].

### **Left-sided Multifractal Measures: When the $f(\alpha)$ and the Cramèr Plot are Insufficient**

Depending on the distribution of the multiplier random variable  $\mathbf{M}$ , it can easily happen that some of the moments  $E(\mathbf{M}^q)$  are infinite. A typical case is that the moments do not exist for  $q < 0$ . For example, this appears to happen in the harmonic measure on diffusion limited aggregates [24, 48, 25, 49]. It is also the case for the exactly self-similar multifractal measure shown in Figure 6. In cases when  $E\mathbf{V} < \infty$  but  $E(\mathbf{V}^2) = \infty$ , the Gaussian central limit theorem does not apply and the left-side ( $\alpha < \alpha(0)$ ) of the maximum of  $f(\alpha)$  is not quadratic. The right-hand side ( $\alpha > \alpha(0)$ ) is a horizontal line with  $f(\alpha) = D$ , i.e. the extremum is attained in infinitely many values of  $\alpha$ . In cases when  $E(\mathbf{V}) = \infty$ , the law of large numbers also fails to apply, and since  $\alpha(0) = E(\mathbf{V}) = \infty$  the whole left-side of the  $f(\alpha)$  is infinitely stretched. The Cramèr large deviation theorems only work for deviations on the left of  $\alpha(0)$ . Alternative central limit theorems apply to these cases. The limits they involve are not Gaussian but Levy stable [40]. This issue is also important and is discussed in Ref. [25, 6, 7].

## References

- [1] Peitgen, H.-O, Jürgens, H., Saupe, D., *Chaos and Fractals* Springer-Verlag, New York, Berlin, Heidelberg (1992)
- [2] Frisch, U., Parisi, G, *Fully developed turbulence and intermittency in Turbulence and Predictability of Geophysical Flows and Climate Dynamics*, Proc. of the International School of Physics "Enrico Fermi," Course LXXXVIII, Varenna 9083, edited by Ghil, M., Benzi, R., Parisi, G., North-Holland, New York (1985) 84
- [3] Evertsz, C.J.G., Mandelbrot, B.B., *Harmonic measure around a linearly self-similar tree* J. Phys. A **25** (1992) 1781-1797
- [4] Siebesma, A.P., Pietronero, P., *Multifractal properties of wave functions for one-dimensional systems with an incommensurate potential* Europhys. Lett. **4** (1987) 597-602
- [5] Blumenfeld, R., Meir, Y., Aharony, A., Harris, A.B., *Resistance fluctuations in random diluted networks* Phys. Rev. B **35** (1987) 3524
- [6] Mandelbrot, B.B., *Selecta Volume N: Multifractals & 1/f Noise: 1963-76*. Springer, New York, to appear
- [7] Mandelbrot, B.B., *Selecta Volume T: Turbulence*. Springer, New York, to appear
- [8] Halsey, T.C., Jensen, M.H., Kadanoff, L.P., Procaccia, I., Shraiman, B.I.: *Fractal measures and their singularities: The characterization of strange sets*. Phys. Rev. A **33** (1986) 1141
- [9] Paladin, G., Vulpiani, A., *Anomalous scaling laws in multifractal objects*, Physics Reports **156** (1987) 145
- [10] Falconer, K., *Fractal Geometry*, John Wiley & Sons, Chichester (1990)
- [11] Schuster, H.G., *Deterministic Chaos*, Physik-Verlag, Weinheim (1987)
- [12] Aharony, A. and Feder, J. (Eds.), *Fractals in Physics*, Physica D **38** (1989); also published by North Holland (1989)
- [13] Feigenbaum, M.J., *Some characterizations of strange sets* J. Stat. Phys. **46** (1987) 919-924
- [14] Peyriere, J., *Multifractal measures*, Proceedings of the NATO ASI "Probabilistic Stochastic Methods in Analysis, with Applications" Il Ciocco, July 14-27 (1991)
- [15] Billingsley, P., *Ergodic Theory and Information*, J. Wiley, New York (1967). Reprinted by Robert E. Krieger Publ. Comp., Huntington, New York (1978)

- [16] Mandelbrot, B.B., *Multifractal measures, especially for the Geophysicist*, Pure and Applied Geophysics **131** (1989) 5-42, also in *Fluctuations and Pattern Formation* (Cargèse, 1988). H.E. Stanley and N. Ostrowsky, Eds., Dordrecht-Boston: Kluwer (1988) 345-360
- [17] Huang, K., *Statistical Mechanics*, M. Wiley, New York (1966) Chapter 8
- [18] Mandelbrot, B.B., *New "anomalous" multiplicative multifractals: left-sided  $f(\alpha)$  and the modeling of DLA*, Physica **A168** (1990) 95-111
- [19] Mandelbrot, B.B., Evertsz, C.J.G., Hayakawa, Y., *Exactly self-similar left-sided multifractal measures*, Phys. Rev. **A42** (1990) 4528-4536
- [20] Mandelbrot, B.B., Evertsz, C.J.G., *Exactly self-similar left-sided multifractal measures, in Fractals and Disordered Systems*, Bunde, A., Havlin, S. (Eds.) (1991) 322-344
- [21] Mandelbrot, B.B., *Intermittent turbulence in self-similar cascades: divergence of high moments and dimension of the carrier*, J. Fluid Mech. **62** (1974) 331.
- [22] Benzi, R., Paladin, G., Parisi, G., Vulpiani, A., *On the multifractal nature of fully developed turbulence and chaotic systems*, J. Phys. A **17** (1984) 3521
- [23] Meneveau, C., Sreenivasan, K.R., *Multifractal nature of turbulent energy dissipation*, J. Fluid Mech. **224** (1991) 429
- [24] Witten, T.A. and Sander, L.M., *Diffusion limited aggregation: A kinetic critical phenomena*, Phys. Rev. Lett. **47** (1981) 1400
- [25] Mandelbrot, B.B., Evertsz, C.J.G., *Multifractality of the harmonic measure on fractal aggregates, and extended self-similarity*, Physica **A 177** (1991) 386-393
- [26] Meneveau, C, Sreenivasan, K.R., *A method for the direct measurement of  $f(\alpha)$  of multifractals, and its applications to dynamical systems and fully developed turbulence*, Phys. Lett. A **137** (1989) 103
- [27] Hentschel, H.G.E., Procaccia, I., *The infinite number of generalized dimensions of fractals and strange attractors*, Physica **8D** (1983) 435
- [28] Chhabra, A., Jensen, R.V., *Direct determination of the  $f(\alpha)$  singularity spectrum*, Phys. Rev. Lett. **62** (1989) 1327
- [29] Grassberger, P., Procaccia, I., *Characterization of Strange Attractors*, Phys. Rev. Lett. **50** (1983) 346
- [30] Renyi, A: *Probability Theory*, North-Holland, Amsterdam (1970)
- [31] Mandelbrot, B. B., *Multiplications aléatoires itérées et distributions invariantes par moyenne pondérée aléatoire, I & II*, Comptes Rendus (Paris): 278A (1974) 289-292 & 355-358.
- [32] Kotz, S., Johnson, N. L., *Encyclopedia of Statistical Sciences*, J. Wiley, New York, 1982

- [33] Billingsley, P., *Probability and Measure*, John Wiley & Sons, New York, Chichester (1979)
- [34] Peitgen, H.-O., Richter, P.H., *The Beauty of Fractals*, Springer-Verlag, Heidelberg (1986)
- [35] Peitgen, H.-O., Saupe, D., (Eds.), *The Science of Fractal Images*, Springer-Verlag (1988)
- [36] Meneveau, C., Sreenivasan, K.R., *Simple multifractal cascade model for fully developed turbulence*, Phys. Rev. Lett. **59** (1987) 1424
- [37] Prasad, R.R., Meneveau, C., Sreenivasan, K.R., *Multifractal nature of the dissipation field of passive scalars in full turbulent flows*, Phys. Rev. Lett. **61** (1988) 2977
- [38] Mandelbrot, B.B., *Negative fractal dimensions and multifractals*, Physica A **163** (1990) 306-315
- [39] Mandelbrot, B.B., *Random multifractals: negative dimensions and the resulting limitations of the thermodynamic formalism*, Proc. R. Soc. Lond. A **434** (1991) 97-88
- [40] Gnedenko, B.V., Kolmogorov, A.N., *Limit distributions for sums of independent random variables*, Addison-Wesley, Reading (Mass.) - London (1968)
- [41] Frisch, U., Vergassola, M., *A prediction of the multifractal model: the intermediate dissipation range*, Europhys. Lett. **14** (1991) 439
- [42] Bunde, A., Havlin, S. (Eds.), *Fractals and Disordered Systems*, North-Holland, Amsterdam (1991)
- [43] Stanley H.E., Ostrowsky, N. (Eds.), *Fluctuations and Pattern Formation*, (Cargèse, 1988) Dordrecht-Boston: Kluwer (1988)
- [44] Procaccia, I., Zeitak, R., *Shape of fractal growth patterns: Exactly solvable models and stability considerations*, Phys. Rev. Lett. **60** (1988) 2511
- [45] Batrouni, G.G., Hansen, A., Roux, S., *Negative moments of the current spectrum in the random-resistor network*, Phys. Rev. A **38** (1988) 3820
- [46] Coleman, P.H., Pietronero, L., *The fractal structure of the universe*, Phys. Rept. **213,6** (1992) 311-389
- [47] Mandelbrot, B.B., Evertsz, C.J.G.: *The potential distribution around growing fractal clusters*, Nature **348** (1990) 143-145
- [48] Blumenfeld, R., Aharony, A., *Breakdown of multifractal behavior in diffusion limited aggregates*, Phys. Rev. Lett. **62** (1989) 2977
- [49] Evertsz, C.J.G., Mandelbrot, B.B., Woog, L.: *Variability of the form and of the harmonic measure for small off-off-lattice diffusion-limited aggregates*, Phys. Rev. A **45** (1992) 5798