#!/usr/bin/python

import os, sys, getopt
import itertools as it
sys.path.append(os.path.dirname(__file__) + "/src")
from pandocLatex import *

latexEngine="lualatex"
highlightstyle='"tango"' #pygments, kate, monochrome, espresso, zenburn, haddock, tango
template="template/document.latex"

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
        "--chapter",
        "-M synctex:yes"
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
                        	"options": ["--interaction=batchmode","-synctex=1"],
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
                        	"options": ["--interaction=batchmode","--output-directory=./tikz/","-synctex=1"],
                    	}),
		]
	}

docGroups={}
docGroups["all"] = it.chain(*(docs[k] for k in docs.keys()))

def printUsage():
	print("Usage:\n")
	print("\trun.py [DocKey] [-g GroupKey]\n")
	print("Documets:")
	for k in docs.keys():
            print("\t{k}".format(k=k))

	print("Groups:")
	for k in docGroups.keys():
	    print("\t{k}".format(k=k))

def printKeysNotFound(keys):
    print("Keys not found:")
    for k in keys:
        print("\t{k}".format(k=k))
    print("")
    print("".join(it.repeat("-",40)))
    print("")
    printUsage()


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "hg:", ["help","group="])
    except getopt.GetoptError as msg:
        printUsage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ['-h','--help']:
            printUsage()
            sys.exit()
        if opt in ['-g','--group']:
            if arg in docGroups.keys():
                processCommands(docGroups[arg])
            else:
                printKeysNotFound([arg])
            sys.exit()

    notfound = list(filter(lambda k: not(k in docs.keys()), args))
    if len(notfound)>0:
        printKeysNotFound(notfound)
        sys.exit()
    processCommands(it.chain(*(docs[k] for k in args)))


if __name__== "__main__":
    sys.exit(main())

# Run pandoc and latex
#processCommands([pandocCmd,latexCmd])
