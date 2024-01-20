# yamiboSign

yamiboSignは、テスト目的でWebアプリケーションを自動化するためにSelenium WebDriverを使用しています。設定は`config.ini`ファイルから読み取り、機密データには環境変数を使用します。

## はじめに

以下の手順に従って、開発とテストのためにローカルマシンでプロジェクトのコピーを稼働させる方法を説明します。

### 前提条件

- Python 3.6以上
- Selenium WebDriver
- ChromeDriver

### インストール

1. リポジトリをクローンします
```bash
git clone https://github.com/yourusername/yamiboSign.git
```

2. 依存関係をインストールします
```bash
pip install -r requirements.txt
```

3. 環境変数を設定します
```bash
export USERNAME=yourusername
export PASSWORD=yourpassword
```

4. スクリプトを実行します
```bash
python main.py
```

### 設定
`config.ini`ファイルには、スクリプトが使用するURLとCSSセレクタが含まれています。このファイルを自分のニーズに合わせて変更することができます。

### 機能
スクリプトは提供されたユーザ名とパスワードを使用してウェブサイトにログインし、サインインアクションを実行します。