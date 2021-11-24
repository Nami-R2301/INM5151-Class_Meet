import Database


def ajout_utilisateur( username_, psw_, email_ ):
   n = Database.Etudiant( username=username_, password=psw_, email=email_) 
   Database.db.session.add(n)
   Database.db.session.commit()
