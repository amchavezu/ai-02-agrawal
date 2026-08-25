# Proposition 3: derivación completa de la varianza

## 0. Fuente, objeto y etiquetas

La fuente primaria es Agrawal, Gans y Goldfarb (2025), sección 4 y apéndice A.3,
en particular la condición (30), la ecuación (34) y la demostración de la Proposition 3.
Esta nota usa tres etiquetas para evitar mezclar afirmaciones:

- **[Paper]**: supuesto, fórmula o afirmación escrita en el paper.
- **[Derivación]**: consecuencia algebraica calculada aquí a partir de esos supuestos.
- **[Slip/duda]**: afirmación que no se sigue de las condiciones declaradas, o problema de
  dominio que debe quedar explícito.

El objeto exacto de Proposition 3 es la **varianza transversal entre agentes** del valor
descontado de sus oportunidades,

\[
\operatorname{Var}_i\!\left(V_i(\theta)\right).
\]

No es la varianza de \(\theta\), de la función de éxito \(p\), ni del beneficio incremental
individual \(V_i(\theta)-V_i(0)\).

## 1. Supuestos del paper y dominio interior

**[Paper]** Para Proposition 3 se especializan las funciones a

\[
p(se;\theta)=\sqrt{se+\theta},
\qquad
c(e)=e.
\]

Las oportunidades satisfacen \(\gamma(0)=\gamma_0\) y
\(\gamma(t)=\gamma\) para \(t>0\). Con \(\delta\gamma<1\), se define

\[
\Gamma=\frac{\gamma_0}{1-\delta\gamma}.
\]

El paper supone que \(\alpha,\gamma_0,\gamma,s\) son mutuamente independientes,
tienen soporte positivo y cumplen \(\mu_x>3\sigma_x\). También escribe

\[
\Delta>\frac{2}{s\sqrt{\alpha}}
\]

“so that optimal effort is positive”, y usa la condición

\[
\boxed{
\frac{\mathbb E[\Gamma^2]}{\mathbb E[\Gamma]^2}
<\mu_s\mathbb E[1/s]
}
\tag{30}
\]

para el resultado de desigualdad.

**[Derivación]** En una oportunidad, el agente resuelve

\[
\max_{e\geq 0}
M(e;\theta)=\alpha\Delta\sqrt{se+\theta}-e.
\]

Si la solución es interior,

\[
\frac{\partial M}{\partial e}
=\frac{\alpha\Delta s}{2\sqrt{se+\theta}}-1=0,
\]

de donde

\[
\sqrt{se^*+\theta}=\frac{\alpha\Delta s}{2}
\]

y

\[
e_{\mathrm{int}}^*(\theta)
=\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}.
\tag{1}
\]

Además,

\[
\frac{\partial^2M}{\partial e^2}
=-\frac{\alpha\Delta s^2}{4(se+\theta)^{3/2}}<0,
\]

por lo que la FOC determina el máximo único siempre que (1) sea positivo. Sustituyendo
la solución interior,

\[
M^*(\theta)
=\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}
\]

y, por tanto,

\[
\boxed{
V(\theta)=\Gamma\left[
\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s}
\right].
}
\tag{2}
\]

Esta es la fórmula de partida solicitada. Toda la derivación cuadrática de las secciones
2--8 supone que (1) sigue siendo interior para los agentes y valores de \(\theta\) que se
comparan. La esquina se estudia por separado en la sección 9.

## 2. Notación que reduce el álgebra

Defina

\[
k=\frac{\Delta^2}{4},
\qquad
H=k\Gamma\alpha^2s,
\qquad
Z=\frac{\Gamma}{s}.
\tag{3}
\]

Entonces (2) se convierte en

\[
\boxed{V(\theta)=H+\theta Z.}
\tag{4}
\]

Para abreviar los momentos, use

\[
\begin{aligned}
a_2&=\mathbb E[\alpha^2], & a_4&=\mathbb E[\alpha^4],\\
g_1&=\mathbb E[\Gamma], & g_2&=\mathbb E[\Gamma^2],\\
s_1&=\mathbb E[s]=\mu_s, & s_2&=\mathbb E[s^2],\\
r_1&=\mathbb E[1/s], & r_2&=\mathbb E[1/s^2].
\end{aligned}
\tag{5}
\]

La independencia mutua del paper implica que \(\Gamma\), \(\alpha\) y \(s\) son
independientes. En particular,

