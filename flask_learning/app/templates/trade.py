class Trade_info:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.parse(goods)

    def parse(self,goods):
        self.total = len(goods)
        self.trades = [self.map_to_trade(single) for single in goods]

    def map_to_trade(self,single):
        if single.creaet_datetime:
            time = single.creaet_datetime.strftime('%Y-%m-%d')
        else:
            time = 'Unkonwn'
        return dict(
            user_name = single.user.nickname,
            time = time,
            id = single.id
        )

