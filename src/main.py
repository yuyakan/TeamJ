#自販機のページを自動生成するスクリプト
import pandas as pd
import os
import re

#このスクリプトから見た場所

#自販機のhtmlファイルのディレクトリ
place_dir = "../site/place"
#自販機の画像ファイルのディレクトリ
image_dir = "../data/image"

#インデックスのページ
index_file = "../cite/index.html"

#自販機のページ(分割している)
upper_file = "../data/upper.html"
main_file = "../data/main.html"
lower_file = "../data/lower.html"

#自販機のデータ
csv_file = f"../data/data.csv"

#自販機データの書き込み
def rewrite_main(lines,data,alt):
    for i,line in enumerate(lines):
        lines[i] = re.sub('<h2><img class="vending_machine_image" src="[\S\s]*" alt="[\S\s]*"></h2>',
                        f'<h2><img class="vending_machine_image" src="../{image_dir}/{data["ファイル名"]}" alt="{alt}"></h2>',
                        line)
        if '<td class="uk-width-small">場所</td>' in line:
            lines[i+1] = re.sub('<td>[\S\s]*</td>',f'<td>{data["場所"]}</td>',lines[i+1])
        if '<td class="uk-width-small">会社</td>' in line:
            lines[i+1] = re.sub('<td>[\S\s]*</td>',f'<td>{data["会社"]}</td>',lines[i+1])
        if '<td class="uk-width-small">商品</td>' in line:
            lines[i+1] = re.sub('<td>[\S\s]*</td>',f'<td>{data["商品"]}</td>',lines[i+1])
    return lines

#htmlファイルの生成
def generate():
    print("start")
    image_names = os.listdir(image_dir)
    data = {re.sub('_[\S\s]*.jpg',"",image_name):{} for image_name in image_names}
    df = pd.read_csv(csv_file,encoding='utf-8')
    df = df.set_index('ファイル名')
    for image_name in image_names:
        alt = re.sub(".jpg","",image_name)
        place = df.loc[alt].dropna(how='all')["備考"]
        building = re.sub("_[\S\s]*","",alt)
        company = df.loc[alt].dropna(how='all')["会社"]
        item = df.loc[alt].dropna(how='all') 
        item = "、".join(list(item[3:].index))
        data[building][alt] = {"場所":place,
                                "会社":company,
                                "商品":item,
                                "ファイル名":image_name}

    for building,d in data.items():
        with open(f"{place_dir}/{building}.html","w",encoding="utf-8-sig") as f:
            with open(upper_file,"r",encoding="utf-8-sig") as u:
                lines = u.readlines()
                for line in lines:
                    f.write(line)
            for alt,_d in d.items():
                with open(main_file,"r",encoding="utf-8-sig") as m:
                    lines = m.readlines()
                    lines = rewrite_main(lines,_d,alt)
                    for line in lines:
                        f.write(line)         
            with open(lower_file,"r",encoding="utf-8-sig") as l:
                lines = l.readlines()
                for line in lines:
                    f.write(line)
    print("finish")
    return
    
if __name__ == "__main__":
    generate()