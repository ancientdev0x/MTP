

# Comparison Between Two Types of Multifractal Modeling<sup>1</sup>

Qiuming Cheng<sup>2</sup> and F. P. Agterberg<sup>3</sup>

---

*The interrelationships between two previously developed multifractal models are discussed. These are the Evertsz-Mandelbrot model developed on the basis of the multifractal spectrum  $f(\alpha)$ , and the Schertzer-Lovejoy model based on the codimension function  $C(\gamma)$  where  $\alpha$  and  $\gamma$  represent Hölder exponent and field order, respectively. It is shown how these two models are interrelated: they are identical for values of  $\gamma$  within the range  $D - \alpha(0) \leq \gamma \leq D - \alpha_{\min}$ , where  $D$  is the Euclidean dimension. For  $D - \alpha_{\max} \leq \gamma \leq D - \alpha(0)$ , however,  $f(\alpha)$  remains a continuous function of  $\alpha$  whereas  $C(\gamma)$  assumes constant value. In this respect, the fractal spectrum  $f(\alpha)$  can provide more information about the multifractal measure than the codimension function  $C(\gamma)$ . The properties of the two models are illustrated by application to the binomial multiplicative cascade model.*

---

**KEY WORDS:** multifractal measure, fractal spectrum, codimension, binomial multiplicative cascade model.

## INTRODUCTION

The concept of multifractals has been developed and applied in physics and chemistry where this approach was shown to be useful for the study of the spatial distribution of physical and chemical quantities with geometrical support (Stanley and Meakin, 1988; Feder, 1988; Schertzer and Lovejoy, 1991a, 1991b; Evertsz and Mandelbrot, 1992; Agterberg, 1994; Cowie, Sornette, and Vanneste, 1995). The multifractal model also has been used in geology for various purposes: (a) analysis of Au concentration values in bedrock samples collected from the Mitchell-Sulphurets mineral district (Agterberg, Cheng, and Wright, 1993; Cheng, 1994; Cheng, Agterberg, and Ballantyne, 1994); (b) spatial point processes for tree seedlings in Lansing Woods, Clinton, Michigan, and Au mineral occurrences in Iskut River area, northwestern British Columbia (Cheng, 1994; Cheng and Agterberg, 1995); (c) spatial distribution of fractures

<sup>1</sup>Received 29 November 1995; revised 15 April 1996.

<sup>2</sup>Department of Earth and Atmospheric Science, York University, North York, Ontario M3J 1P3, Canada; qiuming@unikaat.yorku.ca

<sup>3</sup>Geological Survey of Canada, 601 Booth Street, Ontario K1A 0E8, Canada; agterberg@gsc.emr.ca

in the Lac Du Bonnet Batholith, Manitoba (Agterberg and others, 1996); (d) spatial characteristics of Au and Au-associated faults and igneous rocks in the Mitchell-Sulphurets mineral district, northwestern British Columbia (Cheng, 1994); (e) spatial characteristics of seismic epicenters with associated geophysical anomalies and stream patterns (Cheng, Agterberg, and Bonham-Carter, 1995); and (f) multifractal modeling of geochemical speciation data in tills from the Sudbury Basin (Cheng and others, 1996a, 1996b).

Fractal geometry and some fractal models provide the simplest application of scale invariance, and are useful for characterizing fractal sets. In addition, one may be interested in the measure or field of geometrical sets. For example, in the use of the box-counting method, measures defined on the objects intersected with the boxes or cells can be taken into account in addition to the number of cells. If this measure has self-similarity or scale-invariance properties, it can be described by a multifractal model. Two different multifractal models have been developed on the basis of the fractal dimension function (Evertsz and Mandelbrot, 1992) and codimension function (Scherzer and Lovejoy, 1991a, 1991b), respectively. Both have been used in practice.

The general theory of the multifractal models is introduced briefly in this paper for comparison of the two existing models which will be referred to as the **Evertsz-Mandelbrot model** and the **Scherzer-Lovejoy model**, respectively. A binomial multiplicative cascade model will be used to illustrate the similarities and differences between the two multifractal models.

## THE MULTIFRACTAL MODEL

Suppose  $\mu(S)$  represent the measure of a set  $S$  in  $\mathbf{R}^D$ ,  $D = 1, 2, \text{ or } 3$ . The space  $\mathbf{R}^D$  can be subdivided into cells of the same linear size  $\epsilon$  (equal intervals in  $\mathbf{R}^1$ , squares of side  $\epsilon$  in  $\mathbf{R}^2$ );  $\mu_i(\epsilon)$  denotes the measure on the intersection of  $S$  with the  $i$ th cell of size  $\epsilon$ . For self-similar measure  $\mu$ , the logarithm of the measure of the cell divided by the logarithm of the size of the cell is restricted to an interval  $[\alpha_{\min}, \alpha_{\max}]$  with  $-\infty \leq \alpha_{\min} \leq \alpha_{\max} \leq \infty$ , and

$$\alpha_i = \frac{\log \mu_i(\epsilon)}{\log \epsilon} \quad (1)$$

where  $\alpha_i$  is termed the **coarse Hölder exponent** (Evertsz and Mandelbrot, 1992). For each value of  $\alpha$ ,  $N_i(\alpha)$  represents the number of cells of size  $\epsilon$  having coarse Hölder exponent  $\alpha$ . Now suppose that a cell of size  $\epsilon$  has been selected at random from among the total number of cells which is proportional to  $\epsilon^{-D}$ . The probability of drawing the value  $\alpha$  is  $Pr_i(\alpha) = CN_i(\alpha)\epsilon^D$ , where  $C$  is a constant. In the situation of a multifractal measure, this probability no longer tends to a

limit as  $\epsilon \rightarrow 0$ . Two functions will be considered:

