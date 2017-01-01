# getCidr

IP address range is output in CIDR format.  
(IPアドレスの範囲をCIDR形式で出力します)

## Installation

```
git clone https://github.com/sk39kii/getCidr.git
cd getCidr
```

## Usage

```sh
python getcidr.py [from IP address] [to IP address]
```

### Example.  

##### IP address range：192.168.100.0 - 192.168.100.255

```sh
$ python getcidr.py 192.168.100.0 - 192.168.100.255
192.168.100.0/24
```

Or, A hyphen between IP addresses may or may not be present.  
(IPアドレスの間のハイフンはあってもなくてもよいです)

```sh
$ python getcidr.py 192.168.100.0 192.168.100.255
192.168.100.0/24
```

## Requirement
* Python 2 series  
*Confirm operation with Python 2.7

