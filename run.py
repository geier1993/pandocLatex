import os, sys, getopt
import itertools as it
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/src")
from pandocLatex import *

##################
### Formatting ###
##################

# Some global parameters
latexEngine="lualatex"
highlightstyle='"tango"' #pygments, kate, monochrome, espresso, zenburn, haddock, tango
template="template/document.latex"
beamer="template/beamer.latex"
letter="template/letter.latex"

# Format documents with yaml files
docFormat = [
    "template/format_simple.yaml",
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/titlepage.yaml",
    "template/typography_sans.yaml"
    ]

# Pandoc parameters
docOptions = [
        "-t latex",
        "-s ",
#       "--columns 1",
#        "--filter pandoc-include-code",
#        "--filter pandoc-include",
#        "--filter pandoc-csv2table",
#        "--filter pandoc-crossref",
#   "--filter diagrams-pandoc",
#       "--filter pandoc-placetable", # compiled with inlinemarkdown
        "--filter pandoc-citeproc",
        "--template={template}".format(template=template),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--pdf-engine={le}".format(le=latexEngine),
        "--number-sections",
        "--biblatex",
#        "--chapter",
#        "-M synctex:yes"
        "-M codeBlockCaptions:yes",
    ]


# Presentations
beamerFormat = [
    "template/format_beamer.yaml",
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/typography_lmodern.yaml"
    ]

beamerOptions = [
        "-t beamer",
        "-s ",
#        "-o {out}".format(out=texFile),
#       "--columns 1",
#        "--filter pandoc-include",
#        "--filter pandoc-csv2table",
#        "--filter pandoc-crossref",
#       "--filter diagrams-pandoc",
#       "--filter pandoc-placetable", # compiled with inlinemarkdown
        "--filter pandoc-citeproc",
        "--template={template}".format(template=beamer),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--pdf-engine={le}".format(le=latexEngine),
        "--number-sections",
        "--biblatex",
        "-M synctex:yes"
    ]

# Tikzfiles
# Tikz images can be generated from separate files using the same formatting as their documents
# On this way each figure is generated in a separate pdf
tikzFormat = [
    "template/format_tikz.yaml",    # Just this is different....
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/typography_sans.yaml"
    ]

tikzOptions= [
        "-t latex",
        "-s ",
#       "--columns 1",
        "--template={template}".format(template=template),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--pdf-engine={le}".format(le=latexEngine),
    ]


# PSGraf files
# Files generated with PSGraf - separated in .pdf and .tex file - can be placed in PSGrafIN to generate a standalone image
psgrafFormat = [
    "template/format_psgraf.yaml",    # Just this is different....
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/typography_sans.yaml"
    ]

psgrafOptions= [
        "-t latex",
        "-s ",
#       "--columns 1",
        "--template={template}".format(template=template),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--pdf-engine={le}".format(le=latexEngine),
    ]


inkscapeFormat = [
    "template/format_inkscape.yaml",    # Just this is different....
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/typography_sans.yaml"
    ]

inkscapeOptions= [
        "-t latex",
        "-s ",
#       "--columns 1",
        "--template={template}".format(template=template),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--pdf-engine={le}".format(le=latexEngine),
    ]

letterFormat = [
    "template/format_letter.yaml",
    "template/color_unihd.yaml",
    "template/objects.yaml",
    "template/titlepage.yaml",
    "template/typography_sans.yaml"
    ]

# Pandoc parameters
letterOptions = [
        "-t latex",
        "-s ",
#       "--columns 1",
#        "--filter pandoc-include",
#        "--filter pandoc-csv2table",
#        "--filter pandoc-crossref",
#   "--filter diagrams-pandoc",
#       "--filter pandoc-placetable", # compiled with inlinemarkdown
        "--filter pandoc-citeproc",
        "--template={template}".format(template=letter),
        "--highlight-style={hls}".format(hls=highlightstyle),
        "--pdf-engine={le}".format(le=latexEngine),
        "--number-sections",
        "--biblatex",
#        "--chapter",
#        "-M synctex:yes"
        "-M codeBlockCaptions:yes",
        "-M documentclass:scrlttr2"
    ]

