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

    (61, 16)
                system.cpu|guest_nice  system.cpu|guest  system.cpu|steal  \
    time_idx                                                                
    1600178015                    NaN               NaN               NaN   
    1600178020                    0.0               0.0               0.0   
    1600178021                    0.0               0.0               0.0   
    1600178022                    0.0               0.0               0.0   
    1600178023                    0.0               0.0               0.0   
    
                system.cpu|softirq  system.cpu|irq  system.cpu|user  \
    time_idx                                                          
    1600178015                 NaN             NaN              NaN   
    1600178020            0.000000             0.0         0.753769   
    1600178021            0.000000             0.0         0.251256   
    1600178022            0.251256             0.0         0.753769   
    1600178023            0.000000             0.0         0.751880   
    
                system.cpu|system  system.cpu|nice  system.cpu|iowait  \
    time_idx                                                            
    1600178015                NaN              NaN                NaN   
    1600178020           0.251256              0.0                0.0   
    1600178021           0.753769              0.0                0.0   
    1600178022           0.251256              0.0                0.0   
    1600178023           0.501253              0.0                0.0   
    
                system.ram|free  system.ram|used  system.ram|cached  \
    time_idx                                                          
    1600178015              NaN              NaN                NaN   
    1600178020         2927.668         2543.215           2443.664   
    1600178021         2927.852         2543.031           2443.664   
    1600178022         2927.645         2543.242           2443.660   
    1600178023         2926.496         2544.383           2443.668   
    
                system.ram|buffers  system.load|load1  system.load|load5  \
    time_idx                                                               
    1600178015                 NaN               0.02               0.04   
    1600178020            73.10156               0.02               0.04   
    1600178021            73.10156               0.02               0.04   
    1600178022            73.10156               0.02               0.04   
    1600178023            73.10156               0.02               0.04   
    
                system.load|load15  
    time_idx                        
    1600178015                 0.0  
    1600178020                 0.0  
    1600178021                 0.0  
    1600178022                 0.0  
    1600178023                 0.0  


## Examples

You can find some more examples in the [examples](https://github.com/netdata/netdata-pandas/tree/master/examples) folder. 

Or if you just want to play with it right now you can use [this Google Colab notebook](https://colab.research.google.com/drive/1SGF3Ij1r8gNJOwdk-3cVhCvyUGwGiTnc?usp=sharing) to quickly get started.
