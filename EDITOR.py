



class EDITOR(object):
    def __init__ (self, name,username,user_id,role):
        self.name=name
        self.osm_username=username
        self.osm_user_id=user_id
        self.role=role
        self.new_changesets=[]
        self.list_entry=None  #stores the correspoding QTreeWidget Item