################
### Commands ###
################

# Commands are created using the cmdObj defined in src/pandocLatex.py
# cmdObj(cmd, shellOutput, befor, after)
#   cmd: command string to be executed
#   shellOutput: True/False
#   before: action performed before execution
#   after: action performed after execution
#
#   before and after ta a list of tuples with functions, arguments, and keyword arguments
#   E.g.
#   before = [
#             ...
#             (func,(arg1,arg2,arg3),{kw1: karg1, kw2: kwarg2}),
#             ...
#                ]


def createDirMaybe(name=""):
  dir=os.path.dirname(name)
  if not os.path.exists(dir):
      os.makedirs(dir)

# Convert Markdown to Latex, using a latex template and YAML configuration
def genPandocCmd(out, src, format, options):
        return cmdObj(
            " ".join(["pandoc"] +
                     format +
                        src +
                ["-o {out}".format(out=out)] +
                    options),
            True,
            before=[
              (createDirMaybe,(),{"name": out}),
              (print,("-----\t","Pandoc\t{out}\t".format(out=out),"-----"),{})],
            # Adjust appearance of tables and figures
            # applyOnFile is defined in src/pandocLatex.py
            # Each line in file is passed through a list of filters...
            #after =[(applyOnFile, ([adjustLongtableFilter,centerFigureFilter],texFile) ,{})]
            after =[(applyOnFile, ([adjustLongtableFilter,adjustBeamerFootnote,adjustFigureCaption],out) ,{})]
    )

# Run latex
def genLatexCmd(src, options, pushDir=""):
        return cmdObj(
            " ".join([latexEngine] + options +[src]),
            True,
            before=[
              (print,("-----\t","Latex\t{out}\t".format(out=src),"-----"),{})],
            after =[],
            pushDir =pushDir
    )

# Run biber
def genBiberCmd(src, options):
        return cmdObj(
            " ".join(["biber"] + options + [src]),
            True,
            before=[(print,("-----\t","Biber\t{out}\t".format(out=src),"-----"),{})],
            after =[]
    )

# Make Glossary
def genGlossaryCmd(src, options, pushDir=""):
        return cmdObj(
            " ".join(["makeglossaries"] + options + [src]),
            True,
            before=[(print,("-----\t","Glossary\t{out}\t".format(out=src),"-----"),{})],
            after =[],
            pushDir =pushDir
    )


def genPSGrafWrapCmd(out, src, format, options):
        return cmdObj(
#"echo \"\\begin{{minipage}}[b]{{2.0\\textwidth}}\\PDFfigure{{}}{{{fn}}}{{}}{{}}{{b}}{{T}}{{f}}\\end{{minipage}}\" > {out}".format(fn=src,out=out),
#"echo \"\\PDFfigure{{}}{{{fn}}}{{}}{{}}{{b}}{{T}}{{f}}\" > {out}".format(fn=src,out=out),
"mkdir -p {dir}\n".format(dir=os.path.dirname(out)) +
"echo \"\\PDFfigureStandaloneSTL{{{fn}}}{{T}}\" > {out}".format(fn=src,out=out),
            True,
            before=[
              (createDirMaybe,(),{"name": out}),
              (print,("-----\t","Create PSGraf Wrapper File \t{out}\t".format(out=out),"-----"),{})],
            after =[]
    )



def genInkscapeWrapCmd(out, src, format, options):
        return cmdObj(
"mkdir -p {dir}\n".format(dir=os.path.dirname(out)) +
"echo \"\\input{{{fn}}}\" > {out}".format(fn=src,out=out),
            True,
            before=[
              (createDirMaybe,(),{"name": out}),
              (print,("-----\t","Create Inkscape Wrapper File \t{out}\t".format(out=out),"-----"),{})],
            after =[]
    )




def recursiveListDir(path):
    p2 = os.path.dirname(path)
    for f in os.listdir(p2):
        fp = p2+'/'+f;
        if(os.path.isdir(fp)):
            for f2 in recursiveListDir(fp+'/'):
                yield f2
        else:
            yield fp

