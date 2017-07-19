# Global Variables
class Accounts:
    ZAP_API_IP = '0.0.0.0'
    ZAP_API_PORT = '8080'
    ZAP_API_KEY = '0123456789'

    def __init__(self):
        print ("Accounts loaded")

    ## Admin Email and password for CMS Testing
    admin_url = '/'
    admin_dict = {
        'https://dev.example.com': 'https://dev.example.com/admin',
        'https://test.example.com': 'https://test.example.com/admin',
        'https://staging.example.com': 'https://staging.example.com/admin',
        'https://www.example.com': 'https://www.example.com/admin',
    }

    api_key = 'ENTER_KEY_HERE'

    super_admin_email = 'super@email.com'

    admin_email = 'admin@email.com'
    admin_password = ''
    admin_name = 'Admin'

    editor_email = 'editor@email.com'
    editor_password = ''
    editor_name = 'Editor'

    moderator_email = 'moderator@email.com'
    moderator_password = ''
    moderator_name = 'Moderator'

    normal_user_email = 'user@email.com'
    normal_user_password = ''
    normal_user_name = 'User'
