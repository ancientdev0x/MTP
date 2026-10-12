

![Logo of the International Journal of the Bioflux Society, featuring a stylized yellow and orange figure.](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

Logo of the International Journal of the Bioflux Society, featuring a stylized yellow and orange figure.

# Mathematical methods used in monofractal and multifractal analysis for the processing of biological and medical data and images

Ştefan Țălu

The Technical University of Cluj-Napoca, Faculty of Mechanics, Discipline of Descriptive Geometry and Engineering Graphics, Cluj-Napoca, Romania.

**Abstract.** The purpose of this paper is to present a synthesis concerning the mathematical methods used in monofractal and multifractal analysis for the processing of biological and medical data and images. Different mathematical methods were proposed to estimate the monofractal dimension or multifractal spectrum of a fractal object. A brief overview of these algorithms, the way they work as well as their advantages and disadvantages are presented. Fractal and multifractal geometries provide noninvasive powerful tools that allow biologists, researchers and physicians the early detection and diagnosis of diseases, based on the analyses of biological and medical data and images.

**Key Words:** biology, fractals, image processing, medicine, multifractals.

**Copyright:** This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

**Corresponding Author:** Ș. Țălu, stefan\_ta@yahoo.com

## Introduction

Mathematician Benoît Mandelbrot (1924-2010) coined the term “fractal” in 1975, in order to describe complex irregular patterns and structures found in mathematics and in nature, whose complex geometry cannot be characterized by traditional Euclidean geometry, both locally and globally (Mandelbrot 1982). The central concept in fractal geometry is self-similarity or scale invariance.

An object is self-similar if it can be decomposed into smaller copies of itself (the structure of the whole is contained in its parts) (Mandelbrot 1982; Falconer 2003). Not all irregular shapes found in nature are necessarily fractals (Losa 2009). Monofractal objects are mainly characterized by four properties: a) irregularity of the shape; b) self-similarity of the structure; c) non-integer or fractional dimension; d) complexity (Mandelbrot 1982; Reljin & Reljin 2002; Falconer 2003; Grizzi *et al* 2005). Because monofractals have the same scaling properties, characterized by a single singularity exponent, they are considered as homogeneous objects (Mandelbrot 1982). A monofractal is a set for which the Hausdorff-Besicovitch dimension ( $D_h$ ) strictly exceeds its topological dimension (DT) (Mandelbrot 1982).

In Euclidian geometry, for the topologic objects, the dimension is an integer (0 for the point, 1 for a straight line, 2 for a plain surface, and 3 for a three-dimensional volume). For instance, the point is dimensionless, since the point is not a continuum and cannot be divided, and thus, both Euclidean and topological

dimensions are the same, equal to zero (Nilsson 2007; Reljin & Reljin 2002).

Euclidean geometry is suited for quantifying objects that are ideal, man-made, or regular (Reljin & Reljin 2002; Grizzi *et al* 2005). Standard shapes of Euclidean geometry such as a straight line, polygons, conics, polyhedra, spheres, torus etc. are characterized by having integer dimensionality. The Hausdorff-Besicovitch dimension  $D_h$ , introduced by mathematicians Felix Hausdorff and Abram S. Besicovitch is a quite complex definition, but it has the advantage of being defined for any set and can be expressed as the logarithmic ratio between the number  $N$  of an object's internal homotheties and the reciprocal of the common ratio  $r$  of this homothety (Lopes & Betrouni 2009):

$$D_h = \ln(N) / \ln(1 / r) \quad (1)$$

where the homothety term could be associated to a reduction term.

Multifractal objects can be considered as an infinite set of interwoven monofractals of different dimensions, being intrinsically more complex and inhomogeneous than monofractals. A multifractal object is always invariant by translation. The monofractal and multifractal analyses depend on the experimental and methodological parameters involved such as: diversity of samples, image acquisition, type of image, image processing, monofractal and multifractal analysis methods, including the

algorithm and specific calculation used etc. (Falconer 2003; Xia *et al* 2006; Nilsson 2007; Perfect *et al* 2009; Tălu 2011; Tălu & Giovanzana 2011; Haidekker 2011).

Self-similarity may be manifested as: a) exact self-similarity — this is the strongest type of self-similarity when the fractal appears identical in all scales; b) quasi self-similarity — this is a loose form of self-similarity when the fractal appears approximately (but not exactly) identical at different scales and may contain small copies of the entire fractal in distorted and degenerate forms; c) statistical self-similarity — this is the weakest type of self-similarity when the fractal has numerical or statistical measures which are preserved across scales. Random (stochastic) fractals are examples of fractals which are statistically self-similar, but neither exactly nor quasi-self-similar; d) qualitative self-similarity: as in a time series; e) multifractal scaling: characterized by more than one fractal dimension or scaling rule.

