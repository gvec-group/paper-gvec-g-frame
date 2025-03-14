import os
import glob
import sys

########################################################################################################
def count_and_collect_occurences_in_file( logfilename,searchstr,ignorecase=False): 
  lines=open(logfilename,'r').readlines()
  if(ignorecase):
    foundlines = [ line for line in lines if (searchstr.lower() in line.lower())]
  else:
    foundlines = [ line for line in lines if (searchstr in line)]
  return  foundlines
    
     
  
########################################################################################################

def check_pdflatex_log(texproject,ignore_errors=False):
    '''
    check the logs of a pdflatex run 
    texproject: input of main tex file (without the .tex ending!)
    '''
    logfile=texproject+'.log'
    if not os.path.exists(logfile):
       print('no log file exists with the name: "'+logfile+'"')
       sys.exit(1)
    else:
      warnlines=count_and_collect_occurences_in_file( logfile,"Warning:",ignorecase=False)
      if(len(warnlines) >0):
        print("FOUND WARNINGS:")
        [print(line) for line in warnlines]
        print(("\n FOUND SOME WARNINGS IN %s ...\n ")%logfile)
      errlines=count_and_collect_occurences_in_file( logfile,"Error",ignorecase=False)
      if(len(errlines) >0):
        print("FOUND ERRORS:")
        [print(line) for line in errlines]
        if(ignore_errors):
          print("\n FOUND ERRORS ARE IGNORED!!!\n")
        else:
          print(("ERROR: FOUND ERRORS IN %s !!!")%logfile)
          sys.exit(-1)
      errlines=count_and_collect_occurences_in_file( logfile,"fatal error",ignorecase=True)
      if(len(errlines) >0):
        print("FOUND FATAL ERRORS!")
        [print(line) for line in errlines]
        if(ignore_errors):
          print("\n FATAL ERRORS ARE IGNORED!!!\n")
        else:
          print(("\n ERROR: FOUND FATAL ERRORS IN %s !!!\n")%logfile)
          sys.exit(-1)
      errlines=count_and_collect_occurences_in_file( logfile,"undefined reference",ignorecase=True)
      if(len(errlines) >0):
        print("FOUND UNDEFINED REFERENCES!")
        [print(line) for line in errlines]
        if(ignore_errors):
          print("\n UNDEFINED REFERENCES ARE IGNORED!!!\n")
        else:
          print(("\n ERROR: FOUND UNDEFINED REFERENCES IN %s !!!\n")%logfile)
          sys.exit(-1)
      

########################################################################################################

# MAIN PROGRAM

########################################################################################################
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Latex logfile checker',\
                                    formatter_class=argparse.RawTextHelpFormatter)


    parser.add_argument('-ignore_errors', type=int, default=1, help=' =1: (default) sys.exit(1) if errors are found in logfile. =0: Ignore errors "' )

    parser.add_argument('texproject', type=str,   help='name of the main texfile, without the .tex ending!')
    args = parser.parse_args()
    
    print(args.texproject)
    check_pdflatex_log(args.texproject,(args.ignore_errors==1))
