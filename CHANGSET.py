

class CHANGESET(object):
    def __init__ (self, id,date_created,changes,date_closed,hashtags,source,comment,added,modified,deleted):
        self.id=id
        self.date_created=date_created
        self.date_closed=date_closed
        self.changes=changes
        self.hashtags=hashtags
        self.source=source
        self.comment=comment
        self.added=added
        self.modified=modified
        self.deleted=deleted
        