$$f_\epsilon(\alpha) = - \frac{\log N_\epsilon(\alpha)}{\log \epsilon} \quad (2)$$

$$c_\epsilon(\alpha) = \frac{\log Pr_\epsilon(\alpha)}{\log \epsilon} \quad (3)$$

The definition of Equation (3) is as  $c_\epsilon(\alpha)$  defined by Evertsz and Mandelbrot (1992) with a negative sign. It will be shown that the definition of  $c_\epsilon(\alpha)$  in Equation (3) makes  $c_\epsilon(\alpha)$  a codimension function. As  $\epsilon \rightarrow 0$ , both  $f_\epsilon(\alpha)$  and  $c_\epsilon(\alpha)$  tend to the well-defined limits  $f(\alpha)$  and  $c(\alpha)$ . The relationship between these limits is

$$c(\alpha) = D - f(\alpha) \quad (4)$$

The definition of  $f(\alpha)$  implies that, for each  $\alpha$ , the number of cells increases for decreasing  $\epsilon$  as

$$N_\epsilon(\alpha) \propto \epsilon^{-f(\alpha)} \quad (5)$$

The exponent  $f(\alpha)$  is a continuous function of  $\alpha$ . The values of  $f(\alpha)$  could be interpreted loosely as fractal dimensions of subsets having coarse Hölder exponent  $\alpha$  in the limit  $\epsilon \rightarrow 0$  (Evertsz and Mandelbrot, 1992). Similarly, the values of the function  $c(\alpha)$  can be regarded as representing the codimensions of the subsets. The function  $c(\alpha)$  is not the same as the codimension function  $C(\gamma)$  of Schertzer and Lovejoy (1991a, 1991b) although these two functions are associated with one another as shown later. One definition of multifractals is that they are intertwined spatially fractals with a continuous spectrum of fractal dimensions (Stanley and Meakin, 1988; Evertsz and Mandelbrot, 1992; Agterberg, 1994).

## THE FRACTAL DIMENSION SPECTRUM $f(\alpha)$ AND ITS ESTIMATION

Two methods have been developed to obtain an empirical estimate of  $f(\alpha)$  for an arbitrary measure (Evertsz and Mandelbrot, 1992): the histogram method and the method of moments. In general, the second method produces better results (for examples of application, see Agterberg, 1994; Cheng, 1994). This section contains a more detailed discussion of this topic with a case study for illustration.

The method of moments is based on the partition function defined as:

$$\chi_q(\epsilon) = \sum_{i=1}^{N(\epsilon)} \mu_i^q; \quad -\infty \leq q \leq +\infty. \quad (6)$$

where  $N(\epsilon)$  is total number of cells of size  $\epsilon$  covering the set  $S$ . Taking subsets of cells with  $\alpha$  between  $\alpha$  and  $\alpha + d\alpha$ , and replacing the measure  $\mu_\epsilon(\epsilon)$  by  $\epsilon^\alpha$ , the sum in Equation (6) can be replaced by the integral

$$\chi_q(\epsilon) \propto \int_{\alpha_{\min}}^{\alpha_{\max}} N_\epsilon(\alpha) \epsilon^{\alpha q} d\alpha \quad (7)$$

Replacing  $N_\epsilon(\alpha)$  using Equation (5) gives

$$\chi_q(\epsilon) \propto \int_{\alpha_{\min}}^{\alpha_{\max}} \epsilon^{\alpha q - f(\alpha)} d\alpha \quad (8)$$

In the limit  $\epsilon \rightarrow 0$ , the dominant contribution to the integral comes from  $\alpha$ s close to the value that minimizes the exponent  $\alpha q - f(\alpha)$  (see Evertsz and Mandelbrot, 1992, p. 940). If  $f(\alpha)$  is differentiable, the necessary condition is

$$\frac{\partial}{\partial \alpha} \{ \alpha q - f(\alpha) \} = 0 \quad (9)$$

or

$$\frac{\partial f(\alpha)}{\partial \alpha} = q \quad (10)$$

Suppose that the minimum value of  $\alpha q - f(\alpha)$  for any given  $q$  is

$$\tau(q) = \alpha(q)q - f[\alpha(q)] = \min_{\alpha} [\alpha q - f(\alpha)] \quad (11)$$

Consequently,

$$\chi_q(\epsilon) \propto \epsilon^{\tau(q)} \quad (12)$$

If  $\alpha(q)$  is differentiable, from Equations (10) and (11),

$$\frac{\partial \tau(q)}{\partial q} = \alpha(q) + q\alpha' - f'(\alpha(q))\alpha'(q) = \alpha(q) \quad (13)$$

and

$$f(\alpha) = \alpha q - \tau(q) \quad (14)$$

The function  $f(\alpha)$  can be estimated by Equation (14). It can be interpreted as the negative of the Legendre transform of  $\tau(q)$ .

If the values of  $\chi_q(\epsilon)$  are plotted on log-log paper vs.  $\epsilon$ , they follow a straightline for each  $q$  with slope equal to  $\tau(q)$ . From estimated values of  $\tau(q)$ , the values of  $\alpha(q)$  can be obtained by Equation (13), and the values of  $f(\alpha)$  by

Equation (14). In order to estimate  $f(\alpha)$  it is necessary to be aware of the following properties of  $\tau(q)$ ,  $\alpha(q)$  and  $f(\alpha)$ :

(1) Symmetry or Asymmetry of  $f(\alpha)$ . Equations (2) and (5) shows that degree of symmetry of  $f(\alpha)$  depends on the distribution of the measure  $\mu$ . In the simplest situation, represented by the binomial measure created in a multiplicative cascade model (see later for more discussion), the  $f(\alpha)$  curve is symmetrical around  $f_{\max}$  and shaped similar to the mathematical symbol  $\cap$ . However, the  $f(\alpha)$  curve may be leaning to one side because of the nonbinomial nature of the frequency distribution of the measure  $\mu$  (Agterberg, Cheng, and Wright, 1993; Cheng, 1994). Left-sided multifractals were discussed by Mandelbrot and Evertsz (1991) and by Riedi and Mandelbrot (1995).