\[
g_1
=\mathbb E\!\left[\frac{\gamma_0}{1-\delta\gamma}\right]
=\mathbb E[\gamma_0]\,
  \mathbb E\!\left[\frac{1}{1-\delta\gamma}\right].
\]

## 3. Paso 1: \(\mathbb E[V(\theta)]\)

Partiendo de (4) y usando linealidad de la esperanza,

\[
\mathbb E[V(\theta)]
=\mathbb E[H]+\theta\mathbb E[Z].
\tag{6}
\]

Ahora calcule cada término. Por independencia,

\[
\mathbb E[H]
=k\mathbb E[\Gamma\alpha^2s]
=k\mathbb E[\Gamma]\mathbb E[\alpha^2]\mathbb E[s]
=kg_1a_2s_1,
\tag{7}
\]

y

\[
\mathbb E[Z]
=\mathbb E[\Gamma/s]
=\mathbb E[\Gamma]\mathbb E[1/s]
=g_1r_1.
\tag{8}
\]

Por tanto,

\[
\boxed{
\mathbb E[V(\theta)]
=kg_1a_2s_1+\theta g_1r_1.
}
\tag{9}
\]

Como \(\Gamma>0\) y \(s>0\), la pendiente de la media interior es

\[
\frac{d\mathbb E[V(\theta)]}{d\theta}=g_1r_1>0.
\]

## 4. Paso 2: \(\operatorname{Var}(V(\theta))\)

Primero haga la expansión sin usar independencia. De (4),

\[
V-\mathbb E[V]
=(H-\mathbb E[H])+\theta(Z-\mathbb E[Z]).
\]

Al elevar al cuadrado,

\[
\begin{aligned}
(V-\mathbb E[V])^2
={}&(H-\mathbb E[H])^2\\
&+2\theta(H-\mathbb E[H])(Z-\mathbb E[Z])\\
&+\theta^2(Z-\mathbb E[Z])^2.
\end{aligned}
\]

Tomando esperanzas,

\[
\boxed{
\operatorname{Var}(V(\theta))
=\operatorname{Var}(H)
+2\theta\operatorname{Cov}(H,Z)
+\theta^2\operatorname{Var}(Z).
}
\tag{10}
\]

Ahora calcule los tres coeficientes bajo los supuestos del paper.

### 4.1. Término constante

Como \(H^2=k^2\Gamma^2\alpha^4s^2\),

\[
\mathbb E[H^2]=k^2g_2a_4s_2.
\]

Usando (7),

\[
\boxed{
\operatorname{Var}(H)
=k^2\left[g_2a_4s_2-g_1^2a_2^2s_1^2\right].
}
\tag{11}
\]

### 4.2. Término cuadrático

Como \(Z^2=\Gamma^2/s^2\),

\[
\mathbb E[Z^2]=g_2r_2.
\]

Usando (8),

\[
\boxed{
\operatorname{Var}(Z)=g_2r_2-g_1^2r_1^2.
}
\tag{12}
\]

### 4.3. Término lineal: la cancelación clave

El producto \(HZ\) simplifica antes de tomar esperanzas:

\[
HZ
=\left(k\Gamma\alpha^2s\right)\left(\frac{\Gamma}{s}\right)
=k\Gamma^2\alpha^2.
\tag{13}
\]

El factor \(s\) se cancela exactamente. Por independencia,

\[
\mathbb E[HZ]=kg_2a_2.
\]

Además,

\[
\mathbb E[H]\mathbb E[Z]
=(kg_1a_2s_1)(g_1r_1)
=ka_2g_1^2s_1r_1.
\]

Así,

\[
\boxed{
\operatorname{Cov}(H,Z)
=ka_2\left[g_2-g_1^2s_1r_1\right].
}
\tag{14}
\]

Sustituyendo (11), (12) y (14) en (10), se obtiene la forma completamente expandida:

\[
\boxed{
\begin{aligned}
\operatorname{Var}(V(\theta))
={}&k^2\left[g_2a_4s_2-g_1^2a_2^2s_1^2\right]\\
&+2\theta ka_2\left[g_2-g_1^2s_1r_1\right]\\
&+\theta^2\left[g_2r_2-g_1^2r_1^2\right].
\end{aligned}
}
\tag{15}
\]

## 5. Paso 3: primera derivada

Derive (10) término por término. \(H\) y \(Z\) son variables aleatorias, pero no
dependen de \(\theta\) dentro de la región interior:

