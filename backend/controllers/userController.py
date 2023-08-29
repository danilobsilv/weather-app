from backend.models.userModel import UserModel 


class UserController:
      def __init__(self):
            self.user_model = UserModel()
            

      def checkUserEmail(self, email):
            try:
                  email_db = self.user_model.get_user_by_email(email)
                  if isinstance(email_db, tuple):
                        email_db = email_db[0]

                        if email_db == email: return True
                        
                        else: return False
                              
                  return email_db
                
            except:
                  pass

      def checkUserPassword(self, password):
            pass




 