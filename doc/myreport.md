---
title: |
  | Multi 
  | \text{---}
  | Line
subtitle: Custom Latex Template generated with Pandoc 
author: 
   - Philipp Geier
#date: 2015-08-18
date: {command: "today"}

multipletitlepages:
  firsttext: |
    | Master thesis 
    | in Physics 
    | submitted by 
    | Platon
    | born in Atlantis
  secondtext: |
    | This Master thesis has been carried out by Platon
    | at the Institute of Finding Atlantis
    | under the supervision of
    | Till Eulenspiegel
   
   
affiliation1: Department of Questions
affiliation2: University of Life
institution: Institute of Finding Atlantis
workgroup:  Simulating Reciprocal Destruction
workdegree: Candidature for Master In Beeing A Child
year: 2018
      
dedication: 
  environment: "flushright"
  text: Dedicated to ...

acknowledgements:
  heading: "\\slshape Acknowledgements"
  lang: "english"
  place: "Somewhere, Earth"
  author: "Mullah Nassr Eddin"
  date: "\\today"
  text: |
    I would like to thank....

author-meta: Philipp Geier
title-meta: example document

bibliography: "bib/mybib.bib"
                                                                      
biblatexoptions:
  - "backend=biber"
  
fontsize: 12pt

lol: "yes" # "" to disable
toc: "yes"
lof: "yes"
lot: "yes"
glossary: "yes"

glossaryoptions:
  - acronym

glossaryentries:
  - label: utc
    name: UTC
    description: Coordinate Universal Time

lang: en
babel-lang: "english"
babel-otherlangs:
  - english
  - ngerman
  - french
    
polyglossio-lang: {name: "english", options: ""}
polyglossia-otherlangs: [
  {name: english, option: ""},
  {name: german, option: ""},
  {name: french, option: ""}
  ]


# abstract: Writing some abstract...
#   That is possibly multiline. Let's look what it does look like,
#   whether some indent is given or not. Maybe this is unimportant, 
#   but it may look good. You know, aesthetics always rule.
  
abstractpage: "yes"
abstractheading: "yes"

abstracts:
  - lang: english
    text: |
      Writing some abstract...
      That is possibly multiline. Let's look what it does look like,
      whether some indent is given or not. Maybe this is unimportant, 
      but it may look good. You know, aesthetics always rule.
      \openq{}lal\closeq{} 
      Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   
  - lang: german
    text: |
      Man spricht deutsch 
      Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   


spruch: "\\begin{customquote}Ich muß wohl zwei oder drei Raupen aushalten, 
  wenn ich die Schmetterlinge kennenlernen will.\\end{customquote}
  \\hspace{5cm}
  \\begin{flushright}Der kleine Prinz\\end{flushright}"


declarationofauthorship:
  - lang: english
    heading: Statement of authorship
    place: Earth
    date: "\\today"
    text: I declare that I completed this thesis on my own and that information which has been 
      directly or indirectly taken from other sources has been noted as such. Neither this 
      nor a similar work has been presented to an examination committee.
  - lang: german
    heading: Selbstständigkeitserklärung
    place: Earth
    date: "den \\today"
    text: Ich erkläre hiermit, dass ich die vorliegende Arbeit selbständig verfasst 
      und nur unter Verwendung der angegebenen Quellen und Hilfsmittel angefertigt habe. 
      Weiterhin erkläre ich, eine Diplomarbeit in diesem Studiengebiet erstmalig einzureichen.


---


# PandocLatex {#sec:pandoclatex}

This is just a workflow I am using for document creation. Feel free to use and adjust to your needs.
Markdown and YAML is usd for abstractions.

   * <http://www.pandoc.org/>
   * <https://github.com/jgm/pandocfilters/>
   * <https://github.com/jgm/pandoc/wiki/Pandoc-Filters>
   * <https://github.com/baig/pandoc-csv2table>
   * <https://github.com/lierdakil/pandoc-crossref>
   * <https://github.com/diagrams/diagrams-pandoc>

## Todo

   * add letter template
   * filter for boxes?

## Heading2 

### Heading3

Glossary \gls{utc}.
Ordered list

   1. a
   2. b
      1. b1
      2. b2
      3. b3
   3. c
   
   
Unordered list

   * a
      * a1
      * a2
      * a3
   * b
   * c
   * d


