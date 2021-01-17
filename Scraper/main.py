from DBConnector import DBConnector

#rss scraper for diferent feeds
import globalnews_rss
import bbc_business
import bbc_education
import bbc_entertainment
import bbc_health
import bbc_politics
import bbc_science
import bbc_technology
import ctv_business
import ctv_canada
import ctv_entertainment
import ctv_health
import ctv_lifestyle
import ctv_politics
import ctv_politics
import ctv_science_tech
import ctv_sports
import ctv_world

database = DBConnector()

globalnews_rss.globalnews_rss(database)

bbc_business.bbcnews_business(database)
bbc_education.bbcnews_education(database)
bbc_entertainment.bbcnews_entertainment(database)
bbc_health.bbcnews_health(database)
bbc_politics.bbcnews_politics(database)
bbc_science.bbcnews_science(database)
bbc_technology.bbcnews_technology(database)


ctv_canada.ctvnews_canada(database)
ctv_entertainment.ctvnews_entertainment(database)
ctv_health.ctvnews_health(database)
ctv_lifestyle.ctvnews_lifestyle(database)
ctv_politics.ctvnews_politics(database)
ctv_science_tech.ctvnews_science_tech(database)
ctv_sports.ctvnews_sports(database)
ctv_business.ctvnews_business(database)
ctv_world.ctvnews_world(database)






