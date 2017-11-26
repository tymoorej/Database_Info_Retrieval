import bsddb3,sys,re

def parseQuery(query):
    numeric="[0-9]"
    alphanumeric="[0-9a-zA-Z]"

    term=alphanumeric + "+"
    termPrefix="(title|author|other):"
    termQuery="({})?{}".format(termPrefix,term)

    year=numeric + "+"
    yearPrefix="(year:|year>|year<)"
    yearQuery="{}{}".format(yearPrefix,year)

    phrase="{}(\\s{})*".format(term,term)
    phraseQuery='({})?"{}"'.format(termPrefix,phrase)

    expression="({}|{}|{})".format(yearQuery,termQuery,phraseQuery)
    querySearch="^{}(\\s{})*$".format(expression,expression)


    # y=re.compile(yearQuery)
    # t=re.compile(termQuery)
    # p=re.compile(phraseQuery)
    #

    if re.match(querySearch,query):
        print("\ncorrect query\n")
        
        it = re.finditer(expression, query)
        for m in it:
        		exp=query[m.start():m.end()]
        		if re.match(yearQuery,exp):
					parseYear(exp)
					return
					
				if re.match(termQuery,exp):
					parseQuery(exp)
					return
					
				if re.match(termQuery,exp):
					parsePhrase(exp)
					return
      
            
    else:
        print("\nincorrect query\n")

	
	
def parseYear(exp):
	pass

def parseQuery(exp):
	pass

def parsePhrase(exp):
	pass

def yearGreaterThan(year):
    pass

def yearLessThan(year):
    pass

def yearEqualTo(year):
    pass

def titeEqualTo(title):
    pass

def authorEqualTo(author):
    pass

def otherEqualTo(other):
    pass

def joinQueries():
    pass


def main():
    for line in sys.stdin:
        parseQuery(line)

if __name__ == '__main__':
    main()