Over the last few decades, different methods have been proposed and applied extensively in the biological systems to evaluate the self-organized structures in multiple hierarchical levels, concerning the complexity of their shape (geometrical or spatial complexity) and functions (behavioral complexity) (Grizzi *et al* 2005). These irregular forms and structures, with a high degree of geometrical complexity, non-smoothness and fragmentation, that operate at different spatial and temporal scales, are not completely understood by classical methods, but can be analyzed and reproduced in much detail if they are considered as monofractal or multifractal objects (Kenkel & Walker 1996; Yu *et al* 2001; Reljin & Reljin 2002; Losa *et al* 2005; Nailon 2010; Mirvald *et al* 2011).

As no biological entity corresponds to a regular Euclidean shape, their dimension is always expressed by a non-integer (fractal dimension) falling between two integer topological dimensions (Grizzi *et al* 2005). At the same time, the concepts derived from fractal and chaos theory are fundamental to the description and modelling of scale related phenomena in biology and medicine (Havlin *et al* 1995; Kenkel & Walker 1996).

Biofractals are the fractal textures/contours in biology whose properties aid in the classification of biological and medical data and images (Sztojánov *et al* 2009). Deterministic fractals (algebraic and geometric fractals) are artificially generated structures obtained using exact rules and these fractals are exact self-similar. Algebraic fractals are created by using nonlinear processes in  $n$ -dimensional spaces, being the biggest class of fractals. Geometric fractals are generated by geometric patterns and for their construction two basic components are required: an initiator and a generator. Fractals from nature are non-deterministic, they are not exact self-similar with a regular structure as deterministic fractals, but show statistical self-similarity. This means that a magnification of a small part of the fractal will show similar statistical properties as the whole fractal, but not exactly the same (Nilsson 2007). Mathematical objects are deterministically invariant or self-similar over an unlimited range of scales. Biological components are statistically self-similar only within a fractal domain defined by upper and lower limits, in which the relationship between the scale of

observation and the measured size or length of the object can be established (Losa 2009).

In order to obtain a set for analysis, the image must be segmented, that is, divided into the feature (set) and background. Whereas binary images allow quantitative analysis of the shape of a feature, the methods that operate on gray-scale images focus more on the texture (Haidekker 2011).

## Monofractal Analysis

The monofractal dimension (referred to as FD or  $D$ ) contains information about the object's geometrical structure and can be viewed as a relative measure of complexity, or as an index of the scale-dependency of a pattern. The monofractal dimension, as a fundamental analytical parameter, is always a fractional value that describes how irregular an object is and how much of the space it occupies. A higher monofractal dimension means a greater degree of complexity, a more irregular shape of the structure (Mandelbrot 1982; Falconer 2003; Losa *et al* 2005).

### Methods for computing the fractal dimension

A major disadvantage of the Hausdorff-Besicovitch dimension (Eq. (1)) is that in many cases it is difficult to calculate or to estimate by computer numerical methods. Different numerical methods have been developed to compute the monofractal dimension, each one having its own theoretic basis. These methods approximate Eq. 1 using different algorithms. That often leads to obtaining different monofractal dimensions for the same monofractal object (Lopes & Betrouni 2009).

The most usual methods are classified into three classes (Lopes & Betrouni 2009): a) box-counting methods: a1) box-counting method; a2) differential box-counting method; a3) "extended counting" method; b) fractional Brownian motion methods: b1) variogram method; b2) the power spectrum; c) area measurement methods: c1) isarithm method; c2) blanket method; c3) triangular prism method.

## Multifractal Analysis

A multifractal analysis provides more information about the space filling properties than a monofractal one. Its advantage is that it characterizes the local scales properties in addition to the global properties (Falconer 2003; Nilsson 2007). There are two different ways of approaching multifractal analysis (Falconer 2003): a) a fine theory, where we examine the structure and dimensions of the fractals that arise themselves; b) a coarse theory, where we consider the irregularities of distribution of the measure of balls of small but positive radius  $r$  and then take a limit as  $r \rightarrow 0$ .

A multifractal structure can be characterized as a superposition of homogeneous monofractal structures. The common multifractal measures are the generalized fractal dimensions  $D_q$  and the  $f(\alpha)$  singularity spectrum (Tălu & Giovanzana 2011). Let us consider the set  $E(h)$  of Hölder exponents  $h$  of particles having scaling indices in the interval  $[h, h+dh]$ .  $F(h)$  is defined as the FD of the set  $E(h)$ , that has a monofractal structure (Lopes & Betrouni 2009).

The pair  $(h, F(h))$  can be related to  $(q, \tau(q))$  by means of the Legendre transform as (Lopes & Betrouni 2009):

$$f(h(q)) = q \cdot h(q) - \tau(q) \quad (2)$$

where

