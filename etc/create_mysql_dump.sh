#!/bin/sh

script_dir=$(cd $(dirname $0) && pwd)
app_dir="$script_dir/../"

#Script creates a mysqldump for fo.mail.ru blog in ~/blog_db_dump dir.
if [ $1 == "" ]; then
    echo "No input target path. Usage: $0 /some_path"
    exit 1
fi

DUMP_DIR=$1

# FIXME
db_user=gorodin
db_host="localhost"
db_name="gorodin"
db_password="barcelona1"

#Creating dir, containing our dumps if it not exists
mkdir -p $DUMP_DIR

#Trying to create dump
mysqldump --user=$db_user --host=$db_host --password=$db_password $db_name > $DUMP_DIR/dump-`date +%F--%H-%M`.sql

#If something wrong
if [[ $? -gt 0 ]]; then
 echo "[++--------][`date +%F--%H-%M`] Aborted. Generate database backup failed."
 exit 1
fi

#It's all ok
echo "[`date +%F--%H-%M`] Backup database [$db_name] - successfull."