(2) The domain of  $f(\alpha)$  is bounded by:

$$\alpha_{\max} = \lim_{q \rightarrow -\infty} \sum_{i=1}^{N(\epsilon)} \frac{\mu_i^q(\epsilon)}{\sum \mu_i^q(\epsilon)} \log_{\epsilon} \mu_i(\epsilon) = N(\mu_{\min}) \log_{\epsilon} \mu_{\min} \quad (15)$$

$$\alpha_{\min} = \lim_{q \rightarrow \infty} \sum_{i=1}^{N(\epsilon)} \frac{\mu_i^q(\epsilon)}{\sum \mu_i^q(\epsilon)} \log_{\epsilon} \mu_i(\epsilon) = N(\mu_{\max}) \log_{\epsilon} \mu_{\max} \quad (16)$$

where  $N(\mu_{\min})$  and  $N(\mu_{\max})$  represent the numbers of cells having the smallest measure  $\mu_{\min}$  and the largest measure  $\mu_{\max}$ , respectively.

Therefore,

$$\frac{\alpha_{\max}}{\alpha_{\min}} = \frac{\log [\mu_{\min}^{N(\mu_{\min})}]}{\log [\mu_{\max}^{N(\mu_{\max})}]} \quad (17)$$

which is independent of cell size  $\epsilon$ . Consequently, the domain of  $\alpha$  depends on the ratio of the largest and smallest values of the measure.

(3) When  $q \gg 1$ , then  $\tau(q) = \alpha_{\min} q - f(\alpha_{\min})$ , corresponding to a straightline with slope  $\alpha_{\min}$  and intercept  $f(\alpha_{\min})$ . If this line passes through the origin,  $f(\alpha_{\min}) = 0$ ; otherwise,  $f(\alpha_{\min}) \neq 0$ . Similarly, we have  $\tau(q) = \alpha_{\max} q - f(\alpha_{\max})$  when  $q \ll 1$ .

(4) Suppose  $q \geq q_{\max}$ , and  $\tau(q) = \alpha_{\max} q - f(\alpha_{\max})$  then  $\alpha(q) = \alpha(q_{\max})$  and  $f'(\alpha(q)) = \alpha'(q)q + \alpha(q) - \tau'(q) = \alpha_{\max} - \alpha_{\max} = 0$ ; when  $q \leq -q_{\min}$ , and  $\tau(q) = \alpha_{\min} q - f(\alpha_{\min})$ , then  $\alpha(q) = \alpha(q_{\min})$  and  $f'(\alpha(q)) = \alpha(q)q + \alpha(q) - \tau'(q) = \alpha_{\min} - \alpha_{\min} = 0$ ; and when  $q_{\min} \leq q \leq q_{\max}$ , then  $f'(\alpha(q)) = q$ .

(5) If  $q = 0$ , then  $f(\alpha(0)) = -\tau(0) = -\log N(\epsilon)/\log \epsilon$ , representing the largest dimension or box-counting dimension of the support.

(6) Setting  $q = 1$  in Equation (11) and assuming that  $\sum \mu_i = \text{constant}$ , then  $\tau(1) = 0$  gives

$$\alpha(1) = f(a(1)) = \lim_{\epsilon \rightarrow 0} \frac{\sum_{i=1}^{N(\epsilon)} \mu_i \log \mu_i}{\log \epsilon} \quad (18)$$

The value  $f(\alpha(1)) = \alpha(1)$  is termed the entropy (or information) dimension of the measure. At this point the straightline  $f(\alpha) = \alpha$  is tangent to the curve of  $f(\alpha)$ .

(7) If  $\sum \mu_i$  for  $i = 1, \dots, N(\epsilon)$  is not constant, it may be that  $\tau(1) \neq 0$ . Then, a new partition function can be formed with

$$\chi_q(\epsilon) = \sum_{j=1}^{N(\epsilon)} \left| \frac{\mu_j}{\sum \mu_i} \right|^q \propto \epsilon^{\tau(q) - q\tau(1)} \quad (19)$$

New  $\tau^*(q)$  can be defined that satisfy the relations  $\tau^*(q) = \tau(q) - q\tau(1)$  with  $\tau^*(1) = 0$ . From  $\tau^*(q)$ , it can be derived that  $\alpha^* = \alpha - \tau(1)$  and  $f(\alpha^*) = \alpha^*q - \tau^*(q) = f(\alpha)$ . It shows that the multifractal spectrum  $f(\alpha)$  is the same but  $\tau(q)$  and  $\alpha(q)$  will be changed according to a linear transformation.

## THE CODIMENSION FUNCTION $C(\gamma)$ AND RELATIONSHIPS BETWEEN THE TWO MULTIFRACTAL MODELS

A multifractal model based on the codimension  $C(\gamma)$  has been developed and applied to describe multifractal fields by Schertzer and Lovejoy (1987, 1991a, 1991b, 1992) and Lavallée, Schertzer, and Lovejoy (1991). In this model the scale ratio  $\lambda$  ( $\lambda = L/\epsilon$ , where  $L$  is the largest scale which can be set to 1 without loss of generality) is used instead of  $\epsilon$  itself. The field  $\rho_\lambda$  ( $\epsilon_\lambda$  in Schertzer and Lovejoy, 1991a, 1991b) represents the field on each cell with scale ratio  $\lambda$  ( $\lambda > 1$ ). It can be a flux or density in physics and also a concentration value for a trace element in mineral exploration. This measure or field can be characterized by its probability distribution or by the corresponding law for statistical moments (Schertzer and Lovejoy, 1991a, 1991b):

