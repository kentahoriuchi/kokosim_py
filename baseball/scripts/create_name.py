from random import choice


def create_player_name():
    surnames = ["鈴木", "田中", "佐藤", "山田", "加藤", "吉田", "木村", "林", "清水", "山口", "高橋", "斉藤", "小林",
                "後藤", "坂本", "中村", "池田", "森", "岡田", "松本", "近藤", "遠藤", "長谷川", "藤田", "太田", "井上",
                "石川", "福田", "三浦", "内田", "渡辺", "増田", "小川", "西田", "森田", "平野", "大野", "野口", "松田",
                "菅原", "阿部", "石井", "橋本", "宮崎", "白井", "長田", "中島", "河野", "竹内", "堀田", "須藤", "宮本",
                "谷口", "長尾", "藤井", "菊地", "川口", "小田", "松井", "市川", "横山", "上田", "藤原", "永井", "柴田",
                "中野", "原田", "秋元", "岡本", "広瀬", "北村", "杉山", "阿久津", "平田", "岩本", "今井", "篠原",
                "大西", "谷田", "浜田", "松下", "矢野", "大塚", "中田", "中西", "荒木", "川上", "片山", "田辺", "安藤",
                "千葉", "島田", "沢田", "西山", "川崎", "森本", "福島", "石田", "浅田", "大田", "和田", "高木", "辻",
                "村上", "吉野", "新井", "河合", "金子", "本田", "西川", "渡部", "森山", "大谷", "栗原", "大久保",
                "岸本", "細川", "樋口", "小西", "田村", "後藤", "堀内"]

    givennames = ["湊", "陽斗", "雄太", "拓也", "悠介", "優太", "健太", "大翔", "翔太", "颯太", "太一", "亮介",
                  "真太郎", "大輔", "智洋", "健斗", "翼", "航大", "瑛太", "翔真", "陽菜", "陽向", "瞬", "大和", "和真",
                  "健志", "雄大", "海斗", "未来", "裕太", "翔馬", "大地", "大志", "翔陽", "優樹", "翔希", "陽樹",
                  "太志", "大貴", "翔瑛", "大輝", "陽平", "智大", "瑛志", "太陽", "慧太", "悠斗", "大城", "慎也",
                  "瑛人", "良太", "大磨", "海人", "大空", "健一", "翔太朗", "翔希", "翔平", "大翼",
                  "誠", "大介", "直樹", "雄一", "浩二", "良太", "和真", "俊介", "慎太郎", "拓朗", "隼人", "智也",
                  "裕太郎", "健太朗", "颯太朗", "翼太朗", "大樹", "智大", "翔太郎", "翔希", "大翼", "悠太朗", "瑛太郎",
                  "謙介", "陽太朗", "健一", "浩史", "大志", "裕斗", "智哉", "翔太朗", "太陽", "慎也", "裕太", "拓也",
                  "智久", "翔平", "大輝", "健志", "陽介", "智裕", "拓哉", "大地", "大空", "慎太郎", "陽翔", "健次",
                  "大貴", "翔太郎", "翔真", "浩平", "和真", "健太郎", "瑛太", "大仁", "謙太朗", "翔太", "浩二郎", "悠太"]

    return choice(surnames) + " " + choice(givennames)

def create_team_name():
    areanames = ["札幌", "旭川", "函館", "釧路", "帯広", "室蘭", "盛岡", "仙台", "秋田", "山形", "福島", "水戸",
                 "宇都宮", "前橋", "さいたま", "千葉", "横浜", "川崎", "新潟", "長野", "岐阜", "静岡", "名古屋"]

    prefacturename = ["", "第一", "第二", "第三", "商業", "工業", "農業", "農林水産", "水産", "大付属", "実業",
                      "東", "西", "南", "北", "学院"]

    return choice(areanames) + choice(prefacturename) + "高校"