def recursiveListDirNoFiles(path):
    p2 = os.path.dirname(path)
    for f in os.listdir(p2):
        fp = p2+'/'+f;
        if(os.path.isdir(fp)):
            yield(fp)
            for f2 in recursiveListDirNoFiles(fp+'/'):
                yield f2


#################
### Documents ###
#################

# Take each filename in tikz/ ending with .md and add string to tikzFiles
filterFilesInDir = lambda d, filterf: ("/".join(  (".".join(f[:-1])).split("/")[1:]  ) for f in map(lambda fn: fn.split("."),
                                     recursiveListDir(d)) if filterf(f))
mdFilesInDir = lambda d: filterFilesInDir(d,lambda f: f[-1] == 'md') 
pdfFilesInDir = lambda d: filterFilesInDir(d,lambda f: f[-1] == 'pdf')
pdfTexFilesInDir = lambda d: filterFilesInDir(d,lambda f: f[-1] == 'pdf_tex')

splitPathFile = lambda d: (lambda sl: ( '/'.join(sl[:-1]), sl[-1]))(d.split('/'))

# Has to end with "/"
docInDir = "doc/"
docOutDir = "out/doc/"
presInDir = "pres/"
presOutDir = "out/pres/"
tikzInDir = "tikz/"
tikzOutDir = "out/tikz/"
psgrafInDir = "PSGraf/"
psgrafOutDir = "out/PSGraf"
inkscapeInDir = "Inkscape/"
inkscapeOutDir = "out/Inkscape"
letterInDir = "letter/"
letterOutDir = "out/letter/"

tikzFiles = {"prefix": tikzInDir, "keys": mdFilesInDir(tikzInDir), "suffix": ".md"}
psgrafFiles = {"prefix": psgrafInDir, "keys": pdfFilesInDir(psgrafInDir), "suffix": ".pdf"}
inkscapeFiles = {"prefix": inkscapeInDir, "keys": pdfTexFilesInDir(inkscapeInDir), "suffix": ".pdf_tex"}
docFiles = {"prefix": docInDir, "keys": mdFilesInDir(docInDir), "suffix": ".md"}
presFiles = {"prefix": presInDir, "keys": mdFilesInDir(presInDir), "suffix": ".md"}
letterFiles = {"prefix": letterInDir, "keys": mdFilesInDir(letterInDir), "suffix": ".md"}

