---
title: Machine Learning 
subtitle: test
author: Philipp Geier 
date: 2015-08-18

author-meta: Philipp Geier
title-meta: Machine Learning

documentclass: article
---


# test

## Test2

oeuoe
oeuoe

oeuoe
oeuoe

   1. a
   2. b
   3. c
   
oeuoe
oeuoe

   * i
      + ii
    	 - iii 
    	    * iv
oeuoe
oeuoe
oeuoe

Definition list

: some content


Definition list2
  ~ Def a
  ~ Def b

$$
\alpha = \pi
$$

![](images/Tux.pdf){#fig:fig1 width=50%}

oeuoe
oeuoe
[@fig:figure1RefA;@fig:figure1RefB]
oeuoe
oeuoe
oeuoe
oeuoe


<div id="fig:figure1Ref" style="align: center">

![subfigure1 1 caption](images/Tux_small.png "fig:"){#fig:figure1RefA width=50%}
![subfigure1 2 caption](images/Tux_small.png "fig:"){#fig:figure1RefB rowend=True}

![subfigure1 3 caption](images/Tux_small.png "fig:"){#fig:figure1RefC}
![subfigure1 3 caption](images/Tux_small.png "fig:"){#fig:figure1RefD}

Caption of figure1
</div>

oeuoe
oeuoe
oeuoe
oeuoe
oeuoe
oeuoe

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

oeuoe
oeuoe
oeuoe

   * List with codeblock

    ```{#lst:code .haskell}
    main :: IO ()
    main = putStrLn "Hello World!"
    ```
    
    
Listing: Listing caption

```{#lst:code .haskell}
main :: IO ()
main = putStrLn "Hello World!"
```

oeuoe
oeuoe
oeuoe
oeuoe
<!-- \marginnote{Test 2} -->
oeuoe
oeuoe
oeuoe
oeuoe
oeuoe
oeuoe


```` {.table #my-id type="multiline" inlinemarkdown="yes" aligns="RL" caption="2x2 images in a table" header="no"}
"![](images/Tux.pdf)","![](images/Tux.png)"
"![](images/Tux.pdf)","![](images/Tux.png)"
```` 

```` {.table type="multiline" aligns="RCL" caption="a table" header="yes"}
$\alpha$,$\beta$,$\gamma$
1,2,3
4,5,6
7,8,9
```` 

```` {.table type="multiline" aligns="C" caption="a table" header="yes"}
$\mathrm{Mathrm}$,$\mathit{Mathit}$,$\mathbf{MathBF}$,$\bm{BM}$
$\mathrm{A little text}$,$\mathit{A little text}$,$\mathbf{A little text}$,$\bm{A little text}$
$\mathrm{\nabla \cdot \nabla}$,$\mathit{\nabla \cdot \nabla}$,$\mathbf{\nabla \cdot \nabla}$,$\bm{\nabla \cdot \nabla}$
$\mathrm{\alpha \times 3}$,$\mathit{\alpha \times 3}$,$\mathbf{\alpha \times 3}$,$\bm{\alpha \times 3}$
```` 


Some text after the table

# la

# le 

# le

1

2

3

4

5

6

7


