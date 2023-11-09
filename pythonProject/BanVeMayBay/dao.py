from pythonProject.BanVeMayBay.models import (ChuyenBay, VeMayBay
, PhieuDatCho, PhieuThanhToan, User)

def load_Chuyenbay():
    pass

def load_VeMayBay():
    pass

def load_PhieuDatCho():
    pass

def load_PhieuThanhToan():
    pass
def get_user_by_id(user_id):
    return User.query.get(user_id)