# Global document object storing all keys with a list of cmdObjs
docs = {
#    **{
#    "mydoc": [
#        genPandocCmd(
#           **{
#                       "out" : "out/mydoc.tex",
#                       "src" :  [
#                                   "doc/mydoc.md"
#                                   ],
#                       "format": docFormat,
#                       "options": docOptions
#                       }),
#        # Just uncomment to not rerun it each time
#        genBiberCmd(
#           **{
#                       "src" : "out/mydoc",
#                       "options": [],
#                       }),
#        genLatexCmd(
#           **{
#                       "src" : "out/mydoc.tex",
#                       "options": ["-synctex=1",
#                                   "--output-directory=./out/"],
#                           #"options": ["--interaction=batchmode","-synctex=1"],
#                       }),
#       ]},
     # docFiles
     **{
     keyprefix+key+keysuffix : (
         genPandocCmd(
            **{
                        "out": docOutDir+key+".tex",
                        "src": [
                                docInDir+key+".md",
                                ],
                        "format": docFormat,
                        "options": docOptions,
                        }),
             # Just uncomment to not rerun it each time
             genBiberCmd(
                **{
                            "src" : docOutDir+key,
                            "options": [],
                            }),
             genGlossaryCmd(
              **{
                          "src": key+".glo",
                          "options": [],
                          "pushDir": os.path.abspath(docOutDir) 
                          }),
             genLatexCmd(
            **{
                        "src": docOutDir+key+".tex",
                        "options": ["--output-directory="+docOutDir],
                            #"options": ["--interaction=batchmode","-synctex=1"],
                        }),
                 )
             for (keyprefix,keys,keysuffix) in [(docFiles["prefix"],docFiles["keys"],docFiles["suffix"])] for key in keys
            },
     # presFiles
     **{
     keyprefix+key+keysuffix: (
         genPandocCmd(
            **{
                        "out": presOutDir+key+".tex",
                        "src": [
                                presInDir+key+".md",
                                    ],
                        "format": beamerFormat,
                        "options": beamerOptions,
                        }),
             # Just uncomment to not rerun it each time
             genBiberCmd(
                **{
                            "src" : presOutDir+key,
                            "options": [],
                            }),
             genLatexCmd(
            **{
                        "src": presOutDir+key+".tex",
                        "options": ["--output-directory="+presOutDir],
                            #"options": ["--interaction=batchmode","-synctex=1"],
                        }),
                 )
             for (keyprefix,keys,keysuffix) in [(presFiles["prefix"],presFiles["keys"],presFiles["suffix"])] for key in keys
            },
     # tikzFiles
     **{
     keyprefix+fullkey+keysuffix: (
         genPandocCmd(
            **{
                        "out": tikzOutDir+fullkey+".tex",
                        "src": [
                                tikzInDir+fullkey+".md",
                                    ],
                        "format": tikzFormat,
                        "options": tikzOptions,
                        }),
             genLatexCmd(
            **{
                        "src": tikzOutDir+fullkey+".tex",
                        "options": ["--output-directory="+os.path.abspath(os.path.dirname(tikzOutDir+fullkey))]
                        #"pushDir": os.path.abspath(keyprefix+keydir) 
                        }),
                 )
             for (keyprefix,keys,keysuffix) in [(tikzFiles["prefix"],tikzFiles["keys"],tikzFiles["suffix"])] for fullkey in keys for (keydir,key) in [splitPathFile(fullkey)]
            },
     # psGrafFiles
     **{
     keyprefix+key+keysuffix: (
         genPSGrafWrapCmd(
            **{
                        "out": psgrafOutDir+'/'+key+".md",
                        "src": keyprefix+key,
                        "format": [],
                        "options": [],
                        }),
         genPandocCmd(
            **{
                        "out": psgrafOutDir+'/'+key+".tex",
                        "src": [
                                psgrafOutDir+'/'+key+".md",
                                    ],
                        "format": psgrafFormat,
                        "options": psgrafOptions,
                        }),
             genLatexCmd(
            **{
                        "src": psgrafOutDir+'/'+key+".tex",
                        #"options": ["--output-directory="+os.path.dirname(psgrafOutDir+'/'.join(key.split('/')[1:]))],
                        "options": ["--output-directory="+os.path.dirname(psgrafOutDir+'/'+key)],
                        }),
                 )
             for (keyprefix,keys,keysuffix) in [(psgrafFiles["prefix"],psgrafFiles["keys"],psgrafFiles["suffix"])] for key in keys
            },
     # inkscapeFiles
     **{
     keyprefix+fullkey+keysuffix: (
         genInkscapeWrapCmd(
            **{
                        "out": inkscapeOutDir+'/'+fullkey+".md",
                        "src": key+keysuffix,
                        "format": [],
                        "options": [],
                        }),
         genPandocCmd(
            **{
                        "out": inkscapeOutDir+'/'+fullkey+".tex",
                        "src": [
                                inkscapeOutDir+'/'+fullkey+".md",
                                    ],
                        "format": inkscapeFormat,
                        "options": inkscapeOptions,
                        }),
             genLatexCmd(
            **{
                        "src": os.path.abspath(inkscapeOutDir+'/'+fullkey+".tex"),
                        "options": ["--output-directory="+os.path.abspath(os.path.dirname(inkscapeOutDir+'/'+fullkey))],
                        "pushDir": os.path.abspath(keyprefix+keydir) 
                        }),
                 )
             for (keyprefix,keys,keysuffix) in [(inkscapeFiles["prefix"],inkscapeFiles["keys"],inkscapeFiles["suffix"])] for fullkey in keys for (keydir,key) in [splitPathFile(fullkey)]
            },
     # letterFiles
     **{
     keyprefix+key+keysuffix : (
         genPandocCmd(
            **{
                        "out": letterOutDir+key+".tex",
                        "src": [
                                letterInDir+key+".md",
                                ],
                        "format": letterFormat,
                        "options": letterOptions,
                        }),
             # Just uncomment to not rerun it each time
             genBiberCmd(
                **{
                            "src" : letterOutDir+key,
                            "options": [],
                            }),
             genGlossaryCmd(
              **{
                          "src": key+".glo",
                          "options": [],
                          "pushDir": os.path.abspath(letterOutDir) 
                          }),
             genLatexCmd(
            **{
                        "src": letterOutDir+key+".tex",
                        "options": ["--output-directory="+letterOutDir],
                            #"options": ["--interaction=batchmode","-synctex=1"],
                        }),
                 )
             for (keyprefix,keys,keysuffix) in [(letterFiles["prefix"],letterFiles["keys"],letterFiles["suffix"])] for key in keys
            },
    }


