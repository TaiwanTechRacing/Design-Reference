# Stiffness

## 懸吊行程的剛性限制
[Compressed travel](Compressed_travel/Compressed_travel.md)
 : 用懸吊行程的最低剛性下限制。注意這邊沒有考慮懸吊機構影響單純分析前後軸剛性


## 空力的pitch 行程限制
[Aero Stiffness](Aero_Stiffness/Aero_Stiffness.md)
 : 空力允許姿態變化找出最低剛性限制，這個限制通常會比上一個行程限制更限縮。

## 人體頻率限制
這部分沒有強制限制，但貼出來讓大家體諒一下車手的辛苦

![alt text](image.png)

## 路面震動分析
[PSD](PSD/PSD.md) : 接下來分析一下懸吊需要應付的主要振動頻率範圍，不過裡面有很多複雜的細項有些分析實用性不高，做這個分析ROI蠻低的。

## 輪胎環模態頻率
[Tire Ring Mode](Tire_Ring_Mode/Tire_Ring_Mode.md) : 
分析不同模態階數的頻率，理論上我們需要避開。但基本上結果都在和自然頻率差太多算是做好玩用的。

## 自然頻率轉換
[Frequency Stiffness](Frequency_Stiffness/Frequency_Stiffness.md) : 前面有些有頻率和剛性的分析統一一下單位，把行程需求與空力要求的剛性需求轉到自然頻率進行分析，方便之後和輪胎自然頻率比較

## 輪胎剛性影響
[Tire Stiffness](Tire_Stiffness/Tire_Stiffness.md) : 
輪胎剛性影響的ride rate同時分析，看看輪胎造成的影響與如果要符合預期的話剛性要提升多少。

## 簧下質量與自然頻率
[Frequency mass](Frequency_mass/Frequency_mass.md) : 確定簧上下自然頻率差異足夠大，順便看一下實際簧下質量與設計數值有誤差的話的影響。

## 車架剛性參考
[Overall Rigidity](Overall_Rigidity/Overall_Rigidity.md) : 最後看一下車體剛性用於預設的車架剛性參考

