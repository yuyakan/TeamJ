# TeamJ
## docker関連
イメージは，https://hub.docker.com/r/hajimehirano/teamj_image
にアップしています．
### イメージ(イメージ名:`teamj_image`)の作成とコンテナ(コンテナ名:`teamj_container`)の起動
```
docker-compose up -d
```
コンテナ起動後，http://localhost:8080/
にアクセスすると見れます．

### コンテナの停止・削除，イメージの削除
```
docker-compose down --rmi all
```
現状では，ホストOSのディレクトリをマウントするのではなく，必要なファイル全てをイメージ内にコピーする形を取っているため，ファイルを追加・変更した後には，上記コマンドを実行してコンテナの停止・削除，イメージの削除を行った後，もう一度，`docker-compose up -d`でコンテナを立ち上げないと変更結果は反映されません．  
最終的にコンテナ（イメージ？）を提出するみたいなのでこの形式を取っています．
