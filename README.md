# Universal-Source-Coding
Exponential Gradient Descent
\section{Exponential Gradient Descent}
We assume the decision space to be the following \(S\) is a d-dimensional simplex that is 
\[S=\left\{ w | w_{i} \geq 0 \text{ and }  ||w||_{1}=1 \right\}\]
In exponentiated gradient descent at time \(t=1\) we choose the central point of the simplex namely \(w_{i,d}=\frac{1}{d}\) then we update in the following manner:
$$\forall i \in \left [ d \right ],w_{t+1,i}=\frac{w_{t,i}\text{exp}\left\{-\eta \left[ \nabla c_{t} \left(w_{t} \right) \right]_{i}\right\}}{Z_{t}}$$ where 
$$Z_{t}=\sum_{i} w_{t,i} \left[ \nabla c_{t}\left(w_{t}\right)\right]_{i}$$ 

Here \(\left [ \dot \right]_{i}\) denotes the ith component of the vector.The division by \(\text{Z}_{t}\) normalizes so that \(w_{t+1}\in S\) that is \(||w_{t+1}||_{1}=1\) 
\newline


\begin{algorithm}
\caption{Exponential Gradient descent}
\begin{algorithmic}[1]
\Require {\text{convex} $f:\Delta_{n} \to \mathbb{R}$}
\Ensure {: $\eta \geq 0 ,T>0$}
\State Set $p^{0}=\frac{1}{n}\mathrm{1}$ (The uniform Distribution) $\in \Delta_{n}$
\For{$t=0:T-1$}{
    \newline
    $g^{t} := \nabla f(p^{t})$
    \newline
    $w^{t+1} := p_{i}^{t+1}e^{-\eta g_{i}^{t}}$
    \newline
    $p_{i}^{t+1}:=\frac{w_{i}^{t+1}}{||w_^{t+1}||}$
}
\newline
\State \Return $\bar{p}=\frac{1}{T} \sum_{t=0}^{T-1}p^t$
\end{algorithmic}
\end{algorithm}