\[
\boxed{
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=2\operatorname{Cov}(H,Z)
+2\theta\operatorname{Var}(Z).
}
\tag{16}
\]

En momentos primitivos,

\[
\boxed{
\begin{aligned}
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
={}&2ka_2\left[g_2-g_1^2s_1r_1\right]\\
&+2\theta\left[g_2r_2-g_1^2r_1^2\right].
\end{aligned}
}
\tag{17}
\]

## 6. Paso 4: segunda derivada

Derivando una vez más,

\[
\boxed{
\frac{d^2\operatorname{Var}(V(\theta))}{d\theta^2}
=2\operatorname{Var}(Z)
=2\left[g_2r_2-g_1^2r_1^2\right]\geq0.
}
\tag{18}
\]

Por definición, una varianza nunca es negativa. La curva es estrictamente convexa si y
solo si

\[
\operatorname{Var}(\Gamma/s)>0.
\tag{19}
\]

Si \(\Gamma/s\) es constante, \(Z\) es constante, su varianza y su covarianza con
cualquier variable son cero, y \(\operatorname{Var}(V(\theta))=\operatorname{Var}(H)\)
es constante en la región interior. Por eso la “U” estricta requiere (19), no solo (30).

## 7. Paso 5: condición para una pendiente inicial negativa

Evalúe (16) en \(\theta=0\):

\[
\left.
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
\right|_{\theta=0}
=2\operatorname{Cov}(H,Z).
\tag{20}
\]

Como \(k>0\) y \(a_2>0\), (14) implica

\[
\operatorname{Cov}(H,Z)<0
\iff
g_2<g_1^2s_1r_1.
\]

Dividiendo por \(g_1^2>0\),

\[
\boxed{
\left.
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
\right|_{\theta=0}<0
\iff
\frac{\mathbb E[\Gamma^2]}{\mathbb E[\Gamma]^2}
<\mathbb E[s]\mathbb E[1/s].
}
\tag{21}
\]

Dado que \(\mathbb E[s]=\mu_s\), (21) es exactamente la condición (30). Por tanto,
**(30) sí garantiza una pendiente inicial estrictamente negativa** bajo la independencia
usada para llegar a (14).

## 8. Pasos 6 y 7: turning point y el signo en \(\theta=1\)

### 8.1. Turning point

Si (19) se cumple, iguale (16) a cero:

\[
0=2\operatorname{Cov}(H,Z)+2\theta^*\operatorname{Var}(Z).
\]

Despejando,

\[
\boxed{
\theta^*
=-\frac{\operatorname{Cov}(H,Z)}{\operatorname{Var}(Z)}.
}
\tag{22}
\]

Sustituyendo (12) y (14),

\[
\boxed{
\theta^*
=\frac{ka_2\left[g_1^2s_1r_1-g_2\right]}
{g_2r_2-g_1^2r_1^2}.
}
\tag{23}
\]

La condición (30) hace positivo el numerador. Junto con (19), implica
\(\theta^*>0\). Dentro de la fórmula interior, la pendiente puede escribirse como

\[
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
=2\operatorname{Var}(Z)(\theta-\theta^*).
\tag{24}
\]

Por tanto, la varianza cae para \(\theta<\theta^*\) y sube para
\(\theta>\theta^*\), siempre que la solución interior siga siendo válida.

### 8.2. ¿La condición (30) garantiza pendiente positiva en uno?

Evalúe (24) en \(\theta=1\):

\[
\boxed{
\left.
\frac{d\operatorname{Var}(V(\theta))}{d\theta}
\right|_{\theta=1}
=2\operatorname{Var}(Z)(1-\theta^*).
}
\tag{25}
\]

Si (19) se cumple, el lado derecho es positivo si y solo si

\[
\boxed{\theta^*<1.}
\tag{26}
\]

Equivalentemente, hace falta

\[
ka_2\left[g_2-g_1^2s_1r_1\right]
+\left[g_2r_2-g_1^2r_1^2\right]>0.
\tag{27}
\]

**[Slip]** La condición (30) solo dice que el primer corchete de (27) es negativo;
no compara su magnitud con el segundo corchete positivo. En consecuencia, (30) prueba
la pendiente negativa en cero y \(\theta^*>0\), pero **no** prueba la pendiente positiva
en uno. La afirmación de endpoint de Proposition 3 necesita la condición adicional (26).

