class EDITOR(object):
    def __init__ (self, name,username,user_id,role):
        self.name=name
        self.osm_username=username
        self.osm_user_id=user_id
        self.role=role
        self.new_changesets=[]
        self.list_entry=None  #stores the correspoding QTreeWidget Item

    def set_changeset_info(self,new_changesets,total_count,misspelled_hashtags,missing_hashtags,spell_count,total_changes,added,modified,deleted):
        self.new_changesets_list=new_changesets
        self.new_changesets_count=total_count
        self.total_misspelled_hashtags=misspelled_hashtags
        self.total_missing_hashtags=missing_hashtags
        self.total_misspelled_comments=spell_count
        self.total_new_changes=total_changes
        self.total_new_additions=added
        self.total_new_modifications=modified
        self.total_new_deleted=deleted

    def display_basic_info(self):
        self.list_entry.setText(0, str(self.name))
        self.list_entry.setText(1, str(self.osm_username))
        self.list_entry.setText(2, str(self.osm_user_id))
        self.list_entry.setText(3, str(self.role))

    def display_changeset_info(self):
        self.list_entry.setText(4, str(self.new_changesets_count))
        self.list_entry.setText(5, str(self.total_new_changes))

        self.list_entry.setText(6, str(self.total_new_additions))
        self.list_entry.setText(7, str(self.total_new_modifications))
        self.list_entry.setText(8, str(self.total_new_deleted))

        self.list_entry.setText(9, str(self.total_misspelled_comments))
        self.list_entry.setText(10, str(self.total_misspelled_hashtags))
        self.list_entry.setText(11, str(self.total_missing_hashtags))

    def updateBasicInfo(self,name,username,user_id,role):
        self.name=name
        self.username=username
        self.user_id=user_id
        self.role=role
        self.list_entry.setText(0, str(self.name))
        self.list_entry.setText(1, str(self.osm_username))
        self.list_entry.setText(2, str(self.osm_user_id))
        self.list_entry.setText(3, str(self.role))      