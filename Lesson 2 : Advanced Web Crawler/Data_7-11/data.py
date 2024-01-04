import get_data as gd

result = [
    {
        "City": "台北市",
        "CityID": "01"
    },

    {
        "City": "基隆市",
        "CityID": "02"
    },

    {
        "City": "新北市",
        "CityID": "03"
    },

    {
        "City": "桃園市",
        "CityID": "04"
    },

    {
        "City": "新竹市",
        "CityID": "05"
    },

    {
        "City": "新竹縣",
        "CityID": "06"
    },

    {
        "City": "苗栗縣",
        "CityID": "07"
    },

    {
        "City": "台中市",
        "CityID": "08"
    },

    {
        "City": "台中縣",
        "CityID": "09"
    },

    {
        "City": "彰化縣",
        "CityID": "10"
    },

    {
        "City": "南投縣",
        "CityID": "11"
    },

    {
        "City": "雲林縣",
        "CityID": "12"
    },

    {
        "City": "嘉義市",
        "CityID": "13"
    },

    {
        "City": "嘉義縣",
        "CityID": "14"
    },

    {
        "City": "台南市",
        "CityID": "15"
    },

    {
        "City": "台南縣",
        "CityID": "16"
    },

    {
        "City": "高雄市",
        "CityID": "17"
    },

    {
        "City": "高雄縣",
        "CityID": "18"
    },

    {
        "City": "屏東縣",
        "CityID": "19"
    },

    {
        "City": "宜蘭縣",
        "CityID": "20"
    },

    {
        "City": "花蓮縣",
        "CityID": "21"
    },

    {
        "City": "台東縣",
        "CityID": "22"
    },

    {
        "City": "澎湖縣",
        "CityID": "23"
    },

    {
        "City": "連江縣",
        "CityID": "24"
    },

    {
        "City": "金門縣",
        "CityID": "25"
    }
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}


gd.Get_Data(result)
gd.Get_StoreData(result)




