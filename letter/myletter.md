---
classoption:
  - "titlepage=on"
  - "fromrule=false"
  - "headsepline=true"
  - "fromemail=true"
  - "fromphone=true"
  - "specialmail=true"
#  - "fromrule=aftername"
#  - "backaddress=plain"
#  - "enlargefirstpage"

pagenumber: true
fromalign: location
parskip: full


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
                                                                      
biblatexoptions:
  - "backend=biber"

fontsize: 11pt
papersize: a4
lang: de

komavar:
  -
    var: fromname
    value: Philipp Geier
  -
    var: fromaddress
    value: |
      | Street 5
      | D-694XX Nana
  -
    var: fromphone
    value: +49 176 XX
  -
    var: fromemail
    value: e@mail.de
  -
    var: specialmail
    value: e@mail.de
  -
    var: signature
    value: Philipp Geier
  -
    var: subject
    value: Application for ??
  -
    var: customer
    value: 311768
    options:
      - MatrikelNumber
  -
    var: title
    value: Title
    

#addtokomafont:
#  -
#    var: fromrule
#    value: "\\color{darksecondarycolor}"
#  -
#    var: backaddress
#    value: "\\color{darkprimarycolor}"
#  -
#    var: subject
#    value: "\\color{darkprimarycolor}"
#  -
#    var: title
#    value: "\\color{darkprimarycolor}"
    
    
letter_to: |
  | Name
  | Street 3
  | 69XXX Nunu
  
#letteropening:
#  Sehr geehrte Damen und Herren,
#  
#letterclosing:
#  Mit freundlichen Grü{\ss}en,
  

attachement:
  title: Anhang
  enclosed:
    - Lebenslauf
  
---

\opening{
Sehr geehrte Damen und Herren,
}

ich schreibe Ihnen aufgrund der Vakanz..

![\[\[Short Caption\]\] A figure](images/Tux.pdf){#fig:fig1 width=50%}\


\usekomavar{subject}

-------------------------------------------------------------------------------
ColLeft                   ColCenter                                    ColRight
----------------------  ------------------------------  -----------------------
Line1                   Line1                           Line1

Line2                   Line2                           Line2

![](images/Tux.pdf)     ![](images/Tux.png)             ![](images/Tux.png)
-------------------------------------------------------------------------------

: Caption of table {#tbl:tableid}


\clearpage

Newpage

\closing{
Mit freundlichen Grüßen,
}

\ps

Check out <http://geier.me>
