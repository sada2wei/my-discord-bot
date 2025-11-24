# Discord Online Notifier Bot (Koyeb 用)

この Bot は Discord サーバー内のユーザーがオンラインになった際に、  
自分自身の DM に通知する Bot です。

## 機能

- サーバー内全ユーザーのオンラインを監視
- 通知は自分の個人 DM のみ
- 24時間稼働可能（Koyeb デプロイ）

## セットアップ手順

### 1. GitHub リポジトリにアップロード
- `main.py` と `requirements.txt` をルートに配置
- `README.md` は任意

### 2. Koyeb で新規サービス作成
1. [Koyeb](https://www.koyeb.com/) にログイン
2. 「Create Service」→「GitHub」→リポジトリを選択
3. Build command：空欄
4. Run command：`python main.py`

### 3. Environment Variables 設定
| Key | Value |
|-----|-------|
| TOKEN | Discord Bot の Token |
| NOTIFY_USER_ID | 自分の Discord ID |

### 4. Deploy
- Deploy を実行すると自動で Bot が起動
- 24時間稼働可能

## 注意
- Bot と監視対象ユーザーは同じサーバーにいる必要があります
- Presence Intent と Server Members Intent は Discord Developer Portal で有効にしてください
