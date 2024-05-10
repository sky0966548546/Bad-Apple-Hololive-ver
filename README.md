# Bad Apple Hololive ver

## 使用方法

1. 確保已安裝所需的 Python 套件（Pillow）：

```
pip install Pillow tqdm
```

2. 影片逐幀下載圖片，將它們放在 `assets/images` 目錄下。

3. 執行 `ascii.py` 來生成 ASCII 文字文件。

```
python ascii.py
```

這將在 `assets/text` 目錄下生成相應的文字文件。

4. 執行 `main.py` 腳本來顯示動畫：

```
python main.py
```

這將逐個在終端上顯示動畫。

## 依賴

- Python 3.x
- Pillow - Python 圖像處理庫
- tqdm - 進度條顯示庫

## 注意事項

- 如果屏幕閃爍或顯示不正常，可以嘗試調整 `main.py` 中清除螢幕的方式或頻率。
- 該程式只能處理簡單的圖像，對於複雜的圖像可能效果不佳。

影片連結：[LINK](https://youtu.be/xzSJwd_MZ_k)