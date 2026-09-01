---
layout: base
---

# 地圖資料與賽道半徑分析

由於整個分析項目較大，不支援單一code下載，請上github翻。

## 簡介

本工具用於讀取 OpenTRACK 格式的 Excel 賽道資料，將賽道中心線、曲率、高程、傾角、banking 與 grip factor 轉換成可分析的數值資料，並輸出多張視覺化圖片。相較於只看賽道外型，此工具更重視彎道半徑分布、曲率頻譜與不同半徑區間對比賽分數的影響。

由於 FSAE 賽道通常由大量短直線、連續彎與低速彎組成，單純用平均速度或最小半徑很難描述整體設計需求。本分析將賽道離散成固定間距的點，計算每個位置的曲率與半徑，並用長度分布、時間分布與分數權重找出最值得針對性優化的彎道半徑區間。

## 輸入與輸出

輸入資料主要來自 `input_map.xlsx`，其中包含賽道基本資訊、LINE / ARC 幾何段、高程、banking、grip factor 與 sector 等資料。程式會將這些區段資料展開成連續賽道資料，並輸出 `track.json`、`OpenTRACK.npz` 與多張 PNG 圖片。

以下為分析中主要使用與輸出的資料欄位：

| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| `X`, `Y` | 賽道中心線平面座標 | $m$ |
| `x` | 沿賽道方向累積距離 | $m$ |
| `Z` | 賽道高程 | $m$ |
| `r` | 平滑後曲率 | $1/m$ |
| `kappa_raw` | 原始幾何曲率 | $1/m$ |
| `incl` | 由高程變化推得的縱向坡度角 | $deg$ |
| `bank` | 賽道 banking 角度 | $deg$ |
| `factor_grip` | 路面 grip factor | 無因次 |
| `apex_index` | 平滑曲率偵測出的 apex 位置索引 | - |
| `Radius_distribution_length` | 各半徑區間累積長度分布 | $m$ |
| `Radius_distribution_time` | 各半徑區間估計累積時間分布 | $s$ |
| `Radius_distribution_score` | 各半徑區間對賽事分數的權重估算 | point |

## 計算

### 1. 賽道幾何重建

程式會讀取 Excel 中的 `Shape` 資料，依照每個區段的型態重建中心線。直線段依照起終點插值，圓弧段則依照圓心、半徑與方向沿角度展開。

重建後每個點都會有座標、累積距離、區段編號與曲率資料。直線段曲率為零，圓弧段曲率則由半徑決定：

$$\kappa = \frac{1}{R}$$

左彎與右彎使用曲率正負號區分。

### 2. 曲率平滑與 apex 偵測

由於原始 LINE / ARC 幾何會讓曲率呈現階梯狀變化，程式使用 Gaussian smoothing 對曲率進行平滑，讓彎道變化更接近可用於分析的連續訊號。

平滑後的曲率會用於 apex 偵測。曲率局部極大值對應左彎 apex，曲率局部極小值對應右彎 apex。這能協助快速判斷賽道中主要彎角數量與位置。

### 3. 半徑分布

賽道曲率可轉換為轉彎半徑：

$$R = \frac{1}{|\kappa|}$$

工具會統計不同半徑區間在賽道中累積出現的長度，並用簡化過彎速度模型估算各半徑區間對通過時間的影響：

$$v = \sqrt{\mu_y R}$$

半徑越小，理論過彎速度越低，因此即使長度不一定最長，也可能佔據較大的時間比例。

### 4. 曲率頻譜分析

曲率沿賽道距離的變化可視為一個空間訊號。程式對平滑曲率做 FFT，分別以空間頻率與空間波長呈現頻譜，用來觀察賽道是以短距離連續彎、較長節奏彎，或混合型彎道為主。

這類分析可作為懸吊與轉向響應需求的參考，因為曲率變化越頻繁，車輛需要越快建立側向加速度與 yaw response。

