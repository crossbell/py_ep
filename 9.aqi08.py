"""
    空气质量计算8.0：
    1.使用pandas
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    # 读取csv文件
    data = pd.read_csv('aqi/city_aqi.csv')
    # 单列
    print(data['AQI'])
    # 多列
    print(data[['city', 'AQI']])
    # 基本信息
    print(data.info())
    # 数据预览
    print(data.head(5))
    # 倒数 5条
    print(data.tail(5))

    print('最大值{}'.format(data['AQI'].max()))
    print('最小值{}'.format(data['AQI'].min()))
    print('最小值索引位置{}'.format(data['AQI'].argmin()))
    print('平均值{}'.format(data['AQI'].mean()))
    print('求和值{}'.format(data['AQI'].sum()))
    print('最大值索引{}'.format(data['AQI'].idxmax()))
    print('中位数{}'.format(data['AQI'].median()))
    print('方差{}'.format(data['AQI'].var()))
    print('标准差{}'.format(data['AQI'].std()))
    print('分位数{}'.format(data['AQI'].quantile()))
    print('describe{}'.format(data['AQI'].describe()))

    print('偏度{}'.format(data['AQI'].skew()))
    print('峰值{}'.format(data['AQI'].kurt()))
    print('累计和{}'.format(data['AQI'].cumsum()))
    print('累计最小值{}'.format(data['AQI'].cummin()))
    print('累计最值{}'.format(data['AQI'].cummax()))
    print('累计积{}'.format(data['AQI'].cumprod()))
    print('一阶差分{}'.format(data['AQI'].diff()))

     # 数据过滤，去掉AQI=0的
    filter_data = data[data['AQI'] > 0]
    print(filter_data)

    # top50
    top50_data = filter_data.sort_values(by=['AQI']).head(50)
    print(top50_data)

    # bottom10
    bottom10_data = filter_data.sort_values(by=['AQI'], ascending=False).head(10)
    print(bottom10_data)

    top50_data.to_csv('aqi/top10_aqi.csv', index=False)
    bottom10_data.to_csv('aqi/bottom10_aqi.csv', index=False)

    top50_data.plot(kind='bar', x='city', y='AQI', title='空气质量最好的50个城市')
    plt.savefig('top50_aqi.png')
    plt.show()

if __name__ == '__main__':
    main()