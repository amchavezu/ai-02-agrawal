# Guía para reproducir la derivación a mano

Esta guía organiza el cálculo, pero **no sustituye una foto real de tu propio trabajo**.
No se ha creado ni se debe fabricar una imagen manuscrita. Antes de fotografiar tus hojas,
repite cada igualdad y marca cualquier paso que todavía no puedas explicar.

## Símbolos que debes escribir primero

En la parte superior de la primera hoja escribe

\[
k=\frac{\Delta^2}{4},
\qquad
H=k\Gamma\alpha^2s,
\qquad
Z=\frac{\Gamma}{s},
\qquad
V(\theta)=H+\theta Z.
\]

Debajo, registra los momentos:

\[
\begin{array}{lll}
a_2=E[\alpha^2], & a_4=E[\alpha^4],\\
g_1=E[\Gamma], & g_2=E[\Gamma^2],\\
s_1=E[s], & s_2=E[s^2],\\
r_1=E[1/s], & r_2=E[1/s^2].
\end{array}
\]

Escribe también: “\(\Gamma,\alpha,s\) independientes; solución interior por ahora”.

## Hoja 1: esperanza y expansión de la varianza

### A. Esperanza

1. Empieza con

   \[
   E[V]=E[H]+\theta E[Z].
   \]

2. Usa independencia:

   \[
   E[H]=kE[\Gamma]E[\alpha^2]E[s]=kg_1a_2s_1,
   \]

   \[
   E[Z]=E[\Gamma]E[1/s]=g_1r_1.
   \]

3. Encierra el resultado:

   \[
   \boxed{E[V]=kg_1a_2s_1+\theta g_1r_1}.
   \]

### B. Identidad de varianza

1. Centra la variable:

   \[
   V-E[V]=(H-E[H])+\theta(Z-E[Z]).
   \]

2. Eleva al cuadrado. No saltes el término cruzado:

   \[
   (V-E[V])^2=(H-EH)^2
   +2\theta(H-EH)(Z-EZ)
   +\theta^2(Z-EZ)^2.
   \]

3. Toma esperanzas:

   \[
   \boxed{
   \operatorname{Var}(V)
   =\operatorname{Var}(H)
   +2\theta\operatorname{Cov}(H,Z)
   +\theta^2\operatorname{Var}(Z)}.
   \]

## Hoja 2: calcula los tres coeficientes

### A. \(\operatorname{Var}(H)\)

Escribe, en líneas separadas,

\[
H^2=k^2\Gamma^2\alpha^4s^2,
\]

\[
E[H^2]=k^2g_2a_4s_2,
\]

\[
\boxed{
\operatorname{Var}(H)
=k^2(g_2a_4s_2-g_1^2a_2^2s_1^2)}.
\]

### B. \(\operatorname{Var}(Z)\)

\[
Z^2=\frac{\Gamma^2}{s^2},
\qquad
E[Z^2]=g_2r_2,
\]

\[
\boxed{
\operatorname{Var}(Z)=g_2r_2-g_1^2r_1^2}.
\]

### C. \(\operatorname{Cov}(H,Z)\)

Este es el paso que no debes omitir:

\[
HZ=(k\Gamma\alpha^2s)(\Gamma/s)
=k\Gamma^2\alpha^2.
\]

Se canceló \(s\). Luego,

\[
E[HZ]=kg_2a_2,
\]

\[
E[H]E[Z]=ka_2g_1^2s_1r_1,
\]

\[
\boxed{
\operatorname{Cov}(H,Z)
=ka_2(g_2-g_1^2s_1r_1)}.
\]

Finalmente, sustituye los tres cuadros en la identidad de la Hoja 1.

## Hoja 3: derivadas, condición (30) y turning point

1. Deriva la cuadrática:

   \[
   \boxed{
   \frac{d\operatorname{Var}(V)}{d\theta}
   =2\operatorname{Cov}(H,Z)
   +2\theta\operatorname{Var}(Z)}.
   \]

2. Deriva de nuevo:

   \[
   \boxed{
   \frac{d^2\operatorname{Var}(V)}{d\theta^2}
   =2\operatorname{Var}(Z)\geq0}.
   \]

3. Evalúa en cero:

   \[
   \left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_0
   =2ka_2(g_2-g_1^2s_1r_1).
   \]

4. Como \(2ka_2>0\), la pendiente es negativa si y solo si

   \[
   \frac{g_2}{g_1^2}<s_1r_1
   =\mu_sE[1/s].
   \]

   Escribe al lado: “esta es la condición (30)”.

5. Iguala la primera derivada a cero:

   \[
   \boxed{
   \theta^*
   =-\frac{\operatorname{Cov}(H,Z)}{\operatorname{Var}(Z)}
   =\frac{ka_2(g_1^2s_1r_1-g_2)}
   {g_2r_2-g_1^2r_1^2}}.
   \]

6. Reescribe la pendiente:

   \[
   \frac{d\operatorname{Var}(V)}{d\theta}
   =2\operatorname{Var}(Z)(\theta-\theta^*).
   \]

