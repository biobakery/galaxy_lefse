from galaxy import datatypes,model
import sys,string,time


def timenow():
    """return current time as a string
    """
    return time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(time.time()))

def get_opt(data):
	return [('r','r',False),('c','c',False)]

def red(st,l):
	if len(st) <= l: return st 
	l1,l2 = l/2,l/2
	return st[:l1]+".."+st[len(st)-l2:]

def get_row_names(data,t):
	if data == "": return []
	max_len =38                 
	fname = data.dataset.file_name
	opt = []
	rc = ''
#	lines = [(red(v.split()[0],max_len),'%s' % str(v.split()[0]),False) for i,v in enumerate(open(fname))]
	if t == 'b': lines = [(red(v.split()[0],max_len),'%d' % (i+1),False) for i,v in enumerate(open(fname)) if len(v.split()) > 3 ] 
	else: lines = [(red(v.split()[0],max_len),'%d' % (i+1),False) for i,v in enumerate(open(fname))]
	return sorted(opt+lines)

def get_cols(data,t,c):
	if data == "": return []
	max_len =32 
	fname = data.dataset.file_name
	opt = []
	if c != 'cl':
		opt.append(('no '+c,'%d' % -1,False))
	if t == 'c': 
		rc = ''
		lines = [(red((rc+"#"+str(i+1)+":"+v[0]),max_len),'%d' % (i+1),False) for i,v in enumerate(zip(*[line.split() for line in open(fname)]))]
	else:
		rc = ''
		lines = [(red((rc+"#"+str(i+1)+":"+v.split()[0]),max_len),'%d' % (i+1),False) for i,v in enumerate(open(fname))]
	return opt+lines

"""
def get_phecols(i,addNone,hint):
   hint = hint.lower()
   fname = i.dataset.file_name
   try:
        f = open(fname,'r')
   except:
        return [('get_phecols unable to open file "%s"' % fname,'None',False),]
   header = f.next()
   h = header.strip().split()
   dat = [(x,'%d' % i,False) for i,x in enumerate(h)]
   matches = [i for i,x in enumerate(h) if x.lower().find(hint) <> -1]
   if len(matches) > 0:
       sel = matches[0]
       dat[sel] = (dat[sel][0],dat[sel][1],True)
   if addNone:
        dat.insert(0,('None - no Manhattan plot','0', False ))
   return dat
"""


"""
def exec_after_process(app, inp_data, out_data, param_dict, tool, stdout, stderr):
    outfile = 'out_html'
    job_name = param_dict.get( 'name', 'Manhattan QQ plots' )
    killme = string.punctuation + string.whitespace
    trantab = string.maketrans(killme,'_'*len(killme))
    newname = '%s.html' % job_name.translate(trantab)
    data = out_data[outfile]
    data.name = newname
    data.info='%s run at %s' % (job_name,timenow())
    out_data[outfile] = data
    app.model.context.flush()
"""
