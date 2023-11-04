from sqlalchemy import Integer, Column, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from Backend_ATTT.pythonProject.BanVeMayBay import db, app


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
    __tablename__ = 'ChuyenBay'
    MaCB = Column(String(20), primary_key=True)
    tenCB = Column(String(25), nullable=False)
    GaDi = Column(String(30), nullable=False)
    GaDen = Column(String(30), nullable=False)
    GiaVe = Column(Float, nullable=False)
    SoLuongCho = Column(Integer, nullable=False)  # hôm nay bán 30 vé vs cb VN102


class VeMayBay(db.Model):
    MaVe = Column(String(20), primary_key=True)
    NgDat = Column(DateTime, nullable=False)
    SoGhe = Column(Integer, nullable=False, unique=True)
    SoCua = Column(Integer, nullable=False)
    TinhTrangVe = Column(Boolean, nullable=False)


class PhieuThanhToan(db.Model):
    MaThanhToan = Column(String(20), primary_key=True)
    SoLuongVeDat = Column(Integer, nullable=False)
    ThanhTien = Column(Float, nullable=False)
    NgLapThanhToan = Column(DateTime, nullable=False)
    NgHetHanThanhToan = Column(DateTime, nullable=False)


class KhachHang(db.Model):
    MaKH = Column(String(20), primary_key=True)
    CCCD = Column(String(12), nullable=False, unique=True)
    GioiTinh = Column(Boolean, nullable=False)
    HoTen = Column(String(30), nullable=False)
    SDT = Column(String(15), unique=True)
    NgSinh = Column(DateTime, nullable=False)


class TaiKhoanThanhToan(db.Model):
    SoTK = Column(String(20), primary_key=True)
    TenNganHang = Column(String(50), nullable=True)
    Loai = Column(String(30), nullable=False)


class PhieuDatCho(db.Model):
    MaPhieu = Column(String(20), primary_key=True)
    LoaiVe = Column(String(20), nullable=False)
    NgMua = Column(DateTime, nullable=False)
    TrangThai = Column(String(20), nullable=False)


class DaiLy(db.Model):
    MaDaiLy = Column(String(20), primary_key=True)
    Ten = Column(String(20), nullable=False)


class TaiKhoanDaiLy(db.Model):
    TenTK = Column(String(30), nullable=False)
    MatKhau = Column(String(30), nullable=False)
# class Lichbay(db.Model):
#     pass
#
# class MayBay():
#     pass