$$h(q) \approx \alpha(q) = d\tau(q) / dq \quad (3)$$

$\alpha$  being an approximation of the Hölder coefficient  $h$ .

The relation between the generalized dimension  $D_q$  and the mass (or correlation) exponent  $\tau(q)$  of the  $q$ -th order can be expressed by the following equation:

$$\tau(q) = (q - 1)D_q \quad (4)$$

The generalized dimension  $D_q$  is defined for all real  $q$  and can be expressed as (Telesca *et al* 2003):

$$D_q = \frac{1}{q-1} \lim_{\varepsilon \rightarrow 0} \frac{\ln Z(q, \varepsilon)}{\ln \varepsilon} \quad (5)$$

where:  $Z(q, \varepsilon)$  is the partition function that furnishes information at different scales and moments;  $q$  is a real parameter that indicates the order of the moment of the measure and  $\varepsilon$  is the size of the boxes used to cover the sample.

The generalized dimensions,  $D_q$  for  $q = 0$ ,  $q = 1$  and  $q = 2$ , are known as the capacity (or box-counting), the information (Shannon entropy) and correlation dimensions, respectively. All dimensions are different, satisfying  $D_0 > D_1 > D_2$ . The limits of the generalized dimension spectrum are  $D_{-\infty}$  and  $D_{\infty}$  respectively, which are related to the regions of the set, in which the measure is “most dilute” and “most dense” respectively.  $f(\alpha)$  is a continuous function of  $\alpha$ .

In fact, the curve of spectrum  $f(\alpha)$  is a single-humped function for a multifractal, while it is reduced to a point for a monofractal. The value of  $\alpha$  gives a local information about the pointwise regularity, while the value of  $f(\alpha)$  yields a global information. For a monofractal object  $D(q)$  is independent of  $q$  (being a constant for all values of  $q$ , equal to the unique monofractal dimension) and for a multifractal it is a monotone decreasing function of  $q$ .

### Methods for computing the multifractal spectrum

Different methods may be used to calculate the multifractal spectrum. The most usual methods are classified into two classes (Lopes & Betrouni 2009): a) the methods called box-counting: a1) generalized fractal dimensions and multifractal spectrum; a2) the “sand box” or cumulative mass method; a3) the large-deviation multifractal spectrum; b) the methods based on wavelets: b1) methods based on the discrete wavelet transform; b2) the wavelet transform modulus maxima method; b3) the wavelet leaders method.

### Lacunarity

The term “lacuna” comes from the Latin word *lacuna*, meaning void, gap or hole. Lacunarity was first introduced by B.

Mandelbrot as a means of further classifying fractals and textures which had the same fractal dimension and a very different visual appearance (Mandelbrot 1982; Allain & Cloitre 1991; Tălu & Giovanzana 2011). Beyond being an intuitive measure of gappiness, lacunarity measurement adds information concerning to the description of a monofractal or multifractal object (Smith *et al* 1996). Two different monofractal objects with the same monofractal dimension can have a different fractal lacunarity. In this way, lacunarity is a measure of the structural heterogeneity within a monofractal or multifractal object. If the fractal is dense the lacunarity is small. Lacunarity increases with coarseness. Moreover, lacunarity is interpreted as a measure of the lack of rotational or translational invariance of an image. There are several different methods to assess and interpret lacunarity. Lacunarity can also be used independently as a general tool for describing spatial patterns.

## Conclusions

Biology and medicine are becoming increasingly quantitative in scope and content and are presenting challenges that require sophisticated image analysis and processing methods that enhance visual interpretation, measurement and characterization. In general, in order to extract the data of interest from an image, multiple transformations and a hierarchy in the processing steps are required.

Monofractal and multifractal theory integrates essential concepts for the understanding of patterns and processes in biology and medicine, for describing and understanding biological organisms, their development and growth as well as their structural design and functional properties.

The analysis and interpretation of biological and medical images using monofractal and multifractal analysis is a multi-steps process where the purpose is to describe, measure and quantify the normal state and to detect the potential abnormalities. The significance and the advantage of this geometry compared to traditional Euclidean geometry is that it offers a new tool for examining the complex patterns found in biological and medical practice and it can be used as a non-invasive screening test to investigate the biological structures and signals.

## References

