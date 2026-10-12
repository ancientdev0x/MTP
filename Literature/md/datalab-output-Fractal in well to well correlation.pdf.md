

![Elsevier logo featuring a tree and the text 'NON SOLUS' and 'ELSEVIER'](935eed7aa61f7777f62cfc032e11bee9_img.jpg)

Elsevier logo featuring a tree and the text 'NON SOLUS' and 'ELSEVIER'

![Cover image of Computers & Geosciences journal showing a person working at a computer with a map in the background](390120de4fe440c42fea8154fcaad334_img.jpg)

Cover image of Computers & Geosciences journal showing a person working at a computer with a map in the background

## Research paper

# Fractal parameters and well-logs investigation using automated well-to-well correlation

![CrossMark logo](6ed175c791b5e156d9c98a8dbcc3318c_img.jpg)

CrossMark logo

Seyyed Mohammad Amin Partovi, Saeid Sadeghnejad<sup>\*</sup>

Department of Petroleum Engineering, Faculty of Chemical Engineering, Tarbiat Modares University, Tehran, Iran

## ARTICLE INFO

**Keywords:**  
Well-to-well correlation  
Well-log  
Geological boundary  
Fractal parameters  
Wavelet transform  
Pattern recognition

## ABSTRACT

The aim of well-to-well correlation is to detect similar geological boundaries in two or more wells across a formation, which is usually done manually. The construction of such a correlation by hand for a field with several wells is quite complex and also time-consuming as well. The aim of this study is to speed up the well-to-well correlation process by providing an automated approach. The input data for our algorithm is the depths of all geological boundaries in a reference well. The algorithm automatically searches for similar depths associated with those geological boundaries in other wells (i.e., observation wells). The fractal parameters of well-logs, such as wavelet exponent ( $H_w$ ), wavelet standard deviation exponent ( $H_{ws}$ ), and Hausdorff dimension ( $H_a$ ), which are calculated by wavelet transform, are considered as pattern recognition dimensions during the well-to-well correlation. Finding the proper fractal dimensions in the automatic well-to-well correlation approach that provide the closest geological depth estimation to the results of the manual interpretation is one of the prime aims of this research. To validate the proposed technique, it is implemented on the well-log data from one of the Iranian onshore oil fields. Moreover, the capability of gamma ray, density, and sonic log in automatic detection of geological boundaries by this novel approach is also analyzed in detail. The outcome of this approach shows promising results.

## 1. Introduction

Correlation or stratigraphic correlation is a geological term referring to a process by which two or more geological intervals are equated even though they are spatially separated (Luthi, 2001). Recognition of geological boundaries to provide a three-dimensional geological model of a formation is so essential. This geological model, that contains important information (e.g., the location of geological layers), is required to be accurate for reservoir simulation purposes. Therefore, well-to-well correlation plays an important role in the characterization of hydrocarbon formations.

The common sets of data that are used to build a geological model include well-logs, cores, and seismic data. In particular, these sources of data play an important role in the identification and correlation of stratigraphic units. Available cored wells are usually limited and the entire area of a field is not surveyed geophysically; nevertheless, logging operations are widely performed in most wells. Therefore, **well-logs due to their availability are a desirable source for stratigraphic correlation** (Perez-Muñoz et al., 2013; Hernandez-Martinez et al., 2013a; Limited, 1991). The well-to-well correlation approach is usually implemented on different wire-line logs as input data. These logs reveal

different properties of rock and/or fluid, which make them an essential tool for formation evaluation. There are excellent examples in the literature implementing different wire-line logs for well-to-well correlation purposes for example, correlation based on gamma ray (e.g., Pan et al., 2008; Lapkovsky et al., 2015), density (e.g., Le Nir et al., 1998; López and Aldana, 2007), and sonic log (e.g., Hernandez-Martinez et al., 2013b; López and Aldana, 2007). Well-to-well correlation is usually performed manually. This manual approach usually involves a large amount of visual and qualitative analysis on a big data set, including well log data, drilling data, petrography analyses, etc. (Rivera Vega, 2004; Perez-Muñoz et al., 2013). The experience of an interpreter can accelerate this time consuming manual approach; therefore, the results of this method depend on the experience of the interpreter. Moreover, it may result in multiple identification of stratigraphic boundaries by different interpreters (Chang et al., 2000; Rivera Vega, 2004; Perez-Muñoz et al., 2013). Thus, there is a need to introduce automatic approaches that can assist interpreters during well-to-well correlations. The advantage of introducing such an automated approach, in addition to cost and time saving, is reducing human errors during interpretations (Zahraa and Ghosh, 2017).

Over the last three decades, several approaches have been proposed

<sup>\*</sup> Corresponding author.

E-mail address: [sadeghnejad@modares.ac.ir](mailto:sadeghnejad@modares.ac.ir) (S. Sadeghnejad).

to detect geological boundaries from well-log data. For example, dynamic programming as an optimization method has been used for well-to-well correlation purposes (Zoraster et al., 2004; Lineman et al., 1987; Smith and Waterman, 1980; Le Nir et al., 1998). Unfortunately, the results of this method are highly affected by the thickness changes of geological layers. Moreover, the principal component analysis (PCA) method, based on multivariate statistics, is another method that has been proposed for well-to-well correlation (Sakurai and Melvin, 1988; Avseth et al., 2001; Tang et al., 2004). The limitation of this method is elimination of data in the domain of interest (Yuela et al., 1998). Furthermore, artificial intelligence (AI) has been implemented by many researchers for the well-logs characterization of geological layers (Derek et al., 1990; Wong et al., 1995; Siripitayananon et al., 2001; Bhatt and Helle, 2002; Chang et al., 2002, 2000; Alizadeh et al., 2012). Despite the significant role of artificial intelligence in development of automated well-to-well correlation, this approach cannot be considered systematic and requires a large amount of data as an input for training purposes that are not usually available (Hernandez-Martinez et al., 2013b). Geological boundary detection from well-log data based on the concept of Bayesian neural network (BNN) is another new approach (Ojha and Maiti, 2016; Maiti and Tiwari, 2010b, 2010a, 2005). Maiti and Tiwari (2010b) applied this approach on the German Continental Deep Drilling Program (KTB). The results shows the proposed BNN method is preferable to the conventional artificial neural network approaches. They also developed hybrid Monte Carlo (HMC) based neural network for classifying geological boundaries. Their results on the KTB data in addition to agreeing with earlier findings suggest the presence of finer bed boundaries that were missed in the previous studies (Maiti and Tiwari, 2010a). In addition to the mentioned methods for well-to-well correlation, there are other signal processing techniques that have been implemented to analyze well-logs, including (Tang et al., 2002; Tao et al., 2000; Baldoni et al., 1998) Fourier transform (Weedon, 2003), Walsh transform (Maiti and Tiwari, 2005; Lanning and Johnson, 1983), and wavelet transform (Pan et al., 2008; Yuan et al., 2013; Perez-Muñoz et al., 2013; Prokoph and Veizer, 1999). Recently, Singh et al. (2016) filtered well-log data by using a combined wavelet transform and Fourier transform method. In the introduced algorithm, they used wavelet transform to identify the finer scale boundary (i.e., thin layers) embedded within larger geological units.

Fractal behavior is an important characteristic of non-stationary well-log signals (Subhakar and Chandrasekhar, 2016). Prokoph (1999) applied multi-fractal analysis on well-log data to detect sedimentary discontinuities and fractal clustering of geological layers (Prokoph, 1999). Khue et al. (2002) used a generalized multi-fractal analysis of dipmeter and microresistivity logs to characterize geological formations. López and Aldana (2007) used a wavelet-based fractal analysis and waveform classifier approach to determine the fractal parameters of different well-logs (López and Aldana, 2007). They related the fractal dimension to lithological patterns (e.g., sands and shales). Subhakar and Chandrasekhar (2016) carried out fractal and multifractal studies using detrended fluctuation analysis (DFA) and multifractal DFA respectively. They identified geological boundaries through the multi-fractal behavior of well-logs and also compared the results of their approach with wavelet analysis.