$$Pr(\rho_\lambda \geq \lambda^\gamma) \propto \lambda^{-C(\gamma)} \quad (20)$$

$$\langle \rho_\lambda^\gamma \rangle \propto \lambda^{K(\gamma)} \quad (21)$$

where  $\langle \rangle$  represents mathematical expectation of the statistical moment, and  $C(\gamma)$  is termed the codimension of a subset with field order greater than  $\gamma$ . The relations between  $K(q)$ ,  $C(\gamma)$ , and  $\gamma$  were derived as (Schertzer and Lovejoy, 1991a, 1991b):

$$K(q) = \max_{\gamma} (q\gamma - C(\gamma)) \quad (22)$$

$$C(\gamma) = \max_q (q\gamma - K(q)) \quad (23)$$

The characteristics of the functions  $C(\gamma)$  and  $K(q)$  have been discussed in detail by Schertzer and Lovejoy (1991a) who also proposed a universal model for

fitting  $C(\gamma)$ . In addition, the relationships between their model and the multifractal model based on  $f(\alpha)$  were studied by Schertzer and Lovejoy (1991a).

The following new relations are derived in this paper to associate with one another the fractal dimension function  $f(\alpha)$ , the codimension function  $c(\alpha)$  defined in Equation (3), and the codimension function  $C(\gamma)$  defined by Schertzer and Lovejoy (1991a). The field  $\rho_\lambda$  can be associated with the multifractal measure  $\mu_i$  by the relation  $\rho_\lambda = \mu_i \epsilon^{-D}$ . The relations  $\rho_\lambda \propto \lambda^\gamma$  and  $\mu_i(\epsilon) \propto \epsilon^\alpha$  of Equation (1) yield  $\gamma = D - \alpha$ . From Equation (2) we obtain

$$\begin{aligned} Pr(\rho_\lambda \geq \lambda^\gamma) &= Pr(\mu_i(\epsilon) \geq \epsilon^{-\gamma+D}) = Pr(\mu_i(\epsilon) \geq \epsilon^\alpha) \\ &= \int_{\alpha_{\min}}^{\alpha} P_i(\alpha) d\alpha \propto \int_{\alpha_{\min}}^{\alpha} \epsilon^{D-f(\alpha)} d\alpha \end{aligned} \quad (24)$$

Let  $C(\gamma)$  denote the minimum value of the exponent and

$$\begin{aligned} C(\gamma) &= \min_{[\alpha_{\min}, \alpha]} [D - f(\alpha)] \\ &= D - \max_{[\alpha_{\min}, \alpha]} f(\alpha) \\ &= D - \max_{[D - \alpha_{\max}, D - \gamma]} f(D - \gamma) \end{aligned} \quad (25)$$

From Equation (3), it then follows that

$$C(\gamma) = \min_{[\alpha_{\min}, \alpha]} c(\alpha) \quad (26)$$

From Equations (21) and (12),

$$\begin{aligned} X_q(\epsilon) &\approx \epsilon^{-D} \langle \mu^q(\epsilon) \rangle \\ &= \epsilon^{-D} \epsilon^{qD} \langle \rho_\lambda^q \rangle \\ &= \epsilon^{-D + qD - K(q)} \end{aligned} \quad (27)$$

Therefore,

$$\tau(q) = (q - 1)D - K(q); \quad K(q) = (q - 1)D - \tau(q) \quad (28)$$

Combining Equations (25) and (28) gives, for  $D - \alpha(0) \leq \gamma \leq D - \alpha_{\min}$ ,

$$C(\gamma) = D - f(a) = D - \alpha q + \tau(q) = \gamma q - K(q) \quad (29)$$

If  $\gamma \leq D - \alpha(0)$ ,  $C(\gamma) = \text{constant}$ . This is identical to Equation (23) only for values of  $\gamma$  with  $D - \alpha(0) \leq \gamma \leq D - \alpha_{\min}$ . It shows that relations (25), (28), and (29) are similar to the relations derived by Schertzer and Lovejoy (1991a) but only for a subset of  $\gamma$ . These properties and others to be discussed next are

useful when the multifractal model is applied. For instance, in order to use Schertzer and Lovejoy's (1991a) "universal function" for fitting  $C(\gamma)$ , one must restrict  $\gamma$  to the range  $[D - \alpha(0), D - \alpha_{\min}]$ .

The relationships (25), (28), and (29) and additional properties of the functions  $C(\gamma)$  and  $K(q)$  can be described as follows (also see Figs. 1 and 2):

(1)  $C_{\min}(\gamma_{\min}) = D - f_{\max}(\alpha(0))$ , corresponding to the codimension of the support because  $f_{\max}$  is the box-counting dimension of the support.  $C_{\max}(\gamma_{\max}) = D - f(\alpha_{\min})$ , corresponding to the codimension of subsets with the smallest coarse Hölder exponent  $\alpha_{\min}$  which is associated with the largest values of  $\mu$ . If  $f_{\max}(\alpha(0)) = D$ , as in the binomial multiplicative cascade model, then  $C_{\min} = 0$ , but in most situations  $f_{\max}(\alpha(0)) < D$  and  $C_{\min} > 0$ . If  $f(\alpha_{\min}(+\infty)) = 0$ , then  $C_{\max}(\gamma_{\max}) = D$  which is the box-counting dimension of the support and

