class House(object):
    def __init__(self,**kw):
        self.id=kw.get('id',None)
        self.estate_name=kw.get('estate_name',None) #小区名称
        self.proportion=kw.get('proportion',None) #面积
        self.deal_date=kw.get('deal_date',None) #成交日期
        self.deal_price=kw.get('deal_price',None)#成交价格
        self.sell_price=kw.get('sell_price',None)#挂牌价
        self.unit_price=kw.get('unit_price',None)#单价 元/平
        self.deal_cycle=kw.get('deal_cycle',None)#成交周期
        self.house_direction=kw.get('house_direction',None)#房屋朝向
        self.build_date=kw.get('build_date',None)#建成时间
        self.property_right=kw.get('property_right',None)#产权
    


    