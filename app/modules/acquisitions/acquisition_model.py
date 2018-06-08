from core.ndb import BasicModel
from google.appengine.ext import ndb

class AcquisitionModel (BasicModel):
    acquisition_id = ndb.StringProperty()
    isbn = ndb.StringProperty(indexed=True, required=True)
    title = ndb.StringProperty(required=True)
    other_title = ndb.StringProperty()
    author = ndb.StringProperty()
    other_author = ndb.StringProperty()
    publisher = ndb.StringProperty()
    edition = ndb.StringProperty()
    publication_year = ndb.StringProperty()
    category = ndb.StringProperty()
    description = ndb.StringProperty()
    abstract = ndb.StringProperty()
    #front end fields

    unit_price = ndb.FloatProperty(default=0.0)
    quantity = ndb.IntegerProperty()
    total_price= ndb.FloatProperty()
    discount = ndb.


    is_deleted = ndb.BooleanProperty(default=False, indexed=True)



    # {
    #
    #
    #
    # `Total_Price`
    # double(10, 2)
    # DEFAULT
    # '0.00',
    # `Discount`
    # double(10, 2)
    # DEFAULT
    # '0.00',
    # `Discount_amount`
    # double(10, 2)
    # DEFAULT
    # '0.00',
    # `Net_Price`
    # double(10, 2)
    # DEFAULT
    # '0.00',
    # `Recommended`
    # varchar(45)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `Dept`
    # varchar(50)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `MType`
    # varchar(50)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `Mode`
    # varchar(40)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `Status`
    # varchar(30)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `Dealer`
    # varchar(80)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `WhereIs`
    # varchar(45)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `Da_te`
    # datetime
    # DEFAULT
    # NULL,
    # `Remarks`
    # varchar(100)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `Edition`
    # varchar(45)
    # CHARACTER
    # SET
    # latin1
    # DEFAULT
    # NULL,
    # `ID`
    # float
    # NOT
    # NULL
    # AUTO_INCREMENT,
    # PRIMARY
    # KEY(`ID`)
    # }