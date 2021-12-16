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


An alternative way to call `get_data()` is to define what hosts and charts you want via the `host_charts_dict` param:

```python
# define list of charts for each host you want data for
host_charts_dict = {
    "london.my-netdata.io" : ['system.io','system.ip'],
    "newyork.my-netdata.io" : ['system.io','system.net'],
}
df = get_data(host_charts_dict=host_charts_dict, host_prefix=True)
print(df.shape)
print(df.head())
```

    (61, 8)
                london.my-netdata.io::system.io|in  \
    time_idx                                         
    1604928340                                 NaN   
    1604928341                                 0.0   
    1604928342                                 0.0   
    1604928343                                 0.0   
    1604928344                                 0.0   
    
                london.my-netdata.io::system.io|out  \
    time_idx                                          
    1604928340                                  NaN   
    1604928341                            -53.89722   
    1604928342                            -26.10278   
    1604928343                              0.00000   
    1604928344                              0.00000   
    
                london.my-netdata.io::system.ip|received  \
    time_idx                                               
    1604928340                                       NaN   
    1604928341                                  49.25227   
    1604928342                                 227.22840   
    1604928343                                 123.56787   
    1604928344                                  31.99060   
    
                london.my-netdata.io::system.ip|sent  \
    time_idx                                           
    1604928340                                   NaN   
    1604928341                             -51.85469   
    1604928342                             -85.22854   
    1604928343                             -43.00154   
    1604928344                             -19.55536   
    
                newyork.my-netdata.io::system.io|in  \
    time_idx                                          
    1604928340                                  0.0   
    1604928341                                  0.0   
    1604928342                                  0.0   
    1604928343                                  0.0   
    1604928344                                  0.0   
    
                newyork.my-netdata.io::system.io|out  \
    time_idx                                           
    1604928340                              0.000000   
    1604928341                             -6.545929   
    1604928342                             -9.454071   
    1604928343                              0.000000   
    1604928344                              0.000000   
    
                newyork.my-netdata.io::system.net|received  \
    time_idx                                                 
    1604928340                                   13.778033   
    1604928341                                   18.281470   
    1604928342                                   24.811770   
    1604928343                                   26.406000   
    1604928344                                   26.457510   
    
                newyork.my-netdata.io::system.net|sent  
    time_idx                                            
    1604928340                               -16.97193  
    1604928341                               -19.23857  
    1604928342                               -76.86994  
    1604928343                              -165.55492  
    1604928344                              -115.83034  


## Examples

You can find some more examples in the [examples](https://github.com/netdata/netdata-pandas/tree/master/examples) folder. 

Or if you just want to play with it right now you can use [this Google Colab notebook](https://colab.research.google.com/drive/1SGF3Ij1r8gNJOwdk-3cVhCvyUGwGiTnc?usp=sharing) to quickly get started.