- Allain, C., Cloitre, M., 1991. Characterizing the lacunarity of random and deterministic fractal sets. *Physical Review A* 44(6):3552-3558.
- Falconer, K., 2003. *Fractal Geometry: Mathematical Foundations and Applications*, 2nd Edition, John Wiley & Sons Ltd.
- Grizzi, F., Russo, C., Colombo, P., Franceschini, B., Frezza, E. E., Cobos, E., Chiriva-Internati, M., 2005. Quantitative evaluation and modeling of two-dimensional neovascular network complexity: the surface fractal dimension. *BMC Cancer* 5(14):1-9.
- Haidekker, M. A., 2011. *Advanced Biomedical Image Analysis*, John Wiley & Sons Ltd.
- Havlin, S., Buldyrev, S. V., Goldberger, A. L., Mantegna, R. N., Ossadnik, S. M., Peng, C. K., Simons, M., Stanley, H. E., 1995. Fractals in Biology and Medicine. *Chaos, Solitons and Fractals* 6:171-201.
- Kenkel, N. C., Walker, D. J., 1996. Fractals in the biological sciences. *Coenoses* 11:77-100.

- Lopes, R., Betrouni, N., 2009. Fractal and multifractal analysis: A review. *Medical Image Analysis* 13:634–649.
- Losa, G. A., Merlini, D., Nonnenmacher, T. F., Weibel, E. (eds.), 2005. *Fractals in Biology and Medicine*, Vol. IV. Mathematics and Biosciences in Interaction. Birkhäuser Verlag, Basel, Switzerland.
- Losa, G. A., 2009. The fractal geometry of life. *Rivista di Biologia* 102(1):29-59.
- Mandelbrot, B. B., 1982. *The Fractal Geometry of Nature*, Freeman W. H., San Francisco, USA.
- Mirvald, C., Surcel, C., Gingu, C., Udrea, A., Sinescu, I., 2011. Geometria fractală și aplicațiile acesteia în medicină. *Revista Română de Urologie* 2(10):5-11.
- Nailon, W. H., 2010. *Texture Analysis Methods for Medical Image Characterisation*. In “Biomedical Imaging”, pp. 75-100. Edited by: Youxin Mao, InTech, Croatia, ISBN 978-953-307-071-1.
- Nilsson, E., 2007. Master's Thesis: *Multifractal-based Image Analysis with applications in Medical Imaging*. Umea University, Sweden.
- Perfect, E., Tarquis, A. M., Bird, N. R. A., 2009. Accuracy of generalized dimensions estimated from grayscale images using the method of moments. *Fractals* 17(3):351-363.
- Reljin, I. S., Reljin, B. D., 2002. Fractal geometry and multifractals in analyzing and processing medical data and images. *Archive of Oncology* 10(4):283-293.
- Smith, T. G. Jr., Lange, G. D., Marks, W. B., 1996. Fractal methods and results in cellular morphology - dimensions, lacunarity and multifractals. *Journal of Neuroscience Methods* 69(2):123-36.
- Sztojánov, I., Crişan, D. A., Mina, C. P., Voinea, V., 2009. Image Processing in Biology Based on the Fractal Analysis. In “Image Processing”, pp. 323-344. Edited by: Yung-Sheng Chen, InTech, Croatia, ISBN 978-953-307-026-1.
- Telesca, L., Colangelo, G., Lapenna, V., Macchiato, M., 2003. Monofractal and multifractal characterization of geoelectrical signals measured in southern Italy. *Chaos, Solitons and Fractals* 18(2):385-399.
- Țălu, Ș., Giovanzana, S., 2011. Fractal and multifractal analysis of human retinal vascular network: a review. *Human & Veterinary Medicine* 3(3):205-212.
- Țălu, Ș., 2011. Fractal analysis of normal retinal vascular network. *Oftalmologia* 55(4):11-16.
- Xia, Y., Feng, D., Zhao, R., 2006. Morphology-based multifractal estimation for texture segmentation. *IEEE Trans Image Process* 15(3):614–623.
- Yu, Z. G., Anh, V., Lau, K. S., 2001. Measure representation and multifractal analysis of complete genomes. *Physical Review E: Statistical, Nonlinear, and Soft Matter Physics* 64(3):031903.

## Author

- Ștefan Țălu, The Technical University of Cluj-Napoca, Faculty of Mechanics, Discipline of Descriptive Geometry and Engineering Graphics, B-dul Muncii 103-105, Cluj-Napoca 400641, Romania, e-mail: stefan\_ta@yahoo.com.

|                                        |                                                                                                                                                                                                         |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <b>Citation</b>                        | Țălu, Ș., 2012. Mathematical methods used in monofractal and multifractal analysis for the processing of biological and medical data and images. <i>Animal Biology &amp; Animal Husbandry</i> 4(1):1-4. |
| <b>Editor</b>                          | Miklos Botha                                                                                                                                                                                            |
| <b>Received</b>                        | 10 February 2012                                                                                                                                                                                        |
| <b>Accepted</b>                        | 10 March 2012                                                                                                                                                                                           |
| <b>Published Online</b>                | 10 May 2012                                                                                                                                                                                             |
| <b>Funding</b>                         | None reported                                                                                                                                                                                           |
| <b>Conflicts / Competing Interests</b> | None reported                                                                                                                                                                                           |