Definition list

:   some content

    Stacked definition list
  
    :   with some more content 
    
           * and
           * a 
           * list
           * with some inline math $\tau=\dfrac{\pi}{2}=\frac{\pi}{2}$

        $$
        \alpha = \pi
        $$


![\[\[Short Caption\]\] A figure](images/Tux.pdf){#fig:fig1 width=50%}

A reference to a figure [@fig:fig1] using _pandoc-crossref_ filter.

[@fig:figure1RefA;@fig:figure1RefB]

<div id="fig:figure1Ref" style="align: center">

![subfigure1 caption](images/Tux_small.png "fig:"){#fig:figure1RefA width=50%}
![subfigure2 caption](images/Tux_small.png "fig:"){#fig:figure1RefB rowend=True}

![subfigure3 caption](images/Tux_small.png "fig:"){#fig:figure1RefC}
![subfigure4 caption](images/Tux_small.png "fig:"){#fig:figure1RefD}

A figure with subfigures using _pandoc-crossref_ filter
</div>

<!-- ![Image created with tikz in a separate document](tikz/tikzexample.pdf)
-->

<!-- a comment, not going to be processed -->

Here is a inline ![](images/icon216x16.png)\ figure.


Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
    belong to the previous footnote.
    
        { some.code }
            
    The whole paragraph can be indented, or just the first
    line.  In this way, multi-paragraph footnotes work like
    multi-paragraph list items.
                        
This paragraph won't be part of the note, because it
isn't indented.


   * List with codeblock

    ```{#lst:code .haskell}
    main :: IO ()
    main = putStrLn "Hello World!"
    ```
    

Codeblock with caption

```{#lst:code .haskell caption="test"}
main :: IO ()
main = putStrLn "Hello World!"
```

Table with stuff

-------------------------------------------------------------------------------
ColLeft                   ColCenter                                    ColRight
----------------------  ------------------------------  -----------------------
Line1                   Line1                           Line1

Line2                   Line2                           Line2

![](images/Tux.pdf)     ![](images/Tux.png)             ![](images/Tux.png)
-------------------------------------------------------------------------------

: Caption of table {#tbl:tableid}

Reference to a author @johndoe.
\clearpage

## pandoc-csv2table

Table using _pandoc-csv2table_ to generate a table from csv.
A table should contain a header for proper coloring.

```` {.table #my-id type="multiline" inlinemarkdown="yes" aligns="RL" caption="2x2 images in a table" header="no"}
"![](images/Tux.pdf)","![](images/Tux.png)"
"![](images/Tux.pdf)","![](images/Tux.png)"
```` 

```` {.table type="multiline" aligns="RCL" caption="\label{tbl:test} a table" header="yes"}
$\alpha$,$\beta$,$\gamma$
1,2,3
4,5,6
7,8,9
```` 

For csv tables, latex command \label{} must be put in caption, as @tbl:test shows.

![\label{tbl:extern} Table in a external csv myll](doc/table.csv)

# Math options

```` {.table type="multiline" aligns="C" caption="a table" header="yes"}
$\mathrm{Mathrm}$,$\mathit{Mathit}$,$\bm{bm}$,$\mathbbm{mathbbm}$
$\mathrm{A little text}$,$\mathit{A little text}$,$\bm{A little text}$,$\mathbbm{A little text}$
$\mathrm{\nabla \cdot \nabla}$,$\mathit{\nabla \cdot \nabla}$,$\bm{\nabla \cdot \nabla}$,$\mathbbm{\nabla \cdot \nabla}$
$\mathrm{\alpha \times 3}$,$\mathit{\alpha \times 3}$,$\bm{\alpha \times 3}$,$\mathbbm{\alpha \times 1}$
```` 

Use $\widetilde{widetilde}$ for simple stuff like $\widetilde{f}$.
Use $\widehat{widehat}$ for simple stuff like $\widehat{f}$.
Use mathcal for stuff like $\mathcal{L}$.

$$
  \llbracket     1 \rrbracket       \quad
  \llparenthesis 2 \rrparenthesis   \quad
  \llceil        3 \rrceil          \quad
  \llfloor       4 \rrfloor         \quad
$$




\appendix

# Appendix

## Some more code on

Detailed algorithme explained in @sec:pandoclatex

