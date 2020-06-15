# netdata-pandas
> A helper library to pull data from netdata api into a pandas dataframe.


[![pypi package](https://img.shields.io/pypi/v/netdata-pandas.svg)](https://pypi.python.org/pypi/netdata-pandas/) 
[![CI](https://github.com/netdata/netdata-pandas/workflows/CI/badge.svg)](https://github.com/netdata/netdata-pandas/actions?query=workflow%3ACI)

## Install

`pip install netdata-pandas`

## Quickstart

Get some data into a pandas dataframe.

```python
from netdata_pandas.data import get_data

df = get_data('london.my-netdata.io', ['system.cpu','system.load'], after=-60, before=0)
print(df.shape)
df.head()
```

    (61, 12)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>system.cpu|guest_nice</th>
      <th>system.cpu|guest</th>
      <th>system.cpu|steal</th>
      <th>system.cpu|softirq</th>
      <th>system.cpu|irq</th>
      <th>system.cpu|user</th>
      <th>system.cpu|system</th>
      <th>system.cpu|nice</th>
      <th>system.cpu|iowait</th>
      <th>system.load|load1</th>
      <th>system.load|load5</th>
      <th>system.load|load15</th>
    </tr>
    <tr>
      <th>time_idx</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1592257125</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1592257129</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.501253</td>
      <td>0.751880</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1592257130</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.501253</td>
      <td>0.751880</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1592257131</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.249377</td>
      <td>0.0</td>
      <td>0.997506</td>
      <td>0.498753</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1592257132</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.503778</td>
      <td>0.755668</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


