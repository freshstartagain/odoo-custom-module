<h3 align=center>Odoo Custom Module</h3>
<p align=center>
  <span>Learning how to create custom module for Odoo.</span>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## Installation 

```console
# 1. clone odoo community repo
git clone https://github.com/odoo/odoo.git

# 2. change directory
cd /odoo-repo

# 3. install dependencies (Linux) 
sed -n -e '/^Depends:/,/^Pre/ s/ python3-\(.*\),/python3-\1/p' debian/control | sudo xargs apt-get install -y

# 4. provision a postgres server

# 5. provision odoo server
./odoo-bin --addons-path="addons/" -d $db-name

# 5. copy estate custom module
cp /estate /custom_module/estate

# 6. install estate custom module
./odoo-bin --addons-path="addons/, custom_module/" -d $db-name -i estate

# 7. make sure to activate developer mode on odoo settings, and update the list of apps.
```

## Real Estate App
![real estate module](docs/real-estate-app.png)


> [!NOTE]


