配置新网站
====================

## 需要的包：


* Python3.6
* nginx
* virtualenv + pip
* Git


以Ubuntu为例

    sudo add-apt-repository ppa：deadsnakes / ppa
    sudo apt-get update
    sudo apt_get install nginx git python36 python3.6-venv


## Nginx虚拟主机

* 参考nginx.template.conf
* 把SITENAME替换成所需要的域名，例如staging.my-domain.com


## Systemd服务

* 参考gunicorn-systemd.template.conf
* 把SITENAME替换成所需要的域名，例如staging.my-domain.com


## 文件夹结构
假设有用户账户，家目录为/home/username

/home/username
--sites
    --SITENAME
        --database
        --source
        --static
        --virtualenv