### 8.3. Contraejemplo numérico exacto

Considere variables mutuamente independientes con

\[
\delta=\frac12,
\qquad
\gamma_0=\frac34,
\qquad
\gamma=\frac12,
\qquad
\Gamma=\frac{3/4}{1-(1/2)(1/2)}=1,
\]

\[
\alpha=\frac45,
\qquad
\Delta=4,
\qquad
s=
\begin{cases}
7/10,&\text{con probabilidad }1/2,\\
1,&\text{con probabilidad }1/2.
\end{cases}
\tag{28}
\]

Las variables constantes son independientes de las demás. Todos los soportes son
positivos. Para \(s\),

\[
\mu_s=\frac{17}{20},
\qquad
\sigma_s=\frac{3}{20},
\qquad
\mu_s>3\sigma_s
\quad\left(\frac{17}{20}>\frac9{20}\right).
\]

Las otras variables tienen desviación estándar cero, así que también cumplen
\(\mu_x>3\sigma_x\). Además, \(\delta\gamma=1/4<1\), y la restricción de interioridad
escrita por el paper se cumple incluso para \(s=7/10\):

\[
4>\frac{2}{(7/10)\sqrt{4/5}}\approx3.194.
\]

Los momentos de habilidad son

\[
\mathbb E[s]=\frac{17}{20},
\qquad
\mathbb E[1/s]=\frac{17}{14},
\qquad
\mathbb E[1/s^2]=\frac{149}{98}.
\]

Así, (30) se cumple estrictamente:

\[
\frac{\mathbb E[\Gamma^2]}{\mathbb E[\Gamma]^2}
=1
<\frac{17}{20}\frac{17}{14}
=\frac{289}{280}.
\tag{29}
\]

Como \(k=4\) y \(a_2=16/25\),

\[
\operatorname{Cov}(H,Z)
=\frac{64}{25}\left(1-\frac{289}{280}\right)
=-\frac{72}{875},
\tag{30a}
\]

y

\[
\operatorname{Var}(Z)
=\frac{149}{98}-\left(\frac{17}{14}\right)^2
=\frac{9}{196}.
\tag{31}
\]

Por tanto,

\[
\theta^*
=\frac{72/875}{9/196}
=\frac{224}{125}
=1.792>1.
\tag{32}
\]

Las pendientes son

\[
\left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_{0}
=2\left(-\frac{72}{875}\right)
=-\frac{144}{875}<0,
\]

\[
\left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_{1}
=2\left(-\frac{72}{875}+\frac9{196}\right)
=-\frac{891}{12250}<0.
\tag{33}
\]

También puede comprobarse sin fórmulas de covarianza. Los dos valores son

\[
V_{0.7}(\theta)=\frac{224}{125}+\frac{10}{7}\theta,
\qquad
V_1(\theta)=\frac{64}{25}+\theta.
\]

Con dos observaciones equiprobables, la varianza es un cuarto de la diferencia al
cuadrado:

\[
\operatorname{Var}(V(\theta))
=\frac14\left(-\frac{96}{125}+\frac37\theta\right)^2.
\tag{34}
\]

La diferencia se hace cero en \(\theta=224/125\), confirmando (32). En todo el intervalo
\([0,1]\), la varianza todavía está cayendo.

La solución es interior hasta \(\theta=1\) para ambos tipos:

\[
e^*_{s=0.7}(1)=\frac{318}{875}>0,
\qquad
e^*_{s=1}(1)=\frac{39}{25}>0.
\]

Por ello el contraejemplo no depende de aplicar la fórmula interior fuera de su dominio
en \([0,1]\).

### 8.4. Robustez: todas las habilidades con varianza positiva

Si la frase del paper “individuals vary in judgment and skill parameters” se interpreta
como una exigencia de varianza estrictamente positiva para cada parámetro, perturbe el
ejemplo anterior. Mantenga \(\delta=1/2\), \(\Delta=4\) y \(s\in\{0.7,1\}\), y tome,
de forma mutuamente independiente y con probabilidades iguales,

\[
\alpha\in\{0.79,0.81\},
\qquad
\gamma_0\in\{0.74,0.76\},
\qquad
\gamma\in\{0.49,0.51\}.
\tag{35}
\]

Las medias y desviaciones estándar son, respectivamente,