### 5. 賽事分數權重

`score_weight.py` 會讀取 `track.json` 中的半徑時間分布，將 autocross 與 endurance 的分數依照各半徑區間累積時間分配。接著把 skidpad 分數加到最接近 skidpad 半徑的區間，形成半徑區間的總分數權重。

此結果可用來判斷哪些彎道半徑區間對整體競賽成績最有影響，進而協助設定輪胎、懸吊、轉向與空力分析的優先順序。

## 結果

### 賽道平面與曲率

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_xy_map.png" alt="OpenTRACK_xy_map" width="800">
</div>

XY map 以平面座標呈現賽道中心線，並用顏色表示曲率正負與大小，可快速辨識左彎、右彎與主要彎道區段。

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_radius.png" alt="OpenTRACK_radius" width="800">
</div>

曲率圖比較原始曲率與平滑曲率，並標出平滑後偵測到的 apex。這張圖可用於檢查賽道幾何是否合理，以及 apex 偵測是否過度敏感或漏判。

### 曲率頻譜

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_curvature_fft_frequency.png" alt="OpenTRACK_curvature_fft_frequency" width="800">
</div>

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_curvature_fft_wavelength.png" alt="OpenTRACK_curvature_fft_wavelength" width="800">
</div>

曲率頻譜用來觀察賽道曲率變化的主要空間頻率與波長。若短波長成分較強，代表賽道有較密集的連續轉向需求；若長波長成分較明顯，則代表較多長彎或較緩的曲率變化。

### 半徑分布與分數權重

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_radius_length_distribution.png" alt="OpenTRACK_radius_length_distribution" width="800">
</div>

半徑長度分布顯示各轉彎半徑區間在賽道中累積的距離，可用來判斷賽道幾何最常出現哪些彎道半徑。

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_radius_time_distribution.png" alt="OpenTRACK_radius_time_distribution" width="800">
</div>

半徑時間分布將半徑轉換成估計過彎速度後，統計各半徑區間佔用的時間。低速小半徑彎通常會比長度分布更重要，因為車輛在這些區間花費更多時間。

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_radius_score_weight.png" alt="OpenTRACK_radius_score_weight" width="800">
</div>

分數權重圖將 autocross、endurance 與 skidpad 的分數概念加入半徑分布中，用來判斷哪些半徑區間對總成績影響最大。這張圖適合用來決定車輛設定優先服務的彎道型態。

### 高程、坡度、banking 與 grip factor

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_elevation.png" alt="OpenTRACK_elevation" width="800">
</div>

高程圖顯示賽道沿距離方向的高度變化，可用於評估縱向負載轉移、動力需求與煞車負載的可能變化。

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_inclination.png" alt="OpenTRACK_inclination" width="800">
</div>

坡度圖由高程變化推得，能看出上坡、下坡或坡度快速變化區段，對加速、煞車與懸吊載荷都有參考價值。

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_banking.png" alt="OpenTRACK_banking" width="800">
</div>

Banking 圖顯示賽道橫向傾角，會影響過彎時輪胎正向力與側向力需求的分配。

<div style="text-align: center;">
<img src="OpenTRACK%20Tracks/OpenTRACK_grip_factor.png" alt="OpenTRACK_grip_factor" width="800">
</div>

Grip factor 圖顯示不同賽道區段的路面抓地力修正，可用於後續更完整的 lap simulation 或輪胎負載分析。

## 使用方式

若要重新產生賽道分析圖，先確認 `input_map.xlsx` 與 `track.json` 位於此資料夾中，再執行(如果沒有json 就需要先執行track_data)：

```powershell
python track_data.py
python TrackAnalysis.py
python score_weight.py
```

`TrackAnalysis.py` 會更新賽道幾何資料與大部分視覺化圖，`score_weight.py` 會根據半徑時間分布更新分數權重圖與 `track.json` 中的半徑分數排序。