The aim of this paper is to introduce an automated well-to-well correlation approach to accelerate this process. In order to investigate available geological patterns in the well-log data around target boundaries of the reference well several features are implemented. These features include fractal parameters such as wavelet exponent ( $H_w$ ), wavelet standard deviation exponent ( $H_{ws}$ ), and Hausdorff dimension ( $HA$ ). These fractal dimensions are calculated by the wavelet transform algorithm. In addition to the fractal parameters, the average value of the log signal, as a statistical parameter, is considered as a complementary feature. Our methodology is based on an automatic search for a specific depth in the observation wells that is identical (i.e.,

both fractally and statistically) to the targeted boundary in the reference well. In this study, different well-logs (i.e., gamma ray, density, and sonic) are implemented for automatic well-to-well correlation and the most successful log type is determined. To validate the approach, this algorithm is applied on the data from one of the Iranian onshore formations. In addition, an efficient fractal parameter through the proposed automatic well-to-well correlation method, which can better represent the fractal characteristics of well-logs, is determined.

The structure of this paper is organized as follows. We start with a short introduction to fractals and their applications in formation evaluation. Successively, wavelet transform and the approach to find different fractal properties by this method is investigated. Afterward, we describe our methodology in detail. It is followed by finding the proper fractal parameter. For the validation of the proposed algorithm, wire-line log data from one of the Iranian onshore formations is implemented. This is followed by our conclusions.

## 2. Fractals

A fractal is a natural phenomenon or a mathematical set that exhibits a repeating pattern that displays at different scales (Boeing, 2016). If the replication is exactly the same at every scale, it is called a self-similar pattern (Gouyet and Mandelbrot, 1996). The fractal word is adopted from a Latin word “Frāctus” meaning “broken” or “fractured” (Albers and Alexanderson, 2008; Mandelbrot, 1983). Unlike Euclidean geometry, fractal geometry is a compatible way to explain natural phenomena.

Fractals have two significant characteristics; i.e., **fractal dimension and self-similarity**. Fractal dimension describes smoothness, jaggedness and complexity of the fractal shapes and declares how a fractal shape occupies the area. Another important characteristic of fractals is self-similarity that detail how fractal shapes are similar to the main shape (Pancham, 1994).

Fractal dimension of a self-similar shape which was formed by  $N$  copies of itself obtained from the following definition (Mandelbrot, 1983).

$$D = \frac{\log(N)}{\log(r)} \quad (1)$$

where  $D$  stands for the fractal dimension and  $r$  for the scaling factor.

The Fractal dimension is the most important key factor of any type of fractal phenomena since it contains information about the geometry of self-similar shapes. Unfortunately, fractal dimension is meaningful only for a small class of strictly self-similar sets. Nevertheless, there are other definitions of dimension that are much more widely applicable. For example, Hausdorff dimension, Hurst parameter, etc. (Falconer, 2004).

It has been determined that petrophysical logs represent multi-fractal behavior (Khue et al., 2002). A multi-fractal system is a generalization of a mono-fractal system; wherein, a single exponent (i.e., fractal dimension) is not sufficient to describe throughout the entire signal (Harte, 2001) in other word, a multi-fractal system is composed of several mono-fractal systems.

Each geological layer has its own properties and its well-log shows a fluctuating behavior with a specific fractal dimension. For example, the layers at both sides (i.e., upper and lower) of a geological boundary has their own fractal properties. It is hoped to detect the geological boundary by implementing the fractal properties changes on both sides of the boundary through a pattern recognition-based concept.

## 3. Wavelet-based fractal analysis

There are several methods for calculating fractal parameters. One of the most popular methods is to implement wavelet transform, which has been more applicable over the last decade. Wavelet transform permits detection of the well-log signals in the frequency spectrum and

in depth (Prokoph and Barthelme, 1996). If a signal indicates self-similar behavior, then it can be revealed by applying wavelet transform (Jacquet and Harba, 2004, Cavanaugh et al., 2003). In this study, we implemented three fractal parameters, including, wavelet exponent ( $Hw$ ), wavelet standard deviation exponent ( $Hws$ ), and Hausdorff dimension ( $Ha$ ) to characterize well-log patterns. In the subsequent chapters first of all we generally explain wavelet transform and then we describe the method of calculating the selected fractal parameters (i.e.,  $Hw$ ,  $Hws$ , and  $Ha$ ).

### 3.1. Wavelet analysis

Wavelet analysis is capable of revealing aspects of the data that other signal analysis techniques could miss. These aspects include trends, breakdown points, discontinuities in higher derivatives, and self-similarity (Michel et al., 2010).

Wavelet transform is a rather new technique of the conventional Fourier method. This method is broadly divided into three classes: continuous, discrete, and multi-resolution-based approach (Siesler, 2012).

Wavelet transform breaks down a signal to a set of basis function that are called basis wavelet. The wavelet basis functions are obtained by dilating and translating a mother wavelet function. The result of wavelet transform is some wavelet coefficients, which are functions of position and scale. Multiplying each coefficient by the appropriately scaled and shifted wavelet yields the constituent wavelets of the original signal. The wavelet transform,  $WT(f(x))$  of a signal like  $f(x)$  (i.e., well-log in this study) is defined as

$$WT(f(x)) = \int_{-\infty}^{+\infty} f(x) \psi_{a,b}^*(x) dx \quad (2)$$

where the  $(*)$  represents complex conjugate.  $\psi_{a,b}(x)$  is an analyzing wavelet, which is obtained from a single function  $\psi(x)$  by translations and dilations:

$$\psi_{a,b}(x) = \frac{1}{\sqrt{a}} \psi\left(\frac{x-b}{a}\right) \quad (3)$$

where the parameters of translation,  $b \in R$  and dilations,  $a \in R$  and  $a > 0$  ( $R$  denotes real number) (Nie et al., 2001).

In the wavelet transform process of this study, the Mallat pyramidal algorithm (Mallat, 1989) was used. In this method, an original signal passed through two complementary filters and then emerges as two sets of components: the approximation and detail. The approximations are the high-scale, low-frequency components of the signal; whereas, the details are the low-scale, high-frequency components of it (Michel et al., 2010). Fig. 1 shows the process of wavelet decomposition at different levels. The number of levels in each wavelet transform is depended on the length of input signal, as during each transformation, the size of the signals is divided by a factor of two.

![Block diagram of wavelet transform up to n levels. The process starts with the 'Original Signal', which is split into 'Approximation 1' and 'Detail 1'. 'Approximation 1' is then split into 'Approximation 2' and 'Detail 2'. This pattern continues through 'Approximation 3' and 'Detail 3', followed by a vertical ellipsis, then 'Approximation n-1' and 'Detail n-1', and finally 'Approximation n' and 'Detail n'.](8239bdc2ad69faed67c2741625a1ca79_img.jpg)

Block diagram of wavelet transform up to n levels. The process starts with the 'Original Signal', which is split into 'Approximation 1' and 'Detail 1'. 'Approximation 1' is then split into 'Approximation 2' and 'Detail 2'. This pattern continues through 'Approximation 3' and 'Detail 3', followed by a vertical ellipsis, then 'Approximation n-1' and 'Detail n-1', and finally 'Approximation n' and 'Detail n'.

**Fig. 1.** Block diagram of wavelet transform up to  $n$  levels, the signal is split into an approximation and a detail. The approximation is then itself split into a second-level approximation and detail, and the process is repeated.

### 3.2. Fractal dimension of wavelet exponent ( $Hw$ )

Well-logs were decomposed using discrete wavelet transform, the details obtained at each level were used to calculate  $Hw$ . The variance of the details at each level is calculated by (Liu et al., 2006),

$$Var_j = \frac{1}{N/2^j - 1} \sum_{n=1}^{N/2^j} (d_{j,k} - \bar{d}_j)^2 \quad (4)$$

where  $N$  is the total number of well-log data.  $j$  is the level of decomposition,  $j \in Z$ .  $d_{j,k}$  is the wavelet coefficient at the scale of  $2^j$  and location of  $k/2^j$ , and  $\bar{d}_j$  is the mean value of  $d_{j,k}$  at the scale of  $2^j$ . The well-log data as a fractal series obeys a power law distribution (Malamud and Turcotte, 1999). Therefore, the variance function can be expressed as a power law relation with the form of,