![Figure 1 consists of two plots, A and B. Plot A shows the relationship between f(α) (dotted line), c(α) (solid line), and C(γ) (solid line) versus α. The x-axis ranges from 0 to 4, and the y-axis ranges from 0.0 to 2.5. The curve f(α) is a dotted line that starts at (0,0), peaks at approximately (2.2, 1.8), and then decreases. The curve c(α) is a solid line that starts at (0,0), decreases to a minimum at approximately (2.2, 0.2), and then increases. The curve C(γ) is a solid line that starts at (0,0) and increases monotonically. Plot B shows the relationship between C(γ) (solid line) versus γ. The x-axis ranges from -2 to 2, and the y-axis ranges from 0.0 to 2.5. The curve C(γ) is a solid line that is constant at approximately 0.2 for γ < 0 and then increases sharply for γ > 0.](7ff005f9556dc6518981bb92091d36ab_img.jpg)

Figure 1 consists of two plots, A and B. Plot A shows the relationship between f(α) (dotted line), c(α) (solid line), and C(γ) (solid line) versus α. The x-axis ranges from 0 to 4, and the y-axis ranges from 0.0 to 2.5. The curve f(α) is a dotted line that starts at (0,0), peaks at approximately (2.2, 1.8), and then decreases. The curve c(α) is a solid line that starts at (0,0), decreases to a minimum at approximately (2.2, 0.2), and then increases. The curve C(γ) is a solid line that starts at (0,0) and increases monotonically. Plot B shows the relationship between C(γ) (solid line) versus γ. The x-axis ranges from -2 to 2, and the y-axis ranges from 0.0 to 2.5. The curve C(γ) is a solid line that is constant at approximately 0.2 for γ < 0 and then increases sharply for γ > 0.

**Figure 1.** Relationships between  $f(\alpha)$ ,  $c(\alpha)$ , and  $C(\gamma)$ . A.  $f(\alpha)$ -curve (dotted line) and  $c(\alpha)$ -curve (solid line). Values of  $c(\alpha)$  were computed using Equation (4); B.  $C(\gamma)$ -curve is represented by solid line. Values of  $C(\gamma)$  were computed using Equation (26).

![Figure 2: Characteristics of functions tau(q) and K(q). Plot A shows tau(q) vs q with a solid curve and several straight lines. Plot B shows K(q) vs q with a V-shaped curve.](91be14371a97fb5ce9eeb29ae18d07c3_img.jpg)

Figure 2 consists of two plots, A and B. Plot A shows the function  $\tau(q)$  on the y-axis (ranging from -24 to 24) against  $q$  on the x-axis (ranging from -14 to 18). A solid curve represents  $\tau(q)$ , which is concave down and passes through the origin. A solid straight line represents  $\tau = (q-1)D$ , which is a straight line with a positive slope intersecting the horizontal axis at  $q=1$ . Two dotted lines represent  $\tau = \alpha_{\max}q - f(\alpha_{\max})$  and  $\tau = \alpha_{\min}q - f(\alpha_{\min})$ , both with positive slopes. Plot B shows the function  $K(q)$  on the y-axis (ranging from 0 to 5.5) against  $q$  on the x-axis (ranging from -14 to 18). The curve is V-shaped, symmetric about the y-axis, with a minimum at  $q=0$  and  $K(0) \approx 0.5$ .

Figure 2: Characteristics of functions tau(q) and K(q). Plot A shows tau(q) vs q with a solid curve and several straight lines. Plot B shows K(q) vs q with a V-shaped curve.

**Figure 2.** Characteristics of functions  $\tau(q)$  and  $K(q)$ . A.  $\tau(q)$ -curve is represented by solid curved line; solid straightline is for  $\tau = (q-1)D$  intersecting horizontal axis at  $q = 1$ . Dotted lines represent  $\tau = \alpha_{\max}q - f(\alpha_{\max})$  and  $\tau = \alpha_{\min}q - f(\alpha_{\min})$ , respectively; B.  $K(q)$ -curve.

if  $f(\alpha_{\min}(+\infty)) < 0$ , corresponding to negative dimension (Mandelbrot and Evertsz, 1991), then  $C_{\max}(\gamma_{\max}) > D$ . Examples of these situations are given in Schertzer and Lovejoy (1991a, 1992).

(2) If  $f(\alpha)$  is differentiable, then  $C'(\gamma) \geq 0$ . From Equation (25), if  $D - \alpha_{\max} \leq \gamma \leq D - \alpha(0)$ , then  $C(\gamma) = D - f_{\max}(\alpha(0))$  which is constant and, therefore,  $C'(\gamma) = 0$ . If  $D - \alpha(0) \leq \gamma \leq D - \alpha_{\min}$ , then  $C(\gamma) = D - f(D - \gamma)$  and  $C'(\gamma) = f'(D - \gamma) = f'(\alpha) = q > 0$  (note that  $a_{\min} \leq a \leq a(0)$ ). Thus, the function  $C(\gamma)$  is a continuous nondecreasing function and  $C'(\gamma)$  is a continuous nonnegative function.

(3)  $C(\gamma)$  is tangent with the straightline  $C = \gamma$  at  $\gamma = D - \alpha(1)$ , because  $C(D - \alpha(1)) = D - f(\alpha(1)) = D - \alpha(1)$  and  $C'(D - \alpha(1)) = f'(\alpha(1)) = 1$ .

(4)  $\gamma_{\min} = D - \alpha_{\max}$  and  $\gamma_{\max} = D - \alpha_{\min}$ . If  $\alpha_{\min} \leq D < \alpha_{\max}$ , which

is usual although not required, then  $\gamma_{\min} < 0$  and  $\gamma_{\max} > 0$ . Therefore,  $\gamma$  can have negative value.

(5) Because  $K(q) = (q - 1)D - \tau(q)$ ,  $K'(q) = D - \alpha(q) = \gamma(q)$  which is an increasing function; at  $\alpha(q_D) = D$ ,  $K'(q_D) = 0$ ; if  $q > q_D$ ,  $K'(q) > 0$  and if  $q < q_D$ , then  $K'(q) < 0$ , implying that for  $q < q_D$ ,  $K(q)$  is a decreasing function; and for  $q > q_D$ ,  $K(q)$  is an increasing function with  $K(q_D)$  as its minimum value. The slopes along the curve correspond to the values of  $\gamma(q)$ .

