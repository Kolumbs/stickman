from subprocess import run,PIPE
class Git():
	'''
	Allows to make calls to git through subprocess
	'''
	def __init__(self,path):
		self.path=path
	
	def status(self):
		'''Gives out message fo git status command'''
		print(self.rungit('status'))

	def pull(self):
		'''
		Pulls from git repo, if returncode not 0 raises exception
		'''
		return self.rungit('pull')

	def commit(self,message,single=False):
		'''
		Commits all files with message as commit message, unless single given, then only that given file
		'''
		self.pull()
		if single: 
			addfile=self.path + 'hansa/' + single
		else:
			addfile='-A'
		self.rungit('add',addfile)
		self.rungit('commit','-m',message)
		self.rungit('push')

	def lastCommit(self):
		self.pull()
		author=self.rungit('log','-n','1')
		author=author.split('\n')
		return author[1]	
		
	def rungit(self,*pargs):
		args=['git','-C',self.path]
		for arg in pargs:
			args.append(arg)
		self.lastrun=run(args,capture_output=True)
		if not self.lastrun.returncode==0:
			raise Exception(self.lastrun.stderr.decode())
		return self.lastrun.stdout.decode()
				