\[
(\mu_\alpha,\sigma_\alpha)=(0.8,0.01),
\quad
(\mu_{\gamma_0},\sigma_{\gamma_0})=(0.75,0.01),
\quad
(\mu_\gamma,\sigma_\gamma)=(0.5,0.01),
\]

y \((\mu_s,\sigma_s)=(0.85,0.15)\); todas satisfacen \(\mu_x>3\sigma_x\).
La variable \(\Gamma\) toma los cuatro valores

\[
\left\{\frac{148}{151},\frac{148}{149},
\frac{152}{151},\frac{152}{149}\right\}.
\]

El cálculo exacto da

\[
\frac{\mathbb E[\Gamma^2]}{\mathbb E[\Gamma]^2}
=\frac{63295313}{63281250}
\approx1.000222
<\frac{289}{280},
\]

\[
\operatorname{Cov}(H,Z)
=-\frac{362036469761}{4429293758750}
\approx-0.081737,
\qquad
\operatorname{Var}(Z)
=\frac{1147444048}{24804045049}
\approx0.046260,
\]

\[
\theta^*
=\frac{2534255288327}{1434305060000}
\approx1.766887>1,
\]

y

\[
\left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_1
=-\frac{1099950228327}{15502528155625}
\approx-0.070953<0.
\]

El menor esfuerzo en \(\theta=1\) es
\(55809/175000\approx0.31891>0\). Así, el contraejemplo sobrevive con heterogeneidad
estricta en los cuatro parámetros aleatorios y con interioridad en \([0,1]\).

## 9. Paso 8: ¿qué ocurre cuando \(e^*=0\)?

De (1), defina el umbral individual

\[
\tau(\alpha,s)=\frac{\alpha^2\Delta^2s^2}{4}.
\tag{36}
\]

La solución restringida es

\[
\boxed{
e^*(\theta)
=\max\left\{0,
\frac{\alpha^2\Delta^2s}{4}-\frac{\theta}{s}
\right\}.
}
\tag{37}
\]

Por tanto, el beneficio máximo por oportunidad es

\[
\boxed{
M^*(\theta)=
\begin{cases}
\displaystyle
\frac{\alpha^2\Delta^2s}{4}+\frac{\theta}{s},
&\theta<\tau(\alpha,s),\\[8pt]
\alpha\Delta\sqrt{\theta},
&\theta\geq\tau(\alpha,s).
\end{cases}
}
\tag{38}
\]

En el umbral, las dos ramas coinciden:

\[
\frac{\alpha^2\Delta^2s}{4}+\frac{\tau}{s}
=\frac{\alpha^2\Delta^2s}{2}
=\alpha\Delta\sqrt{\tau}.
\]

Sus primeras derivadas también coinciden:

\[
\left.\frac{dM^*}{d\theta}\right|_{\theta<\tau}
=\frac1s,
\qquad
\left.\frac{dM^*}{d\theta}\right|_{\theta>\tau}
=\frac{\alpha\Delta}{2\sqrt\theta},
\qquad
\frac{\alpha\Delta}{2\sqrt\tau}=\frac1s.
\]

Pero la segunda derivada cambia de cero a

\[
-\frac{\alpha\Delta}{4\theta^{3/2}}<0.
\]

Como \(V_i(\theta)=\Gamma_iM_i^*(\theta)\), agentes heterogéneos llegan a la esquina en
umbrales distintos. Desde el primer umbral, \(V_i(\theta)\) ya no tiene para todos los
agentes la forma común \(H_i+\theta Z_i\). Por eso (15), (18), (23) y la U cuadrática
dejan de ser una descripción global.

Fuera de puntos con masa en los umbrales, y bajo las condiciones usuales que permiten
intercambiar derivada y esperanza, la identidad general es

\[
\boxed{
\frac{d\operatorname{Var}(V)}{d\theta}
=2\operatorname{Cov}(V,V_\theta),
}
\tag{39}
\]

y

\[
\boxed{
\frac{d^2\operatorname{Var}(V)}{d\theta^2}
=2\operatorname{Var}(V_\theta)
+2\operatorname{Cov}(V,V_{\theta\theta}).
}
\tag{40}
\]

En la región mixta, el segundo término de (40) no tiene signo fijo; no puede concluirse
convexidad solo con \(\operatorname{Var}(\Gamma/s)\).

Si **todos** los agentes están en la esquina,

\[
V_i(\theta)=\Delta\sqrt\theta\,\Gamma_i\alpha_i
\]

