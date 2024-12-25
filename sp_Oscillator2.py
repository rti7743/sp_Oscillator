import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

def sp_oscillator2(ticker, divscaller , SellSignalY, OverboughtY, OversoldY, BuySignalY):
	#チャートの範囲
	end_date = datetime.now().date()
	start_date = end_date - timedelta(days=365)  # 1年間分のデータを取得

	# データ取得
	data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'))

	# 欠損値の確認と処理
	data = data.dropna()

	# 移動平均の期間を調整
	short_window = 5   # 短期移動平均の期間
	long_window = 10   # 長期移動平均の期間

	# 移動平均の計算
	data['MA_short'] = data['Close'].rolling(window=short_window).mean()
	data['MA_long'] = data['Close'].rolling(window=long_window).mean()

	# オシレーターの計算
	data['Oscillator'] = (data['MA_short'] - data['MA_long']) / divscaller

	# 欠損値除去（移動平均計算後の欠損を除く）
	data = data.dropna()

	# プロット
	plt.figure(figsize=(12, 6))

	# オシレーターをプロット
	plt.plot(data.index, data['Oscillator'], label='MA5-MA10', color='black')

	# 水準線を追加
	plt.axhline(y=OverboughtY, color='red', linestyle='--', label='Overbought')
	plt.axhline(y=SellSignalY, color='darkviolet', linestyle=':', label='Sell')
	plt.axhline(y=OversoldY, color='green', linestyle='--', label='Oversold')
	plt.axhline(y=BuySignalY, color='blue', linestyle=':', label='Buy')

	# メモリを右側に表示
	plt.tick_params(left=False, right=True, labelleft=False, labelright=True)

	# 最後の値を表示
	last_value = data['Oscillator'].iloc[-1]
	fontcolor = 'black'
	if (last_value >= SellSignalY):
		fontcolor = 'darkviolet'
	elif (last_value >= OverboughtY):
		fontcolor = 'red'
	elif (last_value <= BuySignalY):
		fontcolor = 'blue'
	elif (last_value <= OversoldY):
		fontcolor = 'green'

	plt.text(data.index[-1], last_value, f' {last_value:.1f}', 
	         verticalalignment='bottom', horizontalalignment='left',
	         color=fontcolor, fontsize=19)

	# グラフの設定
	plt.legend()
	plt.grid()
	plt.subplots_adjust(left=0.01, right=0.96, bottom=0.05, top=0.99)

	# JPGファイルに保存
	file_name = f"sp_oscillator_{ticker}.jpg"
	plt.savefig(file_name, format='jpg', dpi=100)
	plt.close()

#SP500先物
sp_oscillator2("ES=F", 10.0,6, 4, -4, -6)
#NASDAQ100先物
sp_oscillator2("NQ=F", 100.0,3, 2, -2, -3)
#日経平均先物
sp_oscillator2("NIY=F", 100.0,6, 5, -5, -6)
#ドル円
sp_oscillator2("USDJPY=X", 0.1,12, 10, -10, -12)
#BTC先物
sp_oscillator2("BTC=F", 500.0,6, 4, -4, -6)
