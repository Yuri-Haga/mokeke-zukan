# モケケ図鑑

持っているご当地モケケと、まだ持っていないモケケを都道府県ごとに見られる個人用の図鑑です。

公開ページ: https://yuri-haga.github.io/mokeke-zukan/

iPhone では Safari で開いて、共有ボタンから「ホーム画面に追加」するとアプリのように開けます。
地域のボタン（例: 大阪 9/20）で絞り込み、「持ってる／まだ」で切り替え。検索はひらがな・カタカナ・漢字・ローマ字（osaka, takoyaki など）で探せます。

## モケケを1体追加するとき

1. 写真を整える（向き直し・縦長・EXIF/GPS 削除）

   ```
   python3 tools/add_photo.py 元写真.jpg photos/takoyaki-shiro.jpg --rotate 90
   ```

   横向きなら `--rotate 90`（時計回り）や `270`。切り抜きたいときは `--crop 0.2,0.05,0.8,0.95`。

2. `data.json` の `items` から該当のモケケを探して、次のように書き換える

   ```json
   "owned": true,
   "photo": "photos/takoyaki-shiro.jpg"
   ```

   一覧にいない子は、`items` の最後に追加します（`id` は重ならなければ何でも OK）。

   ```json
   { "id": "u010", "pref": "大阪", "area": "", "name": "なまえ", "owned": true,
     "photo": "photos/namae.jpg", "unlisted": true, "note": "公式一覧に未掲載" }
   ```

3. コミットして push すると、1〜2分でページに反映されます。

## データの出典

- ラインナップ・商品画像: 株式会社アイアップ「モケケ 全国MAP」 https://www.eyeup.co.jp/gotouchi/mkkmap/ （2026-11-25 取得。靴下は除外、同名の重複は1つにまとめています）
- 版権元: 株式会社シナダ http://www.shinada.net/gotochi_mokeke.html
- 大阪の売り場: モケケ全国販売店マップ https://www.mokeke-storemap.com/cont1/16.html

「まだ」の子の画像は公式サイトの画像を直接表示しているだけで、このリポジトリには保存していません。権利は各権利者に帰属します。
