# sp_Oscillator
pythonでspオシレーターみたいなグラフを描く。
株式の売られ過ぎ、買われ過ぎを分析します。
信頼性は知らん。俺に聞くな。

yfinanceを利用してます。
コードの大半はChatGPT先生が書いてくれました。
俺より優秀なんだから困ったものだぜ。

ChatGPTによると、spオシレーターはMA5-MA10で計算できるらしい。
ただ、spオシレーターと全く同じ値にはならない。
何か秘密のエッセンスがあるのだろう。

いろいろ試したところ、sp500先物を使うとよりそれっぽい結果になりました。
とりあえず、SP500、NASDAQ100、日経平均、ドル円、BTCビットコイン先物の5つspオシレーターみたいな値を計算して求めることができます。
上に行くほど買われ過ぎ。過熱感がある。
下に行くほど売られ過ぎ。

SP500
![SP500先物](https://github.com/rti7743/sp_Oscillator/blob/main/sp_oscillator_ES%3DF.jpg)

NASDAQ100
![NASDAQ100先物](https://github.com/rti7743/sp_Oscillator/blob/main/sp_oscillator_NQ%3DF.jpg)

BTC
![BTC=F](https://github.com/rti7743/sp_Oscillator/blob/main/sp_oscillator_BTC%3DF.jpg)

ドル円
![BTC=F](https://github.com/rti7743/sp_Oscillator/blob/main/sp_oscillator_USDJPY%3DX.jpg)

日経平均
![日経平均は日経新聞社の著作物](https://github.com/rti7743/sp_Oscillator/blob/main/sp_oscillator_NIY%3DF.jpg)


上にいって、赤い線(Overbought)を越えたら買われ過ぎ。
紫の線(Sell)を越えたら売りタイミング。もち空売りでも可。

下にいって、緑色の線(Oversold)を越えたら売られ過ぎ。
青い線(Buy)を越えたら買いのタイミング。

ただし、これで儲かるかは知らん。投資は自己責任で。
あと、yfinanceを使っているので、これを連続して叩きまくるとyahoo finance(米国版)に負荷をかけるので、忖度して自重しろ。

このソフトウェアのライセンスはGPL v3です。
