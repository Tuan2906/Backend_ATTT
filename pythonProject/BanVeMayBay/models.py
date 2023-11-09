from flask_login import UserMixin
from sqlalchemy import Integer, Column, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from pythonProject.BanVeMayBay import db, app


# doi vs 1 N thi ben phia ben co 1 se thiet lap relationship con phia ben N se thiet lap khoa ngoai
# doi VS N N thi thu nhat phai khai bao trung gian ten_dat= db.Table('ten_bang', Colunm('ten_id',interger,ForeginKey('ten.id'),primary_key=true),
# Colum(tuong tu))
# thu 2 la phai relationship 2 bang vd thuoctinh=reklationship('tenbangthu2', secondary='ten_bang', lazy=subquery,backref=
# bacref('tenbangthu1',lazy=true)-> cai nay khai bao trong  bang 1  voi 1 thuoc tinh o 2 bang  relationship vs nhau
# trong backref dung de relatipnship cho bang 2

# lazy= true la no khong lay thang co quan he tru khi tac dong len thi se lay, false lay, subquwey lay nhung ma roi rac
# inset du lieu VD p=tenclass(tenthuoctinh='',...)
# db.session.add(p)
# db.session.commit()
# b1: thuc hien truy van trong cmd from BanVeMay.models import *
# b2: p= Tenclass.query.get(tencantim)
# de xem kq truy van thi p.__dict__
# t1=tentt.query.get(dulieucantim)
# doi voi do du lieu vao bang trung gian thi p.thuoctinh.append(t1)
# Sau do from Banvemaybay import db, db.session.add(p), db.session.commit()
# class Emloyee(db.Model):
#     __tablenam__= 'SinhVien'
#     stt = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(20), nullable=False)

class ChuyenBay(db.Model):
    MaCB = Column(Integer, primary_key=True)
    tenCB = Column(String(25), nullable=False)
    GaDi = Column(String(30), nullable=False)
    GaDen = Column(String(30), nullable=False)
    GiaVe = Column(Float, nullable=False)
    SoLuongCho = Column(Integer, nullable=False)
    cb_lb = relationship("CB_LB", backref="ChuyenBay")
    vemaybay = relationship("VeMayBay", backref="ChuyenBay", lazy=True)


class LichBay(db.Model):
    MaLichBay = Column(Integer, primary_key=True, autoincrement=True)
    GioDi = Column(DateTime, nullable=False)
    GioVe = Column(DateTime, nullable=False)
    cb_lb = relationship("CB_LB", backref="LichBay")


class CB_LB(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    chuyenbay_id = Column(Integer, ForeignKey(ChuyenBay.MaCB))
    lichbay_id = Column(Integer, ForeignKey(LichBay.MaLichBay))


class KhachHang(db.Model):
    MaKH = Column(Integer, primary_key=True)
    CCCD = Column(String(12), nullable=False, unique=True)
    GioiTinh = Column(Boolean, nullable=False)
    HoTen = Column(String(30), nullable=False)
    SDT = Column(String(15), unique=True)
    NgSinh = Column(DateTime, nullable=False)
    vemaybay = relationship("VeMayBay", backref="KhachHang", lazy=True)
    taikhoanthanhtoan = relationship("TaiKhoanThanhToan", backref="KhachHang", lazy=True)


class PhieuThanhToan(db.Model):
    MaThanhToan = Column(Integer, primary_key=True)
    SoLuongVeDat = Column(Integer, nullable=False)
    ThanhTien = Column(Float, nullable=False)
    NgLapThanhToan = Column(DateTime, nullable=False)
    NgHetHanThanhToan = Column(DateTime, nullable=False)
    vemaybay = relationship("VeMayBay", backref="PhieuThanhToan", lazy=True)


class TaiKhoanThanhToan(db.Model):
    SoTK = Column(Integer, primary_key=True)
    TenNganHang = Column(String(50), nullable=True)
    Loai = Column(String(30), nullable=False)
    khachhang_id = Column(Integer, ForeignKey(KhachHang.MaKH), nullable=False)


class VeMayBay(db.Model):
    MaVe = Column(Integer, primary_key=True)
    NgDat = Column(DateTime, nullable=False)
    SoGhe = Column(Integer, nullable=False, unique=True)
    SoCua = Column(Integer, nullable=False)
    TinhTrangVe = Column(Boolean, nullable=False)
    chuyenbay_id = Column(Integer, ForeignKey(ChuyenBay.MaCB), nullable=False)
    khachhang_id = Column(Integer, ForeignKey(KhachHang.MaKH), nullable=False)
    phieuthanhtoan_id = Column(Integer, ForeignKey(PhieuThanhToan.MaThanhToan), nullable=False)
    # ve_datcho = relationship(" Ve_DatCho", backref="VeMayBay")


class PhieuDatCho(db.Model):
    MaPhieu = Column(Integer, primary_key=True)
    LoaiVe = Column(String(20), nullable=False)
    NgMua = Column(DateTime, nullable=False)
    TrangThai = Column(String(20), nullable=False)
    ve_datcho = relationship("Ve_DatCho", backref="PhieuDatCho",lazy=True)


class Ve_DatCho(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    vemaybay_id = Column(Integer, ForeignKey(VeMayBay.MaVe))
    phieudatcho_id = Column(Integer, ForeignKey(PhieuDatCho.MaPhieu),nullable=False)


class DaiLy(db.Model):
    MaDaiLy = Column(Integer, primary_key=True)
    Ten = Column(String(20), nullable=False)
    taikhoandaily = relationship("TaiKhoanDaiLy", backref="Daily", uselist=False)


class TaiKhoanDaiLy(db.Model):
    TK_DaiLy_ID = Column(Integer, primary_key=True, autoincrement=True)
    TenTK = Column(String(30), nullable=False)
    MatKhau = Column(String(30), nullable=False)
    daily_id = Column(Integer, ForeignKey(DaiLy.MaDaiLy), nullable=False)


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        # u = User(name='Admin', username='admin', password=str(12345))
        # db.session.add(u)
        # db.session.commit()

