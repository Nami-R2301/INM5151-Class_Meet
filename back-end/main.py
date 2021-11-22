import Database 

#create object Etudiant that can go in Db
jules = Database.etudiant(username='jules',email='youle21' , password='xxx')
#print( repr(jules) )

# Need to add and commit to save it in Db
Database.db.session.add(jules)
Database.db.session.commit()
