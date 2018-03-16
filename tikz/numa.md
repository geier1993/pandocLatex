
\begin{tikzpicture}[
  innerram/.style={draw,fill=yellow!50,thick,inner sep=3pt,minimum width=8em},
  innercpu/.style={draw,fill=red!50,thick,inner sep=3pt,minimum width=8em},
  outer/.style={draw=gray,dashed,fill=green!1,thick,inner sep=5pt}
  ]
%---------------------------------------------------%
  \node [innerram,minimum width=18em] (A1) at (0.0,0.0) {Memory};
  \node [innercpu,anchor=south west,minimum width=8em] (A2) at ([yshift=1em]A1.north west) {CPU};
  \node [innercpu,anchor=south east,minimum width=8em] (A3) at ([yshift=1em]A1.north east) {CPU};
  \node (text) [anchor=north] at ([yshift=4em]A1.north) {Node 1};
\begin{pgfonlayer}{background}
\node[outer,fit=(A1) (A2) (A3) (text)] (A) {};
\end{pgfonlayer}

  \node [innerram,minimum width=18em] (B1) at (8.0,0.0) {Memory};
  \node [innercpu,anchor=south west,minimum width=8em] (B2) at ([yshift=1em]B1.north west) {CPU};
  \node [innercpu,anchor=south east,minimum width=8em] (B3) at ([yshift=1em]B1.north east) {CPU};
  \node (text) [anchor=north] at ([yshift=4em]B1.north) {Node 2};
\begin{pgfonlayer}{background}
\node[outer,fit=(B1) (B2) (B3) (text)] (B) {};
\end{pgfonlayer}

  \node [innerram,minimum width=18em] (D1) at (8.0,4.0) {Memory};
  \node [innercpu,anchor=south west,minimum width=8em] (D2) at ([yshift=1em]D1.north west) {CPU};
  \node [innercpu,anchor=south east,minimum width=8em] (D3) at ([yshift=1em]D1.north east) {CPU};
  \node (text) [anchor=north] at ([yshift=4em]D1.north) {Node 4};
\begin{pgfonlayer}{background}
\node[outer,fit=(D1) (D2) (D3) (text)] (D) {};
\end{pgfonlayer}

  \node [innerram,minimum width=18em] (C1) at (0.0,4.0) {Memory};
  \node [innercpu,anchor=south west,minimum width=8em] (C2) at ([yshift=1em]C1.north west) {CPU};
  \node [innercpu,anchor=south east,minimum width=8em] (C3) at ([yshift=1em]C1.north east) {CPU};
  \node (text) [anchor=north] at ([yshift=4em]C1.north) {Node 3};
\begin{pgfonlayer}{background}
\node[outer,fit=(C1) (C2) (C3) (text)] (C) {};
\end{pgfonlayer}


\draw[-,thick,color=green] (A) to (B);
\draw[-,thick,color=green] (C) to (D);
\draw[-,thick,color=green] (D) to (B);
\draw[-,thick,color=green] (A) to (C);

\end{tikzpicture}



