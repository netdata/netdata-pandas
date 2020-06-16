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
                system.cpu|guest_nice  system.cpu|guest  system.cpu|steal  \
    time_idx                                                                
    1592303824                      0                 0          0.250627   
    1592303825                      0                 0          0.000000   
    1592303826                      0                 0          0.000000   
    1592303827                      0                 0          0.000000   
    1592303828                      0                 0          0.000000   
    
                system.cpu|softirq  system.cpu|irq  system.cpu|user  \
    time_idx                                                          
    1592303824            0.250627               0         0.501253   
    1592303825            0.000000               0         1.250000   
    1592303826            0.000000               0         0.502513   
    1592303827            0.000000               0         1.005025   
    1592303828            0.000000               0         1.002506   
    
                system.cpu|system  system.cpu|nice  system.cpu|iowait  \
    time_idx                                                            
    1592303824           0.501253                0                0.0   
    1592303825           0.500000                0                0.0   
    1592303826           0.502513                0                0.0   
    1592303827           1.005025                0                0.0   
    1592303828           0.250627                0                0.0   
    
                system.load|load1  system.load|load5  system.load|load15  
    time_idx                                                              
    1592303824                NaN                NaN                 NaN  
    1592303825                0.0               0.02                 0.0  
    1592303826                0.0               0.02                 0.0  
    1592303827                0.0               0.02                 0.0  
    1592303828                0.0               0.02                 0.0  


## Examples

You can find some more examples in the [examples](https://github.com/netdata/netdata-pandas/tree/master/examples) folder. 

Or if you just want to play with it right now you can use [this Google Colab notebook](https://colab.research.google.com/drive/1SGF3Ij1r8gNJOwdk-3cVhCvyUGwGiTnc?usp=sharing) to quickly get started.
