from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dateutil.parser import parse

cluster = None
session = None

class DBConnector:

	# connects to the database
	def connect(self):
		global cluster, session

			# set up the connection to DataStax Astra
		cloud_config= {
				'secure_connect_bundle': 'secure-connect-hackathon.zip'
		}
		auth_provider = PlainTextAuthProvider('dataMan', 'hackathon')
		# provides access to the data cluster
		cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
		# provides access into the keyspaces
		session = cluster.connect()


	# ensure that the database tables are created
	def createTables(self):
		# pick the keyspace
		session.set_keyspace("articles")
		# make sure the article database table exists
		articleTable = """CREATE TABLE IF NOT EXISTS article_info (
							title text,
							link text,
							pubdate timestamp,
							category list<text>,
							description text,
							id int,
							source text,
							PRIMARY KEY (link)
						) ;"""
		row = session.execute(articleTable).one()

		idTable = """CREATE TABLE IF NOT EXISTS id_info (
							varName text,
							maxID int,
							PRIMARY KEY (varName)
						);"""
		row = session.execute(idTable).one()


	# push an article into the database
	def uploadArticle(self, title=None, link=None, pubDate=None, category=None, description=None, source=None):
		title = title.replace("'","''")
		link = link.replace("'","''")
		description = description.replace("'","''")
		time = parse(pubDate)

		for i, word in enumerate(category):
			category[i] = word.replace("'","''")
			category[i] = "'"+category[i].lower()+"'"
		tags = "[" + ", ".join([string.replace('"', "'") for string in category]) + "]"
		
		# get the id if the last article and make an ID for this article
		rows = session.execute('SELECT maxID FROM articles.id_info')
		articleID = rows[0].maxid + 1
		# upload the article
		uploadCommand = "INSERT INTO articles.article_info (title, link, pubdate, category, description, source, id) VALUES ('{}','{}','{}',{},'{}','{}',{});".format(title, link, time, tags, description, source, articleID)
		#print(uploadCommand)
		info = session.execute(uploadCommand).all()
		if info != []:
			print("ERROR uploading:" + info )
		# increment the current max ID
		session.execute("INSERT INTO articles.id_info (maxID,varName) VALUES ({}, 'ID')".format(articleID) ).all()
		

	def getByCategory(self, category, date = None):
		# available World, Business, Politics, Health, Education, Science, Technology, Entertainment, Sports, Lifestyle, Canada
		category = category.lower()
		rows = session.execute("SELECT * FROM articles.article_info where category contains '{}' ALLOW FILTERING;".format(category))
		
		if(date == None):
			date = parse("1000-01-01")
		else:
			date = parse(date)
		rows = session.execute("SELECT * FROM articles.article_info where category contains '{}' AND pubdate >= '{}' ALLOW FILTERING;".format(category, date))
		# to access data, so something like
		# for data in rows:
		# 	data.id, data.category, data.description, data.link, data.pubdate, data.source
		return rows

	
	def __init__(self):
			self.connect()

			#session.set_keyspace("articles")
			#session.execute("DROP TABLE IF EXISTS article_info;")
			#session.execute("DROP TABLE IF EXISTS id_info;")


			self.createTables()

			#session.execute("INSERT INTO articles.id_info (maxID,varName) VALUES (0,'ID')")

			






