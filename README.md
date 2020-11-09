# netdata-pandas
> A helper library to pull data from netdata api into a pandas dataframe.


[![pypi package](https://img.shields.io/pypi/v/netdata-pandas.svg)](https://pypi.python.org/pypi/netdata-pandas/) 
[![CI](https://github.com/netdata/netdata-pandas/workflows/CI/badge.svg)](https://github.com/netdata/netdata-pandas/actions?query=workflow%3ACI)

## Install

`pip install netdata-pandas`

## Documentation

More detailed documentation can be found at https://netdata.github.io/netdata-pandas

## Quickstart

Get some data into a pandas dataframe.

```python
from netdata_pandas.data import get_data

df = get_data('london.my-netdata.io', ['system.cpu','system.load'], after=-60, before=0)
print(df.shape)
print(df.head())
```

    (60, 12)
                system.cpu|guest  system.cpu|guest_nice  system.cpu|iowait  \
    time_idx                                                                 
    1604928205               0.0                    0.0                0.0   
    1604928206               0.0                    0.0                0.0   
    1604928207               0.0                    0.0                0.0   
    1604928208               0.0                    0.0                0.0   
    1604928209               0.0                    0.0                0.0   
    
                system.cpu|irq  system.cpu|nice  system.cpu|softirq  \
    time_idx                                                          
    1604928205             0.0              0.0                 0.0   
    1604928206             0.0              0.0                 0.0   
    1604928207             0.0              0.0                 0.0   
    1604928208             0.0              0.0                 0.0   
    1604928209             0.0              0.0                 0.0   
    
                system.cpu|steal  system.cpu|system  system.cpu|user  \
    time_idx                                                           
    1604928205          0.000000           0.501253         0.501253   
    1604928206          0.000000           0.753769         0.502513   
    1604928207          0.000000           0.505050         0.505050   
    1604928208          0.000000           0.751880         0.501253   
    1604928209          0.251256           0.251256         0.502513   
    
                system.load|load1  system.load|load15  system.load|load5  
    time_idx                                                              
    1604928205               0.03                 0.0               0.04  
    1604928206               0.03                 0.0               0.04  
    1604928207               0.03                 0.0               0.04  
    1604928208               0.03                 0.0               0.04  
    1604928209               0.03                 0.0               0.04  


```python
# an alternative way to use it is to define what hosts and charts you want via the host_charts_dict param

# define list of charts for each host you want data for
host_charts_dict = {
    "london.my-netdata.io" : ['system.io','system.ip'],
    "newyork.my-netdata.io" : ['system.io','system.net'],
}
df = get_data(host_charts_dict=host_charts_dict, host_prefix=True)
print(df.shape)
df.head()
```

    (61, 8)





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
      <th>london.my-netdata.io::system.io|in</th>
      <th>london.my-netdata.io::system.io|out</th>
      <th>london.my-netdata.io::system.ip|received</th>
      <th>london.my-netdata.io::system.ip|sent</th>
      <th>newyork.my-netdata.io::system.io|in</th>
      <th>newyork.my-netdata.io::system.io|out</th>
      <th>newyork.my-netdata.io::system.net|received</th>
      <th>newyork.my-netdata.io::system.net|sent</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1604928205</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.00000</td>
      <td>22.504610</td>
      <td>-98.626510</td>
    </tr>
    <tr>
      <th>1604928206</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>130.73635</td>
      <td>-123.73966</td>
      <td>0.0</td>
      <td>-36.20121</td>
      <td>22.008190</td>
      <td>-16.564677</td>
    </tr>
    <tr>
      <th>1604928207</th>
      <td>0.0</td>
      <td>-26.910170</td>
      <td>282.60690</td>
      <td>-126.88656</td>
      <td>0.0</td>
      <td>-51.79879</td>
      <td>19.258920</td>
      <td>-16.588992</td>
    </tr>
    <tr>
      <th>1604928208</th>
      <td>0.0</td>
      <td>-13.089829</td>
      <td>139.39631</td>
      <td>-69.74703</td>
      <td>0.0</td>
      <td>0.00000</td>
      <td>14.081868</td>
      <td>-17.615410</td>
    </tr>
    <tr>
      <th>1604928209</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>64.39024</td>
      <td>-62.24043</td>
      <td>0.0</td>
      <td>0.00000</td>
      <td>15.863426</td>
      <td>-18.286320</td>
    </tr>
  </tbody>
</table>
</div>



## Examples

You can find some more examples in the [examples](https://github.com/netdata/netdata-pandas/tree/master/examples) folder. 

Or if you just want to play with it right now you can use [this Google Colab notebook](https://colab.research.google.com/drive/1SGF3Ij1r8gNJOwdk-3cVhCvyUGwGiTnc?usp=sharing) to quickly get started.
