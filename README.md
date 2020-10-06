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

```
from netdata_pandas.data import get_data

df = get_data('london.my-netdata.io', ['system.cpu','system.load'], after=-60, before=0)
print(df.shape)
print(df.head())
```

    (61, 12)
                system.cpu|guest_nice  system.cpu|guest  system.cpu|steal  \
    time_idx                                                                
    1600179540                    NaN               NaN               NaN   
    1600179542                    0.0               0.0          0.251889   
    1600179543                    0.0               0.0          0.000000   
    1600179544                    0.0               0.0          0.000000   
    1600179545                    0.0               0.0          0.000000   
    
                system.cpu|softirq  system.cpu|irq  system.cpu|user  \
    time_idx                                                          
    1600179540                 NaN             NaN              NaN   
    1600179542                 0.0             0.0         0.503778   
    1600179543                 0.0             0.0         0.750000   
    1600179544                 0.0             0.0         0.251889   
    1600179545                 0.0             0.0         0.503778   
    
                system.cpu|system  system.cpu|nice  system.cpu|iowait  \
    time_idx                                                            
    1600179540                NaN              NaN                NaN   
    1600179542           0.503778              0.0                0.0   
    1600179543           0.500000              0.0                0.0   
    1600179544           0.503778              0.0                0.0   
    1600179545           0.503778              0.0                0.0   
    
                system.load|load1  system.load|load5  system.load|load15  
    time_idx                                                              
    1600179540            0.04888               0.03                 0.0  
    1600179542            0.04888               0.03                 0.0  
    1600179543            0.04888               0.03                 0.0  
    1600179544            0.04888               0.03                 0.0  
    1600179545            0.04000               0.03                 0.0  
    

## Examples

You can find some more examples in the [examples](https://github.com/netdata/netdata-pandas/tree/master/examples) folder. 

Or if you just want to play with it right now you can use [this Google Colab notebook](https://colab.research.google.com/drive/1SGF3Ij1r8gNJOwdk-3cVhCvyUGwGiTnc?usp=sharing) to quickly get started.