$$Var_j(2^j) \approx (2^j)^{Hw} \quad (5)$$

where  $Hw$  is known as the wavelet exponent.  $Hw$  is the slope obtained with least-squares regression from  $\log_2(Var_j) - \log_2(2^j)$  (Liu et al., 2006).

### 3.3. Fractal dimension of wavelet STD exponent ( $Hws$ )

The standard deviation of wavelet coefficients (STD) at different scales is calculated by (Liu et al., 2006),

$$STD_j = \sqrt{\frac{\sum_{k=1}^{N/2^j} (d_{j,k} - \bar{d}_j)^2}{N/2^j - 1}} = \sqrt{\frac{\sum_{k=1}^{N/2^j} (d_{j,k} - \bar{d}_j)^2}{N/2^j - 1}} \quad (6)$$

The power law distribution of Standard deviation of wavelet exponent can be expressed as,

$$STD_j = Var_j(2^j)^{1/2} \approx (2^j)^{Hws} \quad (7)$$

$$Hws = 0.5Hw \quad (8)$$

$Hws$  is the STD exponent of wavelet and can be calculated from the slope obtained with least-squares regression of  $\log_2(STD_j) - \log_2(2^j)$  (Liu et al., 2006).

### 3.4. Hausdorff dimension ( $Ha$ )

Among fractal dimensions,  $Ha$  is the oldest and one of the most important parameters (Falconer, 2004). This dimension is usually used for non-stationary time series.  $Ha$  normally ranges in  $0 < Ha < 1$ . The energy of details is used to calculate this exponent. The power spectrum  $P(\omega)$  of a fractal signal is represented by (Liu et al., 2006),

$$P(\omega) = a\omega^{-\beta} = a\omega^{-2Ha-1} \quad (9)$$

where  $a$  denotes a constant and  $\omega$  is the angular frequency of the well-log signal. The power spectrum of a fractal signal,  $P_{2^j}(\omega)$ , which is filtered by the high-pass filter  $\hat{\psi}_{2^j}(\omega)$ , can be expressed as (Liu et al., 2006),

$$P_{2^j}(\omega) = P(\omega) |\hat{\psi}(2^{-j}\omega)|^2 \quad (10)$$

where  $\hat{\psi}_{2^j}(\omega) = \hat{\psi}(2^{-j}\omega)$  is the wavelet function with the scale  $2^j$ . The power spectrum of a discrete signal  $P_{2^j}^d(\omega)$  is calculated as follows (Liu et al., 2006),

$$P_{2^j}^d(\omega) = 2^j \sum_{m=-\infty}^{+\infty} P_{2^j}(\omega + 2^j m \pi) \quad (11)$$

Let  $E_{2^j}$  be the energy of details ( $D_{2^j} f$ ), which is a high-frequency signal, and is defined as,

$$E_{2^j} = \frac{2^{-j}}{2\pi} \int_{-2^j\pi}^{+2^j\pi} P_{2^j}^d(\omega) d\omega \quad (12)$$

By combining Eqs. (10) and (11) into (12), the following relation-

ship is obtained,

$$E_{2j+1} = 2^{2Ha} E_{2j} \tag{13}$$

Finally, the Hausdorff dimension ( $Ha$ ) is calculated by

$$Ha = \frac{1}{2} \log_2 \frac{E_{2j+1}}{E_{2j}} \tag{14}$$

Thus,  $Ha$  is half of the slope obtained with the least-squares regression from  $\log_2(\text{Energy}) - \log_2(2^j)$  (Liu et al., 2006).

## 4. Well-logs importance during well-to-well correlation

Wire-line logs, by allowing a continuous record of a formation's rock properties, have become an essential tool for formation's evaluation (Rider, 2002). A geological facies can be defined in terms of its geometry, lithology, paleontology, and sedimentary structure. Any sources which permits the recognition of these properties can form a basis for facies identification (Limited, 1991). Well-logs that are more relevant to reservoir lithology are expected to show more accurate results during well-to-well correlation. For example, the gamma ray log (GR) is a record of formation radioactivity emanating from naturally-occurring uranium, thorium and potassium. The simple GR gives the combined radioactivity of the three elements, while the spectral gamma ray (GRS) log shows the amount of each individual element contributing to this radioactivity. GRS are widely used in subsurface stratigraphy to identify facies (Catuneanu, 2006; Rider, 2002). Uranium salts can be associated with moved water that is not related to lithology. Using a uranium free gamma ray log (CGR) the effects of uranium can be removed. Natural gamma measurements are the most efficient logs for detecting shale beds (Silversides et al., 2015). This log has been one of

the most usable logs in electro-facies identification (e.g., Pan et al., 2008, Lapkovsky et al., 2015, Subhakar and Chandrasekhar, 2016, Hernandez-Martinez et al., 2013b, Hernandez-Martinez et al., 2013a, Hsieh et al., 2005).

Density log (ROHB) is a continuous record of a formation's bulk density. This is the overall density of rock including solid matrix and fluid enclosed in pores (Rider, 2002). The density log also has been used as a part of input data for well-to-well correlation in many examples (e.g., López and Aldana, 2007, Le Nir et al., 1998).

Also Sonic logs (DT) provides formation's interval transit time. The principal use of this log is evaluating porosity, but it also can provide formation lithology (Rider, 2002). There are different studies that used this log during their approaches for well-to-well correlation (e.g., López and Aldana, 2007, Perez-Muñoz et al., 2013, Hernandez-Martinez et al., 2013b).

One of the aims of this study is to find the best well log type as an input data for our automatic well-to-well correlation method. The different aspects of well-logs (i.e., information that they provide to us) is the key factor for their application in any well-to-well correlation method and will be discussed in detail.

## 5. Description of the implemented approach

The wire-line log data are the only input data required for our approach. Moreover, the depths of geological boundaries in one well (i.e., reference well) must be at least available to enable the approach to detect the similar geological boundaries in other wells.

Fig. 2 depicts the flowchart of the analysis. To do the analysis, a window with a constant length is placed on the well-log data of the reference well. The center of the window is placed on the geological

