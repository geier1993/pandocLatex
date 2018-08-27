#!/usr/bin/python
import subprocess as sp
import re #regexpr
import fileinput
import itertools as it
#import pandocfilters as pf



# Line object for parsing a file line by line
# Allows changing the line (i.e. removing, filtering, using regular expressions)
# or to add some lines
class lineObj(object):
      __slots__ = ('lno', 'linecount','line')
      def __init__(self, lno, linecount, line):
               self.lno = lno
               self.linecount = linecount
               self.line = line

      def __repr__(self):
          return ("Line:\t%d/%d, \"%s\"" % (self.lno,self.linecount,self.line))


# Takes a list of generators as defined below and passes all lines through the
# generator list
def applyOnFile(inputgenlist, fname):
    count = sum( (1 for line in open(fname).readlines(  )) )

    # Prepare file input
    # Wrap each line in a lineObj with linenumber and linecount
    def finputgenerator(finput):
        for (ln,lc,l) in zip(range(1,count+1),it.repeat(count,count),finput):
            yield lineObj(ln,lc,l)

    # Intermediate generator that is executed after each generator
    def flowController(filter):
        lastl = 0
        incr  = 0
        for lobj in filter:
            # Check whether a line has been added
            # If yes, increase line number and total linecount
            if(lobj.lno==lastl):
                incr += 1
            lastl =lobj.lno
            lobj.lno += incr
            lobj.linecount += incr
            yield lobj


    # Open file
    finput =fileinput.input(fname,inplace=True)
    # Prepare lines...
    processor = finputgenerator(finput)

    # Consecutively bind of all generators
    for gen in inputgenlist:
        processor = gen(flowController(processor))

    # Now pass each line through list of generators
    for lobj in processor:
        if(lobj.line!=None):
            print(lobj.line,end='')

    finput.close()

def centerFigureFilter(inputgen):
    for lobj in inputgen:
        yield lobj
        if(lobj.line):
            if(lobj.line.startswith("\\begin{figure}") ):
            	 #append on next line
                lobj.line = "\\centering"
                yield lobj

def adjustBeamerFootnote(inputgen):
    for lobj in inputgen:
        if(lobj.line!=None):
            lobj.line=re.sub(r'\\footnote<[^>]*>',
                    r'\\footnote',lobj.line)
        #yield (ln,lc,l)
        yield lobj

# Adjust longtables using regex to remove @{} in table formatting
# I.e \begin{longtable}[c]{@{}lrc@{}}
#       to \begin{longtable}[c]{lrc}
def adjustLongtableFilter(inputgen):
    #for (ln,lc,l) in inputgen:
    for lobj in inputgen:
        if(lobj.line!=None):
            lobj.line=re.sub(r'(\\begin){longtable}(\[\w*\]){@{}([lrc]*)@{}}',
                    r'\1{longtable}\2{\3}',lobj.line)
        #yield (ln,lc,l)
        yield lobj

# editor: https://regex101.com
def adjustFigureCaption(inputgen):
    #for (ln,lc,l) in inputgen:
    ltmp = ""
    for lobj in inputgen:
        if((lobj.line!=None)):
          if(lobj.line.startswith("\\caption")):
            #ltmp += lobj.line.rstrip('\n')
            ltmp += lobj.line
            lobj.line = ""
          elif(ltmp!=""):
            lobj.line = ltmp + lobj.line
            ltmp = ""
            # re.DOTALL makes . also match new line \n
            lobj.line=re.sub(r'(\\caption){{\[}{\[}(.+?(?={\]}{\]})){\]}{\]}',
                    r'\1[\2]{',lobj.line,flags=re.DOTALL)
            lobj.line=re.sub(r'(\\caption){(\\label{.+?}){\[}{\[}(.+?(?={\]}{\]})){\]}{\]}',
                    r'\1[\3]{\2',lobj.line,flags=re.DOTALL)
        yield lobj



# Command Object 
class cmdObj(object):
      __slots__ = ('cmd', 'shellOutput','before','after','pushDir')
      def __init__(self, cmd, shellOutput=True,before=[],after=[],pushDir=""):
               self.cmd = cmd
               self.shellOutput = shellOutput
               self.before = before
               self.after  = after
               self.pushDir = pushDir

      def __repr__(self):
          return ("Cmd:\t%s, ShellOutput:\t%s" % (self.cmd,self.shellOutput))


# Process a list of commands
def processCommands(cmdObjs):
    def __processFunccalls__(calls):
        for (func, args, kwargs) in calls:
            func(*args,**kwargs)

    for cmdObj in cmdObjs:
        rcmd = cmdObj.cmd
        if(cmdObj.pushDir!=""):
          rcmd = "pushd " + cmdObj.pushDir + " && pwd && " + cmdObj.cmd + " && popd"
        __processFunccalls__(cmdObj.before)
        if(cmdObj.shellOutput):
            print(rcmd)
        sp.call(rcmd,shell=cmdObj.shellOutput)
        __processFunccalls__(cmdObj.after)

