#!/usr/bin/python
import subprocess as sp
import re #regexpr
import fileinput
import itertools as it
#import pandocfilters as pf



class lineObj(object):
      __slots__ = ('lno', 'linecount','line')
      def __init__(self, lno, linecount, line):
               self.lno = lno
               self.linecount = linecount
               self.line = line

      def __repr__(self):
          return ("Line:\t%d/%d, \"%s\"" % (self.lno,self.linecount,self.line))


def applyOnFile(inputgenlist, fname):
    count = sum( (1 for line in open(fname).readlines(  )) )

    def finputgenerator(finput):
        for (ln,lc,l) in zip(range(1,count+1),it.repeat(count,count),finput):
            #print((ln,lc,l))
            yield lineObj(ln,lc,l)
            #yield (ln,lc,l)

    def flowController(filter):
        lastl = 0
        incr  = 0
        for lobj in filter:
            if(lobj.lno==lastl):
                incr += 1
            lastl=lobj.lno
            lobj.lno 		+= incr
            lobj.linecount      += incr
            yield lobj


    finput =fileinput.input(fname,inplace=True)
    processor = finputgenerator(finput)
    #processor = finputgenerator(fileinput.input(fname))
    for gen in inputgenlist:
        processor = gen(flowController(processor))
    #for (ln,lc,l) in processor:
    for lobj  in processor:
        if(lobj.line!=None):
            print(lobj.line,end='')

    finput.close()

def centerFigureFilter(inputgen):
    lcincr = 0
    for lobj in inputgen:
        lobj.linecount +=lcincr
        lobj.lno       +=lcincr
        yield lobj
        if(lobj.line):
            if(lobj.line.startswith("\\begin{figure}") ):
                lobj.line = "\\centering"
                yield lobj


def adjustLongtableFilter(inputgen):
    #for (ln,lc,l) in inputgen:
    for lobj in inputgen:
        if(lobj.line!=None):
            lobj.line=re.sub(r'(\\begin){longtable}(\[c\]){@{}([lrc]*)@{}}',
                    r'\1{longtable}\2{\3}',lobj.line)
        #yield (ln,lc,l)
        yield lobj



class cmdObj(object):
      __slots__ = ('cmd', 'shellOutput','before','after')
      def __init__(self, cmd, shellOutput=True,before=[],after=[]):
               self.cmd = cmd
               self.shellOutput = shellOutput
               self.before = before
               self.after  = after

      def __repr__(self):
          return ("Cmd:\t%s, ShellOutput:\t%s" % (self.cmd,self.shellOutput))


def processCommands(cmdObjs):
    def __processFunccalls__(calls):
        for (func, args, kwargs) in calls:
            func(*args,**kwargs)

    for cmdObj in cmdObjs:
        __processFunccalls__(cmdObj.before)
        if(cmdObj.shellOutput):
            print(cmdObj.cmd)
        sp.call(cmdObj.cmd,shell=cmdObj.shellOutput)
        __processFunccalls__(cmdObj.after)

