import sharepy

def download():
    try:

        s = sharepy.connect("https://yourorganization.sharepoint.com",username="####", password="#####")
        
        #r = s.get("https://rbcom.sharepoint.com/:f:/r/sites/auspodc/hh/IS/Smart%20Promo%20Lite")
        
        
        r = s.getfile("sharepoint link/file.extention(csv,xlsx)")
                      
        
        s.save()
        
        
        
        
    except Exception as e:
        print('Error Occured:'+'e')
        



if _name_ == "_main_":
    download()