![Flowchart of automatic well-to-well correlation approach. The process starts with loading a well-log, then setting a window on the geological boundary of a reference well. It calculates average log values and fractal parameters, then sets a sliding window on the upper depth of the observation well. It calculates average log values and fractal parameters again, then analyzes the probability that the depth is identical to the geological boundary in the reference well. If it is not reaching the observation well's lowest depth, it shifts the window to the next depth. If it is, it finds the depth with the highest probability and ends.](9781500979b73a4fe5978f19edc42797_img.jpg)

```

graph TD
    Start([Start]) --> Load[Loading well-log of reference and observation well]
    Load --> SettingWindow[Setting window on geological boundary of reference well]
    SettingWindow --> CalcAvg1[Calculating average log value & fractal parameters of window]
    CalcAvg1 --> SettingSliding[Setting sliding window on upper depth of observation well]
    SettingSliding --> CalcAvg2[Calculating average log value & fractal parameters of window]
    CalcAvg2 --> AnalyzeProb[Analyzing probability that this depth is identical to geological boundary in reference well]
    AnalyzeProb --> Decision1{Is it final boundary?}
    Decision1 -- No --> SettingWindow
    Decision1 -- Yes --> End([End])
    AnalyzeProb --> Decision2{If not reaching to observation well lowest depth}
    Decision2 -- False --> ShiftWindow[Shifting window to the next depth]
    ShiftWindow --> CalcAvg2
    Decision2 -- True --> FindDepth[Finding depth with the highest probability]
    FindDepth --> End
    
```

Flowchart of automatic well-to-well correlation approach. The process starts with loading a well-log, then setting a window on the geological boundary of a reference well. It calculates average log values and fractal parameters, then sets a sliding window on the upper depth of the observation well. It calculates average log values and fractal parameters again, then analyzes the probability that the depth is identical to the geological boundary in the reference well. If it is not reaching the observation well's lowest depth, it shifts the window to the next depth. If it is, it finds the depth with the highest probability and ends.

Fig. 2. Flowchart of automatic well-to-well correlation approach using statistical and fractal parameters.

![Figure 3: Feature extraction in reference and observation wells. The left panel shows a 'Reference Well' with a signal plot and a red line indicating a 'geological boundary' between an 'upper part' and a 'lower part'. The right panel shows an 'Observation Well' with a signal plot and a dashed line indicating a 'window slides along the observation well depth'.](7a3561af571faf036baa93f5f4b1bdb9_img.jpg)

Figure 3: Feature extraction in reference and observation wells. The left panel shows a 'Reference Well' with a signal plot and a red line indicating a 'geological boundary' between an 'upper part' and a 'lower part'. The right panel shows an 'Observation Well' with a signal plot and a dashed line indicating a 'window slides along the observation well depth'.

**Fig. 3.** Feature extraction in reference and observation wells using a moving window along the well depth. Appropriate fractal parameter and average of the signal is calculated in the upper and lower part of the window.

![Figure 4: Map of the studied field and the distance between the wells. The map shows three wells: well #1, well #2, and well #3. Distances are indicated: 3100 m between well #1 and well #2, 3600 m between well #2 and well #3, and 5900 m between well #1 and well #3. A north arrow is also present.](b15e3860e0c96ed16ce77f032da6f107_img.jpg)

Figure 4: Map of the studied field and the distance between the wells. The map shows three wells: well #1, well #2, and well #3. Distances are indicated: 3100 m between well #1 and well #2, 3600 m between well #2 and well #3, and 5900 m between well #1 and well #3. A north arrow is also present.

**Fig. 4.** Map of the studied field and the distance between the wells.

![Figure 5: GR and lithological column of well#3. The figure shows a GR log (API) on the left, a lithological column in the middle, and a legend for lithology on the right. The GR log has values 0, 150, and 2860. The lithological column shows various layers labeled B1 through B5. The legend includes Limestone, Argillaceous Limestone, Shale/Marl, Claystone, Dolomitic Limestone, and Limy Dolostone.](6f1efa91fb9b476380af7a35db4f14bf_img.jpg)

Figure 5: GR and lithological column of well#3. The figure shows a GR log (API) on the left, a lithological column in the middle, and a legend for lithology on the right. The GR log has values 0, 150, and 2860. The lithological column shows various layers labeled B1 through B5. The legend includes Limestone, Argillaceous Limestone, Shale/Marl, Claystone, Dolomitic Limestone, and Limy Dolostone.

**Fig. 5.** GR and lithological column of well#3. The formation is mostly composed of limestone. The depth of the boundaries found by core and well-log data are shown on the GR log.

boundary between two different layers (Fig. 3 left). This window divides each sides of the geological layer into two signals (i.e., signals, belongs to the upper and lower layer around the boundary). The fractal parameters as well as the signal average are calculated on both signals. To find the identical boundaries in other observation wells, a similar window is moved along the depth of those observation wells (Fig. 3 right). The aim is to find a window depth in the observation wells that has similar properties (i.e., fractal and statistical properties) in the upper and lower section of the window to the reference well. Fig. 3 illustrates the applied methodology.

To discover the most probable depth in the observation well that is identical to the selected boundary in the reference well, a probability function approach is implemented. To do the analysis first a conditional probability distribution is calculated for each feature in the upper and lower part of the window. The vector size of this probability function is equal to the number of data points in the observation well. In other word, by sliding the window from the top to the bottom of the observation well (Fig. 3 right), at each depth a probability value is calculated,

$$P(O_{i,m}|R_i) = \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left[-\frac{E_{i,m}^2}{2\sigma_i^2}\right] \quad (15)$$

$P(O_{i,m}|R_i)$  is the conditional probability for feature  $i$  (e.g., fractal dimension or average value of the signal) at depth  $m$  in the observation well.  $O_{i,m}$  is the value of feature  $i$  in the observation well at the depth point  $m$ .  $R_i$  is the value of feature  $i$  at the selected boundary in the reference well.  $\sigma_i$  is the standard deviation of feature  $i$  along the observation well.  $E_{i,m}$  is the difference between the features value at the selected boundary in the reference well,  $R$ , and that in the observation well,  $O$ , at the depth  $m$  (i.e.,  $E_{i,m} = O_{i,m} - R_i$ ). As the features (e.g., fractal dimension or average of the signal) have values with different scales; therefore, in order to compare the probabilities together we should normalize them,

$$P'(O_{i,m}|R_i) = \frac{P(O_{i,m}|R_i)}{P(O_i|R_i)_{\max}} \quad (16)$$

where  $P'(O_{i,m}|R_i)$  is the normalized probability for feature  $i$  at the depth of  $m$  (i.e.,  $0 \leq P' \leq 1$ ). In the above equation,  $P(O_i|R_i)_{\max}$  is the maximum probability value obtained along the observation well for a specific feature,  $i$ . As the features (i.e., average of a signal and its fractal parameter) are independent from each other, the normalized probability of both of them can be computed by multiplying the normalized probabilities of each feature together.

$$P'(O_m|R) = \prod_{i=1}^{N_f} P'(O_{i,m}|R_i) \quad (17)$$

where  $P'(O_m|R)$  is the probability at the depth of  $m$  and  $N_f$  is number of features (i.e.,  $N_f = 2$ , fractal dimension and average signal value). The conditional probability for the top and bottom part of the window at each depth in observation well (Fig. 3 right) is calculated separately by Eq. (17). The total probability of the window showing the similarity of a specific observation depth to the selected geological boundary in the reference well is calculated by multiplying the probability of the upper and lower part of the window,

$$P_{\text{total}}(O_m|R) = P_{\text{lower window}}(O_m|R) \times P_{\text{upper window}}(O_m|R) \quad (18)$$

The algorithm calculates the probability from Eq. (18) along all depth intervals of observation wells. The output is a probability curve as function of depth. The algorithm automatically searches for the highest probable depth (i.e., the highest value of  $P(W_m|R)_{\text{total}}$ ) in the observation well. This depth of the observation well is the most similar depth to the selected boundary in the reference well.

## 6. Validation case study

The present method was validated on the well-log data of one of the

![Figure 6: Four vertical well-log plots for well#1. From left to right: CGR (GAPI), GR (GPAI), RHOB (K/M³), and DT (US/M). The y-axis for all plots is Depth (m) ranging from 2,680 to 2,820. Red horizontal lines indicate geological boundaries B1, B2, B3, B4, and B5 across all four logs.](55d2bfe1c3d04e86df8d7a104d802172_img.jpg)

Figure 6: Four vertical well-log plots for well#1. From left to right: CGR (GAPI), GR (GPAI), RHOB (K/M³), and DT (US/M). The y-axis for all plots is Depth (m) ranging from 2,680 to 2,820. Red horizontal lines indicate geological boundaries B1, B2, B3, B4, and B5 across all four logs.

**Fig. 6.** From left to right this figure contains uranium free gamma ray, gamma ray, density, and sonic Well-logs of well#1, geological boundaries are illustrated by red lines. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![Figure 7: A schematic of a Haar wavelet. The plot shows a step function with values of 1, 0, and -1 over a range of -1 to 2 on the x-axis.](ac99eff233b8fe51d30f499e7413c345_img.jpg)

Figure 7: A schematic of a Haar wavelet. The plot shows a step function with values of 1, 0, and -1 over a range of -1 to 2 on the x-axis.

**Fig. 7.** A schematic of Haar wavelet.

Iranian oil fields. The oil field is located in the west of Ahwaz city, Iran. The relative position of the studied wells is showed in Fig. 4.

The formations of this field are mostly composed of limestone, shelly limestone, and dolomitic limestone. There are also some rather thin layers of shale and sandstone which have been deposited between limestone layers. As an example Fig. 5 depicts the lithological column as well as the GR log of well#3 from the study area. For this field, manual well-to-well correlation data, based on cores and well-log data, is available, which are also shown in the figure. The results of our proposed approach will be compared with these depths.

GR, CGR, RHOB, and DT of three wells (i.e., well#1, well#2, well#3) were used to validate the methodology. Wire-line logs in Well#1 and Well#3 are comprised of 6 different layers with the geological boundary of B1–B5. However, well#2 is limited to only 2

layers (i.e., B4). First, Well#1 was selected as the reference well and the accuracy of the introduced automated well-to-well correlation was investigated in Well#2 and Well#3. Then Well#3 was substituted as the reference well and the accuracy of the introduced automated well-to-well correlation was investigated in other wells. Fig. 6 shows the CGR, GR, RHOB, and DT signal of well#1.

## 7. Results and discussion

### 7.1. Fractal parameters estimation using wavelet transform

The available well-logs were decomposed by discrete wavelet transform. GR, CGR, RHOB, and DT log were decomposed up to three levels by Daubechies wavelet with one vanishing moment (Haar wavelet) which is depicted in Fig. 7. By reflecting layer thickness distribution, this wavelet is the simplest mother wavelet that may give the most efficient decomposition. Moreover, due to its simple shape (Fig. 7) it reduces computation time. Other mother wavelet families can be implemented too; however, detecting the most suitable mother wavelet needs special analyses (e.g., energy to Shannon entropy (Katul and Vidakovic, 1996; Bedekar et al., 2005), correlation coefficient (Singh and Tiwari, 2006; Yang et al., 2004; Ma et al., 2002b, 2002a)) that are out scope of this study. (More details about wavelet families are available in Michel et al., 2010).

As an example, the three level wavelet decomposition of GR of the

![Figure 8: Wavelet decomposition of GR log of well#1 using a Haar wavelet. The figure shows five stacked plots: Original signal (red), Approximation 3 (blue), Detail 3 (green), Detail 2 (green), and Detail 1 (green). The x-axis is Data point (0 to 1000) and the y-axis scales vary for each plot.](6a412ce0ee3ac6bd290d214edd54c1da_img.jpg)

Figure 8: Wavelet decomposition of GR log of well#1 using a Haar wavelet. The figure shows five stacked plots: Original signal (red), Approximation 3 (blue), Detail 3 (green), Detail 2 (green), and Detail 1 (green). The x-axis is Data point (0 to 1000) and the y-axis scales vary for each plot.

**Fig. 8.** Wavelet decomposition of GR log of well#1 using a Haar wavelet. This signal is decomposed up to three levels. Detail coefficients in every level is used for fractal parameter estimation.

![Figure 9: Four panels showing GR (GAPI), Ha, Hw, and Hws versus Depth (m) for well#1. The depth ranges from 2680 to 2820 m. Red horizontal lines mark geological boundaries B1, B2, B3, B4, and B5. The GR (GAPI) panel shows values from 0 to 150. The Ha panel shows values from -3 to 1. The Hw panel shows values from -2 to 6. The Hws panel shows values from -1 to 3.](c0843c6d138705289960d9f53a6e72a1_img.jpg)

Figure 9: Four panels showing GR (GAPI), Ha, Hw, and Hws versus Depth (m) for well#1. The depth ranges from 2680 to 2820 m. Red horizontal lines mark geological boundaries B1, B2, B3, B4, and B5. The GR (GAPI) panel shows values from 0 to 150. The Ha panel shows values from -3 to 1. The Hw panel shows values from -2 to 6. The Hws panel shows values from -1 to 3.

Fig. 9. Fluctuation of GR and fractal parameters extracted from GR log of well#1. From left to right shows: GR,  $H_a$ ,  $H_w$ , and  $H_{ws}$  of the reference well (Well#1).

![Figure 10: A scalogram titled 'Details Coefficients' showing wavelet decomposition levels (1 to 3) versus Depth (m) from 2680 to 2820 m. A color scale at the bottom indicates values from MIN to MAX.](c64e9e9f3b0b828a5f6ac70441877764_img.jpg)

Figure 10: A scalogram titled 'Details Coefficients' showing wavelet decomposition levels (1 to 3) versus Depth (m) from 2680 to 2820 m. A color scale at the bottom indicates values from MIN to MAX.

Fig. 10. Detail coefficients obtained by discrete wavelet decomposition of GR log of well#1.

![Figure 11: Three plots showing the calculation of Hw, Hws, and Ha. Each plot shows data points (red circles) and a linear fit (blue line) of Log2(Var) or Log2(STD) versus Log2(2^j) for j=1 to 4. The plots are titled 'Hw Calculation', 'Hws Calculation', and 'Ha calculation'.](01da0d212fb571933f10f96556157745_img.jpg)

Figure 11: Three plots showing the calculation of Hw, Hws, and Ha. Each plot shows data points (red circles) and a linear fit (blue line) of Log2(Var) or Log2(STD) versus Log2(2^j) for j=1 to 4. The plots are titled 'Hw Calculation', 'Hws Calculation', and 'Ha calculation'.

Fig. 11.  $H_w$ ,  $H_{ws}$ , and  $H_a$  are calculated around the boundary B1 of the GR log in well#3. Each data point is related to one level of decomposition. If the deviation of data points from the least squares regression line is less, the parameter calculated more accurately.

reference well is depicted in Fig. 8. The maximum level of decomposition is directly related to the length of the input signal as during each decomposition level, the length of the signals reduced to the half-length of the previous level.

The fractal parameters (i.e.,  $H_w$ ,  $H_{ws}$ , and  $H_a$ ) can be computed from the wavelet decomposition results by implementing Eqs. (5), (8), and (14), respectively. Fig. 9 represents the GR log and the fractal parameters extracted from GR log of well#1. The boundaries of geological layers B1 to B5 is depicted in the figure.

As it is clear from Fig. 9, GR log has multi-fractal behavior and one can see the changes in the fractal parameter value along the well depth. In addition, the amount of changes in the value of fractal parameters above and below of each geological boundary (i.e., B1–B5) is similar to the GR behavior. This behavior can be implemented in the proposed automatic approach to characterize the fractal parameters (as a pattern recognition tool).

### 7.2. Analyzing fractal parameters for well-log characterization

The performance of fractal parameters in evaluation of the characteristics of a time series depends on the strength and range of persistence of that time series; therefore, it is essential to find the parameter that can better represent the fractal characteristics of well-logs. To do so, the approach of Liu et al. (2006) was implemented. They introduced a new method to find a proper fractal dimension definition for their problem. They also determined the suitable fractal parameter, which has smaller deviation and is able to characterize their problem in wide ranges. Here, their approach is implemented to evaluate the efficiency of the fractal parameters during the characterization of well-logs. For this purpose, GR log of the reference well is decomposed using a Haar wavelet. Fig. 10 is the wavelet scalogram that displays the detail coefficients of the GR log of the reference well.

The detail coefficients obtained by the wavelet decomposition are used to calculate the fractal parameters.  $H_w$  and  $H_{ws}$  can be computed

![Figure 12: Four vertical plots showing geological and probability distributions for Well#3. From left to right: GR (GAPI), Hws, Average (GAPI), and P(Om|R) total. The y-axis for all plots is Depth (m) from 2780 to 2880. A red horizontal line at 2789.9 m is labeled 'Maximum possibility'.](a71911ad87414271aeb190e0eebcb989_img.jpg)

Figure 12: Four vertical plots showing geological and probability distributions for Well#3. From left to right: GR (GAPI), Hws, Average (GAPI), and P(Om|R) total. The y-axis for all plots is Depth (m) from 2780 to 2880. A red horizontal line at 2789.9 m is labeled 'Maximum possibility'.

**Fig. 12.** Total probability distribution and geological boundary detection in well#3, from left to right this figure shows: GR log, *Hws* distribution, Average parameter distribution, and  $P(O_m|R)_{total}$  in well#3.

**Table 1**

Results of automated well-to-well correlation for all well-log data of the field under study. Well#1 was selected as the reference well and boundary depths in well#2 and well#3 are investigated. All the depths and their differences are in meter.

| Boundary | Well#2               |                      |                                      | Well#3               |                      |                                      |
|----------|----------------------|----------------------|--------------------------------------|----------------------|----------------------|--------------------------------------|
|          | <i>D<sub>m</sub></i> | <i>D<sub>u</sub></i> | <i>D<sub>m</sub> – D<sub>u</sub></i> | <i>D<sub>m</sub></i> | <i>D<sub>u</sub></i> | <i>D<sub>m</sub> – D<sub>u</sub></i> |
| GR       | B1                   | –                    | –                                    | 2787.8               | 2786.2               | 1.6                                  |
|          | B2                   | –                    | –                                    | 2790.6               | 2789.9               | 0.7                                  |
|          | B3                   | –                    | –                                    | 2795.2               | 2794.5               | 0.7                                  |
|          | B4                   | 2749.9               | 2751.2                               | 2819.5               | 2821.2               | –1.7                                 |
|          | B5                   | –                    | –                                    | 2873.5               | 2878.9               | –5.4                                 |
| CGR      | B1                   | –                    | –                                    | 2787.8               | 2785.9               | 1.9                                  |
|          | B2                   | –                    | –                                    | 2790.6               | 2789.8               | 0.8                                  |
|          | B3                   | –                    | –                                    | 2795.2               | 2794.3               | 0.9                                  |
|          | B4                   | 2749.9               | 2749.5                               | 2819.5               | FAILED <sup>a</sup>  | FAILED                               |
|          | B5                   | –                    | –                                    | 2873.5               | 2867.9               | 5.6                                  |
| RHOB     | B1                   | –                    | –                                    | 2787.8               | 2795.4               | –7.4                                 |
|          | B2                   | –                    | –                                    | 2790.6               | 2793.7               | –3.1                                 |
|          | B3                   | –                    | –                                    | 2795.2               | 2789.6               | 5.6                                  |
|          | B4                   | 2749.9               | 2750.3                               | 2819.5               | FAILED               | FAILED                               |
|          | B5                   | –                    | –                                    | 2873.5               | 2867.1               | 6.4                                  |
| DT       | B1                   | –                    | –                                    | 2787.8               | FAILED               | FAILED                               |
|          | B2                   | –                    | –                                    | 2790.6               | 2790.0               | 0.6                                  |
|          | B3                   | –                    | –                                    | 2795.2               | 2793                 | 2.2                                  |
|          | B4                   | 2749.9               | 2748.3                               | 2819.5               | FAILED               | FAILED                               |
|          | B5                   | –                    | –                                    | 2873.5               | 2864.8               | 8.7                                  |

<sup>a</sup> The FAILED phrase is used when the approach is not able to successfully detect the boundary and the deviation between the automated approach and manual approach was more than 10 m.

by measuring the slope of the best least-squares fit to  $\log_2(Var_j) - \log_2(2^j)$  and  $\log_2(STD_j) - \log_2(2^j)$ , respectively. In addition, *Ha* is the half of the slope of least-squares regression line from  $\log_2(Energy) - \log_2(2^j)$  as was discussed in Section 3. The fractal parameters were calculated at all depths of the reference well. Fig. 11 shows the fractal calculation process around B1 for the GR log of the reference well. It is worth mentioning that in order to avoid the influence of adjacent layers during parameter estimations in thin layers; we should analyze the well log data within a window whose size is not larger than the thickness of the geological layers. This can restrict the wavelet decomposition levels (i.e., number of data points in Fig. 11) as the number of well-log data points are divided by a factor of

**Table 2**

Results of the automated well-to-well correlation for GR log. Well#3 was selected as the reference well and depths of the boundaries in well#1 and well#2 are investigated. All the depths and their difference are in meter.

| Boundary | Well#1               |                      |                                      | Well#2               |                      |                                      |
|----------|----------------------|----------------------|--------------------------------------|----------------------|----------------------|--------------------------------------|
|          | <i>D<sub>m</sub></i> | <i>D<sub>u</sub></i> | <i>D<sub>m</sub> – D<sub>u</sub></i> | <i>D<sub>m</sub></i> | <i>D<sub>u</sub></i> | <i>D<sub>m</sub> – D<sub>u</sub></i> |
| GR       | B1                   | 2698.9               | 2700.2                               | –1.3                 | –                    | –                                    |
|          | B2                   | 2702.4               | 2703.6                               | –1.2                 | –                    | –                                    |
|          | B3                   | 2707.8               | 2706.7                               | 1.1                  | –                    | –                                    |
|          | B4                   | 2736.0               | 2734.2                               | 1.8                  | 2749.9               | 2752.1                               |
|          | B5                   | 2789.4               | 2786.3                               | 3.1                  | –                    | –                                    |

two during each decomposition level. Considering the layer thicknesses of the formation under study, we can decompose the well-log data by wavelet transform only for four levels.

The residuals that are the vertical difference between data points and the least-squares regression lines were calculated for all available well-logs. The mean value of the residual of *Hw*, *Hws*, and *Ha* were computed as 0.99, 0.56, and 0.61, respectively. Based on Liu et al. (2006), less residual indicates better fitness of data. *Hws* and *Ha* were fitted better than *Hw* so they can be more accurate than *Hw* to represent fractal characteristics of the well-logs.

In addition, it is evident from Fig. 9 that the computed values for *Ha* parameter in some depth intervals has negative values. These negative values are out of the definition of a fractal dimension. Therefore, *Ha* is clearly unsuitable to describe the fractal characteristics of well-log data. As a result, among the three fractal parameters, *Hws* is selected as a proper parameter for well-to-well correlation through the proposed approach.

### 7.3. Well-to-well correlation using the introduced algorithm

Subsequent to the determination of proper fractal parameter, *Hws* along with the average of the signal were calculated at upper and lower part of the window around a selected geological boundary in the reference well. As discussed before, to find the same boundary in the other wells, a similar window is moved along the observation well depth and the associated features are extracted. As an example, Fig. 12 represents the distribution of the features along well#3 and around B2 and the total probability,  $P(O_m|R)_{total}$ , was calculated based on Eqs. (15)–(18). The depth with the maximum probability,

![Figure 13: Comparison of automatic and manual well-to-well correlation results. The figure shows three GR (GAPI) logs for a Reference well (well#1) and two Observation wells (well#2 and well#3). The logs plot GAPI values against Depth (m). Red lines represent manual approach boundaries, and black lines represent automated approach boundaries. boundaries are labeled B1, B2, B3, B4, and B5. Lines connect corresponding boundaries between the reference and observation wells to show the correlation.](91be14371a97fb5ce9eeb29ae18d07c3_img.jpg)

Figure 13: Comparison of automatic and manual well-to-well correlation results. The figure shows three GR (GAPI) logs for a Reference well (well#1) and two Observation wells (well#2 and well#3). The logs plot GAPI values against Depth (m). Red lines represent manual approach boundaries, and black lines represent automated approach boundaries. boundaries are labeled B1, B2, B3, B4, and B5. Lines connect corresponding boundaries between the reference and observation wells to show the correlation.

**Fig. 13.** Comparing results of automatic well-to-well correlation with manual approach. The associated depths from manual approach are shown in black and the predicted depths from the automatic approach are shown in red. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![Figure 14: Bar chart showing the average deviation of automatic approach from manual approach for different well-log types. The y-axis is 'Average deviation from manual approach' (0 to 5). The x-axis is 'Well-logs' (GR, CGR, RHOB, DT).](891ff9b651838b7f59e9a1612a739e15_img.jpg)

| Well-log | Average deviation from manual approach |
|----------|----------------------------------------|
| GR       | 1.9                                    |
| CGR      | 1.92                                   |
| RHOB     | 4.58                                   |
| DT       | 2.82                                   |

Figure 14: Bar chart showing the average deviation of automatic approach from manual approach for different well-log types. The y-axis is 'Average deviation from manual approach' (0 to 5). The x-axis is 'Well-logs' (GR, CGR, RHOB, DT).

**Fig. 14.** Average deviation of automatic approach from manual approach for all available well-logs. The figure shows GR log was the best input for well-to-well correlation.

$m @ \max \{P(O_m | R)_{total}\}$ , is the most possible location which is similar to the selected boundary (i.e., B2) of the reference well. The calculated depth at the most possible location is located at 2789.9 m, which is very close to the depth of boundary B2 in well#3 obtained by the manual well-to-well correlation approach (i.e., at 2790.6 m).

Table 1 summarizes the results of automated well-to-well correlation for all available well-logs of the field under study. In this table, well#1 was selected as the reference well and boundary depths in the other wells were investigated. The difference between the depths obtained by the automatic approach, ( $D_a$ ), and the manual approach, ( $D_m$ ), is shown in this table as a third column ( $D_m - D_a$ ) reflects the accuracy of the automated well-to-well correlation.

The average deviation of the automatic approach applied to the GR log is about 1.9 m; whereas, the automated approach failed in detecting boundaries in other log types at least at one boundary. The relative error along the well#1 is about 0.009, which is really acceptable.

Unfortunately, the field under study is in its early development phase and no more wells have been drilled in it yet. To strengthen our conclusion about the applicability of this approach to further wells, we also substituted observation and reference wells. Table 2 summarizes the results of automated well-to-well correlation on GR data in the case of well#3 as a reference well and well#1 and well#2 as the observation wells. By substituting the wells again the results showed promising outputs in estimation of the geological layer depths with the average deviation of about 1.8 m for GR log.

Fig. 13 compares the boundary depths found by the automatic approach with the manual ones. Considering the advantages of the automated approach over the manual one reveals that this method can be an acceptable approach for the estimation of depth of geological boundaries during well-to-well correlation.

Fig. 14 summarizes the average deviation of the boundary depth from the automatic approach (mentioned in Table 1) comparing with that in manual approach for different well-log types (i.e., GR, CGR, RHOB, and DT). The results indicated that implementing GR, among all studied well-logs, result in a better prediction of the boundary depth in the observation wells. In other word, this log is the most appropriate one and can provide the geological boundaries with less deviation in our automatic approach.

As discussed in Section 4, the response of each log depends on many aspects such as rock properties, type of formation fluid, and diagenesis processes. Relationship between facies and the amount of emitted gamma radiation makes gamma ray an efficient log for stratigraphy interpretation. However, low contrast between some facies can limit geological boundary identification. In addition, loose attachment of uranium cause heterogeneous distribution in sediments and some irregular peaks corresponding to its uneven distribution (Rider, 2002). Nevertheless, uranium contained within some heavy minerals and sometimes associated with organic materials and phosphatic rocks can be indicative of specific lithology and help well-to-well correlation process.

According to the results, GR detects all boundaries and its deviation from manual method is rather acceptable. The shallow depth of investigation of density log makes it dependent on well hole condition. In addition, density log is itself a poor indicator of lithology due to the formation fluid influences. Moreover, the formation response of sonic log is not indicator of lithology too. Variation of the sonic velocity within each lithology type and overlapping between various lithology makes this log unreliable for detecting lithology, which is in agreement by our results.

## 8. Conclusions

In this study, an automated approach of well-to-well correlation on well-logs was presented. Several fractal parameters including  $H_w$ ,

$Hus$ , and  $Ha$  were used to describe the well-log patterns. To compute the fractal parameters of well-logs, wavelet transform decomposition were implemented.

By comparing the results of these fractal parameters during well-log characterization,  $Hus$  was chosen as the most suitable parameter which can evaluate multi-fractal characteristics of well-logs.

Various well-log types, including GR, CGR, RHOB, and DT, were used in our automated technique. According to the results, among all implemented well-log data, GR showed promising results and could detect all boundaries in the field under study.

The results obtained from using this technique on a real case study from one of the Iranian oil fields demonstrated the capability of this automated well-to-well correlation approach. This automated approach can save time and money, and can prevent multiple interpretations. As the detection of the geological boundaries in this approach is based on the pattern recognition of well-logs; therefore, it is not affected by thickness changes across the formation.

## References

- Albers, D.J., Alexanderson, L.G. 2008. Benoit Mandelbrot: In his own Words. *Mathematical People: Profiles and Interviews*. Wellesley, MA: AK Peters, p. 214.
- Alizadeh, B., Najjari, S., Kadkhodaie-Ilkhchi, A., 2012. Artificial Neural Network Modeling and Cluster Analysis for Organic Facies and Burial History Estimation Using Well Log Data: A Case Study of the South Pars Gas Field, Persian Gulf 45. *Computers & Geosciences*, Iran, 261–269.
- Avseth, P., Mukerji, T., Jørstad, A., Mavko, G., Veggeland, T., 2001. Seismic reservoir mapping from 3-D AVO in a North Sea turbidite system. *Geophysics* 66, 1157–1176.
- Bedekar, D., Nair, A., DVO, G., 2005. Choosing the optimal mother wavelet for decomposition of radio-frequency intravascular ultrasound data for characterization of atherosclerotic plaque lesions. *Medical Imaging, Int. Soc. Opt. Photonics*, 490–502.
- Bhatt, A., Helle, H.B., 2002. Determination of facies from well logs using modular neural networks. *Pet. Geosci.* 8, 217–228.
- Boeing, G., 2016. Visual analysis of nonlinear dynamical systems: chaos, fractals, self-similarity and the limits of prediction. *Systems* 4, 37.
- Catuneanu, O., 2006. Principles of Sequence Stratigraphy. Elsevier.
- Cavaugh, J.E., Wang, Y., Davis, J.W., 2003. Locally self-similar processes and their wavelet analysis. *Handb. Stat.* 21, 93–135.
- Chang, H.-C., Kopaska-Merkel, D.C., Chen, H.-C., 2002. Identification of lithofacies using Kohonen self-organizing maps. *Comput. Geosci.* 28, 223–229.
- Chang, H.-C., Kopaska-Merkel, D.C., Chen, H.-C., Durrans, S.R., 2000. Lithofacies identification using multiple adaptive resonance theory neural networks and group decision expert system. *Comput. Geosci.* 26, 591–601.
- Derek, H., Johns, R., Pasternack, E., 1990. Comparative study of back-propagation neural network and statistical pattern recognition techniques in identifying sandstone lithofacies. In: *Proceedings 1990 Conference on Artificial Intelligence in Petroleum Exploration and Production: College Station, TX, Texas A & M University*, pp. 41–49.
- Falconer, K., 2004. *Fractal Geometry: Mathematical Foundations and Applications*. John Wiley & Sons, Chichester, England.
- Gouy, J.-F., Mandelbrot, B., 1996. *Physic and Fractal Structures*. Masson, Paris.
- Harte, D., 2001. *Multifractals: Theory and Applications*. CRC Press, Boca Raton, Florida.
- Hernandez-Martinez, E., Velasco-Hernandez, J.X., Perez-Muñoz, T., Alvarez-Ramirez, J., 2013b. A DFA approach in well-logs for the identification of facies associations. *Phys. A: Stat. Mech. Appl.* 392, 6015–6024.
- Hernandez-Martinez, E., Perez-Muñoz, T., Velasco-Hernandez, J.X., Altamira-Areyan, A., Velasquillo-Martinez, L., 2013a. Facies recognition using multifractal Hurst analysis: Applications to well-log data. *Math. Geosci.* 45, 471–486.
- Hsieh, B.-Z., Lewis, C., Lin, Z.-S., 2005. Lithology Identification of Aquifers from Geophysical Well Logs and Fuzzy Logic Analysis: Shui-Lin Area 31. *Computers & Geosciences*, Taiwan, 263–275.
- Jacquet, G., Harba, R., 2004. Wavelet based estimator for fractional brownian motion: an experimental point of view. In: *Signal Processing Conference*, 2004 12th European, 2004. IEEE, pp. 1175–1178.
- Katul, G., Vidakovic, B., 1996. The partitioning of attached and detached eddy motion in the atmospheric surface layer using Lorentz wavelet filtering. *Bound. Layer. Meteorol.* 77, 153–172.
- Khue, P.N., Huseby, O., Saucier, A., Muller, J., 2002. Application of generalized multifractal analysis for characterization of geological formations. *J. Phys.: Condens. Matter* 14, 2347.
- Lanning, E.N., Johnson, D.M., 1983. Automated identification of rock boundaries: an application of the Walsh transform to geophysical well-log analysis. *Geophysics* 48, 197–205.
- Lapkovsky, V., Istomin, A., Kontorovich, V., Berdov, V., 2015. Correlation of well logs as a multidimensional optimization problem. *Russ. Geol. Geophys.* 56, 487–492.
- Le Nir, I., Van Gysel, N., Rossi, D., 1998. Cross-section construction from automated well log correlation: a dynamic programming approach using multiple well logs. In: *SPWLA 39th Annual Logging Symposium*, 1998. Society of Petrophysicists and Well-Log Analysts.
- Limited, S., 1991. *Log Interpretation Principles/Applications*. Schlumberger Educational Services.
- Lineman, D., Mendelson, J., Tokoz, M.N., 1987. Well-to-well Log Correlation Using Knowledge-based Systems and Dynamic Depth Warping. Massachusetts Institute of Technology. Earth Resources Laboratory.
- Liu, X., Wang, H., Gu, H., 2006. Fractal characteristic analysis of electrochemical noise with wavelet transform. *Corros. Sci.* 48, 1337–1367.
- López, M., Aldana, M., 2007. Facies recognition using wavelet based fractal analysis and waveform classifier at the Oritupano-A Field, Venezuela. *Nonlinear Process. Geophys.* 14, 325–335.
- Luthi, S., 2001. *Geological Well Logs: Their Use in Reservoir Modeling*. Springer-Verlag, Berlin, Heidelberg.
- Ma, X., Zhou, C., Kemp, I., 2002a. Automated wavelet selection and thresholding for PD detection. *IEEE Electr. Insul. Mag.* 18, 37–45.
- Ma, X., Zhou, C., Kemp, I., 2002b. Interpretation of dielectric analysis and its application in partial discharge detection. *IEEE Trans. Dielect. Electr. Insul.* 9, 446–457.
- Maiti, S., Tiwari, R., 2005. Automatic detection of lithologic boundaries using the Walsh transform: a case study from the KTB borehole. *Comput. Geosci.* 31, 949–955.
- Maiti, S., Tiwari, R.K., 2010a. Automatic discriminations among geophysical signals via the Bayesian neural networks approach. *Geophysics* 75, E67–E78.
- Maiti, S., Tiwari, R.K., 2010b. Neural network modeling and an uncertainty analysis in Bayesian framework: a case study from the KTB borehole site. *J. Geophys. Res.: Solid Earth*, 115.
- Malamud, B.D., Turcotte, D.L., 1999. Self-affine time series: measures of weak and strong persistence. *J. Stat. Plan. Inference* 80, 173–196.
- Mallat, S.G., 1989. A theory for multiresolution signal decomposition: the wavelet representation. *Pattern Anal. Mach. Intell. IEEE Trans.* 11, 674–693.
- Mandelbrot, B.B., 1983. *The Fractal Geometry of Nature*. W. H. Freeman and Company, New York.
- Michel, M., Misiti, Y., Oppenheim, G., Poggi, J., 2010. Wavelet Toolbox4 User's Guide. The MathWorks, Inc, Natick, Massachusetts, 1–27.
- Nie, L., Wu, S., Wang, J., Zheng, L., Lin, X., Rui, L., 2001. Continuous wavelet transform and its application to resolving and quantifying the overlapped voltammetric peaks. *Anal. Chim. Acta* 450, 185–192.
- Ojha, M., Maiti, S., 2016. Sediment classification using neural networks: an example from the site-UI344A of IODP Expedition 323 in the Bering Sea. *Deep Sea Res. Part II: Top. Stud. Oceanogr.* 125, 202–213.
- Pan, S.-Y., Hsieh, B.-Z., Lu, M.-T., Lin, Z.-S., 2008. Identification of stratigraphic formation interfaces using wavelet and Fourier transforms. *Comput. Geosci.* 34, 77–92.
- Pancham, S., 1994. Evidence of the Multifractal Market Hypothesis Using Wavelet Transform (Ph.D.). Florida International University, Miami, Florida.
- Perez-Muñoz, T., Velasco-Hernandez, J., Hernandez-Martinez, E., 2013. Wavelet transform analysis for lithological characteristics identification in siliciclastic oil fields. *J. Appl. Geophys.* 98, 298–308.
- Prokoph, A., 1999. Fractal, multifractal and sliding window correlation dimension analysis of sedimentary time series. *Comput. Geosci.* 25, 1009–1021.
- Prokoph, A., Barthelms, F., 1996. Detection of nonstationarities in geological time series: wavelet transform of chaotic and cyclic sequences. *Comput. Geosci.* 22, 1097–1108.
- Prokoph, A., Veizer, J., 1999. Trends, cycles and nonstationarities in isotope signals of phanerozoic seawater. *Chem. Geol.* 161, 225–240.
- Rider, M.H., 2002. *The Geological Interpretation of Well Logs*. rider-french consulting Ltd, Sutherland, Scotland.
- Rivera Vega, N., 2004. *Reservoir Characterization Using Wavelet Transforms* (Master thesis). Texas A & M University.
- Sakurai, S., Melvin, J., 1988. Facies discrimination and permeability estimation from well logs for the Endicott field. In: *SPWLA 29th Annual Logging Symposium*, 1988. Society of Petrophysicists and Well-Log Analysts.
- Siesler, H.W., 2012. *Biomedical Imaging: Principles and Applications*. John Wiley & Sons.
- Silversides, K., Melkumyan, A., Wyman, D., Hatherly, P., 2015. Automated recognition of stratigraphic marker shales from geophysical logs in iron ore deposits. *Comput. Geosci.* 77, 118–125.
- Singh, A., Maiti, S., Tiwari, R., 2016. Modelling discontinuous well log signal to identify lithological boundaries via wavelet analysis: an example from KTB borehole data. *J. Earth Syst. Sci.* 125, 761–776.
- Singh, B.N., Tiwari, A.K., 2006. Optimal selection of wavelet basis function applied to ECG signal denoising. *Digit. Signal Process.* 16, 275–287.
- Siripitayanon, P., Chen, H.-C., Hart, B.S., 2001. A new technique for lithofacies prediction: back-propagation neural network. *ACMSE*. In: *Proceedings of the 39th Association of Computing and Machinery South Eastern Conference*. Citeseer, pp. 31–38.
- Smith, T.F., Waterman, M.S., 1980. New stratigraphic correlation techniques. *J. Geol.*, 451–457.
- Subhalak, D., Chandrasekhar, E., 2016. Reservoir characterization using multifractal detrended fluctuation analysis of geophysical well-log data. *Phys. A: Stat. Mech. Appl.* 445, 57–65.
- Tang, H., White, C., Zeng, X., Gani, M., Bhattacharya, J., 2004. Comparison of multivariate statistical algorithms for wireline log facies classification. *AAPG Annual Meeting Abstract*, p. 13.
- Weedon, G.P., 2003. Time-Series Analysis and Cyclostratigraphy: Examining Stratigraphic Records of Environmental Cycles. Cambridge University Press, Cambridge, England.
- Wong, P., Jian, F., Tuggart, I., 1995. A critical comparison of neural networks and discriminant analysis in lithofacies, porosity and permeability predictions. *J. Pet.*

- Geol. 18, 191–206.
- Yang, L., Judd, M., Bennoch, C., 2004. Denoising UHF signal for PD detection in transformers based on wavelet technique. In: Proceeding of 2004 Annual Report Conference on Electrical Insulation and Dielectric Phenomena, 2004. CEIDP'04. IEEE, pp. 166–169.
- Yuan, X., Guo, Y., Yu, J., Shen, Y., Shao, Y., 2013. Correlation and analysis of well-log sequence with Milankovitch cycles as rulers: a case study of coal-bearing strata of late Permian in western Guizhou. Int. J. Min. Sci. Technol. 23, 563–568.
- Yuca, P., Dai, D., Feng, G., 1998. Wavelet-based PCA for human face recognition. In: 1998 IEEE Southwest Symposium on Image Analysis and Interpretation, IEEE, pp. 223–228.
- Zahraa, A., Ghosh, D., 2017. Seismic Waveform Classification of Reservoir Properties Using Geological Facies Through Neural Network. ICIPEG 2016. Springer.
- Zoraster, S., Paruchuri, R., Darby, S., 2004. Curve alignment for well-to-well log correlation. In: SPE Annual Technical Conference and Exhibition. Society of Petroleum Engineers.