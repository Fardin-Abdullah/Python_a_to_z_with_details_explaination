#Authentication
# when we ccreate any server it is not opened for everyone for this client has to give his introduction and server will test it
# it is called authentication there are many systems to do this among them HTTP BAsic Authentication is best

# have to add this methos in simpleserver class
@classmethod
def set_api_key(cls,username,password):
    #key_str = '{}:{}'.format(username,password):
    cls.key = base64.b64encode(key_str.encode()).decode()
    key_str = f'{username}:{password}'
# here we madea a key by encripting username and password and also have to import base64 module