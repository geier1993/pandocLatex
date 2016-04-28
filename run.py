#!/usr/bin/python

import os, sys
sys.path.append(os.path.dirname(__file__) + "/src")
from pandocLatex import *

mdFile="doc/mydoc.md"
latexEngine="lualatex"
texFile="mydoc.tex"
highlightstyle='"tango"' #pygments, kate, monochrome, espresso, zenburn, haddock, tango
template="template/template.latex"

# Convert Markdown to Latex, using a latex template and YAML configuration
pandocCmd = cmdObj(
        " ".join(["pandoc",
        		"template/format_howto.yaml",
        		"template/color_unihd.yaml",
        		"template/objects.yaml",
        		"template/titlepage.yaml",
        		"template/typography_sans.yaml",
        		mdFile,
                        "-t latex",
                        "-s ",
                        "-o {out}".format(out=texFile),
#                        "--columns 1",
                        "--filter pandoc-csv2table",
                        "--filter pandoc-crossref",
#                        "--filter diagrams-pandoc",
#                        "--filter pandoc-placetable", # compiled with inlinemarkdown
                        "--filter pandoc-citeproc",
                        "--template={template}".format(template=template),
                        "--highlight-style={hls}".format(hls=highlightstyle),
                        "--latex-engine={le}".format(le=latexEngine),
                        "--number-sections",
                        "--chapter"
                        ]),
        True,
        before=[(print,("-----\t","Pandoc\t","-----"),{})],
        # Adjust appearance of tables and figures
        #after =[(applyOnFile, ([adjustLongtableFilter,centerFigureFilter],texFile) ,{})]
        after =[(applyOnFile, ([adjustLongtableFilter],texFile) ,{})]
	)


# Run latex
latexCmd = cmdObj(
        " ".join([latexEngine,texFile,
                        "-draftmode","-interaction=batchmode",
                        ]),
        True,
        before=[(print,("-----\t","Latex\t","-----"),{})],
        after =[]
	)


# Run bibtex
bibtexCmd = cmdObj(
        " ".join(["bibtex",texFile,
                        ]),
        True,
        before=[(print,("-----\t","BibTex\t","-----"),{})],
        after =[]
	)


# Run pandoc and latex
processCommands([pandocCmd,latexCmd])