# Form some groups of keys if desired
docGroups={}
docGroups["all"] = it.chain(*(docs[k] for k in docs.keys()))

docGroups["docs"] = it.chain(*(docs[docFiles["prefix"]+k+docFiles["suffix"]] for k in docFiles["keys"]))
for d in recursiveListDirNoFiles(docInDir):
  docGroups[d] = it.chain(*(docs[docFiles["prefix"]+k+docFiles["suffix"]] for k in mdFilesInDir(d+'/')))

docGroups["pres"] = it.chain(*(docs[presFiles["prefix"]+k+presFiles["suffix"]] for k in presFiles["keys"]))
for d in recursiveListDirNoFiles(presInDir):
  docGroups[d] = it.chain(*(docs[presFiles["prefix"]+k+presFiles["suffix"]] for k in mdFilesInDir(d+'/')))

docGroups["tikz"] = it.chain(*(docs[tikzFiles["prefix"]+k+tikzFiles["suffix"]] for k in tikzFiles["keys"]))
for d in recursiveListDirNoFiles(tikzInDir):
  docGroups[d] = it.chain(*(docs[tikzFiles["prefix"]+k+tikzFiles["suffix"]] for k in mdFilesInDir(d+'/')))

docGroups["psgraf"] = it.chain(*(docs[psGrafFiles["prefix"]+k+psgrafFiles["suffix"]] for k in psgrafFiles["keys"]))
for d in recursiveListDirNoFiles(psgrafInDir):
  docGroups[d] = it.chain(*(docs[psgrafFiles["prefix"]+k+psgrafFiles["suffix"]] for k in pdfFilesInDir(d+'/')))

docGroups["inkscape"] = it.chain(*(docs[inkscapeFiles["prefix"]+k+inkscapeFiles["suffix"]] for k in inkscapeFiles["keys"]))
for d in recursiveListDirNoFiles(inkscapeInDir):
  docGroups[d] = it.chain(*(docs[inkscapeFiles["prefix"]+k+inkscapeFiles["suffix"]] for k in pdfTexFilesInDir(d+'/')))

docGroups["letter"] = it.chain(*(docs[letterFiles["prefix"]+k+letterFiles["suffix"]] for k in letterFiles["keys"]))
for d in recursiveListDirNoFiles(letterInDir):
  docGroups[d] = it.chain(*(docs[letterFiles["prefix"]+k+letterFiles["suffix"]] for k in mdFilesInDir(d+'/')))

def printUsage():
    print(bold("Usage:"))
    print("\t./run [DocKey] [-g GroupKey]\n")
    print(bold("Documets:"))
    for k in docs.keys():
            print("\t{k}".format(k=k))

    print("")
    print(bold("Groups:"))
    for k in docGroups.keys():
        print("\t{k}".format(k=k))

def printKeysNotFound(keys):
    print(bold(red("Keys not found:")))
    for k in keys:
        print(yellow("\t{k}".format(k=k)))
    print("")
    print(underline("".join(it.repeat(" ",40))))
    print("")
    printUsage()



bold = lambda str: "\033[1m" + str + "\033[0m"
underline= lambda str: "\033[4m" + str + "\033[0m"
red= lambda str: "\033[31m" + str + "\033[0m"
yellow= lambda str: "\033[33m" + str + "\033[0m"


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "hg:", ["help","group="])
    except getopt.GetoptError as msg:
        printUsage()
        sys.exit(2)
    if(len(argv)==1):
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