(6) For the fractal model ( $\beta$ -model),  $\tau(q)$  is a straightline with slope  $\alpha$  ( $\alpha_{\min} = \alpha_{\max} = \alpha$ ), and the curve  $f(\alpha)$  reduces to a single spike. In this example,  $K(q)$  is a straightline with  $K(q) = (D - \alpha)q - D_\beta$ . The slope of this line is  $D - \alpha$  and its intercept is  $D_\beta$ , where  $D_\beta$  is the dimension of the so-called  $\beta$ -model. Further,  $\gamma_{\min} = \gamma_{\max} = D - \alpha$ , and the curve  $C(\gamma)$  reduces to a single spike.

In conclusion, the Evertsz-Mandelbrot and Schertzer-Lovejoy models are related closely to one another although they are based on the different concepts of fractal dimension  $f(\alpha)$  and codimension  $C(\gamma)$ , respectively. A detailed comparison has shown that the fractal dimension spectrum  $f(\alpha)$  and the codimension function  $c(\alpha)$  are identical and characterize not only the larger values of the measure (or field) but also the smaller values of the measure. Although the codimension function  $C(\gamma)$  is associated with  $f(\alpha)$  and  $c(\alpha)$  according to Equations (25) and (26), information derived from  $C(\gamma)$  is valid only for  $D - \alpha(0) \leq \gamma$ . This is because  $C(\gamma)$  is the codimension of subsets with fields of order greater than  $\gamma$  (or subsets with coarse Hölder exponents less than  $\alpha$ , since  $\gamma = D - \alpha$ ). In this respect,  $f(\alpha)$  has a wider range of application than  $C(\gamma)$ . These differences and similarities will be illustrated in the next section where the binomial multiplicative cascade model is developed in two different ways using the two multifractal models.

## BINOMIAL CASCADE MODELING IMPLEMENTED USING BOTH MODELS

In order to compare the two multifractal models with one another, the binomial multiplicative cascade model in  $\mathbf{R}^1$  can be used. The concept of deterministic and random multiplicative models was discussed by De Wijs (1951), Meneveau and Sreenivasan (1987), Agterberg (1994), and Cheng and Agterberg (1996). A stochastic version of the binomial model is as follows (Meneveau and Sreenivasan, 1987; Agterberg, 1994). At the first stage ( $k = 1$ ) in a process consisting of  $k$  stages, the interval  $(0, 1]$  with measure  $\xi$  is subdivided into two equal intervals, (a)  $(0, 1/2]$  with measure  $1/2(1 + B)\xi$ , and (b)  $(1/2, 1]$  with  $1/2(1 - B)\xi$ , where  $B$  is a random variable with  $\Pr(B = d) = \Pr(B = -d) = 1/2(d > 0)$ . At stage 2, these two intervals are halved again with new measures for the halves defined in the same way as at stage 1. The process is repeated at stages  $k = 3, 4, \dots$ . At stage  $k$  the  $i$ th subinterval with value measure  $\mu_i(\epsilon)$  has

size  $\epsilon = 1/2^k$ , and  $E\{\mu_\epsilon(\epsilon)\} = \xi$ . The frequency distribution of  $\mu_\epsilon(\epsilon)$  is logbinomial, tending to become lognormal in the center as  $\epsilon \rightarrow 0$  and, depending on the direction of ordering, Pareto in both tails. Figure 3A to 3D illustrate the preceding model with  $d = 0.4$ , after  $k = 4, 5, 6, 7$  stages of cutting.

Because  $\lambda_k = \epsilon_k^{-1} = 2^k$ , a log-log plot of  $\Pr(\rho_\lambda > \lambda^\gamma)$  vs.  $\lambda$  was constructed for Figure 4A by Equation (20). Seven different scales ( $\lambda_k$ ;  $k = 4, \dots, 10$ ) were used. According to Equation (20), the slopes of the lines in this plot are equal to  $C(\gamma)$ . Figure 4B shows the estimates of  $C(\gamma)$ . A parabolic function was fitted to these values within the range  $\gamma \in (0, 0.5)$  by ordinary regression. It can be seen that the minimum value of this curve is close to 0 and the maximum value less than 1.

A log-log plot of partition function vs. block size ( $\epsilon$ ) was constructed for Figure 5A by Equations (6) and (12). Eight different block sizes ( $\epsilon_k$ ;  $k = 3, \dots, 10$ ) were used. According to Equation (12), the slopes of the lines in this plot are equal to  $\tau(q)$ . Figure 5B shows the estimated values of  $\tau(q)$ . Values of

![Figure 3: Four histograms (A, B, C, D) showing the frequency distribution of block measures after k stages of cutting. The x-axis represents block size (epsilon) from 0 to 1, and the y-axis represents frequency. Panel A (k=4) has a y-axis from 0.00 to 0.25. Panel B (k=5) has a y-axis from 0.00 to 0.25. Panel C (k=6) has a y-axis from 0.00 to 0.125. Panel D (k=7) has a y-axis from 0.000 to 0.125. All plots show a distribution that is highly skewed towards smaller block sizes, with a peak near 0 and a long tail towards 1.](eb903413d070b64f45cd763804ba443f_img.jpg)

Figure 3: Four histograms (A, B, C, D) showing the frequency distribution of block measures after k stages of cutting. The x-axis represents block size (epsilon) from 0 to 1, and the y-axis represents frequency. Panel A (k=4) has a y-axis from 0.00 to 0.25. Panel B (k=5) has a y-axis from 0.00 to 0.25. Panel C (k=6) has a y-axis from 0.00 to 0.125. Panel D (k=7) has a y-axis from 0.000 to 0.125. All plots show a distribution that is highly skewed towards smaller block sizes, with a peak near 0 and a long tail towards 1.

