---
layout: base
---

# TOC 文件書寫規則

## 共同規則

所有文件建議遵守以下格式：

1. 文件開頭使用 Jekyll front matter：

```markdown
---
layout: base
---
```

2. front matter 後空一行，接一個一級標題 `#`。一份文件只使用一個一級標題。
3. 標題以中文為主，必要時在括號中補英文專有名詞，例如 `車架剛性與等效懸吊剛度（Overall Rigidity & Equivalent Stiffness）計算與分析說明`。
4. 相對連結優先使用同資料夾或子資料夾路徑，不使用絕對路徑。
5. 程式、圖片、gif 等附件放在該主題相同資料夾內，讓 Markdown 可用相對路徑引用。
6. 公式使用 LaTeX。行內公式用 `$...$`，獨立公式用 `$$...$$`。
7. 程式變數名稱使用反引號，例如 `` `m` ``、`` `k_ride` ``。

## 分類首頁規則

分類首頁用來建立導覽，不放完整計算推導。常見結構如下：

```markdown
---
layout: base
---

# 分類名稱

## [子主題名稱](SubFolder/SubFolder.md)

>一句話摘要，說明這個工具或分析的用途。

用一到兩段文字說明此子主題的背景、設計目的、會解決什麼問題。

## [下一個子主題名稱](NextFolder/NextFolder.md)

>一句話摘要。

補充說明。
```

分類首頁的書寫重點：

1. 子主題使用二級標題 `##` 或在需要群組時使用三級標題 `###`。
2. 可點擊的子主題標題格式為 `## [顯示名稱](相對路徑/檔案.md)`。
3. 每個子主題標題下方通常先放 blockquote 摘要：`>摘要文字`。
4. 摘要後再用一段或條列文字補充背景與用途。
5. 若要放工具圖片，可用 HTML 置中或 flex 排版，但分類首頁以導覽為主，圖片不宜喧賓奪主。

## 圖片與附件規則

圖片通常用 HTML 置中，寬度以 `800` 為主：

```markdown
<div style="text-align: center;">
<img src="figure.png" alt="image" width="800">
</div>
```

多張圖片橫向排列可使用 flex：

```markdown
<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="image.png" alt="image" width="300">
  <img src="image-1.png" alt="image" width="500">
</div>
```

附件命名與引用建議：

1. 程式檔名通常與資料夾或主題名稱一致，例如 `Brake_force.py` 對應 `Brake_force.md`。
2. 圖片檔名應描述輸出內容，例如 `normal_load_vs_acceleration.png`、`Ideal_Brake_Bias.png`。
3. 檔名若包含空白，Markdown/HTML 連結中需使用 URL encode，例如空白寫成 `%20`。
4. 圖片、程式、動畫檔建議與該主題 `.md` 放在同一個子資料夾。

## 公式與表格規則

參數表格建議格式：

```markdown
| 變數名稱 | 物理意義 | 單位 |
| --- | --- | --- |
| `variable_name` | 中文說明與符號 ($x$) | $unit$ |
```

公式書寫建議：

1. 行內提到符號時使用 `$x$`、`$\mu$`、`$k_{ride}$`。
2. 主要推導公式獨立成行，使用 `$$...$$`。
3. 公式前後各空一行，維持 Markdown 可讀性。
4. 若公式中的變數名稱對應程式變數，需在參數表格中列出。
5. 單位使用 LaTeX 或文字皆可，但同一表格內盡量一致，例如 `$N/m$`、`$kg$`、`無因次`。


## 新增文件檢查清單

新增一份 `open` 內的 Markdown 文件前，請確認：

1. 已加入 `layout: base` front matter。
2. 只有一個 `#` 主標題。
3. 若是分類首頁，所有子主題連結都能連到相對路徑。
4. 若是計算頁，已包含 `Download Code`、`參數`、`計算`、`結果` 等必要段落。
5. 參數表格中的程式變數、物理符號與單位一致。
6. 公式前後有空行，且可由文字說明銜接。
7. 圖片或 gif 使用相對路徑，且檔案位於相同主題資料夾或可正確連到的位置。
8. 結果段落不只放圖，也有文字說明圖表意義。
9. 引用理論或資料來源時，可用 blockquote 放在相關段落前，例如 `> 參考數值分析與物理模擬 : ...`。