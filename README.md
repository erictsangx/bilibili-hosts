# bilibili-hosts
腳本修改hosts解決海外用戶觀看B站不能播放

### 教程
首先感謝zczczc1680提供的方法https://bbs.uku.im/t/topic/3704

有能力的大神們想必自己動手了，這教程是給小白們看的
- 下載 dist/main(mac用戶) dist/main.exe(win用戶)
- 在啟動unblock-youku下，打開新番
- 按F12打開CONSOLE，在Network下找到B站分配的伺服器，如：cn-zjhz2-wasu-acache-10.acgvideo.com
![Alt text](images/chrome.png?raw=true "chrome")
- 右鍵複製伺服器，由於hosts屬於系統文件，win用戶請右鍵以系統管理員運行，mac用戶打開終端機輸入 sudo ./download_path/main後再輸入密碼
- 腳本會自動找尋cn-sh-ix-acache-0X.acgvideo.com(X=1-9)中的IP後寫入B站分配的伺服器
![Alt text](images/result.png?raw=true "result")