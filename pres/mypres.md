---
title: Beamer Presentation
author: 
    - Philipp Geier
    - some more authors
date: {command: "today"}

bibliography: "bib/mybib.bib"

biblatexoptions:
  - "backend=biber"

toc: "yes"
fontsize: "8pt"
aspectratio: "43"

---

# Chap1

## Rows & Columns


\row{c}

\col{0.3\textwidth}

![](images/Tux.pdf){#fig:fig1 width=50%}\

Tux here

\col{0.3\textwidth}

Tux there
![](images/Tux.pdf){#fig:fig1 width=50%}\

\rowend

\row{c}

\col{0.3\textwidth}

![](images/Tux.pdf){#fig:fig1 width=50%}\
here again

\col{0.3\textwidth}

there again
![](images/Tux.pdf){#fig:fig1 width=50%}\

\rowend
