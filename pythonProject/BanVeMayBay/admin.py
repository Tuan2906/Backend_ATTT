from flask_admin import BaseView, expose

from pythonProject.BanVeMayBay import admin, db
from pythonProject.BanVeMayBay.models import ChuyenBay
from flask_admin.contrib.sqla import ModelView


class View_Chuyen_Bay(ModelView):
    column_labels = {
        'MaCB': 'Mã chuyến bay',
        'tenCB': 'Máy Bay',
        'GaDi': 'Ga đi',
        'GaDen': 'Ga đến',
        'GiaVe': 'Giá vé',
        'SoLuongCho': 'Số lượng chổ'
    }
    can_view_details = True
    form_columns = ['MaCB', 'tenCB', 'GaDi', 'GaDen', 'GiaVe', 'SoLuongCho']


admin.add_view(View_Chuyen_Bay(ChuyenBay, db.session, name='Chuyến bay'))


# admin.add_view(ModelView(Lichbay,db.session))
# admin.add_view(ModelView(MayBay,db.session))
class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

class CongraView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/congratulation.html')

admin.add_view(StatsView(name='Thống kê báo cáo'))







