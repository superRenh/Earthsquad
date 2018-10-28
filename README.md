# Earthsquad-Montage Mosaic based on thousands of NASA Astronomical images(以Web為上傳介面，使用6000多張NASA太空照片，製作成一張蒙太奇大圖)
<img src="https://github.com/superRenh/Earthsquad/blob/master/crab%20nebula32.jpg" width="80%" height="80%" style="float.left">
</br>
This is the project of NASA Hackthon2018
</br>
Visit our space app page:https://2018.spaceappschallenge.org/challenges/help-others-discover-earth/artify-earth/teams/earthsquad/project
</br>
Our website:https://rensyuan.wixsite.com/earthsquad

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
圖片默認儲存路徑為 ./downloads/
### Command line parameters 參數說明
<ul>
  <li>-k --keywords keywords for search 想要搜尋的圖片關鍵字</li>
  <li>-p --pages amounts of pages download, 100 images per page 想要下載的頁數，每一頁有100張圖片</li>
</ul>

## Create your own Montage Mosaic and uploaded interface of Web
Already download 6806 NASA Images to `output32` for creating Montage Mosaic, unless you want to create your own mosaic block database, or you can skip step "Crawler NASA Image and Video Library".</br>已經下載6806張太空圖片到`output32`資料夾作為馬賽克資料庫，除非你想創造自己的資料庫，否則可以跳過"爬取NASA公開圖庫"這個步驟。</br>
### Folders 資料夾說明
`output32`: 6806 images Mosaic database, resize to 32\*32 pixel   6806張NASA太空圖片，並resize為32\*32 pixel的馬賽克塊</br>
`download`:</br>
`img`:
# Reference
https://github.com/hardikvasa/google-images-download
</br>
https://github.com/ThomasHuai/puzzle

