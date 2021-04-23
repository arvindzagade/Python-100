import sharepy


session = sharepy.connect("https://example.sharepoint.com",username="######",password="#####")

class Share:
    def download_first():
        try:
            r = session.getfile("Sharepoint Location/Filename.extention")
              
        except Exception as e:
            print('Error Occured:'+'e')
            
            
    def download_second():
        
        try:
            r = session.getfile("Sharepoint Location/Filename.extention")
            session.save()
        except Exception as e:
            print('Error Occured:'+'e')
            
    def download_third():
        try:
            r = session.getfile("Sharepoint Location/Filename.extention")
            session.save()
        except Exception as e:
            print('Error Occured:'+'e')
            

if _name_ == "_main_":
    down_one = Share.download_first()
    down_two = Share.download_second()
    down_three = Share.download_third()
