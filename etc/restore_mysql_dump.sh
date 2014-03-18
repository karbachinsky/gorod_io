#!/bin/sh

#Script restores last mysqldump for for go.mail.ru blog.



# FIXME
db_user=root
db_host="localhost"
db_name="gorod_in"
db_password=""

dump_file=$1

#Trying to restore dump
#mysql -h $db_host -u $db_user -p$db_password $db_name < $dump_file
mysql -h $db_host -u $db_user  $db_name < $dump_file

#If something wrong
if [ $? -gt 0 ]; then
 echo "[`date +%F--%H-%M`] Failed. Restoring database failed."
 exit 1
fi

#It's all ok
echo "[`date +%F--%H-%M`] Backup database [$db_name] was successfully restored from file $dump_file"
