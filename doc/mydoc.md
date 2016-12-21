---
title: Example Document
subtitle: Custom Latex Template generated with Pandoc 
author: 
   - Philipp Geier 
   - some more authors 
#date: 2015-08-18
date: {command: "today"}

author-meta: Philipp Geier
title-meta: example document

bibliography: "bib/mybib.bib"

lol: "yes" # "" to disable
toc: "yes"
lof: "yes"
lot: "yes"
codeBlockCaptions: "" # "yes" oder "withsomecontent" to enable
---


# PandocLatex

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


![A figure](images/Tux.pdf){#fig:fig1 width=50%}

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
