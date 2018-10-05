# PyDjango <br/>
Python 3.7<br/>
Django 2.1.1<br/><br/>
### heroku <br/>
網頁: https://goo.gl/9gdQsM<br/>

***

台灣銀行匯率API: https://goo.gl/fjzpbG<br/>

<br/>
### API 回傳參數
<p> { <br/>
    "cn": "美金",  幣別中文 <br/>
    "en": "USD",   幣別英文 <br/>
    "cash_buying": "30.34",  銀行現金買入 <br/>
    "cash_selling": "31.03",  銀行現今賣出 <br/>
    "spot_buying": "30.71",  銀行即期買入 <br/>
    "spot_selling": "30.81",  銀行即期賣出 <br/>
    "bank_id": 2  銀行id <br/>
} </p>

### res:

| Key | 類型 | 描述 |   
| :-------------: | :-------------: | :-------------: |
| bank_id | int | 銀行id | 
| bank_name | str | 銀行名稱 |
| bank_code | str | 銀行代碼 |
| update_at | str | 匯率更新時間 |
| data      | list | 匯率 |

### data Info:

| Key | 類型 | 描述 |
| :-------------: | :-------------: | :-------------: |
| cn | str | 貨幣中文 |
| en | str | 貨幣英文 |
| cash_buying | str | 銀行現金買入 |
| cash_selling | str | 銀行現金賣出 |
| spot_buying | str | 銀行即期買入 |
| spot_selling | str | 銀行即期賣出 |


### 銀行列表API <br/>
https://goo.gl/9HFsYH <br/>


| Key | 類型 | 描述 |
| :-------------: | :-------------: | :-------------: |
| id | int | 銀行ID |
| name | str | 銀行名稱 |
| code | str | 銀行代碼 |