7. Evalúa en uno:

   \[
   \left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_1
   =2\operatorname{Var}(Z)(1-\theta^*).
   \]

8. Encierra la conclusión lógica:

   \[
   \boxed{
   \text{pendiente en }1>0
   \iff\theta^*<1
   }
   \quad\text{si }\operatorname{Var}(Z)>0.
   \]

   Escribe: “(30) da \(\theta^*>0\), pero no da \(\theta^*<1\)”.

## Hoja 4: contraejemplo con fracciones exactas

Usa

\[
\delta=\frac12,
\quad\gamma_0=\frac34,
\quad\gamma=\frac12,
\quad\Gamma=1,
\quad\alpha=\frac45,
\quad\Delta=4,
\]

y \(s=7/10\) o \(s=1\), cada uno con probabilidad \(1/2\).

### A. Comprueba las condiciones

\[
E[s]=\frac{17}{20},
\qquad
\sigma_s=\frac3{20},
\qquad
\frac{17}{20}>3\frac3{20}.
\]

\[
E[1/s]=\frac12\left(\frac{10}{7}+1\right)=\frac{17}{14}.
\]

Entonces

\[
1<\frac{17}{20}\frac{17}{14}=\frac{289}{280},
\]

de modo que (30) se cumple.

### B. Calcula covarianza, varianza y giro

\[
k=4,
\qquad
a_2=\frac{16}{25},
\qquad
ka_2=\frac{64}{25}.
\]

\[
\operatorname{Cov}(H,Z)
=\frac{64}{25}\left(1-\frac{289}{280}\right)
=-\frac{72}{875}.
\]

\[
E[1/s^2]
=\frac12\left(\frac{100}{49}+1\right)
=\frac{149}{98}.
\]

\[
\operatorname{Var}(Z)
=\frac{149}{98}-\left(\frac{17}{14}\right)^2
=\frac9{196}.
\]

\[
\theta^*
=\frac{72/875}{9/196}
=\frac{224}{125}
=1.792.
\]

### C. Comprueba el signo en uno

\[
\left.\frac{d\operatorname{Var}(V)}{d\theta}\right|_1
=2\left(-\frac{72}{875}+\frac9{196}\right)
=-\frac{891}{12250}<0.
\]

Conclusión escrita en palabras: “La condición (30) se cumple, pero la varianza sigue
cayendo en \(\theta=1\); por tanto, la afirmación de endpoint necesita
\(\theta^*<1\)”.

## Hoja 5: esquina de esfuerzo

1. Parte de la solución interior:

   \[
   e_{\mathrm{int}}^*
   =\frac{\alpha^2\Delta^2s}{4}-\frac\theta s.
   \]

2. Impón \(e\geq0\):

   \[
   \boxed{
   e^*=\max\left\{0,
   \frac{\alpha^2\Delta^2s}{4}-\frac\theta s
   \right\}}.
   \]

3. Define el umbral:

   \[
   \tau=\frac{\alpha^2\Delta^2s^2}{4}.
   \]

4. Sustituye cada solución en el objetivo:

   \[
   \boxed{
   M^*(\theta)=
   \begin{cases}
   \alpha^2\Delta^2s/4+\theta/s,&\theta<\tau,\\
   \alpha\Delta\sqrt\theta,&\theta\geq\tau.
   \end{cases}}
   \]

5. Verifica continuidad en \(\tau\): ambas ramas valen
   \(\alpha^2\Delta^2s/2\).

6. Verifica que las primeras derivadas también coinciden:

   \[
   \frac1s
   =\frac{\alpha\Delta}{2\sqrt\tau}.
   \]

7. Escribe la consecuencia: después de que algunos agentes llegan a la esquina,
   \(V_i\) ya no es \(H_i+\theta Z_i\) para todos; la fórmula cuadrática de la varianza
   deja de ser global.

8. Si todos están en la esquina, concluye:

   \[
   \boxed{
   \operatorname{Var}(V(\theta))
   =\Delta^2\theta\operatorname{Var}(\Gamma\alpha)}.
   \]

## Comprobaciones antes de tomar tus fotos

- ¿Se ve la cancelación de \(s\) en \(HZ\)?
- ¿Distinguiste \(\operatorname{Var}(H)\), \(\operatorname{Cov}(H,Z)\) y
  \(\operatorname{Var}(Z)\)?
- ¿Anotaste que convexidad estricta requiere \(\operatorname{Var}(Z)>0\)?
- ¿Separaste “(30) implica \(\theta^*>0\)” de “pendiente en uno positiva implica
  \(\theta^*<1\)”?
- ¿Comprobaste el contraejemplo con fracciones, no solo con decimales?
- ¿Mostraste la solución por tramos cuando \(e^*=0\)?
- ¿Puedes explicar que el objeto es \(\operatorname{Var}_i(V_i(\theta))\)?

Cuando hayas hecho el cálculo tú mismo, fotografía tus hojas reales y colócalas en
`hand/`. Esta guía no declara que la verificación manuscrita esté completa.