y entonces

\[
\boxed{
\operatorname{Var}(V(\theta))
=\Delta^2\theta\operatorname{Var}(\Gamma\alpha).
}
\tag{41}
\]

Esta expresión es lineal y débilmente creciente en \(\theta\), no una cuadrática
estrictamente convexa.

## 10. Dos problemas de dominio que deben declararse

### 10.1. Condición de interioridad escrita en el paper

**[Slip/duda adicional]** De (1), la condición correcta para interioridad en
\(\theta=1\) es

\[
e_{\mathrm{int}}^*(1)>0
\iff
\boxed{\Delta>\frac{2}{\alpha s}},
\tag{42}
\]

no \(\Delta>2/(s\sqrt\alpha)\). Además, ningún \(\Delta\) finito mantiene la solución
interior para todo \(\theta\geq0\), porque (36) es finito.

### 10.2. La forma funcional de “probabilidad”

En el modelo general, \(p\) se interpreta como probabilidad. Sin embargo, en una solución
interior,

\[
p(se^*;\theta)
=\sqrt{se^*+\theta}
=\frac{\alpha\Delta s}{2}.
\]

Interioridad estricta en \(\theta=1\) requiere
\(\alpha\Delta s/2>1\), precisamente lo que hace que \(p>1\). Por tanto, la
especialización de Proposition 3 no puede simultáneamente tener \(p\in[0,1]\) e
interioridad estricta en \(\theta=1\) sin restringir o reinterpretar la forma funcional.
Este es un problema del dominio declarado por el paper; no es una condición añadida al
contraejemplo.

## 11. Distinción final: varianza del nivel frente al beneficio de adopción

En la región interior, el beneficio individual de pasar de \(0\) a \(\theta\) es

\[
B_i(\theta)=V_i(\theta)-V_i(0)
=\theta\frac{\Gamma_i}{s_i}.
\]

Por tanto,

\[
\operatorname{Var}(B_i(\theta))
=\theta^2\operatorname{Var}(\Gamma_i/s_i),
\]

que es creciente para \(\theta>0\) si el cociente es no degenerado. La U condicional de
Proposition 3 corresponde al **nivel** \(V_i(\theta)\), donde el término inicial \(H_i\)
puede covariar negativamente con la exposición marginal \(Z_i\).

## 12. Extensión opcional: correlación entre \(\Gamma\) y \(s\)

**[Derivación, no Proposition 3]** Para preservar la extensión del repositorio, relaje
únicamente \(\Gamma\perp s\) y mantenga \(\alpha\perp(\Gamma,s)\). Las identidades
(4), (10), (16), (18) y (22) no requieren independencia. Lo que cambia son los momentos:

\[
\mathbb E[V(\theta)]
=k\mathbb E[\alpha^2]\mathbb E[\Gamma s]
+\theta\mathbb E[\Gamma/s],
\]

y, usando otra vez \(HZ=k\Gamma^2\alpha^2\),

\[
\operatorname{Cov}(H,Z)
=k\mathbb E[\alpha^2]
\left(
\mathbb E[\Gamma^2]
-\mathbb E[\Gamma s]\mathbb E[\Gamma/s]
\right).
\]

La condición correcta para una caída inicial pasa a ser

\[
\boxed{
\mathbb E[\Gamma^2]
<\mathbb E[\Gamma s]\mathbb E[\Gamma/s].
}
\]

Por tanto, las distribuciones marginales de \(\Gamma\) y \(s\) no bastan cuando están
correlacionadas; hacen falta sus momentos conjuntos. Esta extensión no debe atribuirse al
enunciado de Proposition 3.

## 13. Veredicto reproducible

1. La media interior es lineal y creciente: ecuación (9).
2. La varianza interior es la cuadrática exacta (15).
3. La convexidad estricta requiere \(\operatorname{Var}(\Gamma/s)>0\).
4. La condición (30) equivale a una pendiente negativa en \(\theta=0\).
5. El turning point es (23); (30) lo hace positivo.
6. Una pendiente positiva en \(\theta=1\) requiere además \(\theta^*<1\).
7. El contraejemplo (28)--(34) satisface las condiciones algebraicas relevantes y tiene
   pendiente negativa tanto en cero como en uno.
8. Cuando algún agente llega a \(e^*=0\), debe usarse la solución por tramos (38); la
   cuadrática y su segunda derivada constante dejan de ser globalmente válidas.
