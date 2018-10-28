# Earthsquad-Montage Mosaic based on thousands of NASA Astronomical images(以Web為上傳介面，使用6000多張NASA太空照片，製作成一張蒙太奇大圖)
<img src="https://github.com/superRenh/Earthsquad/blob/master/crab%20nebula32.jpg" width="80%" height="80%" style="float.left">
</br>
This is the project of NASA Hackthon2018:
</br>
<ul>
<li> Visit our space app page:https://2018.spaceappschallenge.org/challenges/help-others-discover-earth/artify-earth/teams/earthsquad/project </li>
<li>Our website:https://rensyuan.wixsite.com/earthsquad</li>
<li>What is Montage Mosaic? 什麼是蒙太奇照片拼圖?</br>
A composite picture made by combining several separate pictures.</br>
簡單來說，所謂蒙太奇拼圖效果，就是指用很多張小圖片拼組成一張全新的圖片。</ul>

## Environment setup環境設定(Python3.6)
1. Install web framework-Flask</br>
`pip install flask`
2. Install googlimagesdownload</br>
`pip install googleimagesdownloads`</br>
3. others: <a href="https://github.com/superRenh/Earthsquad/blob/master/requirement.txt">Requirement.txt</a>
## Crawler NASA Image and Video Library爬取NASA公開圖庫
<ul>
  <li><a href="https://images.nasa.gov/">NASA Image and Video Library</a></li></br>
  <li><a href="https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf">API DOC</a></li>
</ul>

### Command line 命令提示字元
`python NASAImageCrawler.py -k "earth" -p 3`</br>
default saving directory `./downloads/` 圖片默認儲存路徑為 `./downloads/`
### Command line parameters 參數說明
<ul>
  <li>-k --keywords keywords for search 想要搜尋的圖片關鍵字</li>
  <li>-p --amounts of pages downloaded, 100 images per page 總下載頁數，每一頁有100張圖片</li>
</ul>

## Create your own Montage Mosaic and uploaded interface of Web創建蒙太奇大圖及web上傳介面
Already download 6806 NASA Images to `output32` for creating Mosaic block, unless you want to create your own mosaic block database, or you can skip the step of "Crawler NASA Image and Video Library".</br>
已經下載6806張太空圖片到`output32`資料夾作為馬賽克資料庫，除非你想創造自己的資料庫，否則可以跳過"爬取NASA公開圖庫"這個步驟。</br>
### Folders and modules 資料夾及模塊說明
`output32:` 6806 NASA astronomical images, and resize to 32\*32 pixel to create Mosaic block database.</br>
            6806張NASA太空圖片，並resize為32\*32 pixel的馬賽克塊。</br>
`download:`images that upload from web. 從web介面上傳的圖片。</br>
`img:` result of Montage Mosaic consist of thousands mosaic block based on the uploaded image.
       存放最後製作好的蒙太奇大圖。</br>
`puzzle.py:`</br>
`app.py:`
### Remote Connections to Flask Web Service 允許遠端訪問Flask web

### Command line 命令提示字元

### Result 結果展示
# Reference
https://github.com/hardikvasa/google-images-download</br>
https://github.com/ThomasHuai/puzzle

