#!/usr/bin/python

import os, sys, getopt, itertools
sys.path.append(os.path.dirname(__file__) + "/src")
from pandocLatex import *

latexEngine="lualatex"
highlightstyle='"tango"' #pygments, kate, monochrome, espresso, zenburn, haddock, tango
template="template/template.latex"

docFormat = [
    "template/format_howto.yaml",
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/titlepage.yaml",
    "template/typography_sans.yaml"
    ]

docOptions = [
        "-t latex",
        "-s ",
#        "-o {out}".format(out=texFile),
#       "--columns 1",
        "--filter pandoc-csv2table",
        "--filter pandoc-crossref",
# 	"--filter diagrams-pandoc",
#       "--filter pandoc-placetable", # compiled with inlinemarkdown
        "--filter pandoc-citeproc",
        "--template={template}".format(template=template),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--latex-engine={le}".format(le=latexEngine),
        "--number-sections",
        "--chapter"
	]

tikzFormat = [
    "template/format_tikz.yaml",
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/titlepage.yaml",
    "template/typography_sans.yaml"
    ]

tikzOptions= [
        "-t latex",
        "-s ",
#        "-o {out}".format(out=texFile),
#       "--columns 1",
        "--template={template}".format(template=template),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--latex-engine={le}".format(le=latexEngine),
	]


# Convert Markdown to Latex, using a latex template and YAML configuration
def genPandocCmd(out, src, format, options):
        return cmdObj(
            " ".join(["pandoc"] +
            		 format +
            		    src +
                ["-o {out}".format(out=out)] +
            		options),
            True,
            before=[(print,("-----\t","Pandoc\t{out}\t".format(out=out),"-----"),{})],
            # Adjust appearance of tables and figures
            #after =[(applyOnFile, ([adjustLongtableFilter,centerFigureFilter],texFile) ,{})]
            after =[(applyOnFile, ([adjustLongtableFilter],out) ,{})]
    	)


########### Commands ##########
# Run latex
def genLatexCmd(src, options):
        return cmdObj(
            " ".join([latexEngine] + options +[src]),
            True,
            before=[(print,("-----\t","Latex\t{out}\t".format(out=src),"-----"),{})],
            after =[]
	)


# Run bibtex
def genBibtexCmd(src, options):
    	return cmdObj(
            " ".join(["bibtex"] + options + [texFile]),
            True,
            before=[(print,("-----\t","BibTex\t{out}\t".format(out=src),"-----"),{})],
            after =[]
	)



######### Documents .... ##########
docs = {
	 "mydoc": [
	 	 genPandocCmd(
	 	 	**{
                	 	"out" : "mydoc.tex",
                	 	"src" :  [
                            		"doc/mydoc.md"
                            		],
                        	"format": docFormat,
                        	"options": docOptions
                    	}),
	 	 genLatexCmd(
	 	 	**{
                	 	"src" : "mydoc.tex",
                        	"options": ["--interaction=batchmode"],
                    	}),
		],
	"example": [
		 genPandocCmd(
		 	**{
                	 	"out": "tikz/example.tex",
                	 	"src": [
                                        "doc/tikz/example.md"
                                	],
                        	"format": tikzFormat,
                            	"options": tikzOptions
                    	}),
		 genLatexCmd(
		 	**{
                	 	"src": "tikz/example.tex",
                        	"options": ["--interaction=batchmode","--output-directory=./tikz/"],
                    	}),
		]
	}

docs["all"] = itertools.chain(*(docs[k] for k in docs.keys()))

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            ops, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.GetoptError as msg:
            raise Usage(msg)
        # more code, unchanged
        processCommands(itertools.chain(*(docs[k] for k in args)))
    except Usage as err:
        print >>sys.stderr, err,msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__== "__main__":
    sys.exit(main())

# Run pandoc and latex
#processCommands([pandocCmd,latexCmd])