**Figure 3.** Binomial multiplicative model after  $k$  stages ( $k = 4, 5, 6, 7$ ) of cutting blocks into halves. At each cut, amount of measure in block is divided into two parts with 70% going to one half and 30% into other. This ratio (7/3) is kept constant but block with greater measure is selected at random. A  $k = 4$ ; B,  $k = 5$ ; C,  $k = 6$ ; and D,  $k = 7$ .

![Figure 4: Results obtained using multifractal model based on codimension C(γ). Plot A shows Log Pr(ρ_λ > λ') vs. Log λ for various γ values. Plot B shows C(γ) vs. γ.](f176174c2978785e86a8352bd45e322e_img.jpg)

Figure 4 consists of two plots, A and B. Plot A is a log-log plot showing the relationship between  $\text{Log Pr}(\rho_\lambda > \lambda')$  on the y-axis (ranging from -3 to 0.5) and  $\text{Log } \lambda$  on the x-axis (ranging from 1.4 to 3.4). Several straight lines are plotted, each corresponding to a different value of  $\gamma$ : 0.04, 0.08, 0.16, 0.24, 0.40, 0.56, and 0.68. The lines have negative slopes that increase with  $\gamma$ . Plot B shows the estimated values of  $C(\gamma)$  on the y-axis (ranging from 0 to 1) versus  $\gamma$  on the x-axis (ranging from -0.1 to 0.9). The data points are represented by open circles, and a solid parabolic curve is fitted to them, showing an increasing trend.

Figure 4: Results obtained using multifractal model based on codimension C(γ). Plot A shows Log Pr(ρ\_λ > λ') vs. Log λ for various γ values. Plot B shows C(γ) vs. γ.

**Figure 4.** Results obtained using multifractal model based on codimension  $C(\gamma)$ . A, log-log plot representing relationships of  $\text{Pr}(\rho_\lambda > \lambda')$  vs.  $\lambda$ . According to Equation (20), slopes of lines in this figure should be equal to values of  $C(\gamma)$ . B, estimated values of  $C(\gamma)$ . Solid line was fitted by ordinary regression using parabolic function for values of  $-0.09 \leq \gamma \leq 0.49$ .

$\alpha(q)$  (see Fig. 5C) were estimated by applying the central difference technique to successive sets of three values of  $\tau(q)$ . The multifractal spectrum  $f(\alpha)$  (Fig. 5D) was derived from the values shown in Figure 5B and 5C by means of Equation (14).

It has been shown that for the binomial multiplicative cascade model with  $d = 0.4$ ,  $\alpha_{\min} = -\log_2(1 + B)/2 = 0.51$  and  $\alpha_{\max} = -\log_2(1 - B)/2 = 1.74$  (cf. Agterberg, 1994). Therefore, the domain of  $\gamma$  should be  $-0.74 = D - \alpha_{\max} \leq \gamma \leq D - \alpha_{\min} = 0.49$ . It can be seen from Figure 5C that  $\alpha(0) = 1.09$  and according to Equation (25), for  $-0.74 < \gamma < D - \alpha(0) = -0.09$ ,  $C(\gamma)$  is constant and for  $-0.09 \leq \gamma \leq 0.49$ ,  $C(\gamma) = f(D - \gamma)$  represented by triangles in Figure 5D. This shows that for  $\gamma$  close to  $D - \alpha(0)$  or  $\alpha$  close to  $\alpha(0)$ , the results obtained by the two models are similar. For  $\alpha > \alpha(0)$  or  $\gamma$

![Figure 5: Results obtained by multifractal model based on fractal dimension spectrum f(alpha). Panel A: Log-log plot of Log chi_q(epsilon) vs Log epsilon showing multiple straight lines. Panel B: Plot of tau(q) vs q showing a linear relationship. Panel C: Plot of alpha(q) vs q showing a step-like transition. Panel D: Plot of f(alpha) vs alpha showing a symmetric bell-shaped curve.](b05a8a3551db31147979064952179990_img.jpg)

Figure 5: Results obtained by multifractal model based on fractal dimension spectrum f(alpha). Panel A: Log-log plot of Log chi\_q(epsilon) vs Log epsilon showing multiple straight lines. Panel B: Plot of tau(q) vs q showing a linear relationship. Panel C: Plot of alpha(q) vs q showing a step-like transition. Panel D: Plot of f(alpha) vs alpha showing a symmetric bell-shaped curve.

**Figure 5.** Results obtained by multifractal model based on fractal dimension spectrum  $f(\alpha)$ . A, Log-log plot for relationship between  $\chi_q(\epsilon)$  and  $\epsilon$ ; straightlines obtained by method of least squares; B, Estimated values of  $\tau(q)$  including slopes of straightlines in A; C, Singularity  $\alpha$  estimated from B by central difference method; D, multifractal spectrum  $f(\alpha)$  represented by small circles with results based on codimension ( $D - C(\gamma)$ ) represented by triangles. Smallest size is  $\epsilon = 1/2^{10}$ ; logarithmic scales have base 10.

$< D - \alpha(0)$ , however,  $C(\gamma)$  is a constant but  $f(\alpha)$  is a symmetrical curve for this example. Generally, therefore,  $f(\alpha)$  provides more information than  $C(\gamma)$ , especially if  $f(\alpha)$  is an asymmetrical curve.

## CONCLUSION

The newly derived relations between  $f(\alpha)$ ,  $c(\alpha)$ , and  $C(\gamma)$  of Equations (25) and (26) show that the two previously derived multifractal models (Evertsz-Mandelbrot model and Schertzer-Lovejoy model) are interrelated and identical only for values of  $\gamma$  within  $D - \alpha(0) \leq \gamma \leq D - \alpha_{\min}$ . On the other hand, for  $\gamma \leq D - \alpha(0)$ ,  $C(\gamma)$  is constant, whereas  $f(\alpha)$  is a continuous function. In

this respect, the fractal spectrum  $f(\alpha)$  provides more information about the multifractal measure than the codimension function  $C(\gamma)$ . These properties were illustrated further by using the binomial multiplicative model. The properties of  $f(\alpha)$  and  $C(\gamma)$  discussed in this paper also are useful during implementation of the two models for practical applications.

## REFERENCES

- Agterberg, F. P., 1994, Fractals, multifractals, and change of support, in Dimitrakopoulos, R., ed., *Geostatistics for the next century*; Kluwer Acad. Publ., Dordrecht, The Netherlands, p. 223-234.
- Agterberg, F. P., Cheng, Q., and Wright, D. F., 1993, Fractal modelling of mineral deposits, in Elbrond, J., and Tang, X., eds., *Application of computers and operations research in the mineral industry*; Proc. 24th APCOM Symposium (Montreal): Canadian Inst. Mining, Metallurgy and Petroleum Eng., v. 1, p. 43-53.
- Agterberg, F. P., Cheng, Q., Brown, A., and Good, D., 1996, Multifractal modelling of fractures in Lac Du Bonnet Batholith, Manitoba: *Computers & Geosciences*, v. 22, no. 5, p. 497-507.
- Cheng, Q., 1994, *Multifractal modelling and spatial analysis with GIS: gold potential estimation in the Mitchell-Sulphurets area, northwestern British Columbia*, unpubl. doctoral dissertation, Univ. Ottawa, 268 p.
- Cheng, Q., and Agterberg, F. P., 1995, Multifractal modeling and spatial point processes: *Math. Geology*, v. 27, no. 7, p. 831-845.
- Cheng, Q., and Agterberg, F. P., 1996, Multifractal modeling and spatial statistics: *Math. Geology*, v. 27, no. 1, p. 1-16.
- Cheng, Q., Agterberg, F. P., and Ballantyne, S. B., 1994, The separation of geochemical anomalies from background by fractal methods: *Jour. Geochem. Explor.*, v. 51, no. 2, p. 109-130.
- Cheng, Q., Agterberg, F. P., and Bonham-Carter, G. F., 1995, GIS treatment of multifractality of spatial objects: Proc. Geomatics'95 (Ottawa, Ontario, Canada), on CD Rom available from Surveys and Mapping Branch, NRCan, 615 Booth Street, Ottawa, Canada.
- Cheng, Q., Bonham-Carter, G. F., Bajc, A., and Hall, G. E. M., 1996a, Spatial analysis of partial leach data in till from the Sudbury Basin: *Jour. Explor. Geochem.*, in press.
- Cheng, Q., Bonham-Carter, G. F., Bajc, A., and Hall, G. E. M., 1996b, Multifractal analysis of geochemical speciation data: submitted to *Jour. Explor. Geochem.*
- Cowie, P. A., Sornette, D., and Vanneste, C., 1995, Multifractal scaling properties of a growing fruit population: *Geoph. Jour. Intern.*, v. 22, no. 3, p. 457-468.
- De Wijs, H. J., 1951, Statistics of ore distribution: *Geologie en Mijnbouw*, v. 13, no. 8, p. 365-375.
- Evertsz, C. J. G., and Mandelbrot, B. B., 1992, Multifractal measures, Appendix B, in Peitgen, H.-O., Jürgens, H., and Saupe, D., eds., *Chaos and fractals*; Springer Verlag, New York, p. 922-953.
- Feder, J., 1988, *Fractals*; Plenum Press, New York, 283 p.
- Lavallée, D., Schertzer, D., and Lovejoy, S., 1991, On the determination of the codimension function, in Schertzer, D., and Lovejoy, S., eds., *Non-linear variability in geophysics*; Kluwer Acad. Publ., Dordrecht, The Netherlands, p. 99-109.
- Mandelbrot, B. B., and Evertsz, C. J. G., 1991, Exactly self-similar left-sided multifractals, Chapter 10, in Bunde, A., and Havlin, S., eds., *Fractals and disordered systems*; Springer Verlag, Heidelberg, p. 323-344.
- Meneveau, C., and Sreenivasan, K. R., 1987, Simple multifractal cascade model for fully developed turbulence: *Phys. Review Letters* v. 59, no. 13, p. 1424-1427.

- Riedi, R. H., and Mandelbrot, B. B., 1995, Multifractal formalism for infinite multinomial measures: *Advances in Applied Math.*, v. 16, no. 1, p. 132-150.
- Schertzer, D., and Lovejoy, S., 1987, Physically based rain and cloud modeling by anisotropic, multiplicative turbulent cascades: *Jour. Geophys. Res.*, v. 92, no. D8, p. 9693-9714.
- Schertzer, D., and Lovejoy, S., eds, 1991a, Non-linear variability in geophysics: Kluwer Acad. Publ., Dordrecht, The Netherlands, 318 p.
- Schertzer, D., and Lovejoy, S., 1991b, Nonlinear geodynamical variability: multiple singularities, universality and observations, *in* Schertzer, D., and Lovejoy, S., eds., Nonlinear variability in geophysics: Kluwer Acad. Publ., Dordrecht, The Netherlands, p. 41-82.
- Schertzer, D., and Lovejoy, S., 1992, Hard and soft multifractal processes: *Physica A*, v. 185, p. 187-194.
- Stanley, H., and Meakin, P., 1988, Multifractal phenomena in physics and chemistry: *Nature*, v. 335, no. 6189, p. 405-409.