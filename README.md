# ABOUT
競馬予想モデル収支計算・予想公開用のWebサイトです。

GitHubに上げている[競馬予想モデル](https://github.com/KHTTakuya/KeibaPrediction)
または自作の競馬予想モデルと併用すること。

使用言語：Python<br>
フレームワーク：Django, Bootstrap

今後はReact.jsとRESTAPIを使用したアプリケーションの開発を行っていく。


# HOW TO USE
setting.pyを開き以下の箇所を修正する。

①SECRET_KEYの設定
```python
from django.core.management.utils import get_random_secret_key
SECRET_KEY = get_random_secret_key()
```

②DATABASEの設定
```python
import os

DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
```

③メールサーバーの設定(任意)
```python
EMAIL_BACKEND = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = ''
```
Gメールなどで作成後User名やパスワードを発行する。

以上設定が完了したら
```commandline
python manage.py runserver
```

と起動